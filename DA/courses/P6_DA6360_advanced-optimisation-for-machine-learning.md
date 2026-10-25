# DA6360 — Advanced Optimisation for Machine Learning

| | |
|---|---|
| Tier | C |
| Phase (order) | 6 |
| Do this first | DA1002, DA3409 |
| Estimated effort | 12 weeks |
| Unlocks | Research |

## Roadmap

1. Convex analysis, momentum, Adam, second-order methods.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Stanford EE364A Convex Optimization I Stephen Boyd I 2023](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h) (18 videos). Stanford EE364A *Convex Optimization* (Boyd, 2023, official).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Optimization Methods for Machine Learning and Engineering (KIT Winter Term 20/21)](https://www.youtube.com/playlist?list=PLdkTDauaUnQpzuOCZyUUZc0lxf4-PXNR5) (41 videos). KIT *Optimization Methods for Machine Learning and Engineering*: SGD, momentum, Adam, non-convex.
- [Optimisation for Machine Learning: Theory and Implementation (Hindi)](https://www.youtube.com/playlist?list=PLyqSpQzTE6M-pmLzCoMu_ANU6atEFyyJl) (36 videos). NPTEL *Optimisation for Machine Learning: Theory and Implementation* (IIT Madras, in Hindi).
- [July 2024 - Distributed Optimization and Machine Learning](https://www.youtube.com/playlist?list=PLOzRYVm0a65fhKDS8cYIC7YCuVGJ4FOJx) (48 videos). NPTEL *Distributed Optimization and Machine Learning* (IIT Bombay, 2024).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=kV1ru-Inzl4&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=1)–[3](https://www.youtube.com/watch?v=1menqhfNzzo&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=3) | Introduction, convex sets, convex functions (Boyd & Vandenberghe ch. 1-3). Install CVXPY. The 2023 video titles carry no topic names, so the topic split is approximate. |
| 2-3 | [4](https://www.youtube.com/watch?v=U2HRwA7XePU&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=4)–[7](https://www.youtube.com/watch?v=P_SuSVZnrT0&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=7) | Convex optimisation problems: LP, QP, SOCP, SDP, geometric programming (ch. 4). Solve a portfolio problem in CVXPY. |
| 4 | [8](https://www.youtube.com/watch?v=wsRznzNgTS0&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=8)–[10](https://www.youtube.com/watch?v=N3V2AdTImJE&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=10) | Duality, KKT conditions (ch. 5). Derive the dual of an SVM by hand. |
| 5 | [11](https://www.youtube.com/watch?v=trs0RI39uWI&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=11)–[14](https://www.youtube.com/watch?v=dAvxvA4_Euo&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=14) | Approximation and fitting, statistical estimation, geometric problems (ch. 6-8). Robust regression and lasso in CVXPY. |
| 6 | [15](https://www.youtube.com/watch?v=zVO4ccvrwrI&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=15)–[18](https://www.youtube.com/watch?v=4A5opemjRW4&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=18) | Unconstrained and equality-constrained minimisation, Newton's method, interior-point methods (ch. 9-11). Implement gradient descent and Newton with backtracking line search. |

<details>
<summary>All lectures in <i>Stanford EE364A Convex Optimization I Stephen Boyd I 2023</i> (18 videos)</summary>

1. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 1](https://www.youtube.com/watch?v=kV1ru-Inzl4&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=1)
2. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 2](https://www.youtube.com/watch?v=2H4_7izio9Y&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=2)
3. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 3](https://www.youtube.com/watch?v=1menqhfNzzo&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=3)
4. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 4](https://www.youtube.com/watch?v=U2HRwA7XePU&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=4)
5. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 5](https://www.youtube.com/watch?v=AAjG1TQcL7c&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=5)
6. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 6](https://www.youtube.com/watch?v=d2jF3SXcFQ8&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=6)
7. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 7](https://www.youtube.com/watch?v=P_SuSVZnrT0&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=7)
8. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 8](https://www.youtube.com/watch?v=wsRznzNgTS0&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=8)
9. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 9](https://www.youtube.com/watch?v=whE03c84ahA&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=9)
10. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 10](https://www.youtube.com/watch?v=N3V2AdTImJE&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=10)
11. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 11](https://www.youtube.com/watch?v=trs0RI39uWI&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=11)
12. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 12](https://www.youtube.com/watch?v=t8sp9rv-Dqo&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=12)
13. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 13](https://www.youtube.com/watch?v=ankx1lGi5jI&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=13)
14. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 14](https://www.youtube.com/watch?v=dAvxvA4_Euo&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=14)
15. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 15](https://www.youtube.com/watch?v=zVO4ccvrwrI&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=15)
16. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 16](https://www.youtube.com/watch?v=Sx7TKDFJjmk&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=16)
17. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 17](https://www.youtube.com/watch?v=vcTIA2X0UVk&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=17)
18. [Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 18](https://www.youtube.com/watch?v=4A5opemjRW4&list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h&index=18)

</details>


## Books, notes and websites

- Boyd & Vandenberghe; Nocedal & Wright; *Optimization for ML* (Sra et al.)

## Practice / proof of understanding

Compare SGD, Adam and L-BFGS on one problem with plots.

## What your IITM course sheet says

### From the PDF: DA6360

**Official description:** This course focuses on the core concepts of continuous optimisation occurring in data science.The course  includes an introduction to unconstrained and constrained optimisation problems. Popular algorithms such as  gradient descent and Newton methods will be introduced first, followed by advanced optimisation algorithms for  deep learning and other data science use cases. The evaluation will be based on the exams.

**Official syllabus (trimmed):**

> Part I: Linear, quadratic and convex optimisation problems, examples. 4. Gradient descent, Newton Methods
>  algorithm and analysis.
>  Part II: Heavy-Ball, Nesterov Momentum, RMSprop, Adam, K-FAC, Shampoo, AdaHessian, HF, L-BFGS
>  variants, Natural Gradients, Krylov methods, Stochastic Gradient Descent, Simultaneous Perturbation
>  Stochastic Approximation.
>  Part III: Convex sets and functions 1. Convex sets, examples and properties. 2. Convex functions, strict and
>  strong convexity, examples, and convexity preserving operations. 3. Equivalent definitions of convexity under
>  differentiability assumptions.
>  Part IV: Constrained optimisation 1. Constrained optimisation problem, feasible set. 2. Lagrangian, KKT conditions
>  3. Linear and quadratic optimisation 4. Duality for convex optimisation — theorem of alternatives, Farka’s lemma.

**Official textbooks:** 1. Convex Optimization – Boyd & Vandenberghe (Cambridge, 2004)  2. Numerical Optimization – Nocedal & Wright (Springer, 2006)

**Official references:** 1. Optimization for Machine Learning – Sra, Nowozin, Wright (MIT, 2012)  2. Deep Learning – Goodfellow, Bengio, Courville (MIT, 2016) – only for selected chapters on optimization
