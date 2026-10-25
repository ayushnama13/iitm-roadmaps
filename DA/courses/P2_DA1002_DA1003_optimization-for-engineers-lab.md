# DA1002+DA1003 — Optimization for Engineers (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 2 |
| Do this first | DA1000, DA1001 |
| Estimated effort | 12 weeks |
| Unlocks | DA6360, DA3409, DA2400 |

## Roadmap

1. Gradients, Hessians, smoothness.
2. Gradient descent, step sizes, Newton's method.
3. Linear programming and simplex; Lagrangian and KKT.
4. Convexity; lab: implement all of these in Python.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Stanford EE364A Convex Optimization I Stephen Boyd I 2023](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h) (18 videos). Stanford EE364A *Convex Optimization* (Stephen Boyd, 2023, official). Free book: stanford.edu/~boyd/cvxbook.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Optimization Theory and Algorithms - Prof. Uday Khankhoje](https://www.youtube.com/playlist?list=PLyqSpQzTE6M8XNc8SxMLbUxdR7lDSuIGw) (83 videos). NPTEL *Optimization Theory and Algorithms* (Uday Khankhoje, IIT Madras): IITM's own.
- [Jan 2021 - Optimization from fundamentals](https://www.youtube.com/playlist?list=PLOzRYVm0a65dcrQ9lNthjWtnqp1hYcusH) (68 videos). NPTEL *Optimization from Fundamentals* (IIT Bombay, 2021).
- [Optimization Algorithms](https://www.youtube.com/playlist?list=PLXsmhnDvpjORzPelSDs0LSDrfJcqyLlZc) (58 videos). Constantine Caramanis *Optimization Algorithms* (UT Austin): gradient descent, Newton, convergence proofs.

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

- Stanford EE364a (Boyd) lectures + *Convex Optimization* (free PDF)
- ✅ NPTEL *Optimization from Fundamentals* (Ankur Kulkarni, IIT Bombay) — onlinecourses.nptel.ac.in/noc25_me60/preview
- ✅ NPTEL *Convex Optimization* (Joydeep Dutta, IIT Kanpur) — nptel.ac.in/courses/111104068 (YouTube uploads titled Mod-01 Lec-XX Convex Optimization; the noc15 archive page is dead)
- CVXPY docs; Nocedal & Wright

## Practice / proof of understanding

Implement GD, Newton, simplex and projected GD; verify KKT on 3 constrained problems with CVXPY.

## What your IITM course sheet says

### From the PDF: DA1002

**Official description:** The student should be able to  1. Frame a real world problem as a mathematical optimization problem.  2. Identify the type of optimisation problem (continuous/discrete, linear/convex/non-convex)  3. Apply standard optimisation algorithms to appropriate problems.  4. Check a solution for optimality

**Official syllabus (trimmed):**

> Calculus basics: Gradients, linear approximations, quadratic approximation, Hessian, smoothness.
>  Unconstrained optimisation: Gradient descent, Step-size rules, Newton’s method, non-linear equation solving.
>  Linear programming: Linear constraints, feasibility, simplex method.
>  Constrained optimization: Lagrangian, KKT conditions, projected gradient descent.
>  Convexity: Convex sets and functions, local and global minima, convex optimisation problems.

**Official textbooks:** 1. Nocedal, Jorge and Wright, Stephen. Numerical optimization. Springer, 1999  2. Luenberger, David G., and Yinyu Ye. Linear and nonlinear programming. 4th edition. Springer, 2015.  3. Boyd, Stephen, and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.

**Official references:** 1. Nocedal, Jorge and Wright, Stephen. Numerical optimization. Springer, 1999  2. Luenberger, David G., and Yinyu Ye. Linear and nonlinear programming. 4th edition. Springer, 2015.  3. Boyd, Stephen, and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.

### From the PDF: DA1003

**Official description:** The goal of the course is to equip students to visualize functions and implement in Python the algorithms learnt as  part  of the optimization for engineers course.

**Official syllabus (trimmed):**

> 1. Module 1: Python basics, basics of simulation, contour plotting for function visualization
>  2. Module 2: Unconstrained optimization - implementations - gradient methods, step size - exact/inexact search
>  methods Implementation of Newton’s method Autograd vs explicit gradient computations
>  3. Module 3: Constrained optimization algorithms - linear programming - simplex method implementation Projected
>  Gradient Descent implementation, Quadratic optimization implementation
>  4. Module 4: Verifying KKT conditions.
>  5. Module 5: Applications to curve fitting, root finding and other data science applications such as linear
>  regression.

**Official textbooks:** 1. Nocedal, Jorge and Wright, Stephen. Numerical optimization. Springer, 1999  2. Luenberger, David G., and Yinyu Ye. Linear and nonlinear programming. 4th edition. Springer, 2015.  3. Boyd, Stephen, and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.

**Official references:** 1. Nocedal, Jorge and Wright, Stephen. Numerical optimization. Springer, 1999  2. Luenberger, David G., and Yinyu Ye. Linear and nonlinear programming. 4th edition. Springer, 2015.  3. Boyd, Stephen, and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.
