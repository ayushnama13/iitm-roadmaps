# DA5453 — Learning from Human Preferences

| | |
|---|---|
| Tier | C |
| Phase (order) | 7 |
| Do this first | DA1004, DA6800 |
| Estimated effort | 10 weeks |
| Unlocks | LLM alignment |

## Roadmap

1. Bradley-Terry, ranking, RLHF.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [The Post-Training Course (w/ Nathan Lambert's RLHF Book)](https://www.youtube.com/playlist?list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y) (21 videos). Nathan Lambert *The Post-Training Course* (companion to his free *RLHF Book*, rlhfbook.com): reward models, PPO, DPO.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Stanford CS234 I Reinforcement Learning I Spring 2024 I Emma Brunskill](https://www.youtube.com/playlist?list=PLoROMvodv4rN4wG6Nk6sNpTEbuOSosZdX) (16 videos). Stanford CS234 *Reinforcement Learning* (Spring 2024, official): includes RLHF and DPO lectures.
- [Stanford CS224R Deep Reinforcement Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rPwxE0ONYRa_itZFdaKCylL) (19 videos). Stanford CS224R *Deep Reinforcement Learning* (official).
- [Stanford CS336 Language Modeling from Scratch I 2025](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) (17 videos). Stanford CS336 (2025, official): its alignment lectures cover SFT/RLHF at scale.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=jQPiH-KB4B0&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=1)–[4](https://www.youtube.com/watch?v=4gIwiSPmQkU&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=4) | ML prerequisites, post-training overview, instruction tuning, reward models, rejection sampling. Read the matching RLHF Book chapters (rlhfbook.com). |
| 2 | [5](https://www.youtube.com/watch?v=K_Sj_-1BUMM&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=5)–[7](https://www.youtube.com/watch?v=x-MqKBzoxkI&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=7) | Policy gradients, PPO/GRPO for LLMs and their implementation. |
| 3 | [8](https://www.youtube.com/watch?v=o4AB5xHIDdM&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=8)–[12](https://www.youtube.com/watch?v=gB-bYUECpzE&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=12) | Reasoning models, DPO, frontier recipes, distillation and synthetic data. Run DPO on a small model with TRL. |
| 4 | [13](https://www.youtube.com/watch?v=Y2tv5vuaxFs&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=13)–[16](https://www.youtube.com/watch?v=rhA7pLVt4E0&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=16) | Preference data, over-optimisation, regularisation, a case study. |
| 5 | [17](https://www.youtube.com/watch?v=GMry2DzC304&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=17)–[21](https://www.youtube.com/watch?v=3xaaGxSjGN4&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=21) | Tool use and agents, evaluation, character training. |

<details>
<summary>All lectures in <i>The Post-Training Course (w/ Nathan Lambert&#x27;s RLHF Book)</i> (21 videos)</summary>

1. [Welcome to the Post-Training Course for The RLHF Book](https://www.youtube.com/watch?v=jQPiH-KB4B0&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=1)
2. [ML Foundations (prerequisites) for Post-Training | Post-Training Course, Lecture 0](https://www.youtube.com/watch?v=MMDNaeIFVy8&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=2)
3. [Post-Training and RLHF Overview | Post-Training Book Course, Lecture 1](https://www.youtube.com/watch?v=o6l6tJQgUg4&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=3)
4. [RLHF Foundations, IFT, Reward Modeling, Rejection Sampling | Post-Training Course Lecture 2](https://www.youtube.com/watch?v=4gIwiSPmQkU&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=4)
5. [Understanding Policy Gradient Algorithms for RL on LLMs | Post-Training Course Lecture 3](https://www.youtube.com/watch?v=K_Sj_-1BUMM&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=5)
6. [Implementing RL Algorithms for LLMs | Post-Training Course, Lecture 4](https://www.youtube.com/watch?v=i-AIMpZHgeg&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=6)
7. [Q&A 1: Teacher Models, PPO Implementation Questions & More | Post-Training Course](https://www.youtube.com/watch?v=x-MqKBzoxkI&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=7)
8. [The Rise of Reasoning Models  | Post-Training Course Lecture 5](https://www.youtube.com/watch?v=o4AB5xHIDdM&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=8)
9. [Direct Preference Optimization (DPO) and Friends | Post-Training Course, Lecture 6](https://www.youtube.com/watch?v=6g6b4gvO-y0&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=9)
10. [The State of Frontier Post-Training Recipes | Conversation with Finbarr Timbers](https://www.youtube.com/watch?v=sbXEPxIazqY&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=10)
11. [On-Policy Distillation & Using Synthetic Data in Post-Training | Post-Training Course, Lecture 7](https://www.youtube.com/watch?v=6nyJ8y8ghsE&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=11)
12. [Q&A 2: Mastering the Derivations, Running Algorithms at Home & Notation Gotcha's | Post-Train Course](https://www.youtube.com/watch?v=gB-bYUECpzE&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=12)
13. [Preference Data: The Most Opaque Part of Post-Training | Post-Training Course, Lecture 8](https://www.youtube.com/watch?v=Y2tv5vuaxFs&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=13)
14. [Over-Optimization and RLHF’s Bad Reputation | Post-Training Course, Lecture 9](https://www.youtube.com/watch?v=y04JhXpiI4s&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=14)
15. [Regularization in RL, Why RL Generalizes, and Why SFT Forgets | Post-Training Course, Lecture 10](https://www.youtube.com/watch?v=IwpYxANrpUs&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=15)
16. [From Academic Research to a Frontier LLM: A Case Study in DPO | Post-Training Course, Conversation 2](https://www.youtube.com/watch?v=rhA7pLVt4E0&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=16)
17. [How Language Models Use Tools and the Path to Agents | Post-Training Course, Lecture 11](https://www.youtube.com/watch?v=GMry2DzC304&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=17)
18. [Post-Training Recipe Questions Answered | Q&A 3, Post-Training Course (w/ The RLHF Book)](https://www.youtube.com/watch?v=6StK9ttLNbQ&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=18)
19. [How Evaluation Has Evolved with Frontier Model Progress | Post-Training Course, Lecture 12](https://www.youtube.com/watch?v=dFafQmClYq4&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=19)
20. [An Introduction to Character Training | Post Training Course, Lecture 13](https://www.youtube.com/watch?v=xECWRYBxq1E&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=20)
21. [The Mascot of Post-Training (Shoggoth History) | Post-training Course Bonus Video](https://www.youtube.com/watch?v=3xaaGxSjGN4&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=21)

</details>


## Books, notes and websites

- Truong, Haupt, Koyejo, *Machine Learning from Human Preferences* (course text)
- InstructGPT and DPO papers

## Practice / proof of understanding

Train a reward model on a preference dataset.

## What your IITM course sheet says

### From the PDF: DA5453

**Official description:** Learning from human preference and comparison data is a critical component of modern search engines,  recommendation  systems, and AI alignment. This course explores both the mathematical foundations and algorithmic  implementation of  such learning algorithms. The course will involve reading recent research papers and understanding the  algorithms and  proofs presented in these papers. After this course, students will be well prepared to do research in a wide range  of topics  involving learning from comparison data.

**Official syllabus (trimmed):**

> The course is split into the following modules:
>  1. Introduction Myriad applications of learning from comparisons (search, recommendations, feature learning,
>  operations
>  research, LLM alignment), probabilistic choice models (Bradley-Terry, Plackett-Luce, Multinomial Logit)
>  2. Foundations of Bradley-Terry Model (theoretical) Formulate the learning-from-comparisons problem in a
>  statistical
>  learning framework, learning guarantees, algorithms, random walk approach to ranking
>  3. Ranking in Search Engines: Introduction to search, non-learning based approaches via query-document
>  features,
>  evaluation metrics (NDCG, precision@K), datasets (LETOR, MS-MARCO), pointwise/pairwise/listwise approach,
>  seminal algorithms: RankSVM, RankNet, LambdaRank, LambdaMART, ListNet. Students will apply one such
>  algorithm to a real-world dataset as part of homework
>  4. LLM Alignment LLM learning pipeline, need for alignment, alignment datasets, alignment methods (RLHF,
>  DPO), state-of-the-art methods
>  5. Online Learning with Comparisons Active ranking algorithms, dueling bandits, contextual dueling bandits,
>  connections to linear bandits
>  6. Richer choice models Understanding human biases, limitations of simple choice models, alternate richer
>  models,
>  classical research by Tversky, learning-based models with context effects

**Official textbooks:** S. Truong, A. Haupt, and S. Koyejo. ”Machine Learning from Human Preferences.” Stanford University (2025)  2. Liu, Tie-Yan. ”Learning to rank for information retrieval.” Foundations and Trends in Information Retrieval (2009)

**Official references:** Bengs, Viktor, et al. ”Preference-based online learning with dueling bandits: A survey.” Journal of Machine  Learning  Research (2021)
