# DA3407 — Machine Learning II

| | |
|---|---|
| Tier | A |
| Phase (order) | 5 |
| Do this first | DA2400, DA3409 |
| Estimated effort | 12 weeks |
| Unlocks | DA7400, advanced ML |

## Roadmap

1. Kernel methods, probabilistic/graphical models, ensembles at depth, generalisation theory.
2. The PDF gives no syllabus for this one, so follow Bishop's second half.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [CORNELL CS4780 "Machine Learning for Intelligent Systems"](https://www.youtube.com/playlist?list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS) (41 videos). Cornell CS4780 *Machine Learning for Intelligent Systems* (Kilian Weinberger): the clearest rigorous ML course: MLE/MAP, Bayes, kernels, GPs, boosting. Notes on his site.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Stanford CS229M: Machine Learning Theory - Fall 2021](https://www.youtube.com/playlist?list=PLoROMvodv4rP8nAmISxFINlGKSK4rbLKh) (20 videos). Stanford CS229M *Machine Learning Theory* (Tengyu Ma, Fall 2021, official): generalisation bounds.
- [The Gaussian Process Summer School 2020](https://www.youtube.com/playlist?list=PLZ_xn3EIbxZHynuWRdYp4WDtpKm5Xo9Ge) (9 videos). Gaussian Process Summer School 2020 (official).
- [Mathematical Foundations for Machine Learning](https://www.youtube.com/playlist?list=PLgMDNELGJ1CYPJS6m_ygxb4KtHYxh1HjR) (71 videos). NPTEL *Mathematical Foundations for Machine Learning* (IISc).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=MrLPzBxG95I&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=1)–[6](https://www.youtube.com/watch?v=kObhWlqIeD8&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=6) | Supervised learning setup, kNN, curse of dimensionality, perceptron and its convergence proof. Implement kNN and perceptron in NumPy. |
| 2 | [7](https://www.youtube.com/watch?v=RIawrYLVdIw&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=7)–[12](https://www.youtube.com/watch?v=o6FfdP2uYh4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=12) | MLE/MAP, naive Bayes, logistic regression, gradient descent and Newton's method. |
| 3 | [13](https://www.youtube.com/watch?v=_21o_ylL0q4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=13)–[18](https://www.youtube.com/watch?v=YeBowxFenjw&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=18) | Linear/ridge regression, linear SVMs, empirical risk minimisation, regularisation. |
| 4 | [19](https://www.youtube.com/watch?v=zUJbRO0Wavo&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=19)–[21](https://www.youtube.com/watch?v=a7cofmFgwIk&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=21) | Bias-variance decomposition, model selection. |
| 5 | [22](https://www.youtube.com/watch?v=FgTQG2IozlM&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=22)–[27](https://www.youtube.com/watch?v=BzHJ57QCdVo&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=27) | Kernels, kernel SVMs, Gaussian processes. Use sklearn SVC with RBF kernel; tune C and gamma. |
| 6 | [28](https://www.youtube.com/watch?v=E1_WCdUAtyE&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=28)–[34](https://www.youtube.com/watch?v=toOAToTaGV4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=34) | KD/ball trees, decision trees, bagging, random forests, boosting, AdaBoost. Implement a decision tree and AdaBoost. |
| 7 | [35](https://www.youtube.com/watch?v=kPXxbmBsFxs&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=35)–[37](https://www.youtube.com/watch?v=wqpIohLjsAY&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=37), [40](https://www.youtube.com/watch?v=Nu7VZeW5TaE&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=40) | Neural networks and transformers. |

<details>
<summary>All lectures in <i>CORNELL CS4780 &quot;Machine Learning for Intelligent Systems&quot;</i> (41 videos)</summary>

1. [Lecture 1 "Supervised Learning Setup" -Cornell CS4780 Machine Learning for Decision Making SP17](https://www.youtube.com/watch?v=MrLPzBxG95I&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=1)
2. [Lecture 2 "Supervised Learning Setup Continued" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=zj-5nkNKAow&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=2)
3. [Lecture 3 "k-nearest neighbors" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=oymtGlGdT-k&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=3)
4. [Lecture 4 "Curse of Dimensionality / Perceptron" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=BbYV8UfMJSA&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=4)
5. [Lecture 5 "Perceptron" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=wl7gVvI-HuY&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=5)
6. [Lecture 6 "Perceptron Convergence Proof" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=kObhWlqIeD8&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=6)
7. [Lecture 7 "Estimating Probabilities from Data: Maximum Likelihood Estimation" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=RIawrYLVdIw&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=7)
8. [Machine Learning Lecture 8 "Estimating Probabilities from Data: Naive Bayes" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=pDHEX2usCS0&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=8)
9. [Machine Learning Lecture 9 "Naive Bayes continued" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=VDK0nkjFh5U&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=9)
10. [Machine Learning Lecture 10 "Naive Bayes continued" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=rqB0XWoMreU&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=10)
11. [Machine Learning Lecture 11 "Logistic Regression" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=GnkDzIOxfzI&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=11)
12. [Machine Learning Lecture 12 "Gradient Descent / Newton's Method" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=o6FfdP2uYh4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=12)
13. [Machine Learning Lecture 13 "Linear / Ridge Regression" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=_21o_ylL0q4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=13)
14. [Machine Learning Lecture 14 "(Linear) Support Vector Machines" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=xpHQ6UhMlx4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=14)
15. [Machine Learning Lecture 15 "(Linear) Support Vector Machines continued" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=FwYNPomeBBg&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=15)
16. [Machine Learning Lecture 16 "Empirical Risk Minimization" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=AkmPv2WEsHw&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=16)
17. [Machine Learning Lecture 17 "Regularization / Review" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=NLBwFyT9Qks&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=17)
18. [Machine Learning Lecture 18 "Review Lecture II" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=YeBowxFenjw&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=18)
19. [Machine Learning Lecture 19 "Bias Variance Decomposition" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=zUJbRO0Wavo&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=19)
20. [Machine Learning Lecture 20 "Model Selection / Regularization / Overfitting" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=65UJPA10dW8&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=20)
21. [Machine Learning Lecture 21 "Model Selection / Kernels" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=a7cofmFgwIk&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=21)
22. [Machine Learning Lecture 22 "More on Kernels" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=FgTQG2IozlM&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=22)
23. [Machine Learning Lecture 23 "Kernels Continued Continued" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=erqL3y2es1I&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=23)
24. [Machine Learning Lecture 24 "Kernel Support Vector Machine" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=RwF1esLCG4U&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=24)
25. [Machine Learning Lecture 25 "Kernelized algorithms" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=7LlpTABc27s&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=25)
26. [Machine Learning Lecture 26 "Gaussian Processes" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=R-NUdqxKjos&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=26)
27. [Machine Learning Lecture 27 "Gaussian Processes II / KD-Trees / Ball-Trees" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=BzHJ57QCdVo&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=27)
28. [Machine Learning Lecture 28 "Ball Trees / Decision Trees" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=E1_WCdUAtyE&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=28)
29. [Machine Learning Lecture 29 "Decision Trees / Regression Trees" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=a3ioGSwfVpE&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=29)
30. [Machine Learning Lecture 30 "Bagging" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=0LB1cy2sCXc&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=30)
31. [Machine Learning Lecture 31 "Random Forests / Bagging" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=4EOCQJgqAOY&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=31)
32. [Machine Learning Lecture 32 "Boosting" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=dosOtgSdbnY&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=32)
33. [Machine Learning Lecture 33 "Boosting Continued" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=Vd6hzcwEa2k&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=33)
34. [Machine Learning Lecture 34 "Boosting / Adaboost" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=toOAToTaGV4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=34)
35. [Machine Learning Lecture 35 "Neural Networks / Deep Learning" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=kPXxbmBsFxs&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=35)
36. [Machine Learning Lecture 36 "Neural Networks / Deep Learning Continued" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=zmu9wR2c7Z4&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=36)
37. [Machine Learning Lecture 37 "Neural Networks / Deep Learning" -Cornell CS4780 SP17](https://www.youtube.com/watch?v=wqpIohLjsAY&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=37)
38. [In-class Kaggle Competition in less than 5 Minutes](https://www.youtube.com/watch?v=LzkBBjj1rHs&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=38)
39. [Machine Learning Certificate from Cornell University](https://www.youtube.com/watch?v=k3UvZD6DGbQ&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=39)
40. [CS4780 Transformers (additional lecture 2023)](https://www.youtube.com/watch?v=Nu7VZeW5TaE&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=40)
41. [The DBSCAN Clustering Algorithm Explained](https://www.youtube.com/watch?v=4AW_5nYQkuc&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS&index=41)

</details>


## Books, notes and websites

- Book: Bishop PRML, Hastie *ESL* (free)
- Stanford CS229/CS228
- ✅ NPTEL ML (Ravindran)

## Practice / proof of understanding

Implement an SVM with kernels and an EM algorithm for Gaussian mixtures.

## Note

Not in your PDF; roadmap is inferred from the course name and prerequisites.

## What your IITM course sheet says

### From the PDF: DA3407

**Official description:** The students should be able to  1. Identify and distinguish between different ML paradigms based on how they interface with the user and data.  2. Analyse advantages of kernel and Bayesian methods over feature vector based frequentist methods.  3. Construct, learn and perform inference on appropriate probabilistic models for the task at hand based on goals  and  data available.  4. Understand the theoretical basis of some popular Machine learning algorithms, and explain the mathematical  reasoning behind their success.  5. Give conditions under which the theoretical analysis of machine learning breaks down, and use that to  understand  potential failure points of learning algorithms.

**Official syllabus (trimmed):**

> 1. Kernel and Bayesian methods. (4 weeks) Kernel methods, feature maps, RKHS, Regularisation. Bayesian
>  methods, Conjugate priors, Gaussian processes, hyperparameter selection.
>  2. Probabilistic modelling (4 weeks) Bayesian nets, Markov random fields, Factor graphs, Inference and parameter
>  estimation, Markov chain Monte Carlo and Gibbs sampling.
>  3. Learning theory (4 weeks) Generalisation, uniform convergence, effect of regularisation, measures of
>  complexity,
>  margin based bounds, interpolation, grokking and double descent.
>  4. Other paradigms of learning (2 weeks) Active learning, sequential learning, multi-armed bandits, semi-
>  supervised learning, self-supervised learning, in-context learning, recommender systems and collaborative
>  filtering.
>  5. Advanced Topics (1 week) Input and output data formats: Tables, text, speech, images, video, graphs, point
>  clouds. Objectives beyond accuracy: Privacy, fairness, transparency, interpretability, efficiency, Handling missing
>  data and outliers.

**Official textbooks:** 1. Murphy, Kevin P. Probabilistic Machine Learning: An Introduction. Cambridge, MA: The MIT Press, 2022.  2. Bishop, Christopher M. Pattern Recognition and Machine Learning. New York: Springer, 2006.  3. Mohri, Mehryar, Afshin Rostamizadeh, and Ameet Talwalkar. Foundations of Machine Learning. 2nd ed. Cam-  bridge, MA: The MIT Press, 2018.  4. Shalev-Shwartz, Shai, and Shai Ben-David. Understanding Machine Learning: From Theory to Algorithms.  Cam-  bridge: Cambridge University Press, 2014.

**Official references:** Shalev-Shwartz, Shai, and Shai Ben-David. Understanding Machine Learning: From Theory to Algorithms. Cam-  bridge: Cambridge University Press, 2014.
