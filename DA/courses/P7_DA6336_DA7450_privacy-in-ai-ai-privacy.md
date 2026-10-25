# DA6336+DA7450 — Privacy in AI / AI Privacy

| | |
|---|---|
| Tier | C |
| Phase (order) | 7 |
| Do this first | DA1004, DA3409 |
| Estimated effort | 10 weeks |
| Unlocks | Research |

## Roadmap

1. Differential privacy, federated learning, attacks on models.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [A Course In Differential Privacy](https://www.youtube.com/playlist?list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp) (37 videos). Gautam Kamath *A Course in Differential Privacy* (Waterloo, official): the standard DP course.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Differential Privacy Fall 2021](https://www.youtube.com/playlist?list=PLTN4aNO9NiB7UiBbSFznHRSkdieBc0-sk) (16 videos). Yu-Xiang Wang *Differential Privacy* (UCSB, Fall 2021).
- [CS-E4740 Federated Learning ('25)](https://www.youtube.com/playlist?list=PLrbn2dGrLJK9rB05BObJGIcZP-g2nR28Y) (44 videos). Aalto CS-E4740 *Federated Learning* (Alexander Jung, 2025).
- [Responsible & Safe AI Systems](https://www.youtube.com/playlist?list=PLyqSpQzTE6M8zUpa6eG3ff3t4asCMlFTL) (58 videos). NPTEL *Responsible & Safe AI Systems* (IIT Madras).
- [Privacy and Security in Online Social Media](https://www.youtube.com/playlist?list=PLZ2ps__7DhBaKvfv3VjSZlcVueXLymjXB) (47 videos). IIT Madras BS *Privacy and Security in Online Social Media* (Ponnurangam Kumaraguru).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=FJMjNOcIqkc&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=1), [4](https://www.youtube.com/watch?v=EzYXbU-ZE3s&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=4), [6](https://www.youtube.com/watch?v=usOYloLB2SU&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=6), [7](https://www.youtube.com/watch?v=8MkU3czKvpY&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=7), [12](https://www.youtube.com/watch?v=o3qZ0GFlYi0&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=12) | Failed privacy attempts and reconstruction attacks (lectures 1A-2C; the playlist is out of order). |
| 2 | [5](https://www.youtube.com/watch?v=gCjQ-2W9yjs&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=5), [2](https://www.youtube.com/watch?v=W1v_JfL6sZo&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=2), [3](https://www.youtube.com/watch?v=IGQe9BN1TZs&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=3), [10](https://www.youtube.com/watch?v=X1NWwcp0MrE&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=10) | Randomized response, definition of DP, Laplace mechanism (3A-4B). Implement the Laplace mechanism on a counting query. |
| 3 | [8](https://www.youtube.com/watch?v=9QvSO9S2urg&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=8), [9](https://www.youtube.com/watch?v=AS9lfO4trdk&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=9), [13](https://www.youtube.com/watch?v=lkZ8DaPFiNQ&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=13), [20](https://www.youtube.com/watch?v=sosCyU5IyhE&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=20) | Approximate DP, Gaussian mechanism, advanced composition (5A-6B). |
| 4 | [11](https://www.youtube.com/watch?v=J19YM6U2x4U&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=11), [16](https://www.youtube.com/watch?v=Fcg8aUp3znk&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=16), [21](https://www.youtube.com/watch?v=TJySDEnfMXw&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=21), [27](https://www.youtube.com/watch?v=J71IHsVBTCk&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=27), [28](https://www.youtube.com/watch?v=w4-mpXu3vrA&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=28) | Exponential mechanism, private multiplicative weights (7A-8C). |
| 5 | [17](https://www.youtube.com/watch?v=PJEIN9s69qU&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=17), [32](https://www.youtube.com/watch?v=wnW3zfM-STU&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=32), [23](https://www.youtube.com/watch?v=G2Xqe-VeGRI&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=23), [33](https://www.youtube.com/watch?v=w-q5LLJ7ReQ&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=33), [19](https://www.youtube.com/watch?v=zP5qq141wUY&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=19) | Sparse vector, beyond global sensitivity, lower bounds, what is privacy (9A-12). |
| 6 | [15](https://www.youtube.com/watch?v=7VW1vB_x7k4&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=15), [22](https://www.youtube.com/watch?v=xp9ISWq1STI&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=22), [18](https://www.youtube.com/watch?v=HGXOtTmI-sQ&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=18), [26](https://www.youtube.com/watch?v=xIemjUqhDsY&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=26), [14](https://www.youtube.com/watch?v=uTiXla_pHik&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=14), [29](https://www.youtube.com/watch?v=lgmXVCE505M&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=29) | Private ML: DP-SGD, PATE (13A-14C). Train a model with Opacus and compare accuracy across epsilon. |
| 7 | [31](https://www.youtube.com/watch?v=nhEjDm-Pzk4&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=31), [35](https://www.youtube.com/watch?v=Vh0wzhYkUUs&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=35), [37](https://www.youtube.com/watch?v=5Qtd-9LWsFE&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=37), [30](https://www.youtube.com/watch?v=i4MGqlBKvjI&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=30), [36](https://www.youtube.com/watch?v=GDfXRVnLfb0&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=36), [24](https://www.youtube.com/watch?v=eP9RGfQsvtg&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=24), [34](https://www.youtube.com/watch?v=Jn7qva2IMVc&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=34), [25](https://www.youtube.com/watch?v=-ly-mpB6O6s&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=25) | Private mean estimation, adaptive data analysis, deployments and local DP (15A-18). |

<details>
<summary>All lectures in <i>A Course In Differential Privacy</i> (37 videos)</summary>

1. [Lecture 1A: Some Attempts at Data Privacy - NYC Taxis and Netflix](https://www.youtube.com/watch?v=FJMjNOcIqkc&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=1)
2. [Lecture 3B: The Definition of Differential Privacy, and Revisiting Randomized Response](https://www.youtube.com/watch?v=W1v_JfL6sZo&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=2)
3. [Lecture 4A: Intro to Differential Privacy, Part 2 - The Laplace Mechanism](https://www.youtube.com/watch?v=IGQe9BN1TZs&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=3)
4. [Lecture 1B: Some Attempts at Data Privacy - Neural Networks, Medical Studies, k-Anonymity](https://www.youtube.com/watch?v=EzYXbU-ZE3s&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=4)
5. [Lecture 3A: Randomized Response](https://www.youtube.com/watch?v=gCjQ-2W9yjs&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=5)
6. [Lecture 2A: Reconstruction Attacks - How to Attack a Census](https://www.youtube.com/watch?v=usOYloLB2SU&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=6)
7. [Lecture 2B: Reconstruction Attacks - The Dinur-Nissim Attack](https://www.youtube.com/watch?v=8MkU3czKvpY&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=7)
8. [Lecture 5A: Approximate Differential Privacy - Definitions and Interpreting Delta](https://www.youtube.com/watch?v=9QvSO9S2urg&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=8)
9. [Lecture 5B: Approximate Differential Privacy - The Gaussian Mechanism and Properties](https://www.youtube.com/watch?v=AS9lfO4trdk&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=9)
10. [Lecture 4B: Intro to Differential Privacy, Part 2 - Properties of Differential Privacy](https://www.youtube.com/watch?v=X1NWwcp0MrE&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=10)
11. [Lecture 7A: The Exponential Mechanism](https://www.youtube.com/watch?v=J19YM6U2x4U&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=11)
12. [Lecture 2C: Reconstruction Attacks - Cohen-Nissim attack Diffix!](https://www.youtube.com/watch?v=o3qZ0GFlYi0&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=12)
13. [Lecture 6A: Advanced Composition - Reduction to Binary-ish Case](https://www.youtube.com/watch?v=lkZ8DaPFiNQ&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=13)
14. [Lecture 14B: Modern Private ML - Differentially Private Stochastic Gradient Descent](https://www.youtube.com/watch?v=uTiXla_pHik&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=14)
15. [Lecture 13A: Differentially Private Machine Learning - A Quick Primer](https://www.youtube.com/watch?v=7VW1vB_x7k4&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=15)
16. [Lecture 7B: Applications of the Exponential Mechanism](https://www.youtube.com/watch?v=Fcg8aUp3znk&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=16)
17. [Lecture 9A: Sparse Vector - Above Threshold](https://www.youtube.com/watch?v=PJEIN9s69qU&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=17)
18. [Lecture 13C: Differentially Private Machine Learning - Gradient Perturbation](https://www.youtube.com/watch?v=HGXOtTmI-sQ&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=18)
19. [Lecture 12: What is Privacy?](https://www.youtube.com/watch?v=zP5qq141wUY&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=19)
20. [Lecture 6B: Advanced Composition - Composition Proof](https://www.youtube.com/watch?v=sosCyU5IyhE&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=20)
21. [Lecture 8A: Private Multiplicative Weights - Linear Queries](https://www.youtube.com/watch?v=TJySDEnfMXw&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=21)
22. [Lecture 13B: Differentially Private Machine Learning - Output and Objective Perturbation](https://www.youtube.com/watch?v=xp9ISWq1STI&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=22)
23. [Lecture 10: Beyond Global Sensitivity](https://www.youtube.com/watch?v=G2Xqe-VeGRI&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=23)
24. [Lecture 17A: DP Deployments 1, Local DP](https://www.youtube.com/watch?v=eP9RGfQsvtg&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=24)
25. [Lecture 18: DP Deployments 2](https://www.youtube.com/watch?v=-ly-mpB6O6s&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=25)
26. [Lecture 14A: Modern Private ML - Some Background on Neural Networks](https://www.youtube.com/watch?v=xIemjUqhDsY&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=26)
27. [Lecture 8B: Private Multiplicative Weights - Non-Private Multiplicative Weights](https://www.youtube.com/watch?v=J71IHsVBTCk&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=27)
28. [Lecture 8C: Private Multiplicative Weights - Multiplicative Weights for Queries](https://www.youtube.com/watch?v=w4-mpXu3vrA&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=28)
29. [Lecture 14C: Modern Private ML - PATE](https://www.youtube.com/watch?v=lgmXVCE505M&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=29)
30. [Lecture 16A: Adaptive Data Analysis - Intro, Setup, and Results](https://www.youtube.com/watch?v=i4MGqlBKvjI&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=30)
31. [Lecture 15A: Private Mean Estimation - Introduction](https://www.youtube.com/watch?v=nhEjDm-Pzk4&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=31)
32. [Lecture 9B: Sparse Vector - SparseVector, and Online PMW](https://www.youtube.com/watch?v=wnW3zfM-STU&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=32)
33. [Lecture 11: Packing Lower Bounds](https://www.youtube.com/watch?v=w-q5LLJ7ReQ&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=33)
34. [Lecture 17B: DP Deployments 1, Local DP](https://www.youtube.com/watch?v=Jn7qva2IMVc&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=34)
35. [Lecture 15B: Private Mean Estimation - Near-Optimal Univariate Gaussians](https://www.youtube.com/watch?v=Vh0wzhYkUUs&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=35)
36. [Lecture 16B: Adaptive Data Analysis - Proofs](https://www.youtube.com/watch?v=GDfXRVnLfb0&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=36)
37. [Lecture 15C: Private Mean Estimation - Beyond Univariate Gaussians](https://www.youtube.com/watch?v=5Qtd-9LWsFE&list=PLmd_zeMNzSvRRNpoEWkVo6QY_6rR3SHjp&index=37)

</details>


## Books, notes and websites

- Dwork & Roth, *Algorithmic Foundations of Differential Privacy* (free)

## Practice / proof of understanding

Train a model with DP-SGD (Opacus) and measure the accuracy cost.

## What your IITM course sheet says

### From the PDF: DA6336

**Official description:** The recent explosion of data-driven AI techniques also comes with privacy concerns around the memorization and  regurgitation of the vast amounts of data necessary to train these models as well as responsible use of data. The  purpose of this course is to introduce participants to these privacy issues as well as the rigorous  mathematical/statistical tools to tackle them.  The course will cover aspects of privacy in AI from foundational principles and standard algorithms up until  cutting-edge research to tackle emerging challenges. The course will include a strong emphasis on the theoretical  and mathematical aspects (including writing rigorous proofs) as well as designing and implementing algorithms  subject to real-world constraints to solve real-world problems (which we will sample with programming  assignments).

**Official syllabus (trimmed):**

> I. Introduction and Privacy Attacks in AI/ML. (2 weeks)
>  Common examples of privacy/security risks in data-driven AI/ML; privacy attacks and their properties: membership
>  inference, data memorization/reconstruction and extraction, property inference;
>  II Differential Privacy (DP) Foundations and Algorithms. (2 weeks)
>  Statistical notions of privacy and desirable properties; differentially private mean estimation; exponential
>  mechanism; privacy-utility tradeoffs; connection to hypothesis testing; privacy composition; accounting techniques
>  (Renyi, privacy loss);
>  III. Learning with Differential Privacy. (3 weeks)
>  different ways of achieving DP in ML: objective perturbation, teacher ensembles (PATE), stochastic gradient
>  descent with DP, correlated noise mechanisms; practical considerations with automatic differentiation,
>  implementation details and heuristics; privacy-utility-compute tradeoffs; empirical auditing of private learning
>  IV. Protection Against Data Reconstruction (2 weeks)
>  statistical notions of data reconstruction in data analytics and in learning settings; lower bounds; Fisher privacy
>  properties; comparison to DP; accounting and algorithms;
>  V. Privacy Challenges in Generative AI (3 weeks)
>  review of generative AI and LLMs; quantifying memorization; synthetic data: opportunities and challenges;
>  copyright and statistical notions; legal and ethical consideratio

**Official textbooks:** Fioretto, F. and Hentenryck, P.V., 2025. Differential Privacy in Artificial Intelligence: From Theory to Practice.  Boston-Delft: now publishers, http://dx.doi.org/10.1561/9781638284772

**Official references:** 1) Dwork, C. and Roth, A., 2014. The algorithmic foundations of differential privacy. Foundations and Trends in  Theoretical Computer Science, Now Publishers. 9(3–4), pp.211-407.  2) Vadhan, S., 2017. The complexity of differential privacy. Tutorials on the Foundations of Cryptography:  Dedicated to Oded Goldreich, Edited by Yehuda Lindell, pp.347-450. Springer International Publishing, AG 2017,  

### From the PDF: DA7450

**Official description:** The recent explosion of data-driven AI techniques also comes with privacy concerns around the memorization and  regurgitation of the vast amounts of data necessary to train these models as well as responsible use of data. The  purpose of  this course is to tackle a selection of advanced and cutting-edge topics in AI privacy research with a focus on  theoretical  foundations and practical applicability.  This will primarily be a seminar course, where the students are expected to read papers ahead of time and the  class time  will be spent on a discussion, including the technical aspects. Each topic will be led by a different group of  students.

**Official syllabus (trimmed):**

> I. Recap and Basic of Mathematical Toolkit for Privacy. (2 weeks)
>  Differential privacy; Key properties of privacy loss, composition, subsampling; Learning with Differential Privacy;
>  Private
>  selection and private top-k (exponential mechanism, report-noisy-max, permute-and-flip)
>  II. Advanced Differential Privacy Accounting. (2 weeks)
>  Privacy loss accounting; dominating distributions and discrete approximations (connect-the-dots algorithm);
>  characteristic
>  functions accounting; efficient implementation with DFT; Mixture of Gaussians mechanism
>  III. Data-Dependent Differential Privacy. (3 weeks)
>  Privacy accounting beyond-worst-case; subsample-and-aggregate; sparse vector technique; alternatives to global
>  sensitivity
>  (local/inverse/down sensitivity); smooth sensitivity & propose-test-release; application in private text generation in
>  large
>  language models
>  IV. Information-Theoretic Notions of Privacy (3 weeks)
>  average privacy definitions based on mutual information and conditional entropy, and their properties; Fano’s
>  inequality and
>  bounds on data reconstruction; applications to AI training and inference problems, and to synthetic data generation
>  V. Privacy Considerations in Generative AI and Personal Agents (2 week)
>  Privacy attacks via model interrogation; user-level attacks; privacy risks and solutions in
>  retrieval-augmented-generation
>  (RAG); Privacy defenses wit

**Official textbooks:** Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. Foundations and Trends® in  Theoretical Computer  Science, 9(3–4), 211-407.

**Official references:** We will also read several relevant research papers
