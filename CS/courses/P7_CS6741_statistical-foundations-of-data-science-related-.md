# CS6741 — Statistical Foundations of Data Science + related stats/optimisation

| | |
|---|---|
| Tier | C |
| Phase (order) | 7 |
| Do this first | CS6015, CS4011 |
| Estimated effort | 12 weeks |
| Unlocks | CS6464, CS6730, CS7370 |

## Roadmap

1. Estimation, hypothesis testing, regression theory; then PGMs and optimisation.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Statistics 110: Probability](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) (35 videos). Harvard *Stat 110: Probability* (Joe Blitzstein, official Harvard channel): the best probability course online. Free book at probabilitybook.net.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [NOC Jan 2019 : Statistical Inference](https://www.youtube.com/playlist?list=PLbRMhDVUMngeD_vOeveVE-3b7wu_AZph9) (65 videos). NPTEL *Statistical Inference* (IIT Kharagpur): estimation, MLE, hypothesis tests.
- [Statistical Learning with Python](https://www.youtube.com/playlist?list=PLoROMvodv4rPP6braWoRt5UCXYZ71GZIQ) (100+ videos). Stanford *Statistical Learning with Python* (Hastie & Tibshirani, official): the ISLP book as lectures.
- [Stanford EE364A Convex Optimization I Stephen Boyd I 2023](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h) (18 videos). Stanford EE364A *Convex Optimization* (Stephen Boyd, 2023, official): for the optimisation half.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=1)–[6](https://www.youtube.com/watch?v=fDcjhAKuhqQ&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=6) | Counting, axioms, conditional probability, Bayes, Monty Hall. Do Stat 110 strategic practice 1-2 (projects.iq.harvard.edu/stat110). |
| 2 | [7](https://www.youtube.com/watch?v=PNrqCdslGi4&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=7)–[11](https://www.youtube.com/watch?v=TD1N4hxqMzY&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=11) | Random variables, Bernoulli/binomial/hypergeometric, expectation, indicators, Poisson. |
| 3 | [12](https://www.youtube.com/watch?v=Tci---bVs60&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=12)–[14](https://www.youtube.com/watch?v=9vp1Ll2NpRw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=14), [16](https://www.youtube.com/watch?v=bM6nFDjvEns&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=16) | Continuous distributions: uniform, normal, exponential; LOTUS. Simulate each in NumPy and compare histograms with the PDFs. |
| 4 | [17](https://www.youtube.com/watch?v=N8O6zd6vTZ8&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=17)–[20](https://www.youtube.com/watch?v=xiVWNkQUqKk&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=20) | Moment generating functions, joint/marginal/conditional distributions, multinomial. |
| 5 | [21](https://www.youtube.com/watch?v=IujCYxtpszU&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=21)–[24](https://www.youtube.com/watch?v=Qjeswpm0cWY&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=24) | Covariance, correlation, transformations, convolutions, Beta and Gamma, Poisson process. |
| 6 | [25](https://www.youtube.com/watch?v=2LR5JYbhyjg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=25)–[27](https://www.youtube.com/watch?v=gjBvCiRt8QA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=27) | Order statistics, conditional expectation (Adam's and Eve's laws). |
| 7 | [28](https://www.youtube.com/watch?v=UtXK_EQ3Pow&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=28)–[30](https://www.youtube.com/watch?v=MF-XSJOsGqw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=30) | Inequalities, law of large numbers, central limit theorem, chi-square/t, multivariate normal. Demonstrate the CLT by simulation. |
| 8 | [31](https://www.youtube.com/watch?v=8AJPs3gvNlY&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=31)–[34](https://www.youtube.com/watch?v=ChS3K2O-h7o&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=34) | Markov chains, stationary distributions. Simulate a random walk on a graph and compare with the stationary distribution. |

<details>
<summary>All lectures in <i>Statistics 110: Probability</i> (35 videos)</summary>

1. [Lecture 1: Probability and Counting | Statistics 110](https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=1)
2. [Lecture 2: Story Proofs, Axioms of Probability | Statistics 110](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2)
3. [Lecture 3: Birthday Problem, Properties of Probability | Statistics 110](https://www.youtube.com/watch?v=LZ5Wergp_PA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=3)
4. [Lecture 4: Conditional Probability | Statistics 110](https://www.youtube.com/watch?v=P7NE4WF8j-Q&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=4)
5. [Lecture 5: Conditioning Continued, Law of Total Probability | Statistics 110](https://www.youtube.com/watch?v=JzDvVgNDxo8&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=5)
6. [Lecture 6: Monty Hall, Simpson's Paradox | Statistics 110](https://www.youtube.com/watch?v=fDcjhAKuhqQ&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=6)
7. [Lecture 7: Gambler's Ruin and Random Variables | Statistics 110](https://www.youtube.com/watch?v=PNrqCdslGi4&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=7)
8. [Lecture 8: Random Variables and Their Distributions | Statistics 110](https://www.youtube.com/watch?v=k2BB0p8byGA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=8)
9. [Lecture 9: Expectation, Indicator Random Variables, Linearity | Statistics 110](https://www.youtube.com/watch?v=LX2q356N2rU&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=9)
10. [Lecture 10: Expectation Continued | Statistics 110](https://www.youtube.com/watch?v=P1fSFvhPf7Q&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=10)
11. [Lecture 11: The Poisson distribution | Statistics 110](https://www.youtube.com/watch?v=TD1N4hxqMzY&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=11)
12. [Lecture 12: Discrete vs. Continuous, the Uniform | Statistics 110](https://www.youtube.com/watch?v=Tci---bVs60&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=12)
13. [Lecture 13: Normal distribution | Statistics 110](https://www.youtube.com/watch?v=72QjzHnYvL0&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=13)
14. [Lecture 14: Location, Scale, and LOTUS | Statistics 110](https://www.youtube.com/watch?v=9vp1Ll2NpRw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=14)
15. [Lecture 15: Midterm Review | Statistics 110](https://www.youtube.com/watch?v=yFRZf81sB5k&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=15)
16. [Lecture 16: Exponential Distribution | Statistics 110](https://www.youtube.com/watch?v=bM6nFDjvEns&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=16)
17. [Lecture 17: Moment Generating Functions | Statistics 110](https://www.youtube.com/watch?v=N8O6zd6vTZ8&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=17)
18. [Lecture 18: MGFs Continued | Statistics 110](https://www.youtube.com/watch?v=tVDdx6xUOcs&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=18)
19. [Lecture 19: Joint, Conditional, and Marginal Distributions | Statistics 110](https://www.youtube.com/watch?v=J70dP_AECzQ&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=19)
20. [Lecture 20: Multinomial and Cauchy | Statistics 110](https://www.youtube.com/watch?v=xiVWNkQUqKk&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=20)
21. [Lecture 21: Covariance and Correlation | Statistics 110](https://www.youtube.com/watch?v=IujCYxtpszU&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=21)
22. [Lecture 22: Transformations and Convolutions | Statistics 110](https://www.youtube.com/watch?v=yXwPUAIvFyg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=22)
23. [Lecture 23: Beta distribution | Statistics 110](https://www.youtube.com/watch?v=UZjlBQbV1KU&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=23)
24. [Lecture 24: Gamma distribution and Poisson process | Statistics 110](https://www.youtube.com/watch?v=Qjeswpm0cWY&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=24)
25. [Lecture 25: Order Statistics and Conditional Expectation | Statistics 110](https://www.youtube.com/watch?v=2LR5JYbhyjg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=25)
26. [Lecture 26: Conditional Expectation Continued | Statistics 110](https://www.youtube.com/watch?v=PgawcWisb0I&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=26)
27. [Lecture 27: Conditional Expectation given an R.V. | Statistics 110](https://www.youtube.com/watch?v=gjBvCiRt8QA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=27)
28. [Lecture 28: Inequalities | Statistics 110](https://www.youtube.com/watch?v=UtXK_EQ3Pow&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=28)
29. [Lecture 29: Law of Large Numbers and Central Limit Theorem | Statistics 110](https://www.youtube.com/watch?v=OprNqnHsVIA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=29)
30. [Lecture 30: Chi-Square, Student-t, Multivariate Normal | Statistics 110](https://www.youtube.com/watch?v=MF-XSJOsGqw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=30)
31. [Lecture 31: Markov Chains | Statistics 110](https://www.youtube.com/watch?v=8AJPs3gvNlY&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=31)
32. [Lecture 32: Markov Chains Continued | Statistics 110](https://www.youtube.com/watch?v=aBGOyZv2pZE&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=32)
33. [Lecture 33: Markov Chains Continued Further | Statistics 110](https://www.youtube.com/watch?v=Q-pCzTpwPBU&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=33)
34. [Lecture 34: A Look Ahead | Statistics 110](https://www.youtube.com/watch?v=ChS3K2O-h7o&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=34)
35. [Joseph Blitzstein: "The Soul of Statistics" | Harvard Thinks Big 4](https://www.youtube.com/watch?v=dzFf3r1yph8&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=35)

</details>


## Books, notes and websites

- Book: Casella & Berger, *Statistical Inference*
- Book: Boyd & Vandenberghe, *Convex Optimization* (free) + Stanford EE364a
- Book: Koller & Friedman, *Probabilistic Graphical Models*

## Practice / proof of understanding

Fit a Bayesian network and a logistic model, test both, and report confidence intervals.

## What your IITM course sheet says

### From the PDF: CS6741

**Official description:** This course provides an introduction to statistics as applied to data science. It is intended as a first course for  students wanting to specialise in the fields of Data Science and Artificial Intelligence. Upon completion of the  program, students should:  ? Understand the role of statistics in data science, and contextualise it in the broader domain of machine  learning.  ? Interpret different data visualisation methods and choose the right visualisation for a specific data  representation task.  ? Know how to compute statistical measures of centrality and dispersion.  ? Demonstrate knowledge of point and interval estimators on fixed-sample and large-sample data.  ? Distinguish between Type I and Type II errors  ? Understand the central role of hypothesis testing and perform different tests on mean, variance, and  proportions under different conditions  ? Know how to carefully design e

**Official syllabus (trimmed):**

> Descriptive statistics: [2 weeks]
> Types of data such as qualitative[nominal, ordinal], quantitative[discrete, continuous]. Data visualisation tools such
> as relative, cumulative, absolute frequency charts and tables, relative, cumulative absolute histograms and
> frequency tables, scatter plots. Summary statistics such as mean, median, mode, percentiles, range, inter quartile
> range, variance, standard deviation, covariance, correlation (Pearson, Spearman rank correlation. Point Biserial
> correlation)
> Probability Theory (Recap): [2 weeks]
> Sample space, events, axioms of probability, random variables, expectation, joint distributions, condition
> distributions. Discrete probability distributions such as Bernoulli, Binomial, Uniform and Poisson. Continuous
> Distributions such as uniform distribution, normal distribution, exponential family. Analysis of multivariate Gaussian
> distribution.
> Randomised control experiments: [0.5 week]
> Sampling strategies such as simple random sampling, convenience sampling, stratified sampling and cluster
> sampling. Designing experiments with an understanding of explanatory variables, response variables, lurking
> variables, treatments, control groups, experimental units, placebo, single blind and double blind experiments.
> Distributions of sampling statistics: [1 week]
> Central limit theorem, distribution of mean, variance and proportions
> Estimation: [2.5 weeks]
> 

**Official textbooks:** 1) Ross, Sheldon M. Introductory statistics. Academic Press, 2017  2) Computer Age Statistical Inference: Algorithms, Evidence and Data Science, Bradley Efron and Trevor Hastie.  2016 (Cambridge University Press).

**Official references:** 1. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. 2nd Edition, Trevor Hastie, Robert  Tibshirani, and Jerome Friedman, 2009 (Springer) [ Available online:  https://web.stanford.edu/~hastie/ElemStatLearn/ ]  2. Casella, George and Berger Roger L. Statistical Inference. Cengage Learning, 2001

### From the PDF: CS6730

**Official description:** The course provides comprehensive introduction to probabilistic graphical models. At the end of the course the  student should be able to model problems using graphical models; design inference algorithms; and learn the  structure of the graphical model from data.

**Official syllabus (trimmed):**

> Review: Fundamentals of Probability Theory - Views of Probability, Random Variables and Joint Distributions,
>  Conditional Probability, Conditional Independence, Expectation and Variance, Probability Distributions - Conjugate
>  Priors, Introduction to Exponential Family; Fundamentals of Graph Theory - Paths, Cliques, Subgraphs, Cycles
>  and Loops.
>  Graphical Models: Introduction - Directed Models (Bayesian Network), Undirected Models (Markov Random
>  Fields), Dynamic Models (Hidden Markov Model & Kalman Filters) and Factor Graph; Conditional Independence
>  (Bayes Ball Theorem and D-separation), Markov Blanket, Factorization (Hammersley-Clifford Theorem),
>  Equivalence (I-Maps & Perfect Maps); Factor Graphs - Representation, Relation to Bayesian Network and Markov
>  Random Field.
>  Inference in graphical models: Exact Inference - Variable Elimination, Elimination Orderings, Relation to Dynamic
>  Programming, Dealing with Evidence, Forward-Backward Algorithm, Viterbi Algorithm; Junction Tree Algorithm;
>  Belief Propagation (Sum Product); Approximate Inference - Variational Methods (Mean Field, Kikuchi & Bethe
>  Approximation), Expectation Propagation, Gaussian Belief Propagation; MAP Inference - Max-Product, Graph
>  Cuts, Linear Programming Relaxations to MAP (Tree-Reweighted Belief Propagation, MPLP); Sampling - Markov
>  Chain Monte Carlo, Metropolis Hastings, Gibbs (Collapsing & Blocking), 

**Official textbooks:** Koller, D. and Friedman, N. (2009). Probabilistic Graphical Models: Principles and Techniques. MIT Press.

**Official references:** 1. Jensen, F. V. and Nielsen, T. D. (2002). Bayesian Networks and Decision Graphs. Information Science and  Statistics. Springer, 2nd edition.  2. Kevin P. Murphy (2013) Machine Learning: A Probabilistic Perspective. 4th Printing. MIT Press.  3. Barber, D. (2011). Bayesian Reasoning and Machine Learning. Cambridge University Press, 1st edition.  4. Bishop, C. M. (2011). Pattern Recognition and Mac

### From the PDF: CS5020

**Official description:** Optimisation problems arise in a variety of disciplines, for e.g., machine learning, reinforcement learning, signal  processing, networks. This course covers the core concepts of continuous optimisation and includes a thorough  introduction to unconstrained and constrained optimisation problems. Popular algorithms such as gradient and  Newton methods will be introduced and analysed for both convex and non-convex optimisation settings.  The evaluation will be based on the exams and home-works(which will involve both theoretical and programming  components).

**Official syllabus (trimmed):**

> Part 0: Recap of real analysis and linear algebra (Lectures 1-3)
>  1. Sets, functions, sequences, continuity, differentiability, gradients, Taylor series expansion. 2. Vectors, matrices,
>  norms, symmetric matrices, eigenvalue decomposition, positive
>  semidefinite and positive definite matrices.
>  Part I: Convex sets and functions (Lectures 4 – 11)
>  1. Convex sets, examples and properties.
>  2. Convex functions, strict and strong convexity, examples, and convexity preserving operations. 3. Equivalent
>  definitions of convexity under differentiability assumptions.
>  Part II: Unconstrained optimisation (Lectures 12-20)
>  1. Maxima, minima, stationary point, saddle point, local and global maximum/minimum. 2. First order and second
>  order conditions for optimality.
>  3. Linear, quadratic and convex optimisation problems, examples.
>  4. Benefits of convexity.
>  Part III: Constrained optimisation (Lectures 21-29)
>  1. Constrained optimisation problem, feasible set.
>  2. Lagrangian, KKT conditions
>  3. Linear and quadratic optimisation
>  4. Duality for convex optimisation — theorem of alternatives, Farka’s lemma.
>  Part IV: Algorithms for optimisation (Lectures 30-40)
>  1. Gradient descent with fixed step size, line search and Armijo-Goldstein rule
>  2. Newton method and variations
>  3. Conjugate gradient and Quasi-newton methods.
>  4. Algorithms for constrained optimisation: Projected gradient descent,

**Official textbooks:** 1. Stephen Boyd, and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.  2. David G. Luenberger and Yinyu Ye. Linear and nonlinear programming. 4th edition. Springer, 2015.

**Official references:** 1. Dimitri P. Bertsekas. Nonlinear programming. Belmont: Athena scientific, 1999.  2. Jorge Nocedal and Stephen Wright. Numerical optimization. Springer, 1999
