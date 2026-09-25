(function () {
  'use strict';

  /* ============================================================
     Master chapter index — the single source of truth for the
     command palette, fuzzy search, cross-folder next/prev titles,
     and breadcrumbs. [folder, file, title] tuples; folder order
     here IS reading order (matches the homepage TOC).
     ============================================================ */
  var FOLDERS = [
    ['foundations', 'Foundations'],
    ['training-adaptation', 'Training & Adaptation'],
    ['context-retrieval-agents', 'Context, Retrieval & Agents'],
    ['evaluation-safety', 'Evaluation & Safety'],
    ['serving-efficiency', 'Serving & Efficiency'],
    ['emerging-research', 'Emerging Research'],
    ['ml-ops', 'MLOps & Deployment Lifecycle'],
    ['data-ops', 'Data Operations & Engineering'],
    ['dev-ops', 'DevOps & Deployment Engineering'],
    ['computer-vision', 'Computer Vision'],
    ['deep-reinforcement-learning', 'Deep Reinforcement Learning']
  ];
  var FOLDER_LABEL = {};
  FOLDERS.forEach(function (f) { FOLDER_LABEL[f[0]] = f[1]; });
  // short labels for the topbar strip only — full names stay in the flyout
  // header, the left sidebar and breadcrumbs where there's room for them
  var TOPBAR_LABEL = {
    'foundations': 'Foundations', 'training-adaptation': 'Training', 'context-retrieval-agents': 'Context/Agents',
    'evaluation-safety': 'Evaluation', 'serving-efficiency': 'Serving', 'emerging-research': 'Research',
    'ml-ops': 'MLOps', 'data-ops': 'Data Ops', 'dev-ops': 'DevOps',
    'computer-vision': 'Vision', 'deep-reinforcement-learning': 'RL'
  };

  var RAW = [
    ['foundations', 'attention-mechanism.html', 'Attention Mechanism'],
    ['foundations', 'transformer-architecture.html', 'Transformer Architecture'],
    ['foundations', 'positional-encoding.html', 'Positional Encoding'],
    ['foundations', 'tokenization.html', 'Tokenization'],
    ['foundations', 'scaling-laws.html', 'Scaling Laws'],
    ['training-adaptation', 'mixture-of-experts.html', 'Mixture of Experts'],
    ['training-adaptation', 'kv-cache-inference-optimization.html', 'KV-Cache & Inference Optimization'],
    ['training-adaptation', 'quantization.html', 'Quantization'],
    ['training-adaptation', 'pretraining-objectives.html', 'Pre-training Objectives'],
    ['training-adaptation', 'instruction-tuning-sft.html', 'Instruction Tuning & SFT'],
    ['training-adaptation', 'rlhf-dpo-ppo.html', 'RLHF / DPO / PPO'],
    ['training-adaptation', 'constitutional-ai-rl-aif.html', 'Constitutional AI / RL-AIF'],
    ['training-adaptation', 'overfitting-in-llms.html', 'Overfitting in LLMs'],
    ['training-adaptation', 'learning-rate-schedules.html', 'Learning Rate Schedules'],
    ['training-adaptation', 'gradient-checkpointing-zero.html', 'Gradient Checkpointing & ZeRO'],
    ['training-adaptation', 'lora-qlora-full-finetuning-tradeoffs.html', 'LoRA / QLoRA / Full Fine-tuning Trade-offs'],
    ['context-retrieval-agents', 'context-engineering.html', 'Context Engineering'],
    ['context-retrieval-agents', 'rag.html', 'RAG'],
    ['context-retrieval-agents', 'vector-databases-ann.html', 'Vector Databases & ANN'],
    ['context-retrieval-agents', 'self-rag-flare-corrective-rag.html', 'Self-RAG / FLARE / Corrective RAG'],
    ['context-retrieval-agents', 'long-context-models.html', 'Long-Context Models'],
    ['context-retrieval-agents', 'agent-frameworks.html', 'Agent Frameworks'],
    ['context-retrieval-agents', 'memory-systems-for-agents.html', 'Memory Systems for Agents'],
    ['context-retrieval-agents', 'structured-output-json-function-calling.html', 'Structured Output / JSON Mode / Function Calling'],
    ['evaluation-safety', 'llm-evaluation.html', 'LLM Evaluation'],
    ['evaluation-safety', 'red-teaming-jailbreaks.html', 'Red-Teaming & Jailbreaks'],
    ['evaluation-safety', 'hallucination-detection-mitigation.html', 'Hallucination Detection & Mitigation'],
    ['evaluation-safety', 'bias-fairness-in-llms.html', 'Bias & Fairness in LLMs'],
    ['evaluation-safety', 'interpretability.html', 'Interpretability'],
    ['evaluation-safety', 'constitutional-ai-self-correction.html', 'Constitutional AI / Self-Correction'],
    ['serving-efficiency', 'llm-serving.html', 'LLM Serving'],
    ['serving-efficiency', 'speculative-decoding.html', 'Speculative Decoding'],
    ['serving-efficiency', 'model-parallelism.html', 'Model Parallelism'],
    ['serving-efficiency', 'distillation.html', 'Distillation'],
    ['serving-efficiency', 'multimodal-llms.html', 'Multi-Modal LLMs'],
    ['serving-efficiency', 'model-merging.html', 'Model Merging'],
    ['serving-efficiency', 'test-time-compute.html', 'Test-Time Compute'],
    ['serving-efficiency', 'emergent-abilities-capabilities-scaling.html', 'Emergent Abilities & Capabilities Scaling'],
    ['serving-efficiency', 'inference-time-scaling-laws.html', 'Inference-Time Scaling Laws'],
    ['emerging-research', 'neural-architecture-search-for-llms.html', 'Neural Architecture Search for LLMs'],
    ['emerging-research', 'state-space-models-mamba-jamba.html', 'State Space Models (Mamba, Jamba)'],
    ['emerging-research', 'diffusion-models-for-language.html', 'Diffusion Models for Language'],
    ['emerging-research', 'world-models-llm-planners.html', 'World Models / LLM Planners'],
    ['emerging-research', 'federated-learning-for-llms.html', 'Federated Learning for LLMs'],
    ['emerging-research', 'neural-symbolic-integration.html', 'Neural Symbolic Integration'],
    ['ml-ops', 'ml-lifecycle-and-baselines.html', 'ML Lifecycle & Production Baselines'],
    ['ml-ops', 'model-resource-management-pruning.html', 'Model Compression: Pruning & Resource Management'],
    ['ml-ops', 'high-performance-distributed-training.html', 'High-Performance Distributed Training'],
    ['ml-ops', 'model-analysis-slicing.html', 'Model Analysis & Slice-Based Evaluation'],
    ['ml-ops', 'model-serving-fundamentals.html', 'Model Serving Fundamentals'],
    ['ml-ops', 'model-serving-patterns-infrastructure.html', 'Model Serving Patterns & Infrastructure'],
    ['ml-ops', 'model-management-cicd.html', 'Model Management, Packaging & CI/CD for ML'],
    ['ml-ops', 'model-monitoring-observability.html', 'Model Monitoring, Logging & Observability'],
    ['data-ops', 'data-representations.html', 'Data Representations'],
    ['data-ops', 'data-management-fundamentals.html', 'Data Management Fundamentals'],
    ['data-ops', 'data-architectures.html', 'Data Architectures'],
    ['data-ops', 'data-pipelines-etl-elt.html', 'Data Pipelines: ETL & ELT'],
    ['data-ops', 'modern-data-infra-dataops.html', 'Modern Data Infra & DataOps'],
    ['data-ops', 'ml-lifecycle-and-workflow.html', 'ML Lifecycle & Workflow'],
    ['data-ops', 'data-collection-ingestion.html', 'Data Collection & Ingestion'],
    ['data-ops', 'data-profiling-validation.html', 'Data Profiling & Validation'],
    ['data-ops', 'analytics-engineering.html', 'Analytics Engineering'],
    ['data-ops', 'workflow-orchestration-automation.html', 'Workflow Orchestration & Automation'],
    ['data-ops', 'feature-preparations.html', 'Feature Preparations'],
    ['data-ops', 'ml-experimentation-metadata.html', 'ML Experimentation & Metadata'],
    ['data-ops', 'distributed-scalable-data-processing.html', 'Distributed & Scalable Data Processing'],
    ['data-ops', 'data-pipelines-for-llms.html', 'Data Pipelines for LLMs'],
    ['data-ops', 'data-privacy-governance-responsible-ml.html', 'Data Privacy, Governance & Responsible ML'],
    ['dev-ops', 'cicd-pipelines-release-automation.html', 'CI/CD Pipelines & Release Automation'],
    ['dev-ops', 'containerization-docker.html', 'Containerization & Docker'],
    ['dev-ops', 'container-orchestration-kubernetes.html', 'Container Orchestration & Kubernetes'],
    ['dev-ops', 'infrastructure-as-code.html', 'Infrastructure as Code'],
    ['dev-ops', 'deployment-strategies.html', 'Deployment Strategies'],
    ['dev-ops', 'configuration-secrets-management.html', 'Configuration & Secrets Management'],
    ['dev-ops', 'observability-logging-tracing-alerting.html', 'Observability: Logging, Tracing & Alerting'],
    ['dev-ops', 'incident-response-sre.html', 'Incident Response & SRE Practices'],
    ['dev-ops', 'cloud-infra-networking-fundamentals.html', 'Cloud Infrastructure & Networking Fundamentals'],
    ['dev-ops', 'gitops-environment-promotion.html', 'GitOps & Environment Promotion'],
    ['computer-vision', 'convolutional-neural-networks.html', 'Convolutional Neural Networks'],
    ['computer-vision', 'vision-transformers.html', 'Vision Transformers'],
    ['computer-vision', 'image-classification-transfer-learning.html', 'Image Classification & Transfer Learning'],
    ['computer-vision', 'object-detection.html', 'Object Detection'],
    ['computer-vision', 'semantic-instance-segmentation.html', 'Semantic & Instance Segmentation'],
    ['computer-vision', 'generative-adversarial-networks.html', 'Generative Adversarial Networks for Vision'],
    ['computer-vision', 'diffusion-models-for-images.html', 'Diffusion Models for Images'],
    ['computer-vision', 'self-supervised-contrastive-learning.html', 'Self-Supervised & Contrastive Visual Representation Learning'],
    ['computer-vision', 'video-understanding-temporal-models.html', 'Video Understanding & Temporal Models'],
    ['computer-vision', '3d-vision-neural-rendering.html', '3D Vision & Neural Rendering'],
    ['computer-vision', 'vision-language-pretraining.html', 'Vision-Language Pretraining (CLIP-style)'],
    ['computer-vision', 'cv-deployment-edge-inference.html', 'CV Deployment & Edge Inference'],
    ['deep-reinforcement-learning', 'mdps-rl-foundations.html', 'MDPs & RL Foundations'],
    ['deep-reinforcement-learning', 'value-based-methods-dqn.html', 'Value-Based Methods: Q-Learning & DQN'],
    ['deep-reinforcement-learning', 'policy-gradient-actor-critic.html', 'Policy Gradient Methods & Actor-Critic'],
    ['deep-reinforcement-learning', 'trust-region-proximal-policy-methods.html', 'Trust Region & Proximal Policy Methods'],
    ['deep-reinforcement-learning', 'model-based-rl-planning.html', 'Model-Based RL & Planning'],
    ['deep-reinforcement-learning', 'exploration-strategies-rl.html', 'Exploration Strategies in RL'],
    ['deep-reinforcement-learning', 'multi-agent-reinforcement-learning.html', 'Multi-Agent Reinforcement Learning'],
    ['deep-reinforcement-learning', 'offline-batch-reinforcement-learning.html', 'Offline & Batch Reinforcement Learning'],
    ['deep-reinforcement-learning', 'reward-shaping-credit-assignment.html', 'Reward Shaping & Credit Assignment'],
    ['deep-reinforcement-learning', 'continuous-control-robotics.html', 'Continuous Control & Robotics (DDPG/SAC/TD3)'],
    ['deep-reinforcement-learning', 'sim-to-real-transfer-rl-deployment.html', 'Sim-to-Real Transfer & RL Deployment']
  ];
  /* one-sentence excerpt per chapter, same order as RAW above — extracted
     from each chapter's own "In plain English" (.plain-bridge) paragraph,
     not the generic .lede intro every chapter shares. Baked in here rather
     than fetched at hover-time because file:// blocks cross-page fetch. */
  var EXCERPTS = [
    'Attention lets each token look at other relevant tokens and decide what information matters right now.',
    'A Transformer is a stack of blocks that repeatedly mixes information between tokens and then transforms that information.',
    'Transformers need an extra signal to know where each token sits in a sequence, because attention alone does not know order.',
    'Before a model sees text, the text is broken into tokens.',
    'Scaling laws are practical rules of thumb about how model quality tends to change as you add more parameters, data, or compute.',
    'MoE makes a model larger without running every parameter for every token: a router picks a small number of experts to use.',
    'The KV cache saves work during token-by-token generation, but it can quickly become the biggest GPU-memory cost when requests get long.',
    'Quantization stores or computes model values with fewer bits so models use less memory and can often run faster, with some risk to quality.',
    'The training objective tells the model what prediction problem to solve while learning from huge amounts of data.',
    'Instruction tuning teaches a pretrained model how to follow tasks and respond in the format people actually want.',
    'These methods push a capable model toward outputs people prefer by learning from rankings or preference comparisons.',
    'Instead of relying only on human feedback, these approaches use written principles or AI-generated feedback to guide model behavior.',
    'A model can learn its training data too specifically, which makes it look good on familiar examples but less reliable on new ones.',
    'The learning rate controls how aggressively the model changes.',
    'These techniques make large-model training fit by trading extra computation or communication for lower memory use.',
    'Different adaptation methods trade training cost and flexibility against how much of the base model you are willing to change.',
    'Context engineering is deciding what information an LLM should see now, what can be left out, and how it should be organized.',
    'RAG gives the model external information at answer time by retrieving useful documents and placing the evidence in the prompt.',
    'Vector search finds items that are semantically similar without comparing a query against every item exactly.',
    'These retrieval systems try to decide when retrieval is needed and how to recover when the first result is not good enough.',
    'Long-context models can accept more tokens, but fitting more information does not automatically mean the model uses it well.',
    'Agent frameworks coordinate model calls, tools, state, and control flow so an LLM can complete multi-step tasks.',
    'Agent memory decides what information survives beyond the current step and how useful information is found again later.',
    'These features constrain model output so applications can reliably consume data or trigger tools.',
    'LLM evaluation is the discipline of checking whether a model or system is actually improving before shipping it.',
    'Red-teaming deliberately looks for ways a model or application can be pushed into unsafe or unintended behavior.',
    'Hallucination work focuses on detecting unsupported claims and reducing the chance that a model invents information.',
    'Fairness work checks whether model behavior changes in harmful or inconsistent ways across people, groups, or scenarios.',
    'Interpretability tries to understand what internal model components are doing instead of treating the model as a black box.',
    'Self-correction systems ask models to inspect or revise their own outputs using rules, critiques, or verification steps.',
    'LLM serving is the system that turns a model into a reliable product while managing GPU memory, queues, latency, and cost.',
    'Speculative decoding uses a cheaper model to guess several future tokens, then lets the main model verify them efficiently.',
    'Model parallelism splits one large model across multiple devices when it no longer fits or runs fast enough on one device.',
    'Distillation trains a smaller model to copy useful behavior from a larger model so it can be cheaper to run.',
    'Multimodal models connect text with images, audio, video, or other inputs so one system can reason across data types.',
    'Model merging combines parameters or updates from multiple models without necessarily training a new model from scratch.',
    'Test-time compute spends more work while answering — searching, verifying, sampling — to improve difficult answers.',
    'This topic studies how capabilities appear or become easier to measure as models and training setups scale.',
    'Inference-time scaling asks how much answer quality improves when you spend more compute during reasoning or generation.',
    'Architecture search tries to find better model designs by searching over design choices instead of hand-picking them.',
    'State-space models offer another way to process sequences, often aiming for better scaling with long inputs than attention alone.',
    'Diffusion-style language generation explores generating text through iterative refinement rather than one next token at a time.',
    'World-model and planning systems try to predict consequences of actions so an AI system can plan before it acts.',
    'Federated learning trains or adapts models across many devices or organizations without centralizing all raw data.',
    'Neural-symbolic systems combine learned pattern recognition with explicit rules, programs, or symbolic reasoning.',
    'Before you tune a model you need a scoreboard: a baseline for "good" and a repeatable loop that shows where it breaks.',
    'Most trained networks carry weights that barely matter to the output; pruning removes them to fit memory and latency budgets.',
    'Training a model too large or slow for one GPU means splitting the data, layers, or tensors across many GPUs.',
    'A model with 99% overall accuracy can still fail badly for one language, device, or group — slice-based evaluation finds that.',
    'Model serving turns a trained model file into a live, versioned prediction service with a stable request/response contract.',
    'Once a model has a serving contract, the infrastructure question is how many replicas to run and how to pack requests.',
    'Model management is what makes a trained model a governable, promotable release instead of a file someone emails to ops.',
    'A model can be "up" — 200 OK, low latency, no errors — while its predictions quietly get worse in ways infra monitoring misses.',
    'Every dataset, feature store, and training corpus is ultimately bytes on disk in some chosen format and data model.',
    'Data management is the discipline of deciding who can create, change, read, and delete which data, and tracking that.',
    'A data architecture is the organization-wide blueprint for where data lives, who computes on it, and how it flows.',
    'A data pipeline moves data from where it is produced to where it is used, and the modern stack shifted "transform" downstream.',
    'DataOps applies the DevOps playbook — version control, automated testing, CI/CD, monitoring — to data pipelines.',
    'An ML system is really three separate codebases welded together — data, model, and glue code — and outages come from the seams.',
    'Ingestion is how data gets from the system that created it into the systems that use it, and where quality problems start.',
    'Profiling tells you what your data actually looks like; validation is the automated gate that stops it from drifting.',
    'Analytics engineering applies software-engineering discipline — version control, tests, code review — to the SQL layer.',
    'An orchestrator knows which pipeline steps depend on which others, runs them in order on a schedule, and retries failures.',
    'Feature preparation turns raw, messy data into the exact numeric inputs a model consumes.',
    'Experiment tracking and metadata stores are the system of record for "which code, data, and hyperparameters produced this."',
    'Distributed data processing spreads a computation over many machines so data size, not one machine\'s memory, is the limit.',
    'LLM data pipelines are the plumbing that turns raw text into pretraining-ready, deduplicated, filtered corpora.',
    'Privacy engineering makes "delete my data" and "prove you had the right to use it" answerable questions for an ML system.',
    'CI/CD is the automated assembly line that turns a code change into something running safely in production.',
    'A container packages an application with everything it needs to run into one portable, isolated unit.',
    'Kubernetes continuously watches "what\'s actually running" against "what you declared should be running" and reconciles the two.',
    'Infrastructure as Code means describing servers, networks, and cloud resources as version-controlled text instead of clicking.',
    'A deployment strategy decides how much traffic sees a new version at once and how fast you can undo it if it\'s bad.',
    'Configuration and secrets management keeps a service\'s environment-specific settings and credentials out of the code.',
    'Observability means building a system so an engineer can answer "what, where, and why" from its own signals when it breaks.',
    'Incident response and SRE practices turn "the alerting fired" into a coordinated, time-bounded fix.',
    'Cloud infrastructure and networking is how a deployed service gets a private network, safe reachability, and a name.',
    'GitOps runs production off a git repository as the single source of truth, with an automated agent reconciling drift.',
    'A CNN slides a small learned pattern-detector across an image so the same detector can find that pattern anywhere.',
    'A Vision Transformer cuts an image into a grid of patches, treats each patch like a word token, and lets attention learn which matter.',
    'Instead of training a vision model from zero for every new task, reuse a network that already learned general visual features.',
    'Object detection doesn\'t just say what\'s in an image — it draws a box around every instance and labels each one.',
    'Segmentation labels every pixel in an image instead of just drawing a box around an object.',
    'A GAN trains two networks against each other — a generator that fakes realistic images and a discriminator that tries to catch it.',
    'An image diffusion model learns to reverse a process that slowly turns a picture into noise, then runs that in reverse to generate.',
    'These methods teach a vision backbone to produce useful features from unlabeled images alone.',
    'Video understanding takes everything an image model knows about objects and scenes and adds a second axis — time.',
    '3D vision recovers a scene\'s real geometry and appearance from 2D pictures, either as explicit surfaces or a neural representation.',
    'CLIP-style pretraining teaches an image encoder and a text encoder to place matching pictures and captions near each other.',
    'Deploying vision models to real-time or edge hardware is about hitting a frames-per-second budget end-to-end.',
    'A Markov Decision Process is the formal contract that says here is a state, here are your actions, and here is how the world responds.',
    'Q-learning lets an agent learn the value of every action in every situation purely by trial and error, with no world model.',
    'Instead of learning action values and picking the best, policy gradient methods directly adjust the probability of each action.',
    'TRPO and PPO put a leash on how much a single update can change an agent\'s behavior, so noisy gradients don\'t wreck it.',
    'Instead of only learning from trial and error, the agent learns or is given a model of how the world responds to its actions.',
    'Exploration strategies decide when an agent should try something uncertain instead of doing what currently looks best.',
    'Multi-agent RL trains several agents at once whose actions all affect each other\'s rewards and observations.',
    'Offline RL learns a policy purely from a fixed log of past interactions, with no chance to try anything new live.',
    'Most real tasks only signal eventual win or loss, so reward shaping adds denser signal along the way to speed learning.',
    'Joint torques and steering angles aren\'t a menu you can enumerate, so continuous-control RL trains an actor directly.',
    'You train a policy in a cheap, fast, resettable simulator because training directly on real hardware is slow and can break things.'
  ];
  var CHAPTERS = RAW.map(function (r, i) { return { n: i + 1, folder: r[0], file: r[1], title: r[2], excerpt: EXCERPTS[i] || '' }; });

  var seg = location.pathname.split('/').filter(Boolean);
  var CURRENT_FOLDER = seg.length > 1 ? seg[seg.length - 2] : '';
  var CURRENT_FILE = seg.length ? seg[seg.length - 1] : '';
  var AT_DEPTH1 = !!FOLDER_LABEL[CURRENT_FOLDER] || CURRENT_FOLDER === 'assets';
  var ROOT_PREFIX = AT_DEPTH1 ? '../' : '';

  function hrefFor(entry) {
    return entry.folder === CURRENT_FOLDER ? entry.file : ROOT_PREFIX + entry.folder + '/' + entry.file;
  }

  var CURRENT_CHAPTER_IDX = -1;
  for (var _i = 0; _i < CHAPTERS.length; _i++) {
    if (CHAPTERS[_i].folder === CURRENT_FOLDER && CHAPTERS[_i].file === CURRENT_FILE) { CURRENT_CHAPTER_IDX = _i; break; }
  }

  /* ---- reading progress: localStorage-backed, per-browser only. Tracks
     which chapters have been opened, a plain day-streak, and the last
     chapter visited (for a "continue reading" link on the homepage). No
     server, no accounts, no sync — deliberately: research across LeetCode/
     Khan/Codecademy consistently found that once you add points, badges,
     or leaderboards on top of this, it reads as patronizing to a technical
     audience. A number that's always correct beats a reward that's fake. ---- */
  var PROGRESS_KEY = 'aidd-progress';
  function chapterKey(c) { return c.folder + '/' + c.file; }
  function loadProgress() {
    try {
      var raw = localStorage.getItem(PROGRESS_KEY);
      var p = raw ? JSON.parse(raw) : null;
      if (p && p.visited) return p;
    } catch (e) {}
    return { visited: {}, streak: 0, lastDate: '', lastChapter: '' };
  }
  function saveProgress(p) {
    try { localStorage.setItem(PROGRESS_KEY, JSON.stringify(p)); } catch (e) {}
  }
  function todayStr() { return new Date().toISOString().slice(0, 10); }
  function recordVisit() {
    var progress = loadProgress();
    if (CURRENT_CHAPTER_IDX === -1) return progress;
    var c = CHAPTERS[CURRENT_CHAPTER_IDX];
    progress.visited[chapterKey(c)] = true;
    progress.lastChapter = chapterKey(c);
    var today = todayStr();
    if (progress.lastDate !== today) {
      var y = new Date(); y.setDate(y.getDate() - 1);
      progress.streak = (progress.lastDate === y.toISOString().slice(0, 10)) ? (progress.streak || 0) + 1 : 1;
      progress.lastDate = today;
    }
    saveProgress(progress);
    return progress;
  }
  var PROGRESS = recordVisit();
  function visitedCountIn(folder) {
    return CHAPTERS.filter(function (c) { return c.folder === folder && PROGRESS.visited[chapterKey(c)]; }).length;
  }
  function totalVisitedCount() {
    var n = 0;
    for (var k in PROGRESS.visited) if (PROGRESS.visited.hasOwnProperty(k)) n++;
    return n;
  }

  /* ---- glossary term tooltip pin/unpin (original behavior, unchanged) ---- */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('.glossary-term');
    document.querySelectorAll('.glossary-term.pinned').forEach(function (x) {
      if (x !== t) x.classList.remove('pinned');
    });
    if (t) { e.preventDefault(); t.classList.toggle('pinned'); }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.glossary-term.pinned').forEach(function (x) { x.classList.remove('pinned'); });
    }
  });

  /* ---- category accent: ties a chapter page's chrome color to the same
     accent its folder uses on the homepage TOC ---- */
  var FOLDER_ACCENT = {
    'training-adaptation': 'sky', 'context-retrieval-agents': 'teal', 'evaluation-safety': 'violet',
    'emerging-research': 'sky', 'ml-ops': 'teal', 'data-ops': 'violet',
    'computer-vision': 'sky', 'deep-reinforcement-learning': 'teal'
  };
  (function applyCategoryAccent() {
    var accent = FOLDER_ACCENT[CURRENT_FOLDER];
    if (accent) document.documentElement.setAttribute('data-accent', accent);
  })();

  /* ---- site-wide light/dark theme toggle, with a real way back to "system" ---- */
  var STORAGE_KEY = 'aidd-theme';
  var root = document.documentElement;

  function systemPrefersDark() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function currentTheme() {
    return root.getAttribute('data-theme') || (systemPrefersDark() ? 'dark' : 'light');
  }
  (function applyStoredTheme() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'dark' || saved === 'light') root.setAttribute('data-theme', saved);
    } catch (e) { /* storage unavailable; fall back to system preference */ }
  })();

  function buildThemeToggle(container) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'theme-toggle';
    function paint() {
      var dark = currentTheme() === 'dark';
      btn.textContent = dark ? '☀' : '☾';
      btn.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
      btn.title = btn.getAttribute('aria-label');
    }
    paint();
    btn.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      // if the click would only land back on what the OS already prefers,
      // clear the override instead — otherwise a 2-state toggle permanently
      // locks the reader out of "follow system" after one click
      if (next === (systemPrefersDark() ? 'dark' : 'light')) {
        root.removeAttribute('data-theme');
        try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
      } else {
        root.setAttribute('data-theme', next);
        try { localStorage.setItem(STORAGE_KEY, next); } catch (e) {}
      }
      paint();
    });
    (container || document.body).appendChild(btn);
  }

  /* ---- copy buttons on code/diagram blocks: persistent, not hover-only,
     since this is offline and there's no cost to always showing it ---- */
  function buildCopyButtons() {
    var blocks = document.querySelectorAll('.diagram, .two-col pre, .case-chain, .topic-check');
    blocks.forEach(function (block) {
      if (block.querySelector('.copy-btn')) return;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'copy-btn';
      btn.textContent = 'Copy';
      btn.addEventListener('click', function () {
        var text = block.textContent.replace(/^\s*Copy\s*/, '');
        function done() {
          btn.textContent = 'Copied';
          btn.classList.add('copied');
          setTimeout(function () { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1400);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, done);
        } else {
          var ta = document.createElement('textarea');
          ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
          document.body.appendChild(ta); ta.select();
          try { document.execCommand('copy'); } catch (e) {}
          document.body.removeChild(ta);
          done();
        }
      });
      block.appendChild(btn);
    });
  }

  /* ---- back-to-top ---- */
  function buildBackToTop() {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'back-to-top';
    btn.setAttribute('aria-label', 'Back to top');
    btn.textContent = '↑';
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    document.body.appendChild(btn);
    window.addEventListener('scroll', function () {
      btn.classList.toggle('visible', window.scrollY > 480);
    }, { passive: true });
  }

  /* ---- reading progress bar (decorative — hidden from assistive tech,
     not wired to a live region so it doesn't chatter on every scroll tick) ---- */
  function buildProgressBar() {
    var wrap = document.createElement('div');
    wrap.className = 'reading-progress';
    wrap.setAttribute('aria-hidden', 'true');
    var fill = document.createElement('div');
    fill.className = 'reading-progress-fill';
    wrap.appendChild(fill);
    document.body.insertBefore(wrap, document.body.firstChild);

    function update() {
      var doc = document.documentElement;
      var scrollable = doc.scrollHeight - doc.clientHeight;
      var pct = scrollable > 0 ? Math.min(100, Math.max(0, (window.scrollY / scrollable) * 100)) : 0;
      fill.style.width = pct + '%';
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  /* ---- chapter section nav: built from each page's own numbered h2s ---- */
  function buildSectionNav() {
    var chapter = document.querySelector('.chapter');
    if (!chapter) return;

    var heads = Array.prototype.filter.call(chapter.querySelectorAll('h2'), function (h) {
      return /^\s*\d+\./.test(h.textContent);
    });
    if (heads.length < 2) return;

    // give the leading "N." its own mono-styled span — a small, cheap detail
    // that reads as considered rather than templated
    heads.forEach(function (h, i) {
      if (!h.id) h.id = 'sec-' + (i + 1);
      if (!h.querySelector('.chapter-num')) {
        var text = h.textContent;
        var m = /^(\s*\d+\.)\s*/.exec(text);
        if (m) {
          h.textContent = text.slice(m[0].length);
          var span = document.createElement('span');
          span.className = 'chapter-num';
          span.textContent = m[1];
          h.insertBefore(span, h.firstChild);
        }
      }
    });

    function labelOf(h) { return h.textContent.replace(/^\s*\d+\.\s*/, ''); }

    var rail = document.createElement('nav');
    rail.className = 'section-rail';
    rail.setAttribute('aria-label', 'On this page');
    var list = document.createElement('ol');
    heads.forEach(function (h) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = labelOf(h);
      li.appendChild(a);
      list.appendChild(li);
    });
    var indicator = document.createElement('div');
    indicator.className = 'rail-indicator';
    list.appendChild(indicator);
    rail.appendChild(list);
    document.body.appendChild(rail);

    var select = document.createElement('select');
    select.className = 'section-jump';
    select.setAttribute('aria-label', 'Jump to section');
    select.add(new Option('Jump to section…', ''));
    heads.forEach(function (h) { select.add(new Option(labelOf(h), '#' + h.id)); });
    document.body.appendChild(select);

    var links = Array.prototype.slice.call(rail.querySelectorAll('a'));
    var suppressSpy = false, suppressTimer = null;

    function setActive(id) {
      links.forEach(function (l) {
        var on = l.getAttribute('href') === '#' + id;
        l.classList.toggle('active', on);
        if (on) {
          l.setAttribute('aria-current', 'location');
          // slide the indicator to this link's position instead of
          // instantly swapping a highlight — one continuous motion
          indicator.style.transform = 'translateY(' + l.offsetTop + 'px)';
          indicator.style.height = l.offsetHeight + 'px';
        } else {
          l.removeAttribute('aria-current');
        }
      });
      var opt = select.querySelector('option[value="#' + id + '"]');
      if (opt) select.value = opt.value;
    }

    function jumpTo(id) {
      suppressSpy = true;
      clearTimeout(suppressTimer);
      var target = document.getElementById(id);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      setActive(id);
      // re-enable scroll-spy once the smooth scroll has settled
      suppressTimer = setTimeout(function () { suppressSpy = false; }, 700);
    }

    rail.addEventListener('click', function (e) {
      var a = e.target.closest('a');
      if (!a) return;
      e.preventDefault();
      jumpTo(a.getAttribute('href').slice(1));
    });
    select.addEventListener('change', function () {
      if (select.value) jumpTo(select.value.slice(1));
    });

    if ('IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function (entries) {
        if (suppressSpy) return;
        entries.forEach(function (entry) {
          if (entry.isIntersecting) setActive(entry.target.id);
        });
      }, { rootMargin: '-10% 0px -70% 0px', threshold: 0 });
      heads.forEach(function (h) { obs.observe(h); });

      // classic scrollspy gap: a short final section (or simply reaching the
      // bottom of the document) never satisfies the observer's threshold —
      // force the last heading active once the reader can't scroll further
      window.addEventListener('scroll', function () {
        if (suppressSpy) return;
        var doc = document.documentElement;
        if (window.scrollY + doc.clientHeight >= doc.scrollHeight - 4) {
          setActive(heads[heads.length - 1].id);
        }
      }, { passive: true });
    } else {
      setActive(heads[0].id);
    }
  }

  /* ---- breadcrumb + real-title next/prev links (chapter pages only) ---- */
  function enhanceChapterNav() {
    var idx = CURRENT_CHAPTER_IDX;
    if (idx === -1) return; // not a chapter page

    var chapter = document.querySelector('.chapter');
    if (chapter && !chapter.querySelector('.crumb-trail')) {
      var trail = document.createElement('div');
      trail.className = 'crumb-trail';
      var home = document.createElement('a');
      home.href = ROOT_PREFIX + 'index.html';
      home.textContent = 'Contents';
      trail.appendChild(home);
      trail.appendChild(document.createTextNode(' / '));
      var topic = document.createElement('span');
      topic.textContent = FOLDER_LABEL[CURRENT_FOLDER] || CURRENT_FOLDER;
      trail.appendChild(topic);
      trail.appendChild(document.createTextNode(' / '));
      var current = document.createElement('span');
      current.className = 'crumb-current';
      current.textContent = CHAPTERS[idx].title;
      trail.appendChild(current);

      // reading-time estimate — computed live from the chapter's own word
      // count (no build step, no pre-generated data needed)
      var words = (chapter.textContent || '').trim().split(/\s+/).length;
      var mins = Math.max(1, Math.round(words / 200));
      var rt = document.createElement('span');
      rt.className = 'reading-time';
      rt.textContent = '~' + mins + ' min read';
      trail.appendChild(rt);

      chapter.insertBefore(trail, chapter.firstChild);
    }

    var nav = document.querySelector('.chapter-nav');
    if (!nav) return;
    var prev = idx > 0 ? CHAPTERS[idx - 1] : null;
    var next = idx < CHAPTERS.length - 1 ? CHAPTERS[idx + 1] : null;
    nav.querySelectorAll('a').forEach(function (a) {
      var isContents = /index\.html/.test(a.getAttribute('href') || '');
      if (isContents) return;
      var text = a.textContent;
      var isPrev = /previous|←/i.test(text);
      var isNext = /next|→/i.test(text);
      if (isPrev && prev) {
        a.href = hrefFor(prev);
        a.innerHTML = '';
        var pc = document.createElement('span'); pc.className = 'crumb'; pc.textContent = '← Previous';
        var pt = document.createTextNode(prev.title);
        a.appendChild(pc); a.appendChild(pt);
      } else if (isNext && next) {
        a.href = hrefFor(next);
        a.innerHTML = '';
        var nc = document.createElement('span'); nc.className = 'crumb'; nc.textContent = 'Next →';
        var nt = document.createTextNode(next.title);
        a.appendChild(nc); a.appendChild(nt);
      }
    });
  }

  /* ---- unified left panel: on a chapter page it's pinned in the grid,
     always showing "you are here" for the current section. On any other
     page (homepage, glossary) it's an off-canvas drawer, hidden until a
     topbar section is clicked — same element, same render logic either
     way, so the two behaviors can never drift apart. ---- */
  function buildLeftNav(actionsEl) {
    var idx = CURRENT_CHAPTER_IDX;
    var isChapterPage = idx !== -1;

    var aside = document.createElement('aside');
    aside.className = 'chapter-sidebar';
    aside.setAttribute('aria-label', 'Section chapters');

    var scrim = null;
    if (!isChapterPage) {
      scrim = document.createElement('div');
      scrim.className = 'sidebar-scrim';
      document.body.appendChild(scrim);
    }

    var close = document.createElement('button');
    close.type = 'button';
    close.className = 'sidebar-close';
    close.setAttribute('aria-label', 'Close chapter list');
    close.textContent = '✕';
    close.addEventListener('click', function () {
      aside.classList.remove('open');
      if (scrim) scrim.classList.remove('visible');
    });
    aside.appendChild(close);

    var eyebrow = document.createElement('span');
    eyebrow.className = 'sidebar-eyebrow';
    aside.appendChild(eyebrow);

    var title = document.createElement('strong');
    title.className = 'sidebar-title';
    aside.appendChild(title);

    var list = null;
    var groups = null; // off-canvas mode only: accordion of all 11 sections

    if (isChapterPage) {
      list = document.createElement('ol');
      list.className = 'sidebar-list';
      aside.appendChild(list);
    } else {
      // two-tier nav: all 11 sections collapsed to just a header + count;
      // clicking one expands it and collapses the rest (accordion), so
      // browsing stays a single flat list deep rather than 11 always-open
      // lists stacked on top of each other. Topbar itself is untouched —
      // it stays the full always-visible quick-jump row.
      eyebrow.textContent = 'Browse sections';
      title.textContent = 'All 11 sections';
      groups = { wrap: document.createElement('div'), byFolder: {} };
      groups.wrap.className = 'sidebar-groups';
      FOLDERS.forEach(function (f) {
        var folder = f[0];
        var items = CHAPTERS.filter(function (c) { return c.folder === folder; });
        var det = document.createElement('details');
        det.className = 'sidebar-group';
        det.setAttribute('data-accent', FOLDER_ACCENT[folder] || 'gold');
        var sum = document.createElement('summary');
        var name = document.createElement('span');
        name.className = 'group-name';
        name.textContent = FOLDER_LABEL[folder] || folder;
        var count = document.createElement('span');
        count.className = 'group-count';
        count.textContent = visitedCountIn(folder) + '/' + items.length;
        sum.appendChild(name);
        sum.appendChild(count);
        det.appendChild(sum);
        var ol = document.createElement('ol');
        ol.className = 'sidebar-list';
        items.forEach(function (c, i) {
          var li = document.createElement('li');
          var a = document.createElement('a');
          a.href = hrefFor(c);
          a.title = c.excerpt + (PROGRESS.visited[chapterKey(c)] ? ' (read)' : '');
          var n = document.createElement('span');
          n.className = PROGRESS.visited[chapterKey(c)] ? 'check' : 'n';
          n.textContent = PROGRESS.visited[chapterKey(c)] ? '✓' : (i + 1) + '.';
          a.appendChild(n);
          a.appendChild(document.createTextNode(c.title));
          li.appendChild(a);
          ol.appendChild(li);
        });
        det.appendChild(ol);
        det.addEventListener('toggle', function () {
          if (!det.open) return;
          Object.keys(groups.byFolder).forEach(function (k) {
            if (groups.byFolder[k] !== det) groups.byFolder[k].open = false;
          });
        });
        groups.byFolder[folder] = det;
        groups.wrap.appendChild(det);
      });
      aside.appendChild(groups.wrap);
    }

    function render(folder) {
      if (!list) return; // off-canvas mode has no single-section render target
      var items = CHAPTERS.filter(function (c) { return c.folder === folder; });
      var current = isChapterPage ? CHAPTERS[idx] : null;
      var showingOwnSection = current && current.folder === folder;

      // always self-declare (never just omit the attribute) — --cat-accent
      // is an inherited custom property, so leaving it unset here would
      // otherwise leak whatever accent the *current page* happens to be on
      aside.setAttribute('data-accent', FOLDER_ACCENT[folder] || 'gold');
      eyebrow.textContent = showingOwnSection ? 'You are here' : 'Section';
      var pos = showingOwnSection ? items.indexOf(current) + 1 : null;
      var readHere = visitedCountIn(folder);
      title.textContent = (FOLDER_LABEL[folder] || folder) + (pos ? ' · ' + pos + ' of ' + items.length : ' · ' + readHere + ' of ' + items.length + ' read');

      list.innerHTML = '';
      items.forEach(function (c, i) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = hrefFor(c);
        if (current === c) { a.classList.add('active'); a.setAttribute('aria-current', 'page'); }
        a.title = c.excerpt + (PROGRESS.visited[chapterKey(c)] ? ' (read)' : '');
        var n = document.createElement('span');
        n.className = PROGRESS.visited[chapterKey(c)] ? 'check' : 'n';
        n.textContent = PROGRESS.visited[chapterKey(c)] ? '✓' : (i + 1) + '.';
        a.appendChild(n);
        a.appendChild(document.createTextNode(c.title));
        li.appendChild(a);
        list.appendChild(li);
      });
    }

    if (isChapterPage) {
      var layout = document.querySelector('.layout.single');
      if (layout) {
        layout.classList.remove('single');
        aside.classList.add('pinned');
        layout.insertBefore(aside, layout.firstChild);
      } else {
        document.body.appendChild(aside);
      }
      render(CURRENT_FOLDER);
    } else {
      document.body.appendChild(aside);
    }

    if (scrim) {
      scrim.addEventListener('click', function () {
        aside.classList.remove('open');
        scrim.classList.remove('visible');
      });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && aside.classList.contains('open')) {
        aside.classList.remove('open');
        if (scrim) scrim.classList.remove('visible');
      }
    });

    // mobile toggle for the pinned case only — the off-canvas case is
    // opened via the topbar section buttons themselves, see openSection()
    if (isChapterPage && actionsEl) {
      var toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'topbar-btn icon-only sidebar-toggle';
      toggle.setAttribute('aria-label', 'Open chapter list');
      toggle.textContent = '☰';
      toggle.addEventListener('click', function () { aside.classList.toggle('open'); });
      actionsEl.insertBefore(toggle, actionsEl.firstChild);
    }

    return function openSection(folder) {
      if (isChapterPage) {
        render(folder);
      } else {
        aside.classList.add('open');
        if (scrim) scrim.classList.add('visible');
        var det = groups.byFolder[folder];
        if (det) {
          det.open = true; // fires the 'toggle' listener above, closing siblings
          det.scrollIntoView({ block: 'nearest' });
        }
      }
    };
  }

  /* ---- persistent top bar: brand + all 11 sections + search/theme controls.
     Every page gets this — it's the one global nav. Click handlers on the
     section buttons are wired separately (see wireTopbarSections below)
     because they need openSection(), which the left panel only returns
     after it's built — and the left panel needs the topbar's actions
     container first for its mobile toggle. Build topbar shell, then left
     panel, then wire: breaks that circular dependency. ---- */
  function buildTopbar() {
    var bar = document.createElement('div');
    bar.className = 'app-topbar';

    var brand = document.createElement('a');
    brand.className = 'topbar-brand';
    brand.href = ROOT_PREFIX + 'index.html';
    brand.textContent = 'AI Deep Dive';
    bar.appendChild(brand);

    var sections = document.createElement('nav');
    sections.className = 'topbar-sections';
    sections.setAttribute('aria-label', 'Sections');
    var buttons = [];
    FOLDERS.forEach(function (f) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'topbar-section-btn';
      if (f[0] === CURRENT_FOLDER) btn.classList.add('active');
      btn.textContent = TOPBAR_LABEL[f[0]] || f[1];
      btn.title = f[1];
      buttons.push({ folder: f[0], el: btn });
      sections.appendChild(btn);
    });
    bar.appendChild(sections);

    var actions = document.createElement('div');
    actions.className = 'topbar-actions';
    bar.appendChild(actions);

    document.body.insertBefore(bar, document.body.firstChild);
    return {
      actions: actions,
      wireSections: function (openSection) {
        buttons.forEach(function (b) {
          b.el.addEventListener('click', function () { openSection(b.folder); });
        });
      }
    };
  }

  /* ---- command palette: Ctrl/Cmd+K or "/" from anywhere, on every page ---- */
  function buildCommandPalette(container) {
    var trigger = document.createElement('button');
    trigger.type = 'button';
    trigger.className = 'topbar-btn';
    trigger.setAttribute('aria-label', 'Search all chapters');
    trigger.innerHTML = '<span class="topbar-btn-label">Search</span><kbd>/</kbd>';
    (container || document.body).appendChild(trigger);

    var overlay = document.createElement('div');
    overlay.className = 'cmdk-overlay';
    overlay.hidden = true;
    overlay.innerHTML =
      '<div class="cmdk-modal" role="dialog" aria-modal="true" aria-label="Search chapters">' +
        '<input class="cmdk-input" type="text" placeholder="Jump to any of the 101 chapters…" aria-label="Search chapters" autocomplete="off"/>' +
        '<ul class="cmdk-results" role="listbox"></ul>' +
        '<div class="cmdk-hint"><span><kbd>↑</kbd><kbd>↓</kbd> navigate · <kbd>↵</kbd> open</span><span><kbd>esc</kbd> close</span></div>' +
      '</div>';
    document.body.appendChild(overlay);

    var input = overlay.querySelector('.cmdk-input');
    var resultsEl = overlay.querySelector('.cmdk-results');
    var active = 0, current = [];

    function score(title, q) {
      var t = title.toLowerCase();
      var idx = t.indexOf(q);
      if (idx !== -1) return idx;
      var qi = 0;
      for (var i = 0; i < t.length && qi < q.length; i++) { if (t[i] === q[qi]) qi++; }
      return qi === q.length ? 1000 + (t.length - q.length) : -1;
    }

    function render() {
      var q = input.value.trim().toLowerCase();
      var list = !q ? CHAPTERS.slice(0, 20) : CHAPTERS
        .map(function (c) { return { c: c, s: score(c.title, q) }; })
        .filter(function (r) { return r.s !== -1; })
        .sort(function (a, b) { return a.s - b.s; })
        .slice(0, 20)
        .map(function (r) { return r.c; });
      current = list;
      active = 0;
      resultsEl.innerHTML = '';
      if (!list.length) {
        resultsEl.innerHTML = '<div class="cmdk-empty">No chapters match “' + input.value.trim() + '”. Try another term.</div>';
        return;
      }
      // group by folder — a flat 20-row list across 11 sections reads as
      // noise; a folder header whenever it changes gives free structure
      var lastFolder = null;
      var linkIndex = 0;
      list.forEach(function (c) {
        if (c.folder !== lastFolder) {
          var header = document.createElement('li');
          header.className = 'cmdk-group-label';
          header.textContent = FOLDER_LABEL[c.folder] || c.folder;
          header.setAttribute('role', 'presentation');
          resultsEl.appendChild(header);
          lastFolder = c.folder;
        }
        var li = document.createElement('li');
        li.setAttribute('role', 'option');
        var a = document.createElement('a');
        a.href = hrefFor(c);
        a.className = linkIndex === 0 ? 'active' : '';
        a.title = c.excerpt;
        a.innerHTML = '<span>' + c.title + '</span><small>Ch. ' + c.n + '</small>';
        li.appendChild(a);
        resultsEl.appendChild(li);
        linkIndex++;
      });
    }

    function setActive(i) {
      var links = resultsEl.querySelectorAll('a');
      if (!links.length) return;
      active = (i + links.length) % links.length;
      links.forEach(function (l, j) { l.classList.toggle('active', j === active); });
      links[active].scrollIntoView({ block: 'nearest' });
    }

    function open() {
      overlay.hidden = false;
      input.value = '';
      render();
      setTimeout(function () { input.focus(); }, 0);
    }
    function close() { overlay.hidden = true; trigger.focus(); }

    trigger.addEventListener('click', open);
    overlay.addEventListener('click', function (e) { if (e.target === overlay) close(); });
    input.addEventListener('input', render);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); setActive(active + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(active - 1); }
      else if (e.key === 'Enter') {
        e.preventDefault();
        var link = resultsEl.querySelectorAll('a')[active];
        if (link) location.href = link.getAttribute('href');
      } else if (e.key === 'Escape') { close(); }
    });

    document.addEventListener('keydown', function (e) {
      var mod = e.ctrlKey || e.metaKey;
      var typingTarget = /input|textarea|select/i.test((e.target && e.target.tagName) || '') || (e.target && e.target.isContentEditable);
      if (mod && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); open(); return; }
      if (e.key === '/' && !typingTarget && overlay.hidden) { e.preventDefault(); open(); return; }
      if (e.key === 'Escape' && !overlay.hidden) close();
    });
  }

  /* ---- progress badge: plain "N/101 read" + streak, in the topbar ---- */
  function buildProgressBadge(container) {
    var el = document.createElement('span');
    el.className = 'topbar-progress';
    var count = totalVisitedCount();
    var html = '<strong>' + count + '</strong>/' + CHAPTERS.length + ' read';
    if (PROGRESS.streak > 1) html += ' <span class="streak">🔥' + PROGRESS.streak + '</span>';
    el.innerHTML = html;
    (container || document.body).appendChild(el);
  }

  /* ---- resume card: homepage only, only when there's a last-visited
     chapter in localStorage to point back to ---- */
  function buildResumeCard() {
    var overview = document.querySelector('.section-overview');
    if (!overview || !PROGRESS.lastChapter) return;
    var parts = PROGRESS.lastChapter.split('/');
    var target = null;
    for (var i = 0; i < CHAPTERS.length; i++) {
      if (CHAPTERS[i].folder === parts[0] && CHAPTERS[i].file === parts[1]) { target = CHAPTERS[i]; break; }
    }
    if (!target) return;
    var card = document.createElement('div');
    card.className = 'resume-card';
    var left = document.createElement('div');
    var label = document.createElement('span');
    label.className = 'label';
    label.textContent = 'Continue reading';
    var a = document.createElement('a');
    a.href = hrefFor(target);
    a.textContent = target.title;
    left.appendChild(label);
    left.appendChild(a);
    card.appendChild(left);
    overview.parentNode.insertBefore(card, overview);
  }

  /* ---- per-section read counts on the homepage overview list — matched
     by section name text since the accent color repeats across folders
     and can't be used as a unique key back to a folder ---- */
  function annotateSectionOverview() {
    var items = document.querySelectorAll('.section-overview li');
    if (!items.length) return;
    items.forEach(function (li) {
      var strong = li.querySelector('strong');
      if (!strong) return;
      var label = strong.textContent.trim();
      var match = FOLDERS.filter(function (f) { return f[1] === label; })[0];
      if (!match) return;
      var read = visitedCountIn(match[0]);
      if (read > 0) {
        var span = document.createElement('span');
        span.className = 'read-count';
        span.textContent = '· ' + read + ' read';
        var countEl = li.querySelector('.count');
        if (countEl) countEl.after(span);
      }
    });
  }

  /* ---- flagship interactive widgets: hand-built, one per concept, on a
     deliberately small set of chapters. Distill/ciechanow-style widgets
     don't generalize into a reusable component — each one visualizes a
     specific mechanism, so this stays 5 chapters, not all 101. ---- */
  function widgetAttention(container) {
    var sentence = ['The', 'cat', 'sat', 'on', 'the', 'mat'];
    function weight(qi, ki) {
      var q = sentence[qi].toLowerCase(), k = sentence[ki].toLowerCase();
      var dist = Math.abs(qi - ki);
      var shareFirstLetter = q[0] === k[0] ? 1.5 : 0;
      return Math.exp(-dist * 0.5) + shareFirstLetter;
    }
    var wrap = document.createElement('div');
    wrap.className = 'flagship-widget';
    wrap.innerHTML = '<span class="fw-label">Interactive</span><div>Click a word to see where it "attends." A simplified, illustrative weighting (distance + shared first letter) — not real trained weights.</div>';
    var row = document.createElement('div');
    row.className = 'fw-row';
    var bars = document.createElement('div');
    bars.className = 'fw-bars';
    function render(qi) {
      var raws = sentence.map(function (_, ki) { return weight(qi, ki); });
      var sum = raws.reduce(function (a, b) { return a + b; }, 0);
      bars.innerHTML = '';
      sentence.forEach(function (tok, ki) {
        var pct = Math.round((raws[ki] / sum) * 100);
        var r = document.createElement('div');
        r.className = 'fw-bar-row';
        r.innerHTML = '<span>' + tok + '</span><span class="fw-bar-track"><span class="fw-bar-fill" style="width:' + pct + '%"></span></span><span>' + pct + '%</span>';
        bars.appendChild(r);
      });
    }
    sentence.forEach(function (tok, i) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'fw-token'; b.textContent = tok;
      b.addEventListener('click', function () {
        row.querySelectorAll('.fw-token').forEach(function (x) { x.classList.remove('active'); });
        b.classList.add('active');
        render(i);
      });
      row.appendChild(b);
    });
    wrap.appendChild(row);
    wrap.appendChild(bars);
    container.appendChild(wrap);
    row.querySelector('.fw-token').classList.add('active');
    render(0);
  }

  function widgetRAG(container) {
    var docs = [
      'Retrieval-augmented generation looks up documents before answering.',
      'Vector databases store embeddings for fast similarity search.',
      'The Eiffel Tower is a landmark in Paris, France.',
      'Fine-tuning adapts a pretrained model to a new task with labeled data.',
      'Cats are small domesticated carnivorous mammals.'
    ];
    function score(query, doc) {
      var qWords = query.toLowerCase().split(/\W+/).filter(Boolean);
      var dWords = doc.toLowerCase().split(/\W+/);
      return qWords.filter(function (w) { return dWords.indexOf(w) !== -1; }).length;
    }
    var wrap = document.createElement('div');
    wrap.className = 'flagship-widget';
    wrap.innerHTML = '<span class="fw-label">Interactive</span><div>Type a query — documents are ranked by shared-word overlap (a toy stand-in for embedding similarity) and the top matches get stitched into the prompt.</div>';
    var input = document.createElement('input');
    input.type = 'text';
    input.placeholder = 'e.g. Where is the Eiffel Tower?';
    wrap.appendChild(input);
    var list = document.createElement('div');
    list.style.marginTop = '12px';
    wrap.appendChild(list);
    var out = document.createElement('div');
    out.className = 'fw-output';
    wrap.appendChild(out);
    function render(query) {
      var scored = docs.map(function (d, i) { return { d: d, i: i, s: score(query, d) }; })
        .sort(function (a, b) { return b.s - a.s; });
      var top = scored.slice(0, 2).filter(function (r) { return r.s > 0; });
      list.innerHTML = '';
      docs.forEach(function (d, i) {
        var isTop = top.some(function (r) { return r.i === i; });
        var el = document.createElement('div');
        el.className = 'fw-doc' + (isTop ? ' retrieved' : '');
        el.textContent = (isTop ? '✓ retrieved — ' : '') + d;
        list.appendChild(el);
      });
      out.textContent = query
        ? 'Prompt sent to the model:\n\n[Context]\n' + (top.length ? top.map(function (r) { return '- ' + r.d; }).join('\n') : '(no document matched any query word)') + '\n\n[Question]\n' + query
        : 'Type a query above to see which documents get retrieved.';
    }
    input.addEventListener('input', function () { render(input.value.trim()); });
    container.appendChild(wrap);
    render('');
  }

  function widgetPPO(container) {
    var wrap = document.createElement('div');
    wrap.className = 'flagship-widget';
    wrap.innerHTML = '<span class="fw-label">Interactive</span><div>The exact PPO-clip objective: L = min(r·A, clip(r, 1−ε, 1+ε)·A). Move the sliders.</div>';
    function rowFor(labelText, min, max, step, val) {
      var r = document.createElement('div');
      r.className = 'fw-row';
      var label = document.createElement('span');
      label.style.width = '150px';
      label.textContent = labelText;
      var input = document.createElement('input');
      input.type = 'range'; input.min = min; input.max = max; input.step = step; input.value = val;
      var out = document.createElement('span');
      out.style.fontFamily = 'var(--font-mono)'; out.style.width = '48px';
      r.appendChild(label); r.appendChild(input); r.appendChild(out);
      wrap.appendChild(r);
      return { input: input, out: out };
    }
    var eps = rowFor('epsilon (ε)', 0.05, 0.5, 0.01, 0.2);
    var adv = rowFor('advantage (A)', -2, 2, 0.1, 1);
    var ratio = rowFor('ratio r = π/π_old', 0.3, 1.8, 0.01, 1);
    var out = document.createElement('div');
    out.className = 'fw-output';
    wrap.appendChild(out);
    function update() {
      var e = parseFloat(eps.input.value), a = parseFloat(adv.input.value), r = parseFloat(ratio.input.value);
      eps.out.textContent = e.toFixed(2); adv.out.textContent = a.toFixed(1); ratio.out.textContent = r.toFixed(2);
      var clipped = Math.min(Math.max(r, 1 - e), 1 + e);
      var unclippedTerm = r * a, clippedTerm = clipped * a;
      var L = Math.min(unclippedTerm, clippedTerm);
      out.textContent = 'r·A = ' + unclippedTerm.toFixed(3) + '\nclip(r,1−ε,1+ε)·A = ' + clippedTerm.toFixed(3) + (clipped !== r ? '  (r was clamped)' : '') + '\n\nL = min(...) = ' + L.toFixed(3);
    }
    [eps.input, adv.input, ratio.input].forEach(function (i) { i.addEventListener('input', update); });
    update();
    container.appendChild(wrap);
  }

  function widgetQuantization(container) {
    var wrap = document.createElement('div');
    wrap.className = 'flagship-widget';
    wrap.innerHTML = '<span class="fw-label">Interactive</span><div>Linear quantization of a fixed value over the range [−4, 4]. Fewer bits, coarser steps, more error.</div>';
    var value = 3.14159;
    var row = document.createElement('div');
    row.className = 'fw-row';
    var label = document.createElement('span'); label.textContent = 'bit-width';
    var input = document.createElement('input');
    input.type = 'range'; input.min = 1; input.max = 4; input.step = 1; input.value = 3;
    var out = document.createElement('span'); out.style.fontFamily = 'var(--font-mono)';
    row.appendChild(label); row.appendChild(input); row.appendChild(out);
    wrap.appendChild(row);
    var result = document.createElement('div');
    result.className = 'fw-output';
    wrap.appendChild(result);
    var bitsMap = { 1: 2, 2: 4, 3: 8, 4: 16 };
    function update() {
      var bits = bitsMap[input.value];
      out.textContent = bits + '-bit';
      var levels = Math.pow(2, bits);
      var range = 8;
      var step = range / (levels - 1);
      var quantized = Math.round((value + 4) / step) * step - 4;
      var error = Math.abs(value - quantized);
      result.textContent = 'Original: ' + value.toFixed(5) + '\nQuantized (' + bits + '-bit): ' + quantized.toFixed(5) + '\nAbsolute error: ' + error.toFixed(5) + '\nLevels available: ' + levels;
    }
    input.addEventListener('input', update);
    update();
    container.appendChild(wrap);
  }

  function widgetKVCache(container) {
    var wrap = document.createElement('div');
    wrap.className = 'flagship-widget';
    wrap.innerHTML = '<span class="fw-label">Interactive</span><div>Step generation forward and watch the KV cache grow. Illustrative sizing: 2 · layers · heads · head_dim · seq_len · 2 bytes (fp16), using GPT-3-scale dimensions.</div>';
    var layers = 32, heads = 32, headDim = 128, bytesPerVal = 2, MAX_SEQ = 64, seq = 0;
    var row = document.createElement('div');
    row.className = 'fw-row';
    var stepBtn = document.createElement('button'); stepBtn.type = 'button'; stepBtn.className = 'fw-token'; stepBtn.textContent = 'Generate next token';
    var resetBtn = document.createElement('button'); resetBtn.type = 'button'; resetBtn.className = 'fw-token'; resetBtn.textContent = 'Reset';
    row.appendChild(stepBtn); row.appendChild(resetBtn);
    wrap.appendChild(row);
    var track = document.createElement('div');
    track.className = 'fw-bar-track'; track.style.height = '16px';
    var fill = document.createElement('div');
    fill.className = 'fw-bar-fill'; fill.style.width = '0%';
    track.appendChild(fill);
    wrap.appendChild(track);
    var out = document.createElement('div');
    out.className = 'fw-output';
    wrap.appendChild(out);
    function update() {
      var bytes = 2 * layers * heads * headDim * seq * bytesPerVal;
      var mb = bytes / (1024 * 1024);
      fill.style.width = Math.min(100, (seq / MAX_SEQ) * 100) + '%';
      out.textContent = 'Tokens generated: ' + seq + ' / ' + MAX_SEQ + '\nKV cache size: ' + mb.toFixed(1) + ' MB\n(32 layers · 32 heads · 128 head-dim · fp16)';
    }
    stepBtn.addEventListener('click', function () { if (seq < MAX_SEQ) { seq++; update(); } });
    resetBtn.addEventListener('click', function () { seq = 0; update(); });
    update();
    container.appendChild(wrap);
  }

  var FLAGSHIP_WIDGETS = {
    'foundations/attention-mechanism.html': widgetAttention,
    'context-retrieval-agents/rag.html': widgetRAG,
    'training-adaptation/rlhf-dpo-ppo.html': widgetPPO,
    'training-adaptation/quantization.html': widgetQuantization,
    'training-adaptation/kv-cache-inference-optimization.html': widgetKVCache
  };
  function buildFlagshipWidget() {
    if (CURRENT_CHAPTER_IDX === -1) return;
    var fn = FLAGSHIP_WIDGETS[CURRENT_FOLDER + '/' + CURRENT_FILE];
    if (!fn) return;
    var chapter = document.querySelector('.chapter');
    if (!chapter || chapter.querySelector('.flagship-widget')) return;
    var anchor = chapter.querySelector('.lede');
    var container = document.createElement('div');
    if (anchor && anchor.parentNode === chapter) anchor.after(container);
    else chapter.appendChild(container);
    fn(container);
  }

  function boot() {
    var topbar = buildTopbar();
    buildProgressBadge(topbar.actions);
    buildThemeToggle(topbar.actions);
    buildCommandPalette(topbar.actions);
    buildBackToTop();
    buildProgressBar();
    buildSectionNav();
    buildCopyButtons();
    enhanceChapterNav();
    buildFlagshipWidget();
    buildResumeCard();
    annotateSectionOverview();
    var openSection = buildLeftNav(topbar.actions);
    topbar.wireSections(openSection);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
