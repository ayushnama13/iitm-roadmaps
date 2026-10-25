# DA1004 — Probability and Statistics for Engineers

| | |
|---|---|
| Tier | A |
| Phase (order) | 2 |
| Do this first | DA1000 |
| Estimated effort | 12 weeks, ~7 h/week |
| Unlocks | DA2400, DA2403, DA3407 |

## Roadmap

1. Axioms, conditioning, Bayes.
2. Random variables and common distributions; joint/marginal; MGFs.
3. Concentration inequalities, LLN, CLT.
4. Estimation, hypothesis tests, regression.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Statistics 110: Probability](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) (35 videos). Harvard *Stat 110: Probability* (Joe Blitzstein, official). Free book at probabilitybook.net.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Statistics for Data Science 1](https://www.youtube.com/playlist?list=PLZ2ps__7DhBYrMs3zybOqr1DzMFCX49xG) (100+ videos). IIT Madras BS *Statistics for Data Science 1*: descriptive stats, basic probability.
- [Statistics for Data Science 2](https://www.youtube.com/playlist?list=PLZ2ps__7DhBbLZ6RdNTIXvFdaMpvqagt0) (100+ videos). IIT Madras BS *Statistics for Data Science 2*: random variables, estimation, testing.
- [MIT 18.650 Statistics for Applications, Fall 2016](https://www.youtube.com/playlist?list=PLUl4u3cNGP60uVBMaoNERc6knT_MgPKS0) (22 videos). MIT 18.650 *Statistics for Applications* (Fall 2016, official OCW): the inference half, rigorous.

### ⚡ Short videos for intuition and revision

- [Statistics Fundamentals](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) (62 videos). StatQuest *Statistics Fundamentals*: p-values, distributions, MLE, in short clear videos.

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

- Harvard Stat 110 (Blitzstein) — YouTube
- ✅ NPTEL *Probability and Statistics* (Somesh Kumar, IIT Kharagpur) — nptel.ac.in/courses/111105041
- Book: Sheldon Ross, *A First Course in Probability* / *Introduction to Probability and Statistics for Engineers and Scientists* (course texts)
- MIT 6.041

## Practice / proof of understanding

Simulate LLN and CLT in Python and verify Chebyshev numerically.

## What your IITM course sheet says

### From the PDF: DA1004

**Official description:** 1. Understand probabilistic modeling of uncertainty and randomness.  2. Understand distributions, random variables and random process representations.  3. Understand Bayesian and classical frameworks of inference.  4. Perform conditioning, expectation, and correlation.  5. Generate data from a probabilistic model.  6. Learn and apply statistical techniques to infer model parameters from the data.

**Official syllabus (trimmed):**

> 1. Probability Axioms of probability, independence, mutual exclusivity, conditioning, Bayes theorem.
>  2. Random variables Discrete and continuous random variables, probability mass and density functions,
>  transformation
>  of random variables, expectations.
>  3. Distributions Joint and marginal distributions, moment generating functions, characteristic functions, entropy,
>  uniform,
>  exponential, binomial, geometric, Gaussian, Poisson, beta, chi-square and Pareto distributions.
>  4. Concentration inequalities Markov, Chebyshev, and Chernoff inequalities, law of large numbers, central limit
>  theorem.
>  5. Sampling Rejection sampling, acceptance sampling, Monte Carlo methods, bootstrapping, design of
>  experiments.
>  6. Statistical Inference Likelihood, posteriors, bias, maximum likelihood and maximum aposteriori estimation,
>  conjugate
>  prior, confidence interval, p-value, linear regression, hypothesis tests, naive Bayes classifier.

**Official textbooks:** 1. S.M. Ross, Introduction to Probability and Statistics for Engineers and Scientists, 5th Ed., Elsevier.  2. S.M. Ross, A First Course in Probability, 10th Ed., Pearson.  3. A. Papoulis and S. Pillai, Probability - Random Variables and Stochastic Processes, 4th Ed., McGraw Hill.  4. G. Casella and R. L. Berger, Statistical Inference, Cengage Learning.

**Official references:** 1. S.M. Ross, Introduction to Probability and Statistics for Engineers and Scientists, 5th Ed., Elsevier.  2. S.M. Ross, A First Course in Probability, 10th Ed., Pearson.  3. A. Papoulis and S. Pillai, Probability - Random Variables and Stochastic Processes, 4th Ed., McGraw Hill.  4. G. Casella and R. L. Berger, Statistical Inference, Cengage Learning.
