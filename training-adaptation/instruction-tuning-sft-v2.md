\# Instruction Tuning \& SFT



> \*\*One-line idea:\*\* Pre-training teaches a model \*\*what it can learn\*\*; Instruction Tuning / SFT teaches it \*\*how to respond to what we ask it to do\*\*. 



\---



\# 1. Big Idea — What is Instruction Tuning \& SFT?



Imagine you have a pretrained LLM.



It has read enormous amounts of text and learned patterns such as:



\* language structure

\* facts and associations

\* reasoning patterns

\* coding patterns

\* common document structures



But there is a problem:



> \*\*Knowing something is not the same as knowing how to respond to a user's instruction.\*\*



For example, a pretrained model may know what Python is, but that doesn't guarantee it will answer:



> "Explain Python to a beginner in 5 bullet points."



in the format you actually want.



\*\*Instruction tuning / SFT fixes this by showing the model examples of:\*\*



```text

Instruction / Prompt

&#x20;       ↓

Desired Response

```



The model is then trained to reproduce the desired response style and behavior. 



\---



\# 2. What Exactly Is SFT?



\*\*SFT = Supervised Fine-Tuning.\*\*



It is supervised adaptation of a pretrained model using examples like:



```text

Input:

"Explain photosynthesis to a 10-year-old."



Target:

"Photosynthesis is the process by which plants

use sunlight to make food..."

```



The model learns:



```text

Given this kind of instruction

&#x20;           ↓

Produce this kind of response

```



Formally:



> \*\*SFT trains a pretrained model to map task instructions and conversational context to preferred target responses.\*\* 



\---



\# 3. Pre-training vs SFT



This distinction is extremely important.



```text

&#x20;                PRE-TRAINING

&#x20;                     │

&#x20;                     ▼

&#x20;         Learn language/statistical patterns

&#x20;                     │

&#x20;                     ▼

&#x20;               Base LLM

&#x20;                     │

&#x20;                     │

&#x20;                     ▼

&#x20;             INSTRUCTION SFT

&#x20;                     │

&#x20;                     ▼

&#x20;       Learn desired response behavior

&#x20;                     │

&#x20;                     ▼

&#x20;         Instruction-following LLM

```



\### Example



\### Pre-training



The model sees:



```text

The capital of France is

```



and learns to predict:



```text

Paris

```



\### SFT



The model sees:



```text

User:

"What is the capital of France?

Answer in one sentence."

```



and learns:



```text

"The capital of France is Paris."

```



So:



> \*\*Pre-training teaches the model language/statistical structure.\*\*



> \*\*SFT teaches the model how humans want that knowledge expressed in response to instructions.\*\*



The source explicitly frames pretraining as learning distributions/capabilities while SFT addresses desired task behavior and response format. 



\---



\# 4. What Problem Does SFT Solve?



\## Problem



A pretrained model has capabilities, but those capabilities don't uniquely determine:



\* what task to perform

\* how to interpret an instruction

\* how much detail to provide

\* what format to use

\* how to behave conversationally



The source describes this as:



```text

Pretraining

&#x20;   ↓

Learns distributions + capabilities

&#x20;   ↓

BUT

&#x20;   ↓

Doesn't uniquely determine desired behavior

&#x20;   ↓

SFT

&#x20;   ↓

Prompt → Preferred response

```







\---



\# 5. Layman Analogy



Think about teaching a talented employee.



\### Before training



The employee knows:



\* programming

\* mathematics

\* English

\* documentation

\* technical concepts



But you haven't told them how your company expects them to work.



You give them examples:



```text

When customer asks X → respond like this



When user asks Y → format it like this



When task requires Z → perform it like this

```



After seeing many examples, they start following the organization's expected behavior.



That's roughly what SFT does.



```text

Pretraining = knowledge/capability



SFT = behavioral shaping

```



The source explicitly describes SFT as \*\*supervised behavior shaping\*\*. 



\---



\# 6. Core Mental Model



Memorize this:



```text

&#x20;            PRETRAINED MODEL

&#x20;                   │

&#x20;                   ▼

&#x20;            Prompt / Context

&#x20;                   │

&#x20;                   ▼

&#x20;         SFT Training Examples

&#x20;                   │

&#x20;                   ▼

&#x20;       Predict Target Response

&#x20;                   │

&#x20;                   ▼

&#x20;                Loss

&#x20;                   │

&#x20;                   ▼

&#x20;             Backpropagation

&#x20;                   │

&#x20;                   ▼

&#x20;         Update Model Parameters

&#x20;                   │

&#x20;                   ▼

&#x20;      Better Instruction Following

```



The critical idea is:



> \*\*The model is learning a conditional response distribution from demonstrations.\*\* 



\---



\# 7. What Does the Training Data Look Like?



A typical SFT example can look like:



```text

{

&#x20;   "instruction": "Explain recursion",

&#x20;   "input": "",

&#x20;   "output": "Recursion is when a function calls itself..."

}

```



Or conversationally:



```text

User:

Explain recursion with a simple example.



Assistant:

Recursion is when a function calls itself...

```



With many such examples:



```text

Prompt 1 → Good Response 1

Prompt 2 → Good Response 2

Prompt 3 → Good Response 3

Prompt 4 → Good Response 4

...

Prompt N → Good Response N

```



The model learns the statistical relationship between the input context and desired response.



\---



\# 8. Under the Hood



The source gives the following high-level execution process:



```text

1\. Represent the state

&#x20;       ↓

2\. Fine-tune using prompt-response demonstrations

&#x20;       ↓

3\. Apply compute/memory/data constraints

&#x20;       ↓

4\. Preserve required state

&#x20;       ↓

5\. Validate failure boundaries

```







Let's translate that into ML terms.



\---



\## Step 1 — Start with a pretrained model



Suppose we have:



```text

Llama / GPT-like base model

```



with parameters:



$$

\\theta

$$



These parameters already contain the knowledge learned during pretraining.



\---



\## Step 2 — Give it an instruction



Suppose:



```text

x = "Explain transformers simply."

```



Desired answer:



```text

y = "Transformers are neural networks..."

```



Now the model tries to generate the target.



\---



\# 9. The SFT Loss Function



The source gives:



$$

L\_{SFT}

=

\-\\sum\_t \\log p\_\\theta(y\_t|x,y\_{<t})

$$







Let's understand every symbol.



| Symbol       | Meaning                                                 |

| ------------ | ------------------------------------------------------- |

| \\(L\_{SFT}\\)  | SFT training loss                                       |

| \\(x\\)        | input/instruction                                       |

| \\(y\_t\\)      | target token at position \\(t\\)                          |

| \\(y\_{<t}\\)   | target tokens before \\(t\\)                              |

| \\(p\_\\theta\\) | probability predicted by model                          |

| \\(\\theta\\)   | model parameters                                        |

| \\(\\log\\)     | logarithm                                               |

| \\(-\\)        | converts likelihood maximization into loss minimization |



\---



\# 10. What Does the Formula Actually Mean?



Suppose the target response is:



```text

"Paris is the capital."

```



The model generates one token at a time.



```text

Paris

&#x20;  ↓

is

&#x20;  ↓

the

&#x20;  ↓

capital

&#x20;  ↓

.

```



For every token, the model should assign a high probability to the correct next token.



For example:



```text

Input:

"The capital of France is"



Model probabilities:



Paris     → 0.90

London    → 0.03

Berlin    → 0.02

Madrid    → 0.01

...

```



The correct token is:



```text

Paris

```



So the loss is:



$$

\-\\log(0.90)

$$



which is small.



But if the model predicts:



```text

Paris → 0.10

London → 0.60

```



then:



$$

\-\\log(0.10)

$$



is much larger.



Therefore:



```text

Correct response probability ↑

&#x20;       ↓

Loss ↓

&#x20;       ↓

Better training signal

```



\---



\# 11. Why Is It Called "Supervised"?



Because we provide the desired answer.



```text

Input                         Target

────────────────────────────────────────

"Explain AI"           →      "AI is..."

"Translate this"       →      "..."

"Write Python code"    →      "def ..."

```



The target response acts as the supervision.



Compare this with pretraining:



```text

Pretraining:



"The sky is \_\_\_"



Target:

"blue"



```



The training signal comes naturally from the data.



In SFT:



```text

Instruction

&#x20;   ↓

Human/curated/synthetic desired response

&#x20;   ↓

Training target

```



\---



\# 12. Why SFT Changes Behavior



This is the most important conceptual part.



Suppose the pretrained model has many possible responses:



```text

Prompt:

"Explain Docker."



Possible outputs:



A. 2-line explanation

B. 500-word explanation

C. technical explanation

D. beginner explanation

E. tutorial

F. definition

```



SFT data repeatedly shows the model:



```text

Prompt

&#x20; ↓

Preferred answer

```



The training process increases probability around those desired behaviors.



Conceptually:



```text

Before SFT:



&#x20;      many possible behaviors

&#x20;         /  |  |  \\

&#x20;        /   |  |   \\

&#x20;       A    B  C    D





After SFT:



&#x20;      desired behavior

&#x20;             │

&#x20;             ▼

&#x20;       preferred response

```



This is why the source calls SFT \*\*behavior shaping\*\*. 



\---



\# 13. But SFT Does NOT Magically Create New Knowledge



This is a very important distinction.



Suppose the base model doesn't know something.



SFT is not automatically equivalent to:



```text

SFT → magically learn everything

```



Instead, SFT primarily changes the mapping:



```text

Input

&#x20; ↓

Desired behavior/output

```



It can also teach information contained in the fine-tuning data, but the central purpose described here is \*\*behavior shaping and instruction following\*\*.



\---



\# 14. The Biggest Risk: Distribution Narrowing



Now we reach the important engineering problem.



Suppose you train SFT using only:



```text

100,000 customer-support examples

```



The model becomes extremely good at customer support.



But what happens to other capabilities?



Potentially:



```text

General capability

&#x20;      ↓

SFT on narrow domain

&#x20;      ↓

Behavior becomes specialized

&#x20;      ↓

Capability regression / style collapse

```



The source identifies:



> \*\*Overly narrow or duplicated SFT data can cause capability regression, style collapse, or benchmark overfitting.\*\* 



\---



\# 15. What Is Style Collapse?



Imagine the training dataset always contains answers like:



```text

"Certainly! I'd be happy to help you with that..."

```



After enough examples, the model may start producing that style everywhere.



Even when inappropriate.



For example:



```text

User:

What is 2 + 2?



Model:

Certainly! I'd be happy to help you with that.

The answer to this mathematical question is...

```



The model may become overly biased toward the training style.



That's one reason \*\*data diversity matters\*\*.



\---



\# 16. SFT Data Quality Matters More Than "More Data"



A common mistake is:



> "If 100K examples helped, 1M examples must help more."



Not necessarily.



The quality and distribution of the examples matter.



Imagine:



```text

1,000 high-quality diverse examples



vs.



100,000 duplicated / narrow examples

```



The second dataset can potentially produce worse behavior.



The source specifically identifies \*\*data quality and distribution narrowing\*\* as the main practical bottleneck. 



\---



\# 17. Data Distribution Is Extremely Important



Suppose production looks like:



```text

Coding             30%

Reasoning          20%

Summarization      20%

General Q\&A        20%

Domain-specific    10%

```



But your SFT dataset looks like:



```text

Coding             90%

General Q\&A        10%

```



You have a distribution mismatch.



```text

Training distribution

&#x20;       ≠

Production distribution

```



So the model may look excellent on your SFT evaluation but behave poorly in production.



\---



\# 18. SFT vs RLHF / DPO



Think of the larger alignment pipeline:



```text

&#x20;                   PRETRAINING

&#x20;                        │

&#x20;                        ▼

&#x20;                   BASE MODEL

&#x20;                        │

&#x20;                        ▼

&#x20;                      SFT

&#x20;                        │

&#x20;                        ▼

&#x20;            Instruction-following model

&#x20;                        │

&#x20;                        ▼

&#x20;                  RLHF / DPO

&#x20;                        │

&#x20;                        ▼

&#x20;            Preference-aligned model

```



Your uploaded material explicitly places \*\*RLHF / DPO / PPO\*\* as the next topic in the sequence. 



The conceptual difference:



| Stage                   | Main question                                    |

| ----------------------- | ------------------------------------------------ |

| Pretraining             | What patterns can the model learn?               |

| SFT                     | What response should I give to this instruction? |

| Preference optimization | Which response do humans prefer?                 |



\---



\# 19. SFT Production Pipeline



The source recommends a production starting point based around dataset versioning, held-out task slices, and regression suites. 



A practical conceptual pipeline:



```text

&#x20;               RAW DATA

&#x20;                  │

&#x20;                  ▼

&#x20;         Data Cleaning

&#x20;                  │

&#x20;                  ▼

&#x20;      Instruction Formatting

&#x20;                  │

&#x20;                  ▼

&#x20;       Deduplication / Filtering

&#x20;                  │

&#x20;                  ▼

&#x20;         Dataset Versioning

&#x20;                  │

&#x20;                  ▼

&#x20;             SFT TRAINING

&#x20;                  │

&#x20;                  ▼

&#x20;            Evaluation

&#x20;                  │

&#x20;         ┌────────┴────────┐

&#x20;         │                 │

&#x20;      PASS              FAIL

&#x20;         │                 │

&#x20;         ▼                 ▼

&#x20;      Promote          Investigate

&#x20;         │

&#x20;         ▼

&#x20;      Deployment

```



\---



\# 20. Offline vs Online



One subtle point from the source is that the \*\*training process itself belongs in an offline/async path\*\*, while inference is the online critical path.



\### Offline



```text

Data

&#x20;↓

Validate

&#x20;↓

Version

&#x20;↓

Train SFT

&#x20;↓

Evaluate

&#x20;↓

Promote model

```



\### Online



```text

User Request

&#x20;    ↓

Validation

&#x20;    ↓

Inference

&#x20;    ↓

Guard / Verify

&#x20;    ↓

Response

&#x20;    ↓

Telemetry

```



The source's production diagrams emphasize versioning, evaluation, explicit state ownership, replaceable workers, and isolation of slow/failure-prone dependencies. 



\---



\# 21. Where Does SFT Start to Hurt?



The interesting part is that the system can \*\*appear to improve\*\* while actually becoming less general.



```text

SFT benchmark

&#x20;    ↓

Improves

&#x20;    ↓

Looks successful

&#x20;    ↓

But training distribution becomes narrow

&#x20;    ↓

General capabilities regress

&#x20;    ↓

Production edge cases fail

```



The source identifies the major pressure point as:



> \*\*Data diversity and catastrophic style overfitting.\*\* 



\---



\# 22. What Usually Goes Wrong?



| Failure                      | Why it happens                             | What to measure             |

| ---------------------------- | ------------------------------------------ | --------------------------- |

| Capability regression        | Narrow/duplicated SFT data                 | Diverse evaluation slices   |

| Style collapse               | Dataset over-represents one response style | Style/distribution tests    |

| Benchmark overfitting        | Model learns evaluation-like patterns      | Independent evaluation      |

| Offline good, production bad | Evaluation doesn't represent production    | Production-shaped test sets |

| p99/capacity problems        | Resource/state behavior isn't bounded      | Live resource + concurrency |

| Hard-to-rollback model       | Poor artifact/version management           | Model + dataset versioning  |



The source explicitly calls out quality regression, p99/capacity collapse, and offline-good/online-bad failure modes. 



\---



\# 23. SFT Trade-off



The fundamental trade-off can be understood as:



```text

More behavior shaping

&#x20;       ↓

More task-specific behavior

&#x20;       ↓

Potentially less generality

```



So:



$$

\\boxed{\\text{Behavior alignment} \\leftrightarrow \\text{Capability preservation}}

$$



The source describes this as the trade-off between \*\*behavior alignment and capability drift\*\*. 



\---



\# 24. Research Background



The source highlights two important research anchors.



\## 1. Finetuned Language Models Are Zero-Shot Learners



\*\*Wei et al., 2021\*\*



The work showed that multi-task instruction-style fine-tuning can improve generalization to unseen tasks. 



\### Engineering lesson



Instruction data isn't simply about having more examples.



You care about:



```text

Diversity

\+

Quality

\+

Task coverage

```



\---



\## 2. Self-Instruct



\*\*Wang et al., 2022\*\*



The work used model-generated instructions and filtering to bootstrap instruction datasets. 



Conceptually:



```text

Existing LLM

&#x20;    ↓

Generate instructions

&#x20;    ↓

Generate responses

&#x20;    ↓

Filter bad examples

&#x20;    ↓

Create SFT dataset

&#x20;    ↓

Train model

```



This is useful because manually creating millions of examples is expensive.



But it creates another challenge:



```text

Synthetic data

&#x20;     ↓

Quality control

&#x20;     ↓

Contamination control

&#x20;     ↓

Validation

```



The source specifically notes that synthetic data pipelines require quality and contamination controls. 



\---



\# 25. Production Case Study — FLAN / Instruction-Tuned Models



The source uses \*\*FLAN / instruction-tuned models\*\* as the production case study. 



\### Problem



A base next-token model can possess knowledge about many tasks but doesn't necessarily follow user intent consistently.



```text

Base model

&#x20;   ↓

Knows many things

&#x20;   ↓

But task behavior isn't consistently aligned

```



\### Intervention



Train on:



```text

Diverse instructions

&#x20;       +

Desired responses

&#x20;       ↓

SFT

```



\### Resulting conceptual chain



```text

Pretraining prior

&#x20;     ↓

Instruction distribution

&#x20;     ↓

Behavior shaping

&#x20;     ↓

Alignment / generalization trade-off

```



The engineering lesson is important:



> \*\*SFT improves a behavior distribution; it does not eliminate the need to evaluate edge cases.\*\* 



\---



\# 26. AI Engineer Perspective



As an AI engineer, ask:



\### Data



```text

Where does SFT data come from?

How is it cleaned?

How is it deduplicated?

How is it versioned?

```



\### Training



```text

What is the loss?

Which tokens contribute to loss?

What is the training budget?

```



\### Evaluation



```text

Does the model improve on the target task?

Did general capabilities regress?

```



\### Production



```text

What happens at p95/p99?

Can we roll back?

Can we reproduce this model?

```



The source's AI Engineer test emphasizes making the optimization objective, gradient/data path, ownership, metrics, and failure handling explicit. 



\---



\# 27. AI Researcher Perspective



A researcher asks:



> \*\*Why did SFT improve the result?\*\*



Not simply:



> "The benchmark improved."



You should ask:



```text

What was the baseline?

&#x20;       ↓

What changed?

&#x20;       ↓

What dataset?

&#x20;       ↓

What scale?

&#x20;       ↓

What metric?

&#x20;       ↓

Does the result transfer?

```



The source explicitly recommends separating:



\* proven/theoretical claims

\* empirical findings

\* engineering heuristics



and checking whether conclusions survive changes in scale, data distribution, and evaluation metric.  



\---



\# 28. Staff / Senior AI Engineer Perspective



At senior level, the question becomes:



> \*\*Can this training approach survive production complexity?\*\*



Think about:



```text

Dataset version

&#x20;      ↓

Training run

&#x20;      ↓

Checkpoint

&#x20;      ↓

Evaluation

&#x20;      ↓

Model registry

&#x20;      ↓

Deployment

&#x20;      ↓

Monitoring

&#x20;      ↓

Rollback

```



You need to know:



\* where state lives

\* how checkpoints are managed

\* how distributed training is synchronized

\* how results are reproduced

\* what happens during degradation

\* how rollback works



The source specifically highlights optimizer state, distributed synchronization, checkpointing, reproducibility, ownership, degradation behavior, rollback, and observability. 



\---



\# 29. First-Principles Thinking



Reduce the entire topic to:



```text

Required capability

&#x20;       ↓

Binding constraint

&#x20;       ↓

Changed computation

&#x20;       ↓

New resource cost

&#x20;       ↓

New failure mode

```



For SFT:



```text

Need instruction following

&#x20;       ↓

Pretrained model doesn't specify desired behavior

&#x20;       ↓

Train on instruction → response examples

&#x20;       ↓

Model becomes biased toward demonstrated behaviors

&#x20;       ↓

Narrow/duplicated data can cause capability drift

```



This is the \*\*cause → effect chain\*\* you should remember.



The source explicitly recommends this first-principles reduction. 



\---



\# 30. Interview Answer — 30–45 Seconds



If an interviewer asks:



> \*\*"What is Instruction Tuning / SFT?"\*\*



Say:



> \*\*"Instruction tuning, or supervised fine-tuning, is the process of adapting a pretrained language model using instruction-response examples so that it learns to follow tasks and produce preferred responses. Pretraining gives the model broad language and statistical capabilities, but it doesn't uniquely specify how the model should respond to user instructions. During SFT, we minimize conditional negative log likelihood over target responses. The major trade-off is behavior alignment versus capability drift: narrow or duplicated data can cause style collapse or regression in general capabilities. In production, I'd focus not only on benchmark improvement but also on dataset diversity, evaluation slices, versioning, rollback, and p95/p99 behavior."\*\*



This follows the source's interview framing and operational emphasis. 



\---



\# 31. Common Interview Follow-ups



\### Q1. Why do we need SFT if we already have pretraining?



Because:



```text

Pretraining → broad capabilities

SFT         → desired task behavior

```



\---



\### Q2. What loss does SFT use?



Typically conditional negative log likelihood:



$$

L\_{SFT}

=

\-\\sum\_t \\log p\_\\theta(y\_t|x,y\_{<t})

$$







\---



\### Q3. What is the biggest risk?



```text

Narrow / duplicated SFT data

&#x20;         ↓

Distribution narrowing

&#x20;         ↓

Capability regression

Style collapse

Benchmark overfitting

```







\---



\### Q4. Why can offline evaluation look good but production fail?



Because:



```text

Evaluation distribution

&#x20;       ≠

Production distribution

```



The source explicitly recommends comparing production traces against evaluation slices and adding deployment-shaped regressions. 



\---



\### Q5. Is more SFT data always better?



No.



You care about:



```text

Quality

\+

Diversity

\+

Coverage

\+

Distribution

```



not merely dataset size.



\---



\# 32. SFT in the Larger LLM Stack



You should visualize the entire pipeline:



```text

&#x20;                RAW DATA

&#x20;                   │

&#x20;                   ▼

&#x20;            PRETRAINING

&#x20;                   │

&#x20;                   ▼

&#x20;             BASE MODEL

&#x20;                   │

&#x20;                   ▼

&#x20;                 SFT

&#x20;                   │

&#x20;                   ▼

&#x20;      Instruction-following model

&#x20;                   │

&#x20;                   ▼

&#x20;         RLHF / DPO / PPO

&#x20;                   │

&#x20;                   ▼

&#x20;         Preference-aligned model

&#x20;                   │

&#x20;                   ▼

&#x20;           Evaluation / Safety

&#x20;                   │

&#x20;                   ▼

&#x20;             Deployment

&#x20;                   │

&#x20;                   ▼

&#x20;         Monitoring / Feedback

```



The source itself recommends studying SFT as part of:



\*\*architecture → training objective → optimization → inference/runtime → distributed systems → evaluation → safety/reliability.\*\* 



\---



\# 33. The Most Important Distinction



Don't confuse these three:



| Concept                      | Main purpose                                 |

| ---------------------------- | -------------------------------------------- |

| \*\*Pretraining\*\*              | Learn broad statistical structure            |

| \*\*SFT / Instruction Tuning\*\* | Shape desired instruction-following behavior |

| \*\*RLHF / DPO / PPO\*\*         | Optimize toward preference signals           |



So remember:



```text

Pretraining

"What can I learn?"



&#x20;       ↓



SFT

"How should I respond to instructions?"



&#x20;       ↓



Preference optimization

"Which of these possible responses is preferred?"

```



\---



\# 34. The Production Decision Rule



A very important line from the source:



> \*\*Do not treat a better benchmark score as automatically being a deployment decision.\*\*



Instead:



```text

Does it solve the binding constraint?

&#x20;         │

&#x20;         ├── NO → Don't optimize it

&#x20;         │

&#x20;         └── YES

&#x20;               ↓

Does resource/state cost fit SLO?

&#x20;               │

&#x20;               ├── NO → Redesign

&#x20;               │

&#x20;               └── YES

&#x20;                     ↓

Does evaluation match production?

&#x20;                     │

&#x20;                     ├── NO → Improve evaluation

&#x20;                     │

&#x20;                     └── YES → Consider deployment

```







\---



\# 35. One Mental Model to Memorize



```text

PRETRAINING

&#x20;   │

&#x20;   │ learns broad statistical structure

&#x20;   ▼

BASE MODEL

&#x20;   │

&#x20;   │ SFT examples:

&#x20;   │ instruction → desired response

&#x20;   ▼

BEHAVIOR SHAPING

&#x20;   │

&#x20;   ├── better instruction following

&#x20;   │

&#x20;   └── risk:

&#x20;       narrow data

&#x20;       ↓

&#x20;       capability drift

&#x20;       style collapse

&#x20;       overfitting

```



\---



\# 36. One Diagram to Memorize for Interviews



```text

&#x20;       PRETRAINED MODEL

&#x20;              │

&#x20;              ▼

&#x20;      Instruction + Context

&#x20;              │

&#x20;              ▼

&#x20;     Desired Target Response

&#x20;              │

&#x20;              ▼

&#x20;         Token Loss

&#x20;              │

&#x20;              ▼

&#x20;       Backpropagation

&#x20;              │

&#x20;              ▼

&#x20;      Updated Parameters

&#x20;              │

&#x20;              ▼

&#x20;  Better Instruction Following

&#x20;              │

&#x20;              ▼

&#x20;    ┌──────────────────────┐

&#x20;    │ Evaluate Generality  │

&#x20;    │ + Quality + p95/p99  │

&#x20;    └──────────────────────┘

```



\---



\# 37. Cause → Effect Chain



```text

Pretraining gives broad capability

&#x20;           ↓

But desired behavior is underspecified

&#x20;           ↓

Create instruction-response demonstrations

&#x20;           ↓

Optimize conditional response likelihood

&#x20;           ↓

Model learns demonstrated behavior

&#x20;           ↓

Instruction following improves

&#x20;           ↓

But distribution becomes more important

&#x20;           ↓

Narrow/duplicated data can cause capability drift

&#x20;           ↓

Therefore evaluate both target behavior

and preserved general capability

```



\---



\# 38. Final Takeaway



\### In one sentence:



> \*\*SFT is supervised behavior shaping: take a pretrained model and train it on high-quality instruction-response demonstrations so that it learns the response behavior we want.\*\* 



\### If you remember only 5 things:



1\. \*\*Pretraining gives broad capabilities; SFT shapes behavior.\*\*

2\. \*\*SFT learns from instruction → preferred response examples.\*\*

3\. \*\*The core objective is conditional negative log likelihood.\*\*

4\. \*\*Data quality and diversity are critical; narrow/duplicated data can cause capability regression and style collapse.\*\*

5\. \*\*A better benchmark is not enough—production evaluation must match the real deployment distribution.\*\*



