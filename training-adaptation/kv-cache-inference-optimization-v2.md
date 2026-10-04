\# KV-Cache \& Inference Optimization



The easiest way to understand this topic is:



> \*\*KV-cache prevents the LLM from repeatedly recomputing attention information it has already calculated.\*\*



But there is an important twist:



> \*\*The optimization saves computation, but the saved information consumes GPU memory.\*\*



At small scale, that's a huge win. At large scale—long conversations, long contexts, many simultaneous users—the KV cache itself can become the thing limiting your system.



That is the central idea of the entire material. 



\---



\# 1. Big Idea — Plain English



Imagine you're asking an LLM:



> "Explain transformers."



The model generates:



```text

Transformers

are

neural

networks

that

...

```



It generates \*\*one token at a time\*\*.



When generating the next token, the model needs to attend to the tokens it has already seen.



A naive implementation could repeatedly recompute the attention \*\*Key (K)\*\* and \*\*Value (V)\*\* representations for all previous tokens.



That's wasteful.



Instead:



```text

First time:

Prompt

&#x20; ↓

Compute K and V

&#x20; ↓

Store K and V

&#x20; ↓

KV Cache

```



Then:



```text

Next token

&#x20;   ↓

Compute K/V only for new token

&#x20;   ↓

Look at cached K/V

&#x20;   ↓

Generate next token

```



So:



> \*\*KV-cache = remember the expensive attention state you've already computed so you don't calculate it again.\*\*



The source describes KV-cache/inference optimization more broadly as techniques that persist previously computed attention K/V while also optimizing memory movement, batching, and scheduling. 



\---



\# 2. Quick Technical Explanation



During transformer attention, each token gets three representations:



```text

Q = Query

K = Key

V = Value

```



Attention is conceptually:



```text

Attention(Q,K,V)

&#x20;      │

&#x20;      ├── Q → What am I looking for?

&#x20;      ├── K → What information does each token contain?

&#x20;      └── V → What information should I retrieve?

```



During autoregressive generation, the previous tokens' \*\*K and V don't change\*\*.



Therefore, instead of recomputing them:



```text

Previous tokens

&#x20;     ↓

K₁ K₂ K₃ K₄ ...

V₁ V₂ V₃ V₄ ...

&#x20;     ↓

&#x20;     CACHE

```



At the next decoding step:



```text

New token

&#x20;  ↓

New Q, K, V

&#x20;  ↓

Q attends to

cached K/V + new K/V

&#x20;  ↓

Next token

```



The source specifically describes the production mechanism as:



> \*\*Prefill → store K/V → incremental decode → paged/batched serving.\*\* 



\---



\# 3. What Problem Does It Solve?



\## The problem



LLMs generate autoregressively.



That means:



```text

Token 1

&#x20; ↓

Token 2

&#x20; ↓

Token 3

&#x20; ↓

Token 4

&#x20; ↓

...

```



At every step, the model needs information from the previous context.



Without KV-cache, you're repeatedly doing work like:



```text

Step 1:

Calculate K/V for token 1



Step 2:

Calculate K/V for token 1 + token 2



Step 3:

Calculate K/V for token 1 + token 2 + token 3



Step 4:

Calculate K/V for token 1 + token 2 + token 3 + token 4

```



A lot of that is repeated.



\### KV-cache changes this



```text

Prefill:

Prompt → calculate K/V once → store



Decode 1:

New token → calculate only new K/V → use cache



Decode 2:

New token → calculate only new K/V → use cache



Decode 3:

New token → calculate only new K/V → use cache

```



So:



```text

Without cache

Repeated computation

&#x20;      ↓

Wasted work



With cache

Reuse previous K/V

&#x20;      ↓

Less recomputation

```



The important engineering point from the source is that \*\*removing one bottleneck doesn't mean the system is now free of bottlenecks\*\*. The pressure moves toward \*\*KV bandwidth and fragmentation\*\*. 



\---



\# 4. Layman Analogy — A Restaurant Kitchen



Imagine a restaurant receiving a large order.



The kitchen has already prepared:



```text

Rice

Chicken

Sauce

Vegetables

```



Now another dish requires the same rice and sauce.



Would you throw everything away and cook the rice again?



No.



You keep the prepared ingredients and reuse them.



That's KV-cache.



```text

Expensive preparation

&#x20;       ↓

Store prepared state

&#x20;       ↓

Reuse it

&#x20;       ↓

Only prepare the new portion

```



But now imagine \*\*1,000 customers\*\*.



Your refrigerator starts filling up.



Eventually:



```text

More customers

&#x20;    ↓

More stored ingredients

&#x20;    ↓

More refrigerator memory

&#x20;    ↓

Less available space

&#x20;    ↓

You need better storage management

```



That's exactly the KV-cache scaling problem.



\---



\# 5. Core Mental Model



Keep this picture in your head:



```text

&#x20;                   PROMPT

&#x20;                      │

&#x20;                      ▼

&#x20;                  PREFILL

&#x20;                      │

&#x20;                Compute K/V

&#x20;                      │

&#x20;                      ▼

&#x20;                ┌───────────┐

&#x20;                │ KV CACHE  │

&#x20;                └───────────┘

&#x20;                      │

&#x20;                      │

&#x20;         ┌────────────┴────────────┐

&#x20;         ▼                         ▼

&#x20;     New token                Cached history

&#x20;         │                         │

&#x20;      K/V new ─────────────────────┤

&#x20;         │                         │

&#x20;         └──────────┬──────────────┘

&#x20;                    ▼

&#x20;                 ATTENTION

&#x20;                    │

&#x20;                    ▼

&#x20;               NEXT TOKEN

&#x20;                    │

&#x20;                    ▼

&#x20;             Append new K/V

&#x20;                    │

&#x20;                    └──────→ KV CACHE

```



The cache is therefore \*\*state\*\*.



And the deeper engineering question becomes:



> \*\*Where do we keep this state, how much does it cost, and how do we allocate it efficiently?\*\*



That's why the source says generation becomes more of a \*\*state-management and memory-bandwidth workload\*\* at scale rather than simply a matrix-multiplication workload. 



\---



\# 6. Under the Hood — Step by Step



There are two major phases.



\## Phase A — Prefill



Suppose the prompt is:



```text

"The cat sat on the"

```



The model processes the whole prompt.



Conceptually:



```text

"The" → K₁,V₁

"cat" → K₂,V₂

"sat" → K₃,V₃

"on" → K₄,V₄

"the" → K₅,V₅

```



These are stored:



```text

KV Cache:



K₁ V₁

K₂ V₂

K₃ V₃

K₄ V₄

K₅ V₅

```



This is called \*\*prefill\*\*.



\---



\## Phase B — Decode



Now the model generates:



```text

"mat"

```



The newly generated token gets:



```text

K₆

V₆

```



We don't throw away the old cache.



We append:



```text

K₁ V₁

K₂ V₂

K₃ V₃

K₄ V₄

K₅ V₅

K₆ V₆

```



Then the next token can attend over the complete history.



\---



\## Next step



Suppose the model generates:



```text

"and"

```



Only the new token's K/V needs to be added:



```text

K₇

V₇

```



Now:



```text

K₁ V₁

K₂ V₂

K₃ V₃

K₄ V₄

K₅ V₅

K₆ V₆

K₇ V₇

```



And so on.



This is why the cache grows with sequence length.



\---



\# 7. The Important Formula



The source gives:



$$

M\_{KV} \\approx 2LTH\_d \\cdot bytes

$$



Let's decode it.



| Symbol     | Meaning                                      |

| ---------- | -------------------------------------------- |

| \\(M\_{KV}\\) | KV-cache memory                              |

| \\(L\\)      | number of transformer layers                 |

| \\(T\\)      | sequence length / number of tokens           |

| \\(H\_d\\)    | hidden dimension per relevant representation |

| `bytes`    | bytes used per stored value                  |



The `2` is there because we're storing:



```text

K + V

```



So conceptually:



$$

\\text{KV Memory}

\\propto

\\text{layers}

\\times

\\text{tokens}

\\times

\\text{hidden representation}

\\times

2

$$



The most important part is:



$$

\\boxed{M\_{KV} \\propto T}

$$



So if the sequence gets longer, the KV cache gets larger.



And if you have many concurrent requests:



```text

Request 1 → KV cache

Request 2 → KV cache

Request 3 → KV cache

...

Request N → KV cache

```



total memory pressure can become enormous.



\---



\# 8. Small Numerical Example



Suppose, purely for intuition:



```text

Layers = 32

Tokens = 1,000

Hidden dimension = 4,096

Bytes/value = 2

```



Using the simplified formula:



$$

M\_{KV}

\\approx

2 \\times 32 \\times 1000 \\times 4096 \\times 2

$$



That's:



$$

524,288,000\\ bytes

$$



≈ \*\*524 MB\*\* under this simplified formulation.



Now suppose you have:



```text

10 concurrent requests

```



You could be around:



```text

524 MB × 10

≈ 5.24 GB

```



And that's only the KV-cache component under the simplified assumptions.



This is the key scaling intuition:



```text

Longer context

&#x20;     +

More concurrent requests

&#x20;     ↓

More KV state

&#x20;     ↓

More GPU memory pressure

```



\*\*Additional context:\*\* Real model architectures can have different K/V head dimensions and sharing schemes, so the exact memory calculation can differ from this simplified formula.



\*\*Recent real-world example (2026):\*\* DeepSeek-V4.1-Flash reports a global KV cache of \*\*890 bytes per token\*\*. The simplified example above works out to 524,288,000 bytes ÷ 1,000 tokens = \*\*524,288 bytes per token\*\*. That is roughly 590× larger. The two are different models, so this is not a fair benchmark. It only shows how much room real designs have to shrink KV state by sharing it across layers, storing it in fewer bits, and moving it to cheaper storage. See the case study near the end of this chapter.



\---



\# 9. Why KV-Cache Becomes the Problem



Here's the interesting part.



Initially:



```text

Without KV cache

&#x20;      ↓

Huge repeated computation

&#x20;      ↓

KV cache

&#x20;      ↓

Much less recomputation

```



Great.



But now:



```text

More tokens

&#x20;   ↓

More cached K/V

&#x20;   ↓

More GPU memory

```



And with concurrent users:



```text

User A ──→ KV

User B ──→ KV

User C ──→ KV

User D ──→ KV

...

User N ──→ KV

```



Eventually:



```text

GPU memory

████████████████████

&#x20;         ↑

&#x20;      KV cache

```



You have less room for additional requests.



So the optimization creates a \*\*new resource cost\*\*.



That is the fundamental trade-off.



\---



\# 10. Scaling and Trade-offs



The source emphasizes that the practical bottleneck may become \*\*KV bandwidth and fragmentation before raw compute\*\*. 



Think of the system like this:



```text

Workload increases

&#x20;      │

&#x20;      ├── sequence length ↑

&#x20;      ├── concurrency ↑

&#x20;      ├── requests ↑

&#x20;      └── model scale ↑

&#x20;             │

&#x20;             ▼

&#x20;         KV state ↑

&#x20;             │

&#x20;             ▼

&#x20;    Memory pressure ↑

&#x20;             │

&#x20;             ▼

&#x20;   Fragmentation / bandwidth

&#x20;             │

&#x20;             ▼

&#x20;     Capacity decreases

```



So the question isn't simply:



> "What's the Big-O?"



Instead:



> \*\*Which resource saturates first on my actual hardware and workload?\*\*



The source explicitly gives this request-latency decomposition:



$$

T\_{request}

=

T\_{queue}

\+

T\_{compute}

\+

T\_{memory}

\+

T\_{network}

\+

T\_{validation}

$$



This is much more useful operationally because it tells you that compute isn't necessarily the only—or even dominant—source of latency. 



\---



\# 11. Production Architecture



\## Offline / Async



The generic production pipeline from the source is:



```text

Data / Artifacts

&#x20;     ↓

Version + Validate

&#x20;     ↓

Build / Train / Index

&#x20;     ↓

Evaluate + Promote

```



This prepares the artifacts used by the serving system. 



\---



\## Online / Critical Path



During a real user request:



```text

User Request

&#x20;     ↓

Validate / Admit

&#x20;     ↓

KV Cache + Inference Optimization

&#x20;     ↓

Verify / Guard

&#x20;     ↓

Response

&#x20;     +

Telemetry

```



The source recommends several practical mechanisms:



```text

Paged / block KV allocation

&#x20;         +

Continuous batching

&#x20;         +

Prefix caching

&#x20;         +

Admission control

&#x20;         +

Cache-aware scheduling

```



These aren't random optimizations. They're ways of managing the \*\*new bottleneck created by cached state\*\*. 



\---



\# 12. Why Paged KV Cache?



This is one of the most important ideas in the material.



Imagine you have:



```text

GPU memory:



\[Request A]\[Request A]\[Request A]\[free]\[Request B]\[free]\[Request C]

```



Different requests have different lengths.



As requests arrive and finish, you can end up with small holes.



That's \*\*fragmentation\*\*.



Even if total free memory is technically large enough, you may not have memory arranged in the right way for the next request.



\### Traditional approach



Think:



```text

Request A → reserve one big continuous region

Request B → reserve another region

Request C → reserve another region

```



Problem:



```text

Different request lengths

&#x20;       ↓

Different allocation sizes

&#x20;       ↓

Unused gaps

&#x20;       ↓

Fragmentation

&#x20;       ↓

Lower concurrency

```



\---



\## Paged allocation



Instead, divide memory into fixed-size blocks:



```text

GPU Memory



┌─────┬─────┬─────┬─────┬─────┬─────┐

│ B1  │ B2  │ B3  │ B4  │ B5  │ B6  │

└─────┴─────┴─────┴─────┴─────┴─────┘

```



A request can use:



```text

Request A → B1 → B4 → B5

Request B → B2 → B6

Request C → B3

```



They don't necessarily need one giant contiguous region.



This is the central idea behind \*\*PagedAttention\*\*.



\---



\# 13. vLLM Case Study



The source uses \*\*vLLM / PagedAttention\*\* as the production case study.



The problem:



```text

Variable request lengths

&#x20;       ↓

KV-cache fragmentation

&#x20;       +

Over-reservation

&#x20;       ↓

Less concurrent batching

&#x20;       ↓

Capacity / latency problems

```



The design intervention:



```text

KV Cache

&#x20;  ↓

Fixed-size blocks

&#x20;  ↓

Logical block tables

&#x20;  ↓

More flexible memory allocation

```



The source summarizes the causal chain as:



```text

variable lengths

&#x20;      ↓

fragmented KV memory

&#x20;      ↓

smaller batches

&#x20;      ↓

paged allocation

```



The general engineering lesson given is important:



> \*\*Memory management can increase throughput without changing model weights or model quality.\*\* 



That's a very useful AI-infrastructure insight.



Sometimes you don't need a better model.



You need a better \*\*runtime\*\*.



\---



\# 14. Continuous Batching



Suppose:



```text

Request A → needs 100 tokens

Request B → needs 10 tokens

Request C → needs 50 tokens

```



A naive batching strategy may wait for an entire batch to finish.



But generation lengths differ.



That creates wasted capacity.



\*\*Continuous batching\*\* allows the serving system to dynamically manage requests as tokens are generated and requests finish.



Conceptually:



```text

Time →



A █████████████████

B ████

C █████████

D      ███████████

E          █████

```



Instead of treating the entire batch as one rigid unit, the scheduler keeps the GPU occupied with available work.



This connects to the source's research reference:



\*\*Orca (Yu et al., 2022)\*\* introduced iteration-level scheduling to improve throughput for heterogeneous generation lengths. 



\---



\# 15. Prefix Caching



Another optimization mentioned by the source is \*\*prefix caching\*\*.



Suppose many users send requests beginning with:



```text

System prompt

\+

Company documentation

\+

Common instructions

\+

User question

```



The common prefix may be identical.



Instead of computing the same prefix state repeatedly:



```text

Request A ──┐

Request B ──┼──→ Same prefix

Request C ──┘

&#x20;               ↓

&#x20;          Reusable state

```



The system can reuse that state where supported.



Again, you're exchanging:



```text

More stored state

&#x20;      ↕

Less repeated computation

```



\---



\# 16. What Usually Goes Wrong



The source identifies three major classes of failure.



\## Failure 1 — Quality/correctness regression



```text

Long requests

&#x20;    ↓

More state

&#x20;    ↓

Eviction / fragmentation

&#x20;    ↓

Capacity pressure

&#x20;    ↓

Potential system behavior problems

```



The recommended diagnostic approach is to \*\*slice the workload by input regime and inspect intermediate state\*\*, rather than blindly tuning one global threshold. 



\---



\## Failure 2 — p99 / capacity collapse



Cause:



```text

KV bandwidth + fragmentation

```



Detection:



```text

Workload shape

&#x20;     +

Concurrency

&#x20;     +

Live resource utilization

&#x20;     +

Tail latency

```



Then:



```text

Bound state

OR

change scheduling/partitioning

OR

reduce work

```



The important idea is that average latency can look fine while the tail is collapsing.



\---



\## Failure 3 — Looks great offline, fails online



Maybe your benchmark says:



```text

Latency ↓ 20%

```



But production says:



```text

p99 ↑

capacity ↓

OOM ↑

```



Why?



Because your benchmark distribution didn't match production.



The source recommends comparing \*\*production traces with evaluation slices\*\* and adding deployment-shaped regressions and independent quality gates. 



\---



\# 17. The Performance Metrics You Should Watch



Don't only measure:



```text

Average latency

```



You should think about:



```text

&#x20;                   ┌── p50

Latency ────────────┼── p95

&#x20;                   └── p99



Throughput

Memory utilization

KV-cache utilization

Queue time

Compute time

Memory time

Concurrency

Request length

Generation length

```



For example:



```text

p50 = 200 ms

p95 = 500 ms

p99 = 5 seconds

```



Average latency could look acceptable while 1% of users experience terrible latency.



That's why the source repeatedly emphasizes \*\*tail behavior\*\*. 



\---



\# 18. The Three Optimization Levels



The source gives a useful progression.



| Approach              | Main characteristic                                         |

| --------------------- | ----------------------------------------------------------- |

| Simple baseline       | Easy to reason about, low operational complexity            |

| Production baseline   | Measured, guarded, explicitly manages resources             |

| Advanced optimization | Specialized, potentially much better, but higher complexity |



The key principle is:



> \*\*Don't optimize because an optimization exists. Optimize because you've measured a bottleneck.\*\* 



This is probably one of the most important engineering lessons in the whole chapter.



\---



\# 19. Common Misunderstandings



\## Misconception 1



> "More compute automatically gives better results."



Reality:



A system can become constrained by memory, bandwidth, queueing, synchronization, etc.



```text

More compute

&#x20;   ≠

More useful capacity

```



\---



\## Misconception 2



> "Big-O tells me the production bottleneck."



Not necessarily.



Complexity notation abstracts away:



```text

hardware

memory movement

network

synchronization

queueing

execution topology

```



So:



```text

Theoretical complexity

&#x20;       ≠

Actual production latency

```



\---



\## Misconception 3



> "If the prototype works, production is solved."



No.



Production needs:



```text

Versioning

Observability

Isolation

Rollback

Evaluation

Explicit state ownership

```



The source explicitly makes this distinction. 



\---



\# 20. Where Does It Start Hurting?



The interesting threshold is:



```text

KV state growth

&#x20;      ↓

GPU memory pressure

&#x20;      ↓

Fragmentation / bandwidth pressure

&#x20;      ↓

Reduced concurrency

&#x20;      ↓

Queueing

&#x20;      ↓

p95/p99 latency

&#x20;      ↓

Capacity collapse

```



So when planning capacity, don't just ask:



> "How much GPU compute do I have?"



Ask:



> \*\*"How much live KV state can this GPU sustain for my actual request-length and concurrency distribution?"\*\*



That's the more useful production question.



\---



\# 21. Research Background



The source highlights two important research anchors.



\## 1. PagedAttention — Kwon et al., 2023



\### Problem



LLM serving had inefficient KV-cache allocation.



Variable-length requests caused:



```text

KV memory

&#x20;  ↓

fragmentation

&#x20;  +

over-allocation

&#x20;  ↓

wasted memory

```



\### Key idea



Treat KV-cache allocation more like \*\*paged memory management\*\*.



```text

KV Cache

&#x20;  ↓

Fixed-size blocks

&#x20;  ↓

Logical mapping

&#x20;  ↓

Less fragmentation

&#x20;  ↓

Better utilization

```



The source says the work demonstrated reduced fragmentation and enabled sharing, while practitioners use paged/block allocation and continuous batching as core serving primitives. 



\---



\## 2. Orca — Yu et al., 2022



\### Problem



Generation requests have different lengths.



Rigid batching wastes resources.



\### Key idea



\*\*Iteration-level scheduling.\*\*



Instead of treating the whole generation request as one indivisible batch:



```text

Request

&#x20; ↓

iteration

&#x20; ↓

iteration

&#x20; ↓

iteration

```



the scheduler can make decisions at finer granularity.



This improves throughput for heterogeneous generation lengths according to the source. 



\---



\# 22. Research Discipline



Don't interpret:



> "Paper improved throughput by X%"



as:



> "This always improves throughput by X%."



The result depends on:



```text

Model

\+

Hardware

\+

Workload

\+

Dataset

\+

Sequence lengths

\+

Concurrency

\+

Metric

```



So the research-to-production chain should be:



```text

Claim

&#x20;↓

Assumption

&#x20;↓

Measurement

&#x20;↓

Failure boundary

&#x20;↓

Rollback criterion

```



This is explicitly the research/production checkpoint in the material. 



\---



\## 3. DeepSeek-V4.1-Flash — DeepSeek-AI, September 2026 (update)



\### Problem



Agentic workloads send very long, input-heavy contexts (up to 1M tokens). Prefill compute, GPU memory for KV, and KV storage/bandwidth all become expensive at the same time.



\### Key idea



Attack the KV state from several sides at once, instead of only fixing allocation.



```text

KV state too big

&#x20;↓

Share it across layers      (CSA2)

+

Store it in fewer bits      (FP4)

+

Keep less of it on disk     (SWA Bounded Replay)

+

Do less prefill work        (Causal Encoder-Decoder)

&#x20;↓

Smaller HBM footprint + smaller persistent cache

```



PagedAttention manages KV memory better. This paper makes KV memory smaller. They solve different parts of the problem and can be used together. The numbers are reported by the authors on their own model and workload. Apply the research-discipline checkpoint above before trusting them elsewhere.



\---



\# 23. AI/ML Engineer Perspective



As an AI/ML engineer, you should be able to answer:



\### What state am I storing?



```text

K/V representations

```



\### Why am I storing it?



```text

Avoid recomputation

```



\### What does it cost?



```text

GPU memory

\+

memory bandwidth

\+

allocation complexity

```



\### What should I monitor?



```text

KV utilization

GPU memory

request length

concurrency

queue time

p95/p99

throughput

OOM/eviction behavior

```



\### What should I optimize?



Not necessarily the model.



Potentially:



```text

memory allocation

batching

scheduling

prefix reuse

admission control

```



\---



\# 24. Staff / Senior AI Engineer Perspective



At senior level, the question changes.



It's no longer:



> "How does KV-cache work?"



It's:



> \*\*"What is the binding constraint of my serving system?"\*\*



For example:



```text

GPU compute saturated?

&#x20;       ↓

Optimize compute / batching



Memory saturated?

&#x20;       ↓

Optimize KV allocation / quantization / context



KV fragmentation?

&#x20;       ↓

Paged allocation



Queueing?

&#x20;       ↓

Admission / scheduling / capacity



Long-tail latency?

&#x20;       ↓

Investigate p95/p99 and workload distribution

```



The source's deeper principle is:



> \*\*Progress often comes from changing the binding constraint.\*\* 



That is a very strong systems-engineering mindset.



\---



\# 25. First-Principles Thinking



Here are the questions you should be able to reason through.



\### Question 1



\*\*Why does KV-cache exist?\*\*



Because previous tokens' K/V representations can be reused during autoregressive decoding.



\---



\### Question 2



\*\*Why does the cache become a problem?\*\*



Because:



```text

More tokens

&#x20;   ↓

More stored K/V

&#x20;   ↓

More memory

```



and:



```text

More concurrent requests

&#x20;   ↓

More independent KV state

```



\---



\### Question 3



\*\*Why does paging help?\*\*



Because variable-sized allocation can cause fragmentation.



Fixed-size blocks allow more flexible allocation.



\---



\### Question 4



\*\*Why isn't reducing compute automatically enough?\*\*



Because the system can move from:



```text

compute-bound

```



to:



```text

memory-bandwidth-bound

```



or:



```text

memory-capacity-bound

```



or:



```text

queue-bound

```



Optimization often \*\*moves the bottleneck\*\* rather than eliminating bottlenecks altogether.



\---



\### Question 5



\*\*Why can an optimization improve average latency but hurt p99?\*\*



Because production workloads aren't uniform.



A technique may help the typical request while making long requests or high-concurrency cases worse.



\---



\# 26. Interview Answer — 30–45 Seconds



You can say:



> \*\*"KV-cache is a technique used during autoregressive LLM inference where we persist previously computed attention keys and values so we don't recompute them for every generated token. During prefill, we compute the K/V state for the prompt, and during decode we only compute the new token's K/V and attend over the cached history. This reduces recomputation, but the trade-off is that KV state grows with sequence length and concurrency, so memory capacity, bandwidth, and fragmentation can become the new bottlenecks. In production, techniques like paged KV allocation, continuous batching, prefix caching, admission control, and cache-aware scheduling help manage that state. I would measure p95/p99 latency, throughput, KV utilization, memory pressure, and workload distribution rather than relying only on average benchmark results."\*\*



That captures the central mechanism, trade-off, production implications, and measurement mindset from the source. 



\---



\# 27. Follow-up Interview Questions



\### Beginner



\*\*Q: What does KV stand for?\*\*



Key and Value.



\*\*Q: Why don't we cache Query?\*\*



The source focuses on persisting previously computed K/V during autoregressive decoding; Q is generated for the current decoding step rather than representing reusable history.



\*\*Q: When is the cache created?\*\*



During prefill, the model computes the prompt's K/V state.



\---



\### Intermediate



\*\*Q: Why does KV-cache memory grow with sequence length?\*\*



Because each additional token contributes additional K/V state that must be retained for future attention.



\*\*Q: Why does concurrency matter?\*\*



Because each active request can carry its own live KV state.



\*\*Q: What is fragmentation?\*\*



Usable memory becomes split into inefficient gaps or allocations, reducing how effectively available memory can support concurrent requests.



\---



\### Senior



\*\*Q: Why does PagedAttention help?\*\*



It treats KV allocation using fixed-size blocks and logical mappings, reducing fragmentation and over-reservation.



\*\*Q: What would you monitor in production?\*\*



At minimum:



```text

p50/p95/p99 latency

throughput

queue time

GPU memory

KV utilization

request length

generation length

concurrency

OOM/eviction behavior

```



\*\*Q: Besides paged allocation, how can you reduce KV-cache cost?\*\*



Paging fixes fragmentation, but the state itself can also be made smaller or cheaper to keep:



```text

Share      → reuse K/V (and sparse-attention indices) across layers

Shrink     → store K/V in fewer bits (for example FP4 or FP8)

Move       → tier storage: GPU HBM → host DRAM → SSD

Recompute  → rebuild a small piece of state instead of storing it

```



Each lever trades memory for something else: possible quality loss, extra latency, or extra complexity. Measure quality and p99 after each change.



\*\*Q: How would you decide whether an optimization is worth deploying?\*\*



```text

Measured bottleneck

&#x20;      ↓

Optimization addresses bottleneck

&#x20;      ↓

Quality remains acceptable

&#x20;      ↓

SLO remains acceptable

&#x20;      ↓

Operational complexity is justified

&#x20;      ↓

Deploy

```



\---



\# 28. Connected Concepts



This topic sits inside the broader LLM serving stack:



```text

Training

&#x20;  ↓

Transformer Architecture

&#x20;  ↓

Attention

&#x20;  ↓

Autoregressive Generation

&#x20;  ↓

&#x20;       ┌──────────────┐

&#x20;       │  KV CACHE    │

&#x20;       └──────────────┘

&#x20;              ↓

&#x20;    Inference Optimization

&#x20;              ↓

&#x20;    Batching / Scheduling

&#x20;              ↓

&#x20;    Memory Management

&#x20;              ↓

&#x20;     Distributed Serving

&#x20;              ↓

&#x20;      Observability

&#x20;              ↓

&#x20;      Production SLOs

```



The source itself recommends thinking of this as:



```text

Architecture

&#x20;    ↓

Training objective

&#x20;    ↓

Optimization

&#x20;    ↓

Inference/runtime

&#x20;    ↓

Distributed systems

&#x20;    ↓

Evaluation

&#x20;    ↓

Safety/reliability

```



and selecting adjacent concepts based on \*\*what produces the inputs, what consumes the outputs, what resource becomes scarce, and how failure is detected\*\*. 



\---



\# 29. The Most Important Concept: Binding Constraint



This is the deeper lesson I would want you to remember.



Imagine your system initially looks like:



```text

&#x20;                   BOTTLENECK

&#x20;                      ↓

GPU Compute ████████████████████

Memory      ███████

Network     ████

Queue       ██

```



You optimize compute.



Now:



```text

GPU Compute ███████

Memory      ████████████████████  ← NEW BOTTLENECK

Network     ████

Queue       ██

```



You didn't necessarily make the system "bad."



You \*\*moved the bottleneck\*\*.



Then you optimize memory:



```text

GPU Compute ███████

Memory      ███████

Network     ████

Queue       ████████████████████  ← NEW BOTTLENECK

```



This is why the source says:



> \*\*A strong engineer connects model behavior, statistical assumptions, hardware resources, and operational feedback into one causal model rather than optimizing a metric in isolation.\*\* 



\---



\# 30. One Mental Model



If you remember only one thing, remember this:



```text

LLM generates token by token

&#x20;         ↓

Previous K/V is still useful

&#x20;         ↓

Cache it

&#x20;         ↓

Avoid recomputation

&#x20;         ↓

Inference becomes cheaper

&#x20;         ↓

BUT cached state grows

&#x20;         ↓

GPU memory + bandwidth become important

&#x20;         ↓

Fragmentation reduces usable capacity

&#x20;         ↓

Paged allocation + batching + scheduling

&#x20;         ↓

Better serving efficiency

```



\---



\# One Diagram to Memorize



```text

&#x20;                PROMPT

&#x20;                   │

&#x20;                   ▼

&#x20;                PREFILL

&#x20;                   │

&#x20;                K / V

&#x20;                   │

&#x20;                   ▼

&#x20;             ┌───────────┐

&#x20;             │ KV CACHE  │

&#x20;             └─────┬─────┘

&#x20;                   │

&#x20;         ┌─────────┴─────────┐

&#x20;         │                   │

&#x20;      New Token        Cached History

&#x20;         │                   │

&#x20;       K / V ────────────────┘

&#x20;         │

&#x20;         ▼

&#x20;      ATTENTION

&#x20;         │

&#x20;         ▼

&#x20;     NEXT TOKEN

&#x20;         │

&#x20;         ▼

&#x20;    Append K/V

&#x20;         │

&#x20;         └──────────→ KV CACHE

```



\---



\# Cause → Effect Chain



```text

Autoregressive generation

&#x20;         ↓

Repeated attention over history

&#x20;         ↓

Repeated K/V computation is wasteful

&#x20;         ↓

Cache previous K/V

&#x20;         ↓

Less recomputation

&#x20;         ↓

KV state grows with tokens + concurrency

&#x20;         ↓

Memory bandwidth + fragmentation become bottlenecks

&#x20;         ↓

Paged allocation + batching + scheduling

&#x20;         ↓

Better memory utilization / serving capacity

&#x20;         ↓

More operational complexity

```



\---



\# Recent Case Study — DeepSeek-V4.1-Flash (September 2026)



\*\*System:\*\* DeepSeek-V4.1-Flash / long-context agentic serving. \*\*Evidence:\*\* vendor paper, arXiv 2609.19969 (17 Sep 2026). \*\*Scope:\*\* KV footprint + prefill cost + storage tiers.



\## Binding constraint



Agentic workloads (tool calls, long histories, up to 1M tokens of context) are input-heavy. The paper names three pressures at once: expensive prefill compute, GPU memory (HBM) for the live KV cache, and capacity and bandwidth for storing and moving cached KV (SSD and host memory).



\## Design intervention



Four separate moves, each removing a different cost:



```text

KV COST LEVERS



Share      → CSA2: layers reuse main K/V and sparse-attention indices

Shrink     → FP4 main KV cache

Move       → global KV on SSD, sliding-window KV in host DRAM

Recompute  → SWA Bounded Replay rebuilds a small window on a cache hit

```



\### 1. Causal Encoder-Decoder



The 40 layers are split into a 20-layer encoder and a 20-layer decoder. The decoder's global K/V is projected from the encoder's final hidden state instead of being computed layer by layer. During prefill only about \*\*8B\*\* parameters are activated. During decode about \*\*16B\*\* are activated. The paper says this nearly halves prefill computation, which matters because agent workflows send many large input prompts.



```text

PREFILL                          DECODE

Prompt                           New token

&#x20; ↓                                ↓

Encoder (20 layers)              Encoder + Decoder (all layers)

&#x20; ↓                                ↓

Final encoder state              Uses cached K/V

&#x20; ↓

Project K/V for decoder layers

(no full decoder pass for global attention)

```



\### 2. Compressed Sparse Attention 2 (CSA2)



Instead of every layer building its own KV and its own sparse-attention index, each layer gets a fixed mode:



| Mode    | Main KV                      | Sparse indices (top-K)           |

| ------- | ---------------------------- | -------------------------------- |

| Full    | Computed fresh               | New selection                    |

| Reindex | Reused from an earlier layer | Fresh selection with new queries |

| Reuse   | Reused from an earlier layer | Reused too, so no indexing work  |



Most layers are Reuse layers, so most layers add no new global KV to store. Every layer still keeps its own queries and its own sliding-window KV.



\### 3. FP4 main KV cache



K/V values use the E2M1 format with one E4M3 scale per 16 channels. This nearly halves KV storage, both in HBM and on SSD. It was introduced through quantization-aware training in post-training. The sliding-window KV stays in FP8 because it is more sensitive to quantization. The paper reports only marginal quality loss.



\### 4. SWA Bounded Replay



Sliding-window attention (SWA) keeps the last 128 tokens of state in every layer. Storing that on disk for every cached prefix is expensive. The alternative is to replay only the last 128 tokens through the model when a prefix-cache hit finds the global KV but not the window state.



```text

Prefix cache hit on global KV

&#x20;       ↓

Window KV missing?

&#x20;       ↓

Replay last 128 tokens only

&#x20;       ↓

Rebuild window KV (approximate)

&#x20;       ↓

Continue decoding

```



Rebuilding the window state exactly would need a much longer replay. Bounded replay accepts an approximate state to avoid that cost. The paper reports negligible quality impact. Storage is tiered: global KV stays on SSD, and window KV lives in a host-DRAM pool with a short, minute-scale lifetime.



\## Causal chain



```text

agentic input-heavy load

&#x20;↓

prefill compute + KV memory + KV storage pressure

&#x20;↓

share across layers + FP4 + tiered storage + bounded replay

&#x20;↓

smaller HBM and persistent cache,

at the price of approximate window state and variable prefill latency

```



\## Numbers



| Metric                                  | DeepSeek-V4-Flash | DeepSeek-V4.1-Flash                 |

| --------------------------------------- | ----------------- | ----------------------------------- |

| Global KV cache in HBM                  | About 4× larger   | \*\*890 bytes per token\*\*          |

| Persistent KV cache (SSD / host memory) | Baseline          | About 1/8 of the baseline           |

| Activated parameters                    | See paper         | About 8B in prefill, 16B in decode  |



\## What to measure



| Symptom                                | Root mechanism                                                       | What to measure                                                      |

| -------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |

| Agent requests have slow prefill.      | The full model runs over every input token, including long tool outputs. | Prefill latency, prefix-cache hit rate, tokens per request.      |

| Batch size is capped by GPU memory.    | KV bytes per token are too large for the number of live sequences.   | KV bytes per token, KV utilization, maximum concurrent sequences.    |

| Cache storage is large or slow to reload. | Persistent KV includes state that could be rebuilt cheaply.       | Persistent GB per session, cache-hit latency, replay latency.        |



\*\*Generalizable engineering lesson:\*\* KV cache is a budget with four levers: share it, shrink it, move it, or recompute it. Paging (vLLM) fixes how memory is laid out. This case shows that the amount of state and where it lives are also design choices.



\*\*Limits to keep in mind:\*\* the figures are reported by the vendor on its own model and workload and are not independently reproduced here. Bounded replay uses approximate state, and its cost changes with the cache hit pattern, so tail latency should be watched. Even at 890 bytes per token, a million-token context is still a large amount of state. FP4 storage needs quantization-aware training, so it is not a drop-in change for an existing model.



Sources: \[DeepSeek-V4.1-Flash paper\](https://arxiv.org/abs/2609.19969) · \[Hugging Face paper page\](https://huggingface.co/papers/2609.19969)



\*\*Editorial rule:\*\* system facts above come from the paper as read on 25 Sep 2026. The four-lever framing and the lesson are editorial synthesis, and this case study is an addition to the original chapter material.



\---



\# One-Line Summary



> \*\*KV-cache trades repeated computation for persistent memory: it makes autoregressive generation much more efficient, but at production scale the cache itself becomes a state-management, memory-bandwidth, fragmentation, and scheduling problem.\*\*



