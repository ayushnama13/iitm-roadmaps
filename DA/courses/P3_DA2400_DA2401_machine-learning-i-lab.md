# DA2400+DA2401 — Machine Learning I (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | DA1001, DA1004, DA1300, DA1002 |
| Estimated effort | 14 weeks, ~10 h/week |
| Unlocks | DA3407, DA2403, DA3409, DA5400 |

## Roadmap

1. Regression, bias-variance, Lasso/Ridge.
2. Classification: Naive Bayes, logistic regression, SVM, trees, boosting, random forests.
3. Unsupervised: PCA, k-means.
4. Lab: pandas, missing data, model comparison.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Machine Learning Foundations](https://www.youtube.com/playlist?list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN) (93 videos). IIT Madras BS *Machine Learning Foundations*: the IITM DS-programme ML start.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Machine Learning Techniques ( Prof. Arunkumar )](https://www.youtube.com/playlist?list=PLZ2ps__7DhBbA_e6_G3FI-BA1f7lCINUu) (74 videos). IIT Madras BS *Machine Learning Techniques* (Arun Rajkumar): PCA, clustering, regression, SVM, ensembles.
- [NPTEL MOOC Machine Learning 2016](https://www.youtube.com/playlist?list=PL1xHD4vteKYVpaIiy295pg6_SY5qznc77) (88 videos). NPTEL *Introduction to Machine Learning* (Balaraman Ravindran, IIT Madras).
- [Stanford CS229: Machine Learning led by Andrew Ng | Autumn 2018](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) (21 videos). Stanford CS229 (Andrew Ng, Autumn 2018, official): the maths-heavy classic.
- [Machine Learning Practice Course](https://www.youtube.com/playlist?list=PLZ2ps__7DhBb3ovNQam2c_WcGeiW9OhQo) (98 videos). IIT Madras BS *Machine Learning Practice*: scikit-learn, for the lab (DA2401).

### ⚡ Short videos for intuition and revision

- [Machine Learning](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) (100+ videos). StatQuest *Machine Learning*: one clear video per algorithm.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=zuS1WZQGhAs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=1)–[9](https://www.youtube.com/watch?v=JG5Z9np4Tbs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=9) | What ML is: regression, classification, dimensionality reduction, density estimation. |
| 2 | [10](https://www.youtube.com/watch?v=Gi9nUcrZAJs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=10)–[16](https://www.youtube.com/watch?v=YNJMUyNlqFQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=16) | Univariate and multivariate calculus, linear approximation. |
| 3 | [17](https://www.youtube.com/watch?v=9Ynm5oJRjxY&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=17)–[24](https://www.youtube.com/watch?v=Ijn-HGlVifU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=24) | Four subspaces, orthogonality, projections, least squares. Implement least squares regression in NumPy. |
| 4 | [25](https://www.youtube.com/watch?v=x7UJYkGHVJw&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=25)–[31](https://www.youtube.com/watch?v=SPF2ovt7uYg&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=31) | Polynomial regression, eigenvalues, diagonalisation. |
| 5 | [32](https://www.youtube.com/watch?v=G6A3PDivChQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=32)–[37](https://www.youtube.com/watch?v=__TUd8Sq-wU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=37) | Complex, Hermitian and unitary matrices. |
| 6 | [38](https://www.youtube.com/watch?v=fTErMgNIKHQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=38)–[44](https://www.youtube.com/watch?v=0vb0c-0waik&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=44) | SVD, positive definite matrices. |
| 7 | [45](https://www.youtube.com/watch?v=K5vOOARxVyU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=45)–[49](https://www.youtube.com/watch?v=XrDPtTvuYz4&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=49), [93](https://www.youtube.com/watch?v=tywEGBtZTu0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=93) | PCA. Implement PCA from scratch and apply it to MNIST. |
| 8 | [50](https://www.youtube.com/watch?v=LYZPWUppGGc&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=50)–[57](https://www.youtube.com/watch?v=ohQfHMpjTlQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=57) | Unconstrained optimisation, gradient descent, Taylor series. |
| 9-10 | [58](https://www.youtube.com/watch?v=fFJHsQBo6NE&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=58)–[71](https://www.youtube.com/watch?v=M2qvsHZxlI0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=71), [92](https://www.youtube.com/watch?v=WbLg1drl2UY&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=92) | Constrained optimisation, Lagrange multipliers, convexity, duality, KKT. |
| 11 | [72](https://www.youtube.com/watch?v=DpYlIh_3ttY&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=72)–[86](https://www.youtube.com/watch?v=sBT-TWoCMj4&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=86) | Probability: discrete and continuous random variables, expectation, common distributions. |
| 12 | [87](https://www.youtube.com/watch?v=yNPMeKXjISQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=87)–[91](https://www.youtube.com/watch?v=UExuNuc8IKo&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=91) | Multivariate normal, parameter estimation, GMM and EM, concentration inequalities. Implement EM for a 1-D GMM. |

<details>
<summary>All lectures in <i>Machine Learning Foundations</i> (93 videos)</summary>

1. [W1.L1. What is machine learning? | intro to machine learning & its applications](https://www.youtube.com/watch?v=zuS1WZQGhAs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=1)
2. [W1_L2: Data, models & machine learning task](https://www.youtube.com/watch?v=zssr9nOZlVg&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=2)
3. [W1_L3: Supervised learning: regression](https://www.youtube.com/watch?v=iVcrCdEaJ7A&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=3)
4. [W1_L4: Supervised learning: classification](https://www.youtube.com/watch?v=QtOrjs0Fzzc&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=4)
5. [W1_L5: Unsupervised learning: dimensionality reduction](https://www.youtube.com/watch?v=EuNPsw9zA1k&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=5)
6. [W1_L6: Unsupervised learning: density estimation](https://www.youtube.com/watch?v=Gj6-61UDeMs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=6)
7. [W1_T1: To machine learning or not to machine learning](https://www.youtube.com/watch?v=5G4klfCCoIs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=7)
8. [W1_T2: Illustration with a real world dataset](https://www.youtube.com/watch?v=T7vdFVC6DOo&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=8)
9. [W1_T3: Dimensionality reduction & density estimation with applications](https://www.youtube.com/watch?v=JG5Z9np4Tbs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=9)
10. [W2_L1: Sets & functions](https://www.youtube.com/watch?v=Gi9nUcrZAJs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=10)
11. [W2_L2: Univariate calculus: continuity & differentiability](https://www.youtube.com/watch?v=yvaPORg2w9c&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=11)
12. [W2_L3: Univariate calculus: derivatives & linear approximations](https://www.youtube.com/watch?v=AG2fQvxEpbE&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=12)
13. [W2_L4: Univariate calculus: applications & advanced rules](https://www.youtube.com/watch?v=En15LA59Fsw&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=13)
14. [W2_L5: Multivariate calculus: lines & planes in higher dimensional space](https://www.youtube.com/watch?v=O5jrvVi05wA&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=14)
15. [W2_L6: Multivariate calculus: linear approximation & applications](https://www.youtube.com/watch?v=dLLbl0vucCc&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=15)
16. [Week 2: Tutorial](https://www.youtube.com/watch?v=YNJMUyNlqFQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=16)
17. [W3_L1: Four fundamental subspaces](https://www.youtube.com/watch?v=9Ynm5oJRjxY&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=17)
18. [W3_L2: Orthogonal vectors & subspaces](https://www.youtube.com/watch?v=fHorO_JCaYA&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=18)
19. [W3_L3: Projections](https://www.youtube.com/watch?v=kVYR7II5KUA&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=19)
20. [W3_L4: Least squares & projections onto a subspace](https://www.youtube.com/watch?v=_QRlIQBwIk8&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=20)
21. [W3_L5: Example of least squares](https://www.youtube.com/watch?v=wZlwod57blE&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=21)
22. [W3_T1: Four fundamental vector subspaces](https://www.youtube.com/watch?v=rbBiDiFC584&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=22)
23. [W3_T2: Row space computation using reduced row echelon form & solution to ax = b](https://www.youtube.com/watch?v=kRJIiQXiOqU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=23)
24. [W3_T3: Orthogonality, projections & least squares method](https://www.youtube.com/watch?v=Ijn-HGlVifU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=24)
25. [W4_L1: Linear & polynomial regression](https://www.youtube.com/watch?v=x7UJYkGHVJw&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=25)
26. [W4_L2: Eigenvalues & Eigenvectors](https://www.youtube.com/watch?v=GA6m_T4d_d0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=26)
27. [W4_L3: Diagonalization of a matrix](https://www.youtube.com/watch?v=WKZUxnrLmRk&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=27)
28. [W4_L4: Solving fibonacci sequence using diagonalization](https://www.youtube.com/watch?v=ISB87lDKOVE&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=28)
29. [W4_L5: Orthogonality diagonalizable matrices](https://www.youtube.com/watch?v=f0hVL9xhL94&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=29)
30. [W4_T1: Polynomial regression](https://www.youtube.com/watch?v=EF85-fHy-m0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=30)
31. [W4_T2: Tutorial on eigenvalues & eigenvectors](https://www.youtube.com/watch?v=SPF2ovt7uYg&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=31)
32. [W5_L1: Complex matrices](https://www.youtube.com/watch?v=G6A3PDivChQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=32)
33. [W5_L2: Hermitian matrices](https://www.youtube.com/watch?v=aHykfDdjDiw&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=33)
34. [W5_L3: Unitary matrices](https://www.youtube.com/watch?v=2DAG0I1NKiI&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=34)
35. [W5_L4: Diagonalization of hermitian matrices | part 1](https://www.youtube.com/watch?v=qG1tlEa2Zn0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=35)
36. [W5_L5: Diagonalization of hermitian matrices | part 2](https://www.youtube.com/watch?v=u9uFJNrCL0E&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=36)
37. [W5_T1: Some problems to think & solve](https://www.youtube.com/watch?v=__TUd8Sq-wU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=37)
38. [W6_L1: Singular value decomposition](https://www.youtube.com/watch?v=fTErMgNIKHQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=38)
39. [W6_L2: Example of singular value decomposition (SVD)](https://www.youtube.com/watch?v=lP1UKRK4h5k&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=39)
40. [W6_L3: Positive definiteness](https://www.youtube.com/watch?v=HspdIGCore0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=40)
41. [W6_L4: Positive definite matrices](https://www.youtube.com/watch?v=N-iBr_r9jic&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=41)
42. [W6_T1: Real world application of SVD](https://www.youtube.com/watch?v=SYFGwuf-v9k&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=42)
43. [W6_T2: Geometric interpretation of SVD](https://www.youtube.com/watch?v=BHIpHagNcgw&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=43)
44. [W6_T3: Positive definite functions & matrices](https://www.youtube.com/watch?v=0vb0c-0waik&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=44)
45. [W7_L1: Principal component analysis(PCA)](https://www.youtube.com/watch?v=K5vOOARxVyU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=45)
46. [W7_L2: Principal component analysis (contd.)](https://www.youtube.com/watch?v=TDlSb1-QhhA&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=46)
47. [W7_L3: PCA as maximizing variance](https://www.youtube.com/watch?v=BHovu_rftQA&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=47)
48. [W7_L4: PCA in higher dimensions](https://www.youtube.com/watch?v=d0Ch0S1hAs8&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=48)
49. [W7_T1: Tutorial | principal component analysis](https://www.youtube.com/watch?v=XrDPtTvuYz4&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=49)
50. [W8_L1: Pillars of machine learning](https://www.youtube.com/watch?v=LYZPWUppGGc&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=50)
51. [W8_L2: Introduction to optimization](https://www.youtube.com/watch?v=-2bXHwSNwTc&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=51)
52. [W8_L3: Solving an unconstrained optimization problem | part 1](https://www.youtube.com/watch?v=CkxFp_ZPqAw&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=52)
53. [W8_L4: Solving an unconstrained optimization problem | part 2](https://www.youtube.com/watch?v=-bXrog1dbrM&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=53)
54. [W8_L5: Basic algorithm for unconstrained optimization: gradient descent](https://www.youtube.com/watch?v=3rxDd68TE3o&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=54)
55. [W8_L6: Gradient descent & taylor series](https://www.youtube.com/watch?v=X35txJMlYsc&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=55)
56. [W8_L7: Gradient descent for multivariate functions](https://www.youtube.com/watch?v=DLYQu-r7TKI&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=56)
57. [W8_L8: Taylor series in higher dimensions](https://www.youtube.com/watch?v=ohQfHMpjTlQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=57)
58. [W9_L1: Constrained optimization | part -1](https://www.youtube.com/watch?v=fFJHsQBo6NE&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=58)
59. [W9_L2: Constrained optimization | part -2](https://www.youtube.com/watch?v=q9JJc3Zj_js&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=59)
60. [W9_L3: Method of lagrange multiplier, projected gradient descent](https://www.youtube.com/watch?v=PoAPXmDlk4U&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=60)
61. [W9_L4: Introduction to convexity](https://www.youtube.com/watch?v=_qlBaMTiVXk&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=61)
62. [W9_L5: Properties of convex sets](https://www.youtube.com/watch?v=PfDvKJ2UTPg&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=62)
63. [W9_L6: Convex functions](https://www.youtube.com/watch?v=xExRalp3eY8&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=63)
64. [W9_L7: Properties of convex functions](https://www.youtube.com/watch?v=gqUwsig0geA&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=64)
65. [W9_T1: Constrained optimization, lagrange multpliers, convex sets & convex functions](https://www.youtube.com/watch?v=TQc50S0alsA&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=65)
66. [W10_L1: Properties of convex functions](https://www.youtube.com/watch?v=c9LZ0Uw9wpE&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=66)
67. [W10_L2: Applications of optimization in machine learning](https://www.youtube.com/watch?v=4jN8XhwGa48&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=67)
68. [W10_L3: Revisiting constrained optimization](https://www.youtube.com/watch?v=eM17jHQwrOY&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=68)
69. [W10_L4: Relation between primal & dual problem, karush-kuhn-tucker(KKT) conditions](https://www.youtube.com/watch?v=JiHrrqdMWAM&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=69)
70. [W10_L5: Karush-kuhn-tucker (KKT) conditions continued](https://www.youtube.com/watch?v=SItUaM_X4C4&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=70)
71. [W10_T1: Linear programming, KKT conditions, relationship between primal & dual problem](https://www.youtube.com/watch?v=M2qvsHZxlI0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=71)
72. [Probability space](https://www.youtube.com/watch?v=DpYlIh_3ttY&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=72)
73. [Conditioning](https://www.youtube.com/watch?v=mDPni6P0uAQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=73)
74. [Random variables](https://www.youtube.com/watch?v=nYC6DPjbuDM&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=74)
75. [Expectation:definition & properties](https://www.youtube.com/watch?v=J8X2DDu_ue0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=75)
76. [Multiple random variables](https://www.youtube.com/watch?v=KV5WOeqtbgs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=76)
77. [Bernoulli, binomial, poisson & geometric random variables](https://www.youtube.com/watch?v=n1rrbgWwY6I&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=77)
78. [Solved examples](https://www.youtube.com/watch?v=fdignY8Q-Ls&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=78)
79. [W11_L1: Continuous random variables](https://www.youtube.com/watch?v=K1-JKrms2SU&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=79)
80. [W11_L2: Conditional pdf](https://www.youtube.com/watch?v=cjCJIUOCwAs&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=80)
81. [W11_L3: Expectation](https://www.youtube.com/watch?v=XFYz9KyPU48&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=81)
82. [W11_L4: Multiple random variables](https://www.youtube.com/watch?v=-dyVWffZlRE&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=82)
83. [W11_L5: Independent random variables](https://www.youtube.com/watch?v=734WLw-fb5Y&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=83)
84. [W11_L6: Transformed random variables](https://www.youtube.com/watch?v=aWbs8AGk5zM&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=84)
85. [W11_L7: Uniform, exponential, normal](https://www.youtube.com/watch?v=vo3f56Gc1i8&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=85)
86. [W11_T1: Examples on continuous random variables](https://www.youtube.com/watch?v=sBT-TWoCMj4&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=86)
87. [W12_L1: Bivariate & multivariate normal](https://www.youtube.com/watch?v=yNPMeKXjISQ&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=87)
88. [W12_L2: Estimation of parameters using machine learning](https://www.youtube.com/watch?v=gbqYl44DdX0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=88)
89. [W12_L3: Gaussian mixture models & expectation maximization](https://www.youtube.com/watch?v=6Zk77RKcI2Q&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=89)
90. [W12_L4: Laws of large numbers: markov, chebyshev, hoeffding, central limit](https://www.youtube.com/watch?v=iwidPQHOe_I&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=90)
91. [W12_T1: Solved examples](https://www.youtube.com/watch?v=UExuNuc8IKo&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=91)
92. [Revisiting Constrained Optimization](https://www.youtube.com/watch?v=WbLg1drl2UY&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=92)
93. [Week 7: Tutorial](https://www.youtube.com/watch?v=tywEGBtZTu0&list=PLZ2ps__7DhBammhVmBE9f5eezTj2kDfTN&index=93)

</details>


## Books, notes and websites

- ✅ NPTEL *Introduction to Machine Learning* (Ravindran, IIT Madras) — nptel.ac.in/courses/106106139/
- Stanford CS229; Book: *ISLP* (statlearning.com, free) — the lab text
- Book: Bishop PRML; Deisenroth *Mathematics for ML* (mml-book.com)
- scikit-learn user guide; Kaggle Learn

## Practice / proof of understanding

Implement 5 algorithms from scratch in NumPy; finish 3 Kaggle tabular competitions with proper CV.

## What your IITM course sheet says

### From the PDF: DA2400

**Official description:** The students should be able to  1. Identify the type of machine learning problem suited to the task at hand, based on the problem characteristics  and  data availability.  2. Design the details of the ML problem like evaluation metrics, data preprocessing  3. Construct basic algorithms for the most common type of ML problems.  4. Implement these algorithms on the computer for a variety of settings.

**Official syllabus (trimmed):**

> 1. Foundations. (1 week) Linear algebra, probability, optimisation, data, models, learning algorithms, train and
>  test data.
>  2. Regression. (3 weeks) Squared loss minimisation, regularisation, closed form and optimisation based solutions:
>  pseudo-inverse and (mini-batch, stochastic) gradient descent, overfitting/underfitting, bias-variance decomposition,
>  Lasso regression.
>  3. Classification (3 weeks) Generative and discriminative models for classification, naive Bayes classifiers, logistic
>  regression, multiclass reductions, discriminant methods, softmax classifiers, support vector machines, k-nearest
>  neighbour, decision trees, ensemble methods: bagging, boosting, random forests.
>  4. Unsupervised Learning (3 weeks) Dimensionality reduction: principal component analysis, encoders and de-
>  coders, reconstruction error. Clustering: k-means, Lloyd’s algorithm, hierarchical clustering, inertia, Rand-index.
>  Density estimation: maximum likelihood, generative models, scoring and sampling based methods. Frequent
>  pattern
>  mining: basket analysis, bump finding, apriori algorithm.
>  5. Advanced Topics (3 weeks) Neural networks and automatic differentiation. Other paradigms of learning: rein-
>  forcement learning, self-supervised learning, semi-supervised learning, active learning, online learning. Other ML
>  tasks and evaluation metrics: ranking, structured prediction, confusion matrix, 

**Official textbooks:** 1. Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong. Mathematics for Machine Learning. Cambridge  University Press.  2. Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani and Jonathan Taylor. An Introduction to  statistical  learning: with applications in Python.  3. Christopher Bishop. Pattern Recognition and Machine Learning. Springer.

**Official references:** 1. Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong. Mathematics for Machine Learning. Cambridge  University Press.  2. Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani and Jonathan Taylor. An Introduction to  statistical  learning: with applications in Python.  3. Christopher Bishop. Pattern Recognition and Machine Learning. Springer.

### From the PDF: DA2401

**Official description:** The students should be able to  1. Construct basic algorithms for the most common type of ML problems.  2. Implement these algorithms on the computer for a variety of settings.  3. Identify failure modes of various algorithms and debug them.

**Official syllabus (trimmed):**

> 1. Foundations. (1 week) Linear equation solving, simulations and histograms, gradient descent, python tools for
>  machine learning.
>  2. Regression. (3 weeks) Model selection, analysis of bias and variance, Lasso regression.
>  3. Classification (4 weeks) Naive Bayes classifier, logistic regression, support vector machines, decision trees,
>  boost-
>  ing, random forests.
>  4. Unsupervised Learning (2 weeks) PCA for compression, clustering using Lloyd’s algorithm,
>  5. Other topics (4 weeks) Handling multiple data files, data preprocessing, handling missing data, comparing
>  performance of various algorithms, statistical tests of significance. Automatic differentiation with Pytorch. Learning
>  neural network models.

**Official textbooks:** 1. Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani and Jonathan Taylor. An Introduction to  statistical learning: with applications in Python.  2. Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong. An Introduction to statistical learning: with applica-  tions in Python. Cambridge University Press.  3. Christopher Bishop. Pattern Recognition and Machine Learning. Springer.

**Official references:** 1. Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani and Jonathan Taylor. An Introduction to  statistical learning: with applications in Python.  2. Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong. An Introduction to statistical learning: with applica-  tions in Python. Cambridge University Press.  3. Christopher Bishop. Pattern Recognition and Machine Learning. Springer.

### From the PDF: DA5400

**Official description:** The objective of this course is to introduce fundamentals of machine learning techniques and their applications in  different problems.

**Official syllabus (trimmed):**

> a. Representation Learning - PCA b. Estimation - Review of MLE, Bayesian estimation c. Clustering -
>  K-Means, Hierarchical Clustering, Spectral Clustering 2. Supervised Learning: a. Regression b. Linear
>  Regression, Ordinary Least Squares, PCR c. Non-linear regression (basis functions) d. Ridge
>  Regression, LASSO 3. Binary Classification: a. K-Nearest Neighbors b. Decision Trees, CART c.
>  Bias-Variance Dichotomy, Model Validation: Cross validation d. Bayesian Decision Theory e. Generative
>  vs Discriminative Modeling for classification i. Generative 1. Naive Bayes, Gaussian Discriminant
>  Analysis 2. Hidden Markov Model ii. Discriminative 1. Logistic Regression 4.
>  Advanced Methods for Classification a. Support Vector Machines - Kernels b. Ensemble Methods:
>  i. Bagging - Random Forest ii. Boosting - Adaboost/GBDT/XgBoost iii. Artificial Neural Networks
>  iv. Multi-Class Classification - one vs all, one vs one 5. Sequential Decision Making

**Official textbooks:** 1. Hastie, T., Tibshirani, R., Friedman, J. H., & Friedman, J. H. (2009). The elements of statistical learning: data  mining, inference, and prediction. New York: Springer.2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).  An introduction to statistical learning. New York: Springer.

**Official references:** 1. Duda, R. O. & Hart, P. E. (2006). Pattern Classification. John Wiley & Sons.2. Bishop C. M. & Nasrabadi. N. M.  (2006). Pattern Recognition and Machine Learning, New York: Springer.

### From the PDF: DA5401

**Official description:** Covers basics of python or R. Simple analytics tasks - regression, classification,clustering, associations, etc.  Emphasis will be on choice of models, evaluation of results, significance analysis, visualization and interpretation  of results.

**Official syllabus (trimmed):**

> 1.Introduction to various Python toolkits: Numpy for handling arrays and matrices; SciPy for scientific computing;
>  Matplotlib for data visualization; Pandas for data manipulation; SciKit Learn library for machine learning.2.Linear
>  models for regression: Ordinary least squares; Ridge regression (l2 regularization); Lasso (l1 regularization);
>  Elastic Net (l2-l1 regularization).3.Linear classification: Linear Discriminant Analysis (LDA); Logistics regression;
>  Linear Support Vector Machine (SVM); l2 and l1 regularized versions of these algorithms.4.Non-linear algorithms:
>  Kernel SVM, Random forrest. Neural network.5.Unsupervised learning: Dimensionality reduction technique such
>  as Principal Component Analysis (PCA), Clustering techniques such as k-Means clustering and Agglomerative
>  clustering

**Official textbooks:** 1.Sarah Guido, Andreas C. Müller, Introduction to Machine Learning with Python, O'Reilly Media, Inc.,  2016.2.Jerome H. Friedman, Robert Tibshirani, and Trevor Hastie, The Elements of Statistical Learning, Second  Edition (Springer Series in Statistics)

**Official references:** 1.Edouard Duchesnay, Tommy Löfstedt, Statistics and Machine Learning in Python, Draft by the authors, available  online.
