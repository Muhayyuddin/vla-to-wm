# From Reactive Vision–Language–Action Policies to Predictive World Models: A Review for Robotic Manipulation

Companion materials for a manuscript being prepared for IEEE Access. This repository brings together the paper, editable LaTeX source, a linked literature register, verified plotting data, figures, and a guide to the models discussed in the review. Publication details will be added when available.

[Previous manuscript render](paper/manuscript.pdf) · [Latest LaTeX source](paper/manuscript.tex) · [Bibliography](paper/references.bib) · [Excel data and source register](data/VLA_WM_verified_data_and_plots.xlsx) · [Build instructions](docs/BUILD.md)

The [review-response record](docs/REVIEW_RESPONSE_2026-10-02.md) documents the 2 October changes and remaining build limitation. The [finalized literature register](data/VLA_WM_Literature_Register.xlsx) is the source for the 144 included-report total.

**Build status:** `paper/manuscript.pdf` is the **PREVIOUS RENDER**, built on 1 October 2026 at 13:51. It does not contain the 2 October revisions. The latest LaTeX source, bibliography, literature register and standalone vector figures are newer. A current main-manuscript PDF has not yet been verified; the last reported built-in editor compilation failed with “Unable to find standard directories for platform”. Use the [latest source](paper/manuscript.tex) and [build guide](docs/BUILD.md), and do not treat the previous PDF as the final draft.


**Companion snapshot: 2 October 2026.** The author-confirmed corpus contains **144 reports: 69 VLA, 42 world-model and 33 dataset/benchmark/evaluation reports**. The reading guide contains 74 policy rows, 55 world-model/predictive-system rows and 31 related-method rows. Hybrid systems can appear in both main tables; catalogue rows are not distinct-paper or included-study counts.

### Quick navigation

- [VLA policies](#vla-policies-and-language-conditioned-manipulation-policies)
- [World models and predictive systems](#world-models-and-related-predictive-systems)
- [Related methods and contextual systems](#related-training-methods-planners-controllers-and-data-engines)
- [Representative architectures](#representative-architectures)
- [Taxonomy](#taxonomy-used-in-the-paper) and [evidence synthesis](#what-the-evidence-supports)
- [Verified data and figures](#verified-quantitative-data)
- [Open research directions](#research-questions-left-open)
- [Literature register and review status](#literature-counts-and-review-status)
- [Files and reproduction](#using-the-files)

## What the review examines

The review asks how robotic manipulation can progress from generating actions from observations and instructions to predicting the consequences of those actions. It connects six recurring VLA limitations to candidate world-model mechanisms, then examines whether the reported experiments demonstrate the intended benefit.

The emphasis is on manipulation, including grasping, dexterous interaction, and mobile manipulation. Earlier control methods, passive-video prediction, and results from other domains provide context where relevant. Evidence from games or navigation is distinguished from physical manipulation evidence.

Four questions organize the paper:

1. Which VLA systems have been proposed for manipulation, and which problems do they address?
2. What limitations and evaluation gaps are documented in current VLA research?
3. Which predictive mechanisms could address those limitations, and how directly are their effects supported?
4. Under which experimental protocols can results be compared, and where is evidence still incomplete?

## Terms and boundaries

**Vision–language–action policy.** A policy that uses visual observations and language instructions to produce robot actions. The catalogue uses this broad interface definition: it covers both policies built on large pretrained vision–language models and earlier language-conditioned visuomotor policies. Planning systems that call separate controllers, policies without language conditioning, and training or inference methods are identified separately.

**Reactive policy interface.** An interface that selects actions without exposing an action-conditioned transition model for comparing predicted consequences. “Reactive” does not mean that the policy has no memory, reasoning process, or learned representation of dynamics.

**World model.** A predictive model of environmental change. For control, the central question is whether it can predict how state changes under a supplied action. The review also considers generative video models and predictive representations that contribute to policy learning or are subsequently adapted to action-conditioned prediction.

**World–action model.** A system that combines prediction and action generation within a shared architecture or training process. Jointly predicting images and actions does not, by itself, demonstrate explicit search over alternative action sequences. Action conditioning also does not, by itself, establish causal validity.

These are overlapping functional descriptions. A single system may learn predictive representations, generate synthetic trajectories, and produce actions, while using only some of those capabilities during deployment.

## Representative architectures

The [detailed VLA architecture](paper/figures/vla-detailed-architecture.pdf) separates learning from demonstrations from deployment. Images, language and optional proprioception/history form a context for one of several action-head alternatives; an action chunk is partly executed before observations are refreshed. [Editable TikZ source](paper/tkz/vla-detailed-architecture.tex).

The [detailed world-model architecture](paper/figures/world-model-detailed-architecture.pdf) separates transition training, supplied-action prediction and one model-based planning loop. Task goals guide scoring, while candidate actions condition dynamics; observation, task-outcome and uncertainty heads are optional. This interface does not imply that every predictive model plans online or provides calibrated uncertainty. [Editable TikZ source](paper/tkz/world-model-detailed-architecture.tex).

## Model catalogue

The tables cover the current manuscript's named policies and predictive systems, retain the earlier catalogue's contextual coverage, and include the author-confirmed Seer, Video Prediction Policy and Unified World Models additions. They are a reading guide, not a ranking, a screening ledger, or a count of included reports. A row can denote a family, variant, platform component, or method; predictive policies intentionally appear in both main tables.

“VLA” here uses the broad interface criterion of visual observations and language conditioning leading to robot actions. Earlier language-conditioned policies are labeled as precursors. Related planners, controllers without language conditioning, optimization methods, and conventional-simulator data engines appear in a separate table. OXE, DROID, BridgeData V2, AgiBot World, RH20T, and RoboMIND are datasets rather than model entries; RT-X is included as the policy family associated with OXE.

Links identify primary papers where available. Official model cards and technical announcements are explicitly labeled; their presence does not imply independent evaluation or a dedicated research paper. Descriptions distinguish auxiliary predictive training, future generation, action-conditioned dynamics, and online planning. Historical Dreamer/Genie variants and Sora provide family context; HULC is retained as a related comparator, QueST as a named RIPT-VLA baseline, and Mobility VLA only as related navigation outside the manipulation scope.

### VLA policies and language-conditioned manipulation policies

| Name | Role | Short description | Primary paper / source |
| --- | --- | --- | --- |
| 3D-CAVLA | VLA policy | Combines depth information, task-relevant visual regions, and intermediate reasoning to adapt VLA policies for manipulation. | [Paper](https://arxiv.org/abs/2505.05800) |
| 3D-VLA (predictive-policy hybrid) | Predictive VLA policy; world-model overlap | Combines 3D visual-language representations with generation of future observations and robot actions, linking spatial grounding with predictive policy learning. | [Paper](https://arxiv.org/abs/2403.09631) |
| Act3D (language-conditioned 3D policy) | Language-conditioned policy / precursor | Uses a hierarchical 3D feature field to predict manipulation actions from visual observations and task instructions. | [Paper](https://arxiv.org/abs/2306.17817) |
| BitVLA | VLA policy | Uses low-bit model weights and a compressed visual encoder to reduce the memory and inference cost of a VLA policy. | [Paper](https://arxiv.org/abs/2506.07530) |
| BridgeVLA | VLA policy | Projects 3D observations into multiple image views and predicts spatial action heatmaps, aligning the policy's input and output representations. | [Paper](https://arxiv.org/abs/2506.07961) |
| CogACT | VLA policy | Conditions a specialized diffusion action transformer on a vision-language backbone to connect semantic interpretation with continuous manipulation actions. | [Paper](https://arxiv.org/abs/2411.19650) |
| Cosmos Policy | Predictive policy; world-model table overlap | Adapts a video model to jointly generate actions, future states and values; evaluates direct policy execution and a separate package for rollout refinement and candidate selection. | [Paper](https://arxiv.org/abs/2601.16163) |
| CoT-VLA (predictive-policy hybrid) | Predictive VLA policy; world-model overlap | Predicts future images as intermediate visual goals before generating action sequences. It combines visual prediction and control without, by itself, establishing candidate-action search. | [Paper](https://arxiv.org/abs/2503.22020) |
| DexVLA | VLA policy | Connects a vision-language backbone to a pretrained diffusion action expert, with staged adaptation across robot embodiments and tasks. | [Paper](https://arxiv.org/abs/2502.05855) |
| Discrete Diffusion VLA | VLA policy | Generates discretized action chunks through iterative diffusion-style refinement within a shared transformer, supporting parallel action decoding. | [Paper](https://arxiv.org/abs/2508.20072) |
| DreamVLA | Predictive policy; world-model table overlap | Forecasts compact dynamic, spatial and semantic representations and conditions diffusion-based action generation on this predicted world knowledge. | [Paper](https://arxiv.org/abs/2507.04447) |
| DreamZero | Predictive policy; world-model table overlap | DreamZero jointly predicts future video and robot actions using a pretrained video-diffusion backbone. It uses this world-action representation for closed-loop control and studies transfer from heterogeneous robot data and video demonstrations. | [Paper](https://arxiv.org/abs/2602.15922) |
| ECoT | VLA policy | Trains a VLA to generate intermediate plans and visually grounded reasoning before predicting robot actions. | [Paper](https://arxiv.org/abs/2407.08693) |
| EdgeVLA / EVLA | VLA policy | Combines a smaller language backbone with non-autoregressive action prediction to reduce deployment cost on resource-constrained robot hardware. | [Paper](https://arxiv.org/abs/2507.14049) |
| FAST / π0-FAST | Action tokenizer and demonstrated policy variant | FAST compresses continuous action chunks into frequency-domain tokens for autoregressive prediction. π0-FAST is a policy variant demonstrating this tokenization approach. | [Paper](https://arxiv.org/abs/2501.09747) |
| FLARE — implicit world modeling | Predictive policy; world-model table overlap | Aligns policy features with embeddings of future observations to incorporate latent prediction into diffusion-based action learning; also supports co-training with action-free video. | [Paper](https://arxiv.org/abs/2505.15659) |
| ForceVLA | VLA policy | Integrates force-torque feedback with visual-language features through a force-aware mixture-of-experts module for contact-rich manipulation. | [Paper](https://arxiv.org/abs/2505.22159) |
| FP3 (language-conditioned 3D policy) | Language-conditioned policy | Pretrains a diffusion-transformer manipulation policy using point clouds, proprioception, and CLIP-encoded instructions, then adapts it to downstream tasks. | [Paper](https://arxiv.org/abs/2503.08950) |
| GE-Act (Genie Envisioner component) | Predictive platform action policy | Uses the Genie Envisioner video representation for instruction-conditioned robot action generation. It is the platform's action-policy component; GE-Sim is its learned-simulator component. | [Paper](https://arxiv.org/abs/2508.05635) |
| Gemini Robotics | VLA policy | A Gemini-based VLA family for language-conditioned robot control across manipulation tasks and embodiments; reported evaluations originate from the model developer. | [Paper](https://arxiv.org/abs/2503.20020) |
| Gemini Robotics 1.5 | VLA policy | A vendor-reported multi-embodiment VLA that integrates reasoning with action generation and supports motion transfer across robot configurations. | [Paper](https://arxiv.org/abs/2510.03342) |
| Gemini Robotics On-Device | VLA policy | A vendor-reported VLA designed to run locally on robot hardware and adapt to manipulation tasks through fine-tuning. | [Official technical source](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/) |
| GeoVLA | VLA policy | Fuses image-language representations with point-cloud geometry in a spatially informed action expert. | [Paper](https://arxiv.org/abs/2508.09071) |
| GR-1 (predictive-policy hybrid) | Predictive VLA policy; world-model overlap | Predicts future images and robot actions from language, image history, and proprioception after video pretraining. Joint prediction is distinct from evaluating supplied candidate actions. | [Paper](https://arxiv.org/abs/2312.13139) |
| GR-2 (predictive-policy hybrid) | Predictive VLA policy; world-model overlap | Uses large-scale video pretraining followed by joint video and action learning for generalist manipulation. | [Paper](https://arxiv.org/abs/2410.06158) |
| GR00T N1 | VLA policy | A generalist humanoid policy that connects vision-language interpretation to diffusion-based action generation. | [Paper](https://arxiv.org/abs/2503.14734) |
| GR00T N1.5 | VLA policy | Extends GR00T N1 with architectural and data changes, including future-latent representation alignment for policy learning. | [Official technical source](https://research.nvidia.com/labs/gear/gr00t-n1_5/) |
| GR00T N1.7 | VLA policy | GR00T N1.7 is a cross-embodiment robot policy that conditions action chunks on visual observations, language, and proprioception. Its released model uses a flow-matching action transformer and supports post-training for particular robots and tasks. | [Official model card; no dedicated paper identified](https://huggingface.co/nvidia/GR00T-N1.7-3B) |
| GraspVLA | VLA policy | Combines autoregressive perception and flow-matching action generation for grasping, using large-scale synthetic robot data alongside semantic pretraining. | [Paper](https://arxiv.org/abs/2505.03233) |
| HarmoWAM | Predictive policy; world-model table overlap | Combines predictive and reactive action experts through adaptive gating to balance generalization and precise control. | [Paper](https://arxiv.org/abs/2605.10942) |
| Helix | VLA policy | A vendor-reported humanoid VLA combining a slower vision-language component with a faster continuous-action controller for upper-body manipulation. | [Official technical source](https://www.figure.ai/news/helix) |
| Helix 02 | VLA and whole-body control system | Helix 02 combines language and scene reasoning, a full-body visuomotor policy, and a learned low-level whole-body controller. The vendor describes coordinated locomotion and manipulation using visual, tactile, and proprioceptive inputs. | [Official technical release; vendor-reported](https://www.figure.ai/news/helix-02) |
| Hi Robot | VLA policy | Uses hierarchical vision-language-action policies to interpret complex instructions and user feedback, then execute the selected manipulation steps. | [Paper](https://arxiv.org/abs/2502.19417) |
| HULC (language-conditioned policy) | Language-conditioned comparator; related context | A hierarchical language-conditioned imitation policy using latent plans and aligned visual-language representations for multi-task manipulation. | [Paper](https://arxiv.org/abs/2204.06252) |
| LAPA | VLA policy | Learns latent actions from video without ground-truth action labels during pretraining, then adapts the latent policy to robot actions using robot data. | [Paper](https://arxiv.org/abs/2410.11758) |
| LaWAM | Predictive policy; world-model table overlap | Predicts latent visual subgoals and conditions action generation on them, using a latent world model to provide foresight without dense pixel generation. | [Paper](https://arxiv.org/abs/2606.15768) |
| LingBot-VLA 2.0 | VLA policy with auxiliary predictive supervision | LingBot-VLA 2.0 extends a generalist VLA with whole-body action spaces and training across multiple robot embodiments and human videos. Auxiliary future prediction uses video-representation and depth-estimation supervision to connect action learning with temporal and geometric information. | [Paper](https://arxiv.org/abs/2607.06403) |
| LLARVA | VLA policy | Uses vision-action instruction tuning and intermediate 2D visual traces to align multimodal representations with robot behavior. | [Paper](https://arxiv.org/abs/2406.11815) |
| LoHoVLA | VLA policy | Jointly generates subtask language and robot-action tokens, using hierarchical feedback to support multi-step manipulation. | [Paper](https://arxiv.org/abs/2506.00411) |
| Long-VLA | VLA policy | Uses phase-aware masking of sensory inputs to improve subtask coordination and long-horizon manipulation. | [Paper](https://arxiv.org/abs/2508.19958) |
| ManiGaussian | Predictive policy; world-model table overlap | Uses dynamic Gaussian representations and future-scene reconstruction as predictive supervision for language-conditioned manipulation; the cited evaluation uses RLBench simulation. | [Paper](https://arxiv.org/abs/2403.08321) |
| MemoryVLA | VLA policy | Combines perceptual and semantic memory retrieval with a memory-conditioned diffusion action expert for temporally dependent manipulation. | [Paper](https://arxiv.org/abs/2508.19236) |
| Octo | VLA policy | An open generalist robot policy with a diffusion action head, supporting language or image goals and adaptation to new observation and action interfaces. | [Paper](https://arxiv.org/abs/2405.12213) |
| OneTwoVLA | VLA policy | Unifies reasoning and action generation, switching between explicit reasoning and execution as the task progresses. | [Paper](https://arxiv.org/abs/2505.11917) |
| OpenVLA | VLA policy | An open VLA that combines pretrained visual-language representations with autoregressive robot-action prediction and task-specific fine-tuning. | [Paper](https://arxiv.org/abs/2406.09246) |
| OpenVLA-OFT | VLA adaptation recipe and resulting policy | An optimized fine-tuning recipe for OpenVLA using action chunking and parallel continuous regression rather than sequential action-token decoding. | [Paper](https://arxiv.org/abs/2502.19645) |
| PerAct (language-conditioned 3D policy) | Language-conditioned policy / precursor | A language-conditioned behavior-cloning policy that uses voxelized observations and a Perceiver architecture for 6-DoF manipulation. | [Paper](https://arxiv.org/abs/2209.05451) |
| π0 | VLA policy | Pairs a pretrained vision-language backbone with a flow-matching action expert for continuous robot control across tasks and embodiments. | [Paper](https://arxiv.org/abs/2410.24164) |
| π0.5 | VLA policy | Extends the π0 approach through heterogeneous co-training and hierarchical task conditioning for manipulation beyond familiar training environments. | [Paper](https://arxiv.org/abs/2504.16054) |
| π0.7 | VLA policy | π0.7 conditions a generalist robot policy on language and additional context such as subgoal images and task-performance metadata. This conditioning supports steering the execution strategy while training on demonstrations, autonomous experience, and non-robot data. | [Paper](https://arxiv.org/abs/2604.15483) |
| PointVLA | VLA policy | Adds point-cloud features to pretrained VLA action modules through lightweight adaptation, improving access to 3D geometry. | [Paper](https://arxiv.org/abs/2503.07511) |
| QueST (language-conditioned skill policy) | Language-conditioned policy | Learns quantized temporal skill representations from action sequences and predicts skills from visual observations and task descriptions for multitask and few-shot control. It provides a lightweight policy baseline for RIPT-VLA. | [Paper](https://arxiv.org/abs/2407.15840) |
| RationalVLA | VLA policy | Couples high-level instruction reasoning with manipulation control and includes rejection of commands judged infeasible or defective. | [Paper](https://arxiv.org/abs/2506.10826) |
| RDT-1B | VLA policy | A diffusion-transformer policy for bimanual manipulation that uses a unified action representation across robot configurations. | [Paper](https://arxiv.org/abs/2410.07864) |
| RoboFlamingo | VLA policy | Adapts a pretrained OpenFlamingo vision-language model to robot imitation learning with an action-prediction interface. | [Paper](https://arxiv.org/abs/2311.01378) |
| RoboMamba | VLA policy | Uses a Mamba state-space backbone to connect multimodal reasoning with efficient manipulation-action prediction. | [Paper](https://arxiv.org/abs/2406.04339) |
| RT-1 (contextual precursor) | Language-conditioned policy / precursor | A transformer policy that maps camera observations and language instructions to discretized robot-control commands. | [Paper](https://arxiv.org/abs/2212.06817) |
| RT-2 | VLA policy | Represents robot actions as tokens and co-trains on robot trajectories and vision-language tasks to transfer semantic knowledge into control. | [Paper](https://arxiv.org/abs/2307.15818) |
| RT-H | VLA policy | Introduces a language-mediated action hierarchy between task instructions and low-level robot commands. | [Paper](https://arxiv.org/abs/2403.01823) |
| RT-X family (RT-1-X / RT-2-X) | VLA policy | Cross-embodiment robot policies trained using the Open X-Embodiment collection. This entry concerns the RT-X models rather than the dataset itself. | [Paper](https://arxiv.org/abs/2310.08864) |
| RVT (language-conditioned 3D policy) | Language-conditioned policy / precursor | Combines rendered multi-view observations and language-goal embeddings in a transformer to predict spatially grounded manipulation actions. | [Paper](https://arxiv.org/abs/2306.14896) |
| RVT-2 | VLA policy | Improves the efficiency and spatial precision of multi-view manipulation policies, emphasizing learning from limited demonstrations. | [Paper](https://arxiv.org/abs/2406.08545) |
| Seer | Predictive VLA policy; world-model overlap | Learns a predictive inverse-dynamics policy that produces robot actions conditioned on forecast visual states. It is pretrained on robot demonstrations and evaluated in simulated and physical manipulation, including robustness and generalization tests. | [Paper (2024)](https://arxiv.org/abs/2412.15109) |
| SmolVLA | VLA policy | A compact VLA with a flow-matching action expert and asynchronous inference intended to support affordable robot training and deployment. | [Paper](https://arxiv.org/abs/2506.01844) |
| SpatialVLA | VLA policy | Uses geometric visual representations and spatial action tokens to improve language-conditioned manipulation. | [Paper](https://arxiv.org/abs/2501.15830) |
| StructVLA | Predictive policy; world-model table overlap | First trains a generative model to predict sparse visual milestones from instructions and observation history. A second stage adapts the model to action-token prediction conditioned on instructions and interleaved observation–action history. | [Paper](https://arxiv.org/abs/2603.12553) |
| Tactile-VLA | VLA policy | Combines tactile feedback and multimodal reasoning with a hybrid position-force controller for physical interaction. | [Paper](https://arxiv.org/abs/2507.09160) |
| Tactile-WAM | Predictive policy; world-model table overlap | Jointly models visual, tactile and action information with tactile asymmetric attention, directing contact information toward action prediction while limiting interference with video generation. | [Paper](https://arxiv.org/abs/2606.26663) |
| TinyVLA | VLA policy | Combines a compact multimodal backbone with a diffusion action decoder for data-efficient manipulation learning. | [Paper](https://arxiv.org/abs/2409.12514) |
| TouchWorld | Predictive policy; world-model table overlap | Combines predicted tactile subgoals and visuomotor action chunks with a faster tactile/proprioceptive correction policy for contact-rich dexterous manipulation. | [Paper](https://arxiv.org/abs/2607.07287) |
| Video Prediction Policy (VPP) | Predictive VLA policy; world-model overlap | Uses representations inside a video diffusion model to condition an implicit inverse-dynamics policy. The video model is adapted with robot and human-manipulation data and evaluated on generalization and dexterous manipulation. | [Paper (2024)](https://arxiv.org/abs/2412.14803) |
| VIMA (contextual multimodal policy) | Language-conditioned policy / precursor | Uses interleaved image and text prompts to specify manipulation tasks, then generates robot actions with a transformer policy. | [Paper](https://arxiv.org/abs/2210.03094) |
| VLA-JEPA | Predictive policy; world-model table overlap | Pretrains a policy backbone to predict future latent states from current observations, then fine-tunes an action head. The future frames provide supervision rather than inputs to the prediction pathway. | [Paper](https://arxiv.org/abs/2602.10098) |
| WorldVLA | Predictive policy; world-model table overlap | Uses shared autoregressive modeling for actions and future observations. Predictive supervision is evaluated as a training component, separately from the question of online candidate-action search. | [Paper](https://arxiv.org/abs/2506.21539) |

### World models and related predictive systems

This table includes latent control models, generative environments, predictive representations, data/evaluation pipelines, and predictive action architectures. An auxiliary future-prediction objective or joint video/action generator does not, by itself, establish a forward-model interface for supplied candidate actions or online search. Game-domain and representation-learning precursors remain explicitly distinguished from physical robot control.

| Name | Role | Short description | Primary paper / source |
| --- | --- | --- | --- |
| 3D-VLA | Predictive action architecture; VLA overlap | Combines a 3D vision-language backbone with generation of goal images or point clouds and robot actions, linking multimodal prediction with manipulation. | [Paper](https://arxiv.org/abs/2403.09631) |
| AVDC | Video prediction / generated environments | Generates task-directed videos and uses dense inter-frame correspondences to infer control actions from action-free demonstrations. | [Paper](https://arxiv.org/abs/2310.08576) |
| Cosmos | Video prediction / generated environments | Provides video tokenization and generative world foundation models for physical-AI development. Specific action-conditioning and robot-control capabilities depend on the chosen model and adaptation. | [Paper](https://arxiv.org/abs/2501.03575) |
| Cosmos Policy | Predictive action architecture; VLA overlap | Adapts a video model to jointly generate actions, future states and values; evaluates direct policy execution and a separate package for rollout refinement and candidate selection. | [Paper](https://arxiv.org/abs/2601.16163) |
| CoT-VLA | Predictive action architecture; VLA overlap | Predicts future visual goals as an intermediate representation before generating action sequences; its visual chain of thought is a predictive policy mechanism. | [Paper](https://arxiv.org/abs/2503.22020) |
| Ctrl-World | Learned simulation / data / evaluation | Combines multi-view video prediction, frame-level action conditioning and pose-conditioned memory retrieval for policy rollouts, evaluation and generation of corrective training data. | [Paper](https://arxiv.org/abs/2510.10125) |
| DINO-WM | Predictive representation / latent planning | Learns action-conditioned transitions over pretrained DINO patch features and plans toward visual goals without reconstructing images. | [Paper](https://arxiv.org/abs/2411.04983) |
| DreamDojo | Action-conditioned video world model | DreamDojo learns an action-conditioned video world model from human videos using continuous latent actions as proxy controls, then adapts it with robot data. Its generated rollouts support applications including policy evaluation and model-based planning. | [Paper](https://arxiv.org/abs/2602.06949) |
| Dreamer (first generation) | Historical / family context | Learns an actor and value function from imagined trajectories in a latent dynamics model, with gradients through predicted states for visual continuous control. | [Paper](https://arxiv.org/abs/1912.01603) |
| Dreamer 4 | Latent dynamics / model-based control | Trains policies inside a scalable video world model using offline data; separate ablations examine action conditioning with partial labels. Its principal demonstration is Minecraft, not physical manipulation. | [Paper](https://arxiv.org/abs/2509.24527) |
| DreamerV2 | Historical / family context | Uses discrete latent dynamics and learns behavior in imagination; its central demonstrations concern Atari. | [Paper](https://arxiv.org/abs/2010.02193) |
| DreamerV3 | Latent dynamics / model-based control | Uses latent imagination with training procedures designed to work across varied control domains using one configuration; a general reinforcement-learning foundation rather than a manipulation-specific VLA. | [Paper](https://arxiv.org/abs/2301.04104) |
| DreamGen | Learned simulation / data / evaluation | Generates task-conditioned robot videos and infers pseudo-actions with inverse dynamics to augment policy-training data; it is an offline data-generation pipeline. | [Paper](https://arxiv.org/abs/2505.12705) |
| DreamVLA | Predictive action architecture; VLA overlap | Forecasts compact dynamic, spatial and semantic representations and conditions diffusion-based action generation on this predicted world knowledge. | [Paper](https://arxiv.org/abs/2507.04447) |
| DreamZero | World-action model and predictive VLA policy | DreamZero jointly predicts future video and robot actions using a pretrained video-diffusion backbone. It uses this world-action representation for closed-loop control and studies transfer from heterogeneous robot data and video demonstrations. | [Paper](https://arxiv.org/abs/2602.15922) |
| FLARE — implicit world modeling | Predictive action architecture; VLA overlap | Aligns policy features with embeddings of future observations to incorporate latent prediction into diffusion-based action learning; also supports co-training with action-free video. | [Paper](https://arxiv.org/abs/2505.15659) |
| GE-Sim — Genie Envisioner component | Learned simulation / data / evaluation | Provides action-conditioned neural simulation for closed-loop policy rollouts within the Genie Envisioner platform; it shares the platform's reference paper. | [Paper](https://arxiv.org/abs/2508.05635) |
| Genie (first generation) | Video prediction / generated environments | Learns latent actions and interactive video dynamics from unlabelled video, allowing generated environments to respond to controls. It is a contextual environment-generation precursor. | [Paper](https://arxiv.org/abs/2402.15391) |
| Genie 2 | Historical / family context | Generates action-controllable 3D visual environments from an image for interactive exploration; included as a predecessor in the Genie family. | [Official research announcement; no paper cited](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) |
| Genie 3 | Video prediction / generated environments | Generates interactive visual environments that respond to user control; the cited release concerns environment generation rather than validated physical robot dynamics. | [Official research announcement; no paper cited](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) |
| Genie Envisioner | Video prediction / generated environments | Unifies instruction-conditioned video modeling, action generation and learned simulation through GE-Base, GE-Act and GE-Sim; the simulator component is listed separately. | [Paper](https://arxiv.org/abs/2508.05635) |
| GR-1 | Predictive action architecture; VLA overlap | Jointly predicts future images and robot actions from language, visual history and robot state after video pretraining; joint prediction does not itself establish online candidate-action search. | [Paper](https://arxiv.org/abs/2312.13139) |
| GR-2 | Predictive action architecture; VLA overlap | Scales video-language-action pretraining and joint visual/action prediction using web video and robot trajectories for manipulation. | [Paper](https://arxiv.org/abs/2410.06158) |
| GWM — Gaussian World Models | Geometric / physical prediction | Uses action-conditioned dynamics over Gaussian scene representations to predict manipulation outcomes, with applications to predictive pretraining and learned simulation. | [Paper](https://arxiv.org/abs/2508.17600) |
| HarmoWAM | Predictive action architecture; VLA overlap | Combines predictive and reactive action experts through adaptive gating to balance generalization and precise control. | [Paper](https://arxiv.org/abs/2605.10942) |
| I-JEPA — representation precursor | Predictive representation precursor; not an action-conditioned world model | Predicts target image-region embeddings from visible image context without reconstructing pixels. It is an image representation learner, not a temporal action-conditioned robot world model. | [Paper](https://arxiv.org/abs/2301.08243) |
| iVideoGPT | Video prediction / generated environments | Autoregressively models tokenized observations, actions and rewards, supporting interactive video prediction, visual planning and model-based reinforcement learning. | [Paper](https://arxiv.org/abs/2405.15223) |
| LaWAM | Predictive action architecture; VLA overlap | Predicts latent visual subgoals and conditions action generation on them, using a latent world model to provide foresight without dense pixel generation. | [Paper](https://arxiv.org/abs/2606.15768) |
| LingBot-VLA 2.0 | VLA with auxiliary predictive supervision; policy-table overlap | LingBot-VLA 2.0 extends a generalist VLA with whole-body action spaces and training across multiple robot embodiments and human videos. Auxiliary future prediction uses video-representation and depth-estimation supervision to connect action learning with temporal and geometric information. | [Paper](https://arxiv.org/abs/2607.06403) |
| ManiGaussian | Geometric / physical prediction | Uses dynamic Gaussian representations and future-scene reconstruction as predictive supervision for language-conditioned manipulation; the cited evaluation uses RLBench simulation. | [Paper](https://arxiv.org/abs/2403.08321) |
| MuZero | Latent dynamics / model-based control | Learns latent transitions that predict rewards, values and action priors for tree search without reconstructing observations. The cited evidence concerns games. | [Paper](https://arxiv.org/abs/1911.08265) |
| PhysDreamer | Geometric / physical prediction | Distills motion priors from video generation into physical material estimates and interactive 3D dynamics. Its evidence concerns synthesized object responses, not downstream physical robot task success. | [Paper](https://arxiv.org/abs/2404.13026) |
| PlaNet | Latent dynamics / model-based control | Learns action-conditioned recurrent latent dynamics from images and selects action sequences with model-predictive control. | [Paper](https://arxiv.org/abs/1811.04551) |
| Seer | Predictive action architecture; VLA overlap | Learns a predictive inverse-dynamics policy that produces robot actions conditioned on forecast visual states. It is pretrained on robot demonstrations and evaluated in simulated and physical manipulation, including robustness and generalization tests. | [Paper (2024)](https://arxiv.org/abs/2412.15109) |
| Sora — 2024 report | Historical / family context | Uses text-conditioned diffusion over spacetime latent patches to generate video; the report discusses emergent simulation properties and limitations rather than verified robot control. | [Technical report](https://openai.com/index/video-generation-models-as-world-simulators/) |
| StructVLA | Predictive action architecture; VLA overlap | First trains a generative model to predict sparse visual milestones from instructions and observation history. A second stage adapts the model to action-token prediction conditioned on instructions and interleaved observation–action history. | [Paper](https://arxiv.org/abs/2603.12553) |
| SuSIE | Video prediction / generated environments | Fine-tunes an image-editing diffusion model to propose visual subgoals from an observation and instruction; a goal-conditioned controller executes the subgoals. | [Paper](https://arxiv.org/abs/2310.10639) |
| Tactile-WAM | Predictive action architecture; VLA overlap | Jointly models visual, tactile and action information with tactile asymmetric attention, directing contact information toward action prediction while limiting interference with video generation. | [Paper](https://arxiv.org/abs/2606.26663) |
| TD-MPC2 | Latent dynamics / model-based control | Learns task-conditioned latent dynamics and value functions for model-predictive control across continuous-control tasks. | [Paper](https://arxiv.org/abs/2310.16828) |
| TesserAct | Geometric / physical prediction | Predicts RGB, depth and surface-normal video to represent the evolution of 3D scenes over time; the multimodal predictions also support inverse-dynamics learning. | [Paper](https://arxiv.org/abs/2504.20995) |
| TouchWorld | Predictive action architecture; VLA overlap | Combines predicted tactile subgoals and visuomotor action chunks with a faster tactile/proprioceptive correction policy for contact-rich dexterous manipulation. | [Paper](https://arxiv.org/abs/2607.07287) |
| UnifoLM-WMA-0 | Released world-model/action framework | Unitree's released world-model/action framework uses predictive video dynamics for simulation and policy enhancement; the cited artifact is a technical release, not a reference paper. | [Official release; paper not identified](https://github.com/unitreerobotics/unifolm-world-model-action) |
| Unified World Models (UWM) | Coupled video/action diffusion | Couples video and action diffusion in one transformer with separate diffusion timesteps for the modalities. Its conditioning supports policy, forward-dynamics, inverse-dynamics and video-generation modes, including learning from action-free video. | [Paper (2025)](https://arxiv.org/abs/2504.02792) |
| UniPi | Video prediction / generated environments | Generates a language-conditioned video plan and recovers executable actions through inverse dynamics; generated plans are not predictions conditioned on supplied candidate robot actions. | [Paper](https://arxiv.org/abs/2302.00111) |
| UniSim | Video prediction / generated environments | Learns an interactive video simulator that responds to high-level instructions or low-level controls, supporting simulated policy learning and evaluation. | [Paper](https://arxiv.org/abs/2310.06114) |
| V-JEPA 2 — action-free backbone | Predictive representation / latent planning | Scales predictive video representation learning for understanding and anticipation. Robotic action-conditioned planning belongs to the separately adapted 2-AC configuration. | [Paper](https://arxiv.org/abs/2506.09985) |
| V-JEPA 2-AC | Predictive representation / latent planning | Adapts V-JEPA 2 with robot-action data to predict latent consequences of actions and plan toward image goals; its robot results use specified goal images and camera configurations. | [Paper](https://arxiv.org/abs/2506.09985) |
| V-JEPA — representation precursor | Predictive representation precursor; not an action-conditioned world model | Learns video representations by predicting masked spatiotemporal features; its pretraining objective does not supply candidate robot actions. | [Paper](https://arxiv.org/abs/2404.08471) |
| Video Prediction Policy (VPP) | Predictive action architecture; VLA overlap | Uses representations inside a video diffusion model to condition an implicit inverse-dynamics policy. The video model is adapted with robot and human-manipulation data and evaluated on generalization and dexterous manipulation. | [Paper (2024)](https://arxiv.org/abs/2412.14803) |
| Video Language Planning (VLP) | Video prediction / generated environments | Searches over language proposals and generated video continuations, using vision-language policies and value functions; a goal-conditioned policy executes the resulting visual plan. | [Paper](https://arxiv.org/abs/2310.10625) |
| VLA-JEPA | Predictive action architecture; VLA overlap | Pretrains a policy backbone to predict future latent states from current observations, then fine-tunes an action head. The future frames provide supervision rather than inputs to the prediction pathway. | [Paper](https://arxiv.org/abs/2602.10098) |
| World Models | Latent dynamics / model-based control | Combines a variational image encoder, recurrent latent dynamics and a compact controller; demonstrates learning behavior within a learned environment in simulated control tasks. | [Paper](https://arxiv.org/abs/1803.10122) |
| World-Gymnast | Learned simulation / data / evaluation | Trains robot policies with reinforcement learning inside a learned environment and tests transfer to hardware. The paper's comparison with conventional simulation has mixed results across four physical tasks. | [Paper](https://arxiv.org/abs/2602.02454) |
| WorldEval / Policy2Vec | Learned simulation / data / evaluation | Adapts video generation to action-following simulation with Policy2Vec and uses generated policy rollouts for evaluation. It is an evaluation pipeline built on a learned simulator, not a benchmark alone. | [Paper](https://arxiv.org/abs/2505.19017) |
| WorldVLA | Predictive action architecture; VLA overlap | Uses shared autoregressive modeling for actions and future observations. Predictive supervision is evaluated as a training component, separately from the question of online candidate-action search. | [Paper](https://arxiv.org/abs/2506.21539) |

### Related training methods, planners, controllers, and data engines

These entries explain the paper's surrounding methodology; they are not all separate VLA models or world models.

| Name | Role | Short description | Primary paper / source |
| --- | --- | --- | --- |
| ACT / ALOHA (contextual) | Imitation-learning baseline / platform | Action Chunking with Transformers learns sequences of bimanual control commands from demonstrations. ALOHA provides the associated low-cost teleoperation platform. | [Paper](https://arxiv.org/abs/2304.13705) |
| CEED-VLA | Policy training / inference method | Accelerates action-token generation through consistency distillation and early-exit decoding. | [Paper](https://arxiv.org/abs/2506.13725) |
| Code as Policies (contextual planner) | Contextual planner / control system | Generates robot policy programs from language instructions. The programs connect perception outputs to control APIs and feedback loops. | [Paper](https://arxiv.org/abs/2209.07753) |
| ConRFT | Policy training / inference method | Fine-tunes VLA policies through offline and online reinforcement learning using a consistency-based objective and human intervention during online training. | [Paper](https://arxiv.org/abs/2502.05450) |
| DAgger | Dataset-aggregation imitation-learning method | Iteratively gathers expert labels for states visited by the current policy and adds them to the training data. It addresses the distribution shift induced by a learned policy rather than defining a VLA or world-model architecture. | [Paper](https://proceedings.mlr.press/v15/ross11a.html) |
| DeeR-VLA | Policy training / inference method | Uses a multi-exit multimodal backbone to adapt inference depth to the current input and computational constraints. | [Paper](https://arxiv.org/abs/2411.02359) |
| DexMimicGen | Conventional-simulator data engine; not a learned world model | Extends demonstration-based data generation to bimanual dexterous manipulation in simulation, including coordination between manipulators. | [Paper](https://arxiv.org/abs/2410.24185) |
| Diffusion Policy (contextual) | Imitation-learning baseline / platform | Models visuomotor action sequences through conditional denoising diffusion and executes them with a receding-horizon controller. | [Paper](https://arxiv.org/abs/2303.04137) |
| EfficientVLA | Policy training / inference method | Accelerates existing VLAs without retraining through language-layer pruning, visual-token selection, and reuse of diffusion-head features. | [Paper](https://arxiv.org/abs/2506.10100) |
| FLaRe (RL fine-tuning) | Policy training / inference method | Uses large-scale reinforcement-learning fine-tuning to improve pretrained robot policies. This is distinct from the predictive representation method named FLARE. | [Paper](https://arxiv.org/abs/2409.16578) |
| GRAPE | Policy training / inference method | Aligns robot policies using trajectory preferences derived from successful and unsuccessful behavior, with task-specific spatial and temporal constraints. | [Paper](https://arxiv.org/abs/2411.19309) |
| iRe-VLA | Policy training / inference method | Alternates reinforcement-learning improvement with supervised learning to stabilize interactive VLA adaptation. | [Paper](https://arxiv.org/abs/2501.16664) |
| KnowNo (contextual assurance framework) | Uncertainty / help-seeking method | Uses conformal prediction to calibrate uncertainty in language-model planning and determine when a robot should request assistance. | [Paper](https://arxiv.org/abs/2307.01928) |
| Lift3D Foundation Policy | Visuomotor policy without language conditioning | Adapts pretrained 2D visual features to implicit and explicit 3D representations for manipulation policies. The reported policy uses point clouds and robot state without language conditioning. | [Paper](https://arxiv.org/abs/2411.18623) |
| MimicGen | Conventional-simulator data engine; not a learned world model | Transforms and recombines a small set of human demonstrations to generate additional robot trajectories in conventional simulation; included as a data-generation precedent. | [Paper](https://arxiv.org/abs/2310.17596) |
| Mobile ALOHA (contextual) | Imitation-learning baseline / platform | Combines whole-body teleoperation with imitation learning for coordinated mobile and bimanual manipulation. | [Paper](https://arxiv.org/abs/2401.02117) |
| Mobility VLA (contextual navigation policy) | Related navigation only; outside manipulation scope | Combines long-context visual-language understanding with a topological navigation controller. Its evidence concerns navigation rather than manipulation. | [Paper](https://arxiv.org/abs/2407.07775) |
| MOKA (VLM control framework) | Contextual planner / control system | Uses marked images and point-based affordances to translate language instructions into geometric manipulation commands. | [Paper](https://arxiv.org/abs/2403.03174) |
| OK-Robot (modular control system) | Contextual planner / control system | Integrates open perception, navigation, and grasping components for language-directed mobile manipulation in unfamiliar environments. | [Paper](https://arxiv.org/abs/2401.12202) |
| Onto-LLM-TAMP | Knowledge-guided task-and-motion planning | Uses ontology-based reasoning to structure prompts and connect language-model task planning with task-and-motion planning. It is a planning framework rather than a low-level VLA or learned dynamics model. | [Paper, original preprint version](https://arxiv.org/abs/2412.07493v1) |
| OWMM-Agent / OWMM-VLM | Contextual planner / control system | Uses a multimodal agent with scene and robot-state context to coordinate mobile manipulation through function calls, supported by task-specific instruction tuning. | [Paper](https://arxiv.org/abs/2506.04217) |
| PaLM-E (contextual embodied VLM) | Contextual planner / control system | Incorporates visual and continuous sensor observations into a language model to support embodied reasoning and high-level robot planning. | [Paper](https://arxiv.org/abs/2303.03378) |
| PD-VLA | Policy training / inference method | Speeds up action-chunk decoding through parallel fixed-point iterations applied to an autoregressive VLA. | [Paper](https://arxiv.org/abs/2503.02310) |
| ReKep (constraint-based planner) | Contextual planner / control system | Uses visual-language reasoning to specify relational keypoint constraints, then optimizes robot motions to satisfy those constraints. | [Paper](https://arxiv.org/abs/2409.01652) |
| RIPT-VLA | Policy training / inference method | Applies interactive reinforcement-learning post-training to pretrained policies using sparse binary task-success rewards. | [Paper](https://arxiv.org/abs/2505.17016) |
| RLDG | Policy training / inference method | Distills trajectories generated by task-specific reinforcement-learning policies into a generalist robot policy. | [Paper](https://arxiv.org/abs/2412.09858) |
| SayCan (contextual planner) | Contextual planner / control system | Combines language-model task suggestions with skill-value estimates to select robot behaviors that are relevant and feasible. | [Paper](https://arxiv.org/abs/2204.01691) |
| SimpleVLA-RL | Policy training / inference method | Uses online reinforcement learning to adapt VLA policies under different demonstration budgets, with stochastic action-token decoding in the reported training framework. | [Paper](https://arxiv.org/abs/2509.09674) |
| VLA-Cache | Policy training / inference method | Reduces repeated visual computation by caching minimally changed tokens while recomputing task-relevant information. | [Paper](https://arxiv.org/abs/2502.02175) |
| VLA-RL | Policy training / inference method | Improves autoregressive VLA policies through online reinforcement learning, including a learned progress-reward model and scalable training infrastructure. | [Paper](https://arxiv.org/abs/2505.18719) |
| VoxPoser (contextual planner) | Contextual planner / control system | Builds composable 3D value maps from language and visual observations, then uses them to guide robot motion planning. | [Paper](https://arxiv.org/abs/2307.05973) |

Catalogue coverage: **72 policy rows, 52 predictive-system rows, and 31 related-method/context rows**. These overlapping row counts are not distinct-paper counts. Source identities for the six additions were checked on 1 October 2026; the established entries retain prior primary-source checks and were reconciled with the current manuscript.

## Taxonomy used in the paper

The VLA groups describe different design choices and practical challenges rather than mutually exclusive architecture classes.

| Group | Focus | Question for the reader |
| --- | --- | --- |
| A — Action tokens | Discrete representations and action-sequence decoding | How are continuous robot actions represented and generated? |
| B — Continuous actions | Continuous regression, diffusion or flow-based action generation and action chunks | How does the policy generate precise, multimodal motion? |
| C — Hierarchical reasoning | Task decomposition, intermediate reasoning, and skill coordination | How are longer instructions organized into executable steps? |
| D — Spatial grounding | Depth, point clouds, voxels, and geometric features | What spatial information is available to the controller? |
| E — Interactive learning | Reinforcement learning and other forms of policy improvement from interaction | How can a policy learn beyond its demonstrations? |
| F — Efficient deployment | Smaller models, caching, pruning, and faster decoding | What computation is required at inference time? |
| G — Embodiment | Transfer across robots, dexterous control, and mobile manipulation | How does the policy accommodate different bodies and control interfaces? |

The predictive-system taxonomy separates representation from use. The first four families emphasize what is predicted; the final two emphasize how prediction participates in a larger system.

| Family | Main role | Important distinction |
| --- | --- | --- |
| WM1 — Latent dynamics | Predict compact state transitions for planning or learning in imagination | A useful control model need not reconstruct every image detail. |
| WM2 — Generative video | Generate future observations or interactive visual environments | Visual plausibility is not sufficient evidence of correct contact dynamics. |
| WM3 — Latent prediction | Forecast learned features or task-relevant representations | Representation pretraining and action-conditioned planning are distinct stages. |
| WM4 — Physical state models | Represent geometry, objects, material properties, or contact more explicitly | Explicit physical structure does not automatically guarantee accurate dynamics. |
| WM5 — Learned environments | Generate training data, evaluate policies, or support reinforcement learning | Each use requires its own validation against physical outcomes. |
| WM6 — World–action models | Couple prediction with robot-action generation | Predictive supervision, direct policy execution, and rollout-based search must be evaluated separately. |

## What the evidence supports

The paper separates evidence that a limitation exists from evidence that a proposed mechanism improves it. A high task-success score alone does not establish why a system improved.

| Limitation | Outcome or gap examined |
| --- | --- |
| L1 — Execution monitoring and recovery | Detecting failed or incomplete execution and correcting behavior; the absence of an explicit world model is not itself a measured failure. |
| L2 — Distribution shift | Performance under declared changes in objects, scenes, instructions, embodiment or task conditions. |
| L3 — Data requirements | Dependence on robot interaction data and evidence for effective use of passive or synthetic data. |
| L4 — Physical grounding | Whether geometry, contact and physical consequences are represented well enough for the tested decisions. |
| L5 — Evaluation validity | Whether benchmark scores and learned evaluators reflect the physical performance they are intended to measure. |
| L6 — Safety and uncertainty | Calibration, constraint violations, abstention, irreversibility and tested fallback behavior. |

Prediction and search cost are discussed separately as limitations of predictive systems in Sec. VI-I and as a research issue in D8; they are not a seventh VLA limitation. Direct policies, recovery data and external correction mechanisms can also support recovery.

**Evidence directness and outcome direction are separate.** Direct, indirect and prospective describe the relation between a tested contrast and the claim. Favorable, adverse, mixed or inconclusive describe its direction. For example, PolaRiS provides direct adverse evidence for the evaluated learned policy-ranking pipeline; adverse does not mean indirect. Component attribution is a further question: a package-level improvement need not isolate one mechanism.

The selected-example evidence heatmap summarizes **selected source-linked examples**, not an exhaustively coded 144-report evidence census. Its entries describe claims or contrasts; repeated entries from a study are not independent papers. An unfilled cell does not establish that the literature has no evidence for that limitation.

Inspect the [claim-level evidence ledger](data/selected_evidence_ledger.csv), its [JSON version](data/selected_evidence_ledger.json), [scope and coding notes](data/selected_evidence_scope.json), [plotted rows](data/selected_evidence_plotted_rows.csv) and [heatmap cell values](data/selected_evidence_heatmap_cells.csv). The [reproduction script](scripts/generate_selected_evidence_heatmap.py) builds the selected-example display from these records; it does not extract or code the full corpus.


- **Predictive supervision and synthetic trajectories:** Selected policy ablations and synthetic-data pipeline comparisons support gains under their reported configurations. These designs do not imply an exhaustive evidence ranking or isolate every pipeline component. DreamGen’s task-score augmentation contrasts are kept separate from the GR00T N1-to-N1.5 model-version comparison.
- **Practice inside learned environments:** World-Gymnast provides physical transfer evidence on four tasks. Three reported comparisons favor learned-world-model practice and one favors SIMPLER. The comparison concerns the complete training packages and does not isolate world-model quality.
- **Comparison of candidate actions:** the reviewed Cosmos Policy experiment evaluates a combined rollout-refinement and candidate-selection configuration. Its benefit cannot be attributed to search alone without a matched component ablation.
- **Passive-video pretraining:** large pretraining pools and small action-conditioned adaptation sets are promising, but their relative sizes do not isolate the contribution of passive video or establish equal-performance data savings.
- **Learned policy evaluation:** the PolaRiS findings show that generated rollouts can contain incorrect interactions and disagree with physical policy rankings. A visually convincing simulator is therefore not automatically a valid evaluation instrument.
- **Safety and physical grounding:** prediction quality, constraint satisfaction, uncertainty calibration, and recovery behavior remain separate targets. The review does not establish an end-to-end manipulation system that verifies all of them together.

The synthesis is descriptive. Differences in observations, embodiment, training data, controllers, task splits, and evaluation procedures prevent the paper's cross-study tables from functioning as a common leaderboard or pooled effect estimate.

## Verified quantitative data

The workbook contains two quantitative datasets used in the figures: seven source-reported data-scale records and four World-Gymnast task comparisons. Values were checked against version-specific primary sources and retained with their original bounds and uncertainty interpretation. This verification concerns those plotted records; it does not validate every claim or screening decision in the review.

### Data scale and reporting role

All durations below are in hours. `≈` denotes an approximation, `>` a lower bound, and `<` an upper bound. A reported point value is a source's stated quantity, not an independently measured duration with unlimited precision.

| System / record | Hours | Type | What the number represents | Primary source and locator |
| --- | ---: | --- | --- | --- |
| Cosmos WFM | ≈20,000,000 | Approximation | Raw candidate-video collection **before curation**, not retained training hours. | [Cosmos v3](https://arxiv.org/html/2501.03575v3), §3.1 |
| V-JEPA 2 | >1,000,000 | Lower bound | Action-free video pretraining pool; image inputs are not converted into video-hours. | [V-JEPA 2 v1](https://arxiv.org/html/2506.09985v1), abstract and §2 |
| π0 | >10,000 | Lower bound | Robot pretraining mixture, including existing robot datasets; excludes the vision–language backbone's broader pretraining exposure. | [π0 v4](https://arxiv.org/html/2410.24164v4), introduction and conclusion |
| Dreamer 4 video | 2,541 | Reported point | Combined VPT contractor gameplay pool, with a 90/10 training/evaluation split. | [Dreamer 4 v1](https://arxiv.org/pdf/2509.24527v1), §4 and Appendix A |
| DROID | 350 | Reported point | Reported demonstration-corpus scale; not an established duration for every released trajectory or file. | [DROID v2](https://arxiv.org/html/2403.12945v2), abstract and §III-C |
| Dreamer 4 action labels | 100 | Reported point | A **nested action-label ablation condition** within the gameplay pool; not additional footage or the full successful agent's action-label budget. | [Dreamer 4 v1](https://arxiv.org/pdf/2509.24527v1), §4.3 and Fig. 7 |
| V-JEPA 2-AC | <62 | Upper bound | Filtered robot video for action-conditioned adaptation, with end-effector states and actions derived from consecutive states; excludes prior action-free pretraining. | [V-JEPA 2 v1](https://arxiv.org/html/2506.09985v1), §3.1 and Appendix B.1 |

Workbook locations: `Verified Data Scale!E2:F8` contains the plotted values and bound types; columns G–I record versions, locators, and links. The workbook category `exact` is interpreted here as **reported point value**.

These records describe different populations and stages of learning. They should not be summed, treated as equal supervision budgets, or used to rank sample efficiency or annotation cost. In particular, Dreamer 4's 100-hour condition is contained within its 2,541-hour pool. Bounds are thresholds, not measured point estimates, and no SE, SD, or confidence interval is supplied for these scale records.

### Data-scale visualization

![Source-reported data scales, with explicit bounds and reporting roles](figures/figure_06_data_scale_bubbles.png)

The circles use a distinct light color for each plotted record and show the reported values or bound thresholds on a logarithmic hours scale. Larger circles indicate larger orders of magnitude; their areas are **not proportional to raw hours**. The labels retain `≈`, `>`, and `<`, so a circle placed at a bound represents the reported threshold rather than an exact duration. Reporting roles remain explicit in the text labels.

For reproduction, circle area varies linearly with the logarithm of the displayed value or threshold:

```text
A(h) = A_min + (A_max − A_min) × log(h / 62) / log(20,000,000 / 62)
A_min = π × (4 pt)²
A_max = π × (22 pt)²
```

Here `h` is the reported hour value or threshold. The visible minimum radius is 4 points and the maximum is 22 points for the current records. This compressed size mapping keeps smaller records visible across more than five orders of magnitude. It does not convert a lower or upper bound into a point estimate, and circle-area ratios should not be interpreted as data-volume ratios.

### World-Gymnast real-robot comparison

The metric is **AutoEval real-robot task success after policy training**. Values below reproduce [World-Gymnast v1, §4.1 and Table 1](https://arxiv.org/html/2602.02454v1). Each policy–task evaluation uses 10 real-robot trials and is repeated five times. The five repeats are evaluations, not five independently trained policy seeds.

| Task | SIMPLER success, mean ± SE (%) | World-Gymnast success, mean ± SE (%) | World-Gymnast − SIMPLER (percentage points) |
| --- | ---: | ---: | ---: |
| Open the drawer | 34 ± 7 | 58 ± 4 | +24 |
| Close the drawer | 74 ± 5 | 62 ± 6 | −12 |
| Put the eggplant into the blue sink | 32 ± 10 | 72 ± 10 | +40 |
| Put the eggplant into the yellow basket | 40 ± 10 | 78 ± 2 | +38 |

Workbook locations: `World-Gymnast!C2:D5` and `F2:G5` contain means and standard errors; `P2:P5` contains the differences. The calculation is `World-Gymnast mean − SIMPLER mean`. For example, 58% − 34% = **24 percentage points**, not a 24% relative improvement.

The error terms are **standard errors**, not standard deviations or 95% confidence intervals. Raw repeat-level observations, pairing, and covariance are unavailable in the plotting inputs, so no uncertainty interval or significance test is inferred for the differences. The task-comparison and task-difference plots present the same experiment in complementary views; they are not independent replications. The adverse close-drawer result remains visible.

## Research questions left open

The paper proposes ten directions, grouped into five practical themes:

| Theme | Directions | Evidence needed |
| --- | --- | --- |
| Predictive foundations | D1 unified prediction/action; D2 control-oriented objectives; D3 stable memory; D4 contact-aware state | Matched ablations that connect better predictions to better physical decisions, including behavior under occlusion and contact. |
| Learning and data | D5 imagined post-training; D6 data composition | Transfer studies that hold training conditions fixed and report data provenance, mixing ratios, and failure cases. |
| Evaluation and deployment | D7 evaluation validity; D8 efficient deliberation | Physical policy-ranking checks, versioned protocols, uncertainty reporting, and separate measurements of planning latency and control frequency. |
| Safety and assurance | D9 risk-aware control | Calibrated uncertainty, constraint-violation and irreversibility measures, abstention, and tested fallback behavior. |
| Verified planning | D10 verified imagination | Explicit state and predicate mappings, bounded model error within a declared operating region, and runtime checks for unsupported actions. |

“Verified imagination” is the paper's proposed research direction: integrate learned prediction with explicit constraints and runtime assurance. It is not a capability established by the current collection, and any future guarantees would depend on the complete architecture and its stated assumptions.

## Literature counts and review status

The author-confirmed corpus contains **144 included reports: 69 VLA, 42 world-model, and 33 dataset/benchmark/evaluation reports**. The finalized register contains 214 distinct source records: 144 `Include`, 60 `Background` and 10 `Exclude` author decisions, with **zero pending decisions**. Seer and Video Prediction Policy add two VLA reports; Unified World Models adds one world-model report. Each is counted once under its primary category despite the catalogue’s deliberate overlap. Four further contextual references are recorded as Background and do not increase the included-report total.

| Quantity | Current state | Interpretation |
| --- | --- | --- |
| Manuscript bibliography | Cited research, methodological references and contextual sources | Citation totals are not inclusion totals; use the finalized register for corpus membership. |
| Preserved workbook `Current References` tab | Historical snapshot: 179 cited sources, comprising 171 papers and 8 technical/software sources | Its original Pending values are preserved for provenance and do not override current author decisions. |
| Preserved workbook `Cited Papers` tab | Earlier snapshot: 175 rows, comprising 169 papers and 6 technical/software sources | Retained unchanged as an earlier citation audit. |
| [Finalized literature register](data/VLA_WM_Literature_Register.xlsx), `Literature Register` tab | 144 included reports: 69 + 42 + 33 | One row per source record with a stable identifier, primary link and explicit author decision. |
| Figure 3 revision | 144 included reports after 182 full-text exclusions | The author-confirmed flow is arithmetically reconciled; the main PDF remains an older render until rebuilt. |

The current flow records **2,455 database/indexed-proceedings records + 100 supplementary records = 2,555 identified records**. The supplementary group comprises **97 original LLM-assisted/citation-chasing records plus 3 author-supplied papers**. Removing 704 duplicates leaves **1,851 screened records**; 1,525 title/abstract exclusions leave **326 reports sought and assessed**. Full-text exclusions are **62 navigation-only + 49 without action/control relevance + 44 with insufficient technical detail + 27 superseded reports = 182**, leaving **144 included reports**.

These figures are author-confirmed screening totals. Arithmetic reconciliation does not reconstruct the original record-level search and exclusion log or establish independent dual screening. The earlier 21-exclusion discrepancy has been resolved by the confirmed reason totals; it is not an outstanding gap in this snapshot.

The workbook preserves the 12 historical sheets and adds `Corpus Summary`, `Literature Register`, `Table Coverage` and `Search Notes`. Raw recommendations remain separate from finalized author decisions. The table-coverage audit preserves an earlier mapping in which 23 included reports were absent from the then-current citations; it should not be treated as a count of omissions in every later manuscript. Targeted supplementary searches and source checks do not retrospectively recreate an exhaustive search log. The historical plotting audit’s 147 data rows and the catalogue’s overlapping model/component rows are also distinct from the 144 included reports.

## Using the files

```text
.
├── README.md
├── paper/                         # PDF, LaTeX, bibliography, class, all figure assets
│   ├── manuscript.pdf
│   ├── manuscript.tex
│   ├── references.bib
│   ├── figures/
│   └── tkz/                       # Available editable diagram sources
├── data/                          # Excel register and machine-readable plotting inputs
├── figures/                       # Standalone figure exports and previews
├── scripts/                       # Data-scale and task-difference plotting scripts
├── docs/                          # Build guide and provenance notes
└── requirements.txt
```


| File | Purpose |
| --- | --- |
| [Finalized literature register](data/VLA_WM_Literature_Register.xlsx) | Author-confirmed 144-report corpus, category totals, manuscript-table mapping, and supplementary search records. |
| [Literature register CSV](data/literature_register.csv) | Machine-readable export with finalized author decisions for all 214 source records. |
| [Previous manuscript render](paper/manuscript.pdf) | Historical PDF from 13:51 on 1 October 2026; newer source and figure changes are not reflected. |
| [paper/manuscript.tex](paper/manuscript.tex) | Edit the manuscript source. |
| [paper/references.bib](paper/references.bib) | Inspect and maintain the cited bibliography. |
| [data/VLA_WM_verified_data_and_plots.xlsx](data/VLA_WM_verified_data_and_plots.xlsx) | Inspect source links, metadata notes, historical citation-register decisions, and numerical plotting inputs. |
| [Latest cited-reference export](data/current_cited_references_2026-10-02.csv) | Current manuscript citation inventory, including contextual references; distinct from the included-report register. |
| [data/current_references.csv](data/current_references.csv) | Historical export of the 179-source citation snapshot, with years, descriptions, links and preserved review status. |
| [data/verified_data_scale.csv](data/verified_data_scale.csv) | Seven scale records with source versions, bound types, reporting roles, and workbook cells. |
| [data/verified_world_gymnast_real_robot.csv](data/verified_world_gymnast_real_robot.csv) | Four task comparisons with means, standard errors, and differences in percentage points. |
| [data/verified_plot_inputs.json](data/verified_plot_inputs.json) | Structured inputs used by the plotting scripts. |
| [figures/figure_06_data_scale_bubbles.png](figures/figure_06_data_scale_bubbles.png) | View the data-scale figure directly. |
| [docs/BUILD.md](docs/BUILD.md) | Follow the package-specific instructions for rebuilding the paper and figures. |

Use the source/version and protocol fields alongside each number. The workbook's native charts are previews; their simplified appearance should not replace the manuscript figures' explicit bounds and uncertainty labels. Rebuilding a figure reproduces its presentation from the supplied values, not the original experiments. After changing an input, verify the corresponding labels, bound direction, units, and derived differences in the regenerated output.


### Reproduce the figures and paper

The [build guide](docs/BUILD.md) lists the required software and the source-to-figure mapping. With Python and a TeX distribution installed, run these commands from the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/generate_figure_06.py
python scripts/generate_figure_10.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd -outdir=build paper/manuscript.tex
```

The figure scripts write to `figures/`. After inspecting a regenerated PDF, copy it into `paper/figures/` before compiling the manuscript. PNG previews additionally require Poppler. All referenced figure files are included. The chronology, paper organization, VLA interface and taxonomy, control interfaces, world-model taxonomy and family architectures, and research roadmap now have readable native vector diagrams and editable TikZ sources. The paper-organization and world-model-family diagrams use `paper-roadmap.pdf` and `wm-architectures.pdf`; their original PNGs are retained as historical assets. The detailed VLA and world-model architectures add separate training/deployment views in `vla-detailed-architecture.pdf` and `world-model-detailed-architecture.pdf`. The evidence heatmap is a selected-example display, not a corpus-wide prevalence map. Rebuild and inspect the main manuscript before replacing its previous PDF; successful standalone-figure compilation does not validate the complete paper.

### Maintain the literature register

Use `Literature Register` for the 214 source records and finalized 144-report corpus. `Corpus Summary` derives 69 VLA, 42 world-model and 33 dataset/benchmark/evaluation reports from the author decisions. `Current References` and `Cited Papers` retain historical citation snapshots; their Pending values do not override the finalized register. For later revisions, record decisions against an explicit eligibility rule and stable identifier, retain reasons and source versions, and update the screening-flow arithmetic together with corpus membership.

For a bibliographic correction, identify the citation key, the corrected primary source, and the field that needs changing. For a quantitative correction, include the paper version, section/table/figure locator, unit, reporting scope, and workbook cell. Update the workbook source row, relevant CSV/JSON, and figure together so the spreadsheet and manuscript figure remain traceable.

### Cite and reuse

Please cite the original papers when using a model, result, dataset, or evaluation protocol. The model tables link to those primary sources. For discussion of this synthesis, use the manuscript title **From Reactive Vision–Language–Action Policies to Predictive World Models: A Review for Robotic Manipulation** and its final bibliographic record when available; this working snapshot does not supply an invented DOI or accepted-publication citation.

The linked papers, third-party figures, model code, datasets, and weights retain their respective terms. No repository-wide license is assigned in this prepared package. Maintainers can add the chosen license, public repository URL, and final publication metadata before release.
