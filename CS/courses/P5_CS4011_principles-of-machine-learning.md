# CS4011 — Principles of Machine Learning

| | |
|---|---|
| Tier | A |
| Phase (order) | 5 |
| Do this first | CS6015 or equivalent, CS2800 |
| Estimated effort | 12-14 weeks, ~9 h/week |
| Unlocks | CS5691, CS6910, CS6700, CS6370, CS6350 |

## Roadmap

1. Linear/ridge regression; Bayesian classification and parameter estimation.
2. Evaluation and model selection; kNN; logistic regression, perceptron, SVM.
3. PCA/LDA; decision trees; ensembles; clustering.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [NPTEL MOOC Machine Learning 2016](https://www.youtube.com/playlist?list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77) (88 videos). NPTEL *Introduction to Machine Learning* (Balaraman Ravindran, IIT Madras): this is the IITM ML course.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Stanford CS229: Machine Learning led by Andrew Ng | Autumn 2018](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) (21 videos). Stanford CS229 Autumn 2018 (Andrew Ng, official Stanford Online): more maths-heavy; use the free CS229 notes.
- [Machine Learning Course - CS 156](https://www.youtube.com/playlist?list=PLD63A284B7615313A) (18 videos). Caltech CS156 *Learning from Data* (Abu-Mostafa, official): the best explanation of generalisation/VC theory.
- [Machine Learning Foundations](https://www.youtube.com/playlist?list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN) (93 videos). IIT Madras BS *Machine Learning Foundations*: maths refresh (linear algebra, PCA, probability) for ML.

### ⚡ Short videos for intuition and revision

- [Machine Learning](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) (100+ videos). StatQuest *Machine Learning*: 10-20 min intuitive explanation of each algorithm.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=r4sgKrRL2Ys&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=1)–[5](https://www.youtube.com/watch?v=9vMpHk44XXo&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=5), [85](https://www.youtube.com/watch?v=AXvGBmPD9q4&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=85)–[88](https://www.youtube.com/watch?v=6KBUU2Aa6lw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=88) | Intro, supervised/unsupervised/RL; the probability and linear algebra tutorials at the end of the playlist. |
| 2 | [6](https://www.youtube.com/watch?v=qNMElN-3Wmg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=6)–[10](https://www.youtube.com/watch?v=kETBe_lnfHs&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=10) | Decision theory, bias-variance, linear and multivariate regression. Implement linear regression with the normal equation and with gradient descent. |
| 3 | [11](https://www.youtube.com/watch?v=U9bURX-UGVU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=11)–[20](https://www.youtube.com/watch?v=E1bHf4BlCBQ&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=20), [84](https://www.youtube.com/watch?v=0YCu10BwG4s&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=84) | Subset selection, ridge/lasso, PCR, PLS, logistic regression, LDA. |
| 4 | [21](https://www.youtube.com/watch?v=_VXGGhRprAg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=21)–[26](https://www.youtube.com/watch?v=9dPjKuTYkx4&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=26), [83](https://www.youtube.com/watch?v=EdwAd002lzQ&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=83) | Perceptron, SVMs, kernels, hinge loss. Use sklearn SVC on a real dataset; plot decision boundaries. |
| 5 | [27](https://www.youtube.com/watch?v=olgnwStG9DE&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=27)–[33](https://www.youtube.com/watch?v=5RAJL_YPPQU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=33) | Neural networks + backprop, MLE, MAP, Bayesian estimation. Implement a 2-layer MLP in NumPy. |
| 6 | [34](https://www.youtube.com/watch?v=yG1nETGyW2E&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=34)–[47](https://www.youtube.com/watch?v=ReJfSYzB_jc&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=47), [82](https://www.youtube.com/watch?v=2nRayZAt1aA&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=82) | Decision trees, evaluation measures, cross-validation, ROC. Implement a decision tree from scratch. |
| 7 | [48](https://www.youtube.com/watch?v=OGLxVh1J-xk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=48)–[53](https://www.youtube.com/watch?v=3GvtQlShKmI&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=53) | Hypothesis testing and confidence intervals (for comparing models). |
| 8 | [54](https://www.youtube.com/watch?v=foWzsWFAmas&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=54)–[58](https://www.youtube.com/watch?v=1B_lrrEo5ds&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=58), [65](https://www.youtube.com/watch?v=WZQvKgx4BdU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=65) | Bagging, boosting, gradient boosting, random forests, naive Bayes, multi-class. Kaggle Titanic with XGBoost. |
| 9 | [59](https://www.youtube.com/watch?v=XBbNUyWAiks&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=59)–[64](https://www.youtube.com/watch?v=VfBUglMnRUw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=64) | Bayesian networks, undirected models, HMMs, variable elimination, belief propagation. |
| 10-11 | [66](https://www.youtube.com/watch?v=zop2zuwF_bc&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=66)–[77](https://www.youtube.com/watch?v=feFSsFu1TCk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=77) | Clustering (k-means, hierarchical, BIRCH, CURE, DBSCAN), GMMs and EM, spectral clustering, frequent itemsets. Implement k-means and EM for a GMM. |
| 12 | [78](https://www.youtube.com/watch?v=urmNFMSUBF8&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=78)–[81](https://www.youtube.com/watch?v=JbN2R68bZCw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=81) | Learning theory, intro to RL. |

<details>
<summary>All lectures in <i>NPTEL MOOC Machine Learning 2016</i> (88 videos)</summary>

1. [Introduction to Machine Learning](https://www.youtube.com/watch?v=r4sgKrRL2Ys&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=1)
2. [Week 1 - Lecture 1 - Introduction to Machine Learning](https://www.youtube.com/watch?v=fC7V8QsPBec&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=2)
3. [Week 1 Lecture 2 - Supervised Learning](https://www.youtube.com/watch?v=OTAR0kT1swg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=3)
4. [Week 1 Lecture 3 - Unsupervised Learning](https://www.youtube.com/watch?v=HTSCbxSxs-g&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=4)
5. [Week 1 Lecture 4 - Reinforcement Learning](https://www.youtube.com/watch?v=9vMpHk44XXo&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=5)
6. [Week 2 Lecture 5 - Statistical Decision Theory - Regression](https://www.youtube.com/watch?v=qNMElN-3Wmg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=6)
7. [Week 2 Lecture 6 - Statistical Decision Theory - Classification](https://www.youtube.com/watch?v=TUht9K5VXGs&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=7)
8. [Week 2 Lecture 7 - Bias - Variance](https://www.youtube.com/watch?v=W21YA1dLb6o&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=8)
9. [Week 2 Lecture 8 - Linear Regression](https://www.youtube.com/watch?v=_M7Km1XZERU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=9)
10. [Week 2 Lecture 9 - Multivariate Regression](https://www.youtube.com/watch?v=kETBe_lnfHs&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=10)
11. [Week 3 Lecture 10 Subset Selection 1](https://www.youtube.com/watch?v=U9bURX-UGVU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=11)
12. [Week 3 Lecture 11 Subset Selection 2](https://www.youtube.com/watch?v=gRkBOH7Cftg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=12)
13. [Week 3 Lecture 12 Shrinkage Methods](https://www.youtube.com/watch?v=KfuCtcj1qnc&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=13)
14. [Week 3 Lecture 13 Principal Components Regression](https://www.youtube.com/watch?v=FdzK33RymyQ&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=14)
15. [Week 3 Lecture 14 Partial Least Squares](https://www.youtube.com/watch?v=7XEV7gqat_8&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=15)
16. [Week 3 Lecture 15 Linear Classification](https://www.youtube.com/watch?v=cvEpBTmJNuw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=16)
17. [Week 3 Lecture 16 Logistic Regression](https://www.youtube.com/watch?v=g__LURKuIj4&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=17)
18. [Week 3 Lecture 17 Linear Discriminant Analysis 1](https://www.youtube.com/watch?v=UudeDPTtMos&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=18)
19. [Week 3 Lecture 18 Linear Discriminant Analysis 2](https://www.youtube.com/watch?v=2NrWhUResTg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=19)
20. [Week 3 Lecture 19 Linear Discriminant Analysis 3](https://www.youtube.com/watch?v=E1bHf4BlCBQ&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=20)
21. [Week 4 Lecture 20 Perceptron Learning](https://www.youtube.com/watch?v=_VXGGhRprAg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=21)
22. [Week 4 Lecture 21 SVM - Formulation](https://www.youtube.com/watch?v=jkFjfdQ1JDQ&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=22)
23. [Week 4 Lecture 22 SVM - Interpretation & Analysis](https://www.youtube.com/watch?v=C8CMqfmb7Bs&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=23)
24. [Week 4 Lecture 23 SVMs for Linearly Non Separable Data](https://www.youtube.com/watch?v=3-FhNaTkAZo&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=24)
25. [Week 4 Lecture 24 SVM Kernels](https://www.youtube.com/watch?v=-QDguusDi2E&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=25)
26. [Week 4 Lecture 25 SVM - Hinge Loss Formulation](https://www.youtube.com/watch?v=9dPjKuTYkx4&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=26)
27. [Week 5 Lecture 26 ANN I - Early Models](https://www.youtube.com/watch?v=olgnwStG9DE&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=27)
28. [Week 5 Lecture 27 ANN II - Backprogpogation I](https://www.youtube.com/watch?v=fUTwNOvoiyA&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=28)
29. [Week 5 Lecture 28 ANN III - Backpropogation II](https://www.youtube.com/watch?v=93UyKhN2FRM&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=29)
30. [Week 5 Lecture 29 ANN IV - Initialization, Training & Validation](https://www.youtube.com/watch?v=_eTMnZ1GIUM&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=30)
31. [MAXIMUM LIKELIHOOD ESTIMATE](https://www.youtube.com/watch?v=ugeG5DuZ3gc&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=31)
32. [Week 5 Lecture 31 Parameter Estimation II - Priors & MAP](https://www.youtube.com/watch?v=qpGo87YV1R0&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=32)
33. [Week 5 Lecture 32 Parameter Estimation III - Bayesian Estimation](https://www.youtube.com/watch?v=5RAJL_YPPQU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=33)
34. [Week 6 Lecture 33 Decision Trees - Introduction](https://www.youtube.com/watch?v=yG1nETGyW2E&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=34)
35. [Week 6 Lecture 34 Regression Trees](https://www.youtube.com/watch?v=CIYeuKAV-3c&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=35)
36. [Week 6 Lecture 35 Stopping Criteria & Pruning](https://www.youtube.com/watch?v=zLrNSXJF_As&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=36)
37. [Week 6 Lecture 36 Decision Trees for Classification - Loss Functions](https://www.youtube.com/watch?v=KH75AFuq74c&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=37)
38. [Week 6 Lecture 37 Decision Trees - Categorical Attributes](https://www.youtube.com/watch?v=8hwRXZiopUM&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=38)
39. [Week 6 Lecture 38 Decision Trees - Multiway Splits](https://www.youtube.com/watch?v=iWU8qZ3gU9Y&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=39)
40. [Week 6 Lecture 39 Decision Trees - Missing Values, Imputation & Surrogate Splits](https://www.youtube.com/watch?v=cbnqYfpukFQ&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=40)
41. [Week 6 Lecture 40 Decision Trees - Instability, Smoothness & Repeated Subtrees](https://www.youtube.com/watch?v=MVgo6eU0YCg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=41)
42. [Week 6 Lecture 41 Decision Trees - Example](https://www.youtube.com/watch?v=Jx3fWGPrx_k&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=42)
43. [Week 6 Lecture 42 Evaluation Measures 1](https://www.youtube.com/watch?v=Du8PsWbX1Y0&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=43)
44. [Week 6 Lecture 43 Bootstrapping & Cross Validation](https://www.youtube.com/watch?v=7mhLNwcBWyE&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=44)
45. [Week 6 Lecture 44 - 2 Class Evaluation Measures](https://www.youtube.com/watch?v=sosZp0cUsIk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=45)
46. [Week 6 Lecture 45 - The ROC Curve](https://www.youtube.com/watch?v=9Iq6pz9XJ7w&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=46)
47. [Week 6 Lecture 46 - Minimum Description Length & Exploratory Analysis](https://www.youtube.com/watch?v=ReJfSYzB_jc&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=47)
48. [Week 7 Lecture 47 - Introduction to Hypothesis Testing](https://www.youtube.com/watch?v=OGLxVh1J-xk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=48)
49. [Week 7 Lecture 48 - Basic Concepts](https://www.youtube.com/watch?v=XMWZdmNdrdw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=49)
50. [Week 7 Lecture 49 - Hypothesis Testing II - Sampling Distributions & The Z test](https://www.youtube.com/watch?v=PArYoTDMgtM&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=50)
51. [Week 7 Lecture 50 -STUDENT'S T-TEST](https://www.youtube.com/watch?v=c5kR4Vjdl_U&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=51)
52. [Week 7 Lecture 51 - Hypothesis Testing IV - The Two Sample and Paired Sample t-tests](https://www.youtube.com/watch?v=RY3Ya5NGCu0&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=52)
53. [Week 7 Lecture 52 - Confidence Intervals](https://www.youtube.com/watch?v=3GvtQlShKmI&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=53)
54. [Week 8 Lecture 53 - Ensemble Methods - Bagging, Committee Machines and Stacking](https://www.youtube.com/watch?v=foWzsWFAmas&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=54)
55. [Week 8 Lecture 54 - Boosting](https://www.youtube.com/watch?v=NrdtKndsC1I&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=55)
56. [Week 8 Lecture 55 - Gradient Boosting](https://www.youtube.com/watch?v=Y7_q5hByKuo&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=56)
57. [Week 8 Lecture 56 - Random Forests](https://www.youtube.com/watch?v=6K48CbOm99Y&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=57)
58. [Week 8 Lecture 57 - Naive Bayes](https://www.youtube.com/watch?v=1B_lrrEo5ds&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=58)
59. [Week 9 Lecture 58 Bayesian Networks](https://www.youtube.com/watch?v=XBbNUyWAiks&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=59)
60. [Week 9 Lecture 59 Undirected Graphical Models - Introduction](https://www.youtube.com/watch?v=3IM-xZ7ZscU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=60)
61. [Week 8 Lecture 60 Undirected Graphical Models - Potential Functions](https://www.youtube.com/watch?v=m8Ln4rBpfHs&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=61)
62. [Week 9 Lecture 61 Hidden Markov Models](https://www.youtube.com/watch?v=qGtth60V6nM&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=62)
63. [Week 9 Lecture 62 Variable Elimination](https://www.youtube.com/watch?v=gb5CpZOntFI&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=63)
64. [Week 9 Lecture 63 Belief Propagation](https://www.youtube.com/watch?v=VfBUglMnRUw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=64)
65. [Lecture 64 Multi-class Classification](https://www.youtube.com/watch?v=WZQvKgx4BdU&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=65)
66. [Week 10 Lecture 65 Partional Clustering](https://www.youtube.com/watch?v=zop2zuwF_bc&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=66)
67. [Week 10 Lecture 66 Hierarchical Clustering](https://www.youtube.com/watch?v=tlIv3IT_hHk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=67)
68. [Week 10 Lecture 67 Threshold Graphs](https://www.youtube.com/watch?v=1SxPbhaK_uc&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=68)
69. [Week 10 Lecture 68 The BIRCH Algorithm](https://www.youtube.com/watch?v=Skn1q837TUM&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=69)
70. [Week 10 Lecture 69 The CURE Algorithm](https://www.youtube.com/watch?v=CdEatQP0IDg&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=70)
71. [Week 10 Lecture 70 Density Based Clustering](https://www.youtube.com/watch?v=qrmneD5_VrM&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=71)
72. [Week 11 Lecture 71 Gaussian Mixture Models](https://www.youtube.com/watch?v=FK9izGvLzU8&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=72)
73. [Week 11 Lecture 72 Expectation Maximization](https://www.youtube.com/watch?v=NgWiPBH6jHA&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=73)
74. [Week 11 Lecture 73 Expectation Maximization Continued](https://www.youtube.com/watch?v=Jj7MzS-YwGY&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=74)
75. [Lecture 76 Spectral Clustering](https://www.youtube.com/watch?v=AFsKM4spCPk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=75)
76. [The Apriori Property](https://www.youtube.com/watch?v=VI6eGXxsrIk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=76)
77. [Frequent Itemset Mining](https://www.youtube.com/watch?v=feFSsFu1TCk&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=77)
78. [Lecture 79 Learning Theory](https://www.youtube.com/watch?v=urmNFMSUBF8&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=78)
79. [Lecture 80 Introduction to Reinforcement Learning](https://www.youtube.com/watch?v=-U5ezelRSlA&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=79)
80. [Lecture 81 - RL Framework and TD Learning](https://www.youtube.com/watch?v=NhAYuEoWZ1w&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=80)
81. [Lecture 82 Solution Methods & Applications](https://www.youtube.com/watch?v=JbN2R68bZCw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=81)
82. [Week 6 Decision Trees Tutorial](https://www.youtube.com/watch?v=2nRayZAt1aA&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=82)
83. [Week 4 Tutorial 4 - Optimization](https://www.youtube.com/watch?v=EdwAd002lzQ&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=83)
84. [Week 3 Weka Tutorial](https://www.youtube.com/watch?v=0YCu10BwG4s&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=84)
85. [Week 2 Tutorial 2 - Linear Algebra (2)](https://www.youtube.com/watch?v=AXvGBmPD9q4&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=85)
86. [Week 2 Tutorial 2 - Linear Algebra (1)](https://www.youtube.com/watch?v=7Py7x8pds24&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=86)
87. [Week 1 Tutorial 1 - Probability Basics (2)](https://www.youtube.com/watch?v=ymBN8m1SL2s&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=87)
88. [Week 1 Tutorial 1 - Probability Basics (1)](https://www.youtube.com/watch?v=6KBUU2Aa6lw&list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77&index=88)

</details>


## Books, notes and websites

- ✅ NPTEL *Introduction to Machine Learning* (Balaraman Ravindran, IIT Madras) — nptel.ac.in/courses/106106139/
- Stanford CS229 (Andrew Ng) — cs229.stanford.edu
- Book: Bishop, *Pattern Recognition and Machine Learning* (the course text, free PDF)
- Book: *An Introduction to Statistical Learning* (statlearning.com, free)
- scikit-learn tutorials; Kaggle Learn

## Practice / proof of understanding

Re-implement linear regression, logistic regression, k-means and a decision tree from scratch with NumPy, then compare with scikit-learn on 3 Kaggle datasets.

## What your IITM course sheet says

### From the PDF: CS4011

**Official description:** This course will serve as a comprehensive introduction to various topics in machine learning. At the end of the  course the students should be able to design and implement machine learning solutions to classification,  regression, and clustering problems; and be able to evaluate and interpret the results of the algorithms.

**Official syllabus (trimmed):**

> - Introduction to the course, recap of linear algebra and probability theory basics.
>  - Linear Regression, Ridge Regression, Sensitivity Analysis, Multivariate Regeression
>  - Bayesian Classification: Naive Bayes, Parameter Estimation (ML, MAP), Sequential Pattern Classification
>  - Evaluation and Model Selection: ROC Curves, Evaluation Measures, Significance tests
>  - Non-parametric Methods: k-Nearest Neighbours, Parzen Window
>  - Discriminative Learning models: Logistic Regression, Perceptrons, Artificial Neural Networks, Support Vector
>  Machines
>  - Dimensionality Reduction: Principal Component Analysis, Fischer's Discriminant Analysis
>  - Decision Trees: Splitting Criteria, CART
>  - Ensemble Methods: Boosting, Bagging, Random Forests
>  - Clustering: Partitional, Hierarchical, density based clustering.

**Official textbooks:** 1. Pattern Recognition and Machine Learning, Christopher Bishop, Springer 2006.

**Official references:** 1. Introduction to Statistical Learning, Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, Springer,  2013.  2. Pattern Classification, 2nd Ed., Richard Duda, Peter Hart, David Stork, John Wiley & Sons, 2001.

### From the PDF: CS5691

**Official description:** At the end of the course, the students should be able to design and implement machine learning techniques for  solving pattern recognition tasks such as classification, regression, and clustering, and be able to evaluate and  interpret the results of the techniques.

**Official syllabus (trimmed):**

> 1. Basics of Linear Algebra, Probability Theory and Optimization: Vectors, Inner product, Outer product,
>  Eigenanalysis, Probability distributions – Discrete distributions and Continuous distributions; Conditional probability
>  distribution and Joint probability distribution, Bayes theorem, Unconstrained optimization, Constrained optimization
>  – Lagrangian multiplier method. (5 Lectures)
>  2. Methods for Function Approximation: Linear models for regression, Parameter estimation method,
>  Regularization, Ridge regression (6 Lectures)
>  3. Probabilistic Models for Classification: K-Nearest neighbours classifier, Bayesian decision theory, Bayes
>  classifier, Normal (Gaussian) density – Discriminant functions, Decision surfaces, Maximum-Likelihood
>  estimation; Gaussian mixture models -- Expectation-Maximization method for parameter estimation; Naive Bayes
>  classifier, Non-parametric techniques for density estimation -- Parzen-window method, K-nearest neighbors
>  method (15 Lectures)
>  4. Discriminative Learning based Models for Classification: Logistic regression, Perceptron, Multilayer
>  feedforward neural network – Gradient descent method, Error backpropagation method; Support vector machine.
>  (12 Lectures)
>  5. Dimensionality Reduction Techniques: Principal component analysis, Fisher discriminant analysis (3 Lectures)
>  6. Non-Metric Methods for Classification: Decision trees, Random fore

**Official textbooks:** 1. C.M.Bishop, Pattern Recognition and Machine Learning, Springer, 2006  2. R.O.Duda, P.E.Hart and D.G.Stork, Pattern Classification, John Wiley, 2001

**Official references:** 1. S.Theodoridis and K.Koutroumbas, Pattern Recognition, Academic Press, 2009  2. E.Alpaydin, Introduction to Machine Learning, Prentice-Hall of India, 2010
