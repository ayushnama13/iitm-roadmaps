# CS6015 — Linear Algebra and Random Processes

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | School maths |
| Estimated effort | 12 weeks |
| Unlocks | Every ML course |

## Roadmap

1. Vector spaces, rank, eigen decomposition, SVD.
2. Probability, random variables, expectation, Markov chains and processes.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [MIT 18.06 Linear Algebra, Spring 2005](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8) (36 videos). MIT 18.06 *Linear Algebra* (Gilbert Strang, 2005): the most-loved linear algebra course ever recorded.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Mathematics - Linear Algebra](https://www.youtube.com/playlist?list=PLbMVogVj5nJQ2vsW_hmyvVfO4GYWaaPp7) (52 videos). NPTEL *Linear Algebra* (nptelhrd, IIT Madras): rigorous vector-space treatment.
- [MIT 6.041SC Probabilistic Systems Analysis and Applied Probability, Fall 2013](https://www.youtube.com/playlist?list=PLUl4u3cNGP60A3XMwZ5sep719_nh95qOe) (76 videos). MIT 6.041SC *Probabilistic Systems Analysis* (Tsitsiklis): the probability + random processes half.
- [MIT RES.6-012 Introduction to Probability, Spring 2018](https://www.youtube.com/playlist?list=PLUl4u3cNGP60hI9ATjSFgLZpbNJ7myAg6) (100+ videos). MIT RES.6-012 *Introduction to Probability* (2018): short, polished lectures of the same course.
- [Introduction to Probability Theory and Stochastic Processes](https://www.youtube.com/playlist?list=PLp6ek2hDcoNBtK-hVSSPlbBzfxXwWON4x) (93 videos). NPTEL *Introduction to Probability Theory and Stochastic Processes* (IIT Delhi): Markov chains, Poisson processes.

### ⚡ Short videos for intuition and revision

- [Essence of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (16 videos). 3Blue1Brown *Essence of linear algebra*: watch first, before Strang.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [2](https://www.youtube.com/watch?v=J7DzL2_Na80&list=PLE7DDD91010BC51F8&index=2)–[6](https://www.youtube.com/watch?v=JibVXBElKL0&list=PLE7DDD91010BC51F8&index=6) | Geometry of Ax=b, elimination, inverses, LU, permutations. Implement Gaussian elimination with partial pivoting in NumPy. |
| 2 | [7](https://www.youtube.com/watch?v=8o5Cmfpeo6g&list=PLE7DDD91010BC51F8&index=7)–[13](https://www.youtube.com/watch?v=6-wh6yvk6uc&list=PLE7DDD91010BC51F8&index=13) | Column/null space, solving Ax=0 and Ax=b, independence, basis, four subspaces, graphs. |
| 3 | [15](https://www.youtube.com/watch?v=YzZUIYRCE38&list=PLE7DDD91010BC51F8&index=15)–[18](https://www.youtube.com/watch?v=0MtwqhIwdrI&list=PLE7DDD91010BC51F8&index=18) | Orthogonality, projections, least squares, Gram-Schmidt. Fit a line with least squares by hand, then np.linalg.lstsq. |
| 4 | [19](https://www.youtube.com/watch?v=srxexLishgY&list=PLE7DDD91010BC51F8&index=19)–[21](https://www.youtube.com/watch?v=QNpj-gOXW9M&list=PLE7DDD91010BC51F8&index=21) | Determinants. |
| 5 | [22](https://www.youtube.com/watch?v=cdZnhQjJu4I&list=PLE7DDD91010BC51F8&index=22)–[25](https://www.youtube.com/watch?v=lGGDIGizcQ0&list=PLE7DDD91010BC51F8&index=25) | Eigenvalues, diagonalisation, exp(At), Markov matrices. Compute PageRank on a small graph by power iteration. |
| 6 | [27](https://www.youtube.com/watch?v=UCc9q_cAhho&list=PLE7DDD91010BC51F8&index=27)–[33](https://www.youtube.com/watch?v=0h43aV4aH7I&list=PLE7DDD91010BC51F8&index=33) | Symmetric/positive-definite matrices, SVD, linear transformations, change of basis. Compress an image with truncated SVD. |
| 7-10 | Probability (alt playlists) | Random processes half: MIT 6.041SC or RES.6-012 (alt): random variables, conditional expectation, Markov chains, Poisson processes, stationarity. |

<details>
<summary>All lectures in <i>MIT 18.06 Linear Algebra, Spring 2005</i> (36 videos)</summary>

1. [An Interview with Gilbert Strang on Teaching Linear Algebra](https://www.youtube.com/watch?v=7UJ4CFRGd-U&list=PLE7DDD91010BC51F8&index=1)
2. [1. The Geometry of Linear Equations](https://www.youtube.com/watch?v=J7DzL2_Na80&list=PLE7DDD91010BC51F8&index=2)
3. [2. Elimination with Matrices.](https://www.youtube.com/watch?v=QVKj3LADCnA&list=PLE7DDD91010BC51F8&index=3)
4. [3. Multiplication and Inverse Matrices](https://www.youtube.com/watch?v=FX4C-JpTFgY&list=PLE7DDD91010BC51F8&index=4)
5. [4. Factorization into A = LU](https://www.youtube.com/watch?v=MsIvs_6vC38&list=PLE7DDD91010BC51F8&index=5)
6. [5. Transposes, Permutations, Spaces R^n](https://www.youtube.com/watch?v=JibVXBElKL0&list=PLE7DDD91010BC51F8&index=6)
7. [6. Column Space and Nullspace](https://www.youtube.com/watch?v=8o5Cmfpeo6g&list=PLE7DDD91010BC51F8&index=7)
8. [7. Solving Ax = 0: Pivot Variables, Special Solutions](https://www.youtube.com/watch?v=VqP2tREMvt0&list=PLE7DDD91010BC51F8&index=8)
9. [8. Solving Ax = b: Row Reduced Form R](https://www.youtube.com/watch?v=9Q1q7s1jTzU&list=PLE7DDD91010BC51F8&index=9)
10. [9. Independence, Basis, and Dimension](https://www.youtube.com/watch?v=yjBerM5jWsc&list=PLE7DDD91010BC51F8&index=10)
11. [10. The Four Fundamental Subspaces](https://www.youtube.com/watch?v=nHlE7EgJFds&list=PLE7DDD91010BC51F8&index=11)
12. [11. Matrix Spaces; Rank 1; Small World Graphs](https://www.youtube.com/watch?v=2IdtqGM6KWU&list=PLE7DDD91010BC51F8&index=12)
13. [12. Graphs, Networks, Incidence Matrices](https://www.youtube.com/watch?v=6-wh6yvk6uc&list=PLE7DDD91010BC51F8&index=13)
14. [13. Quiz 1 Review](https://www.youtube.com/watch?v=l88D4r74gtM&list=PLE7DDD91010BC51F8&index=14)
15. [14. Orthogonal Vectors and Subspaces](https://www.youtube.com/watch?v=YzZUIYRCE38&list=PLE7DDD91010BC51F8&index=15)
16. [15. Projections onto Subspaces](https://www.youtube.com/watch?v=Y_Ac6KiQ1t0&list=PLE7DDD91010BC51F8&index=16)
17. [16. Projection Matrices and Least Squares](https://www.youtube.com/watch?v=osh80YCg_GM&list=PLE7DDD91010BC51F8&index=17)
18. [17. Orthogonal Matrices and Gram-Schmidt](https://www.youtube.com/watch?v=0MtwqhIwdrI&list=PLE7DDD91010BC51F8&index=18)
19. [18. Properties of Determinants](https://www.youtube.com/watch?v=srxexLishgY&list=PLE7DDD91010BC51F8&index=19)
20. [19. Determinant Formulas and Cofactors](https://www.youtube.com/watch?v=23LLB9mNJvc&list=PLE7DDD91010BC51F8&index=20)
21. [20. Cramer's Rule, Inverse Matrix, and Volume](https://www.youtube.com/watch?v=QNpj-gOXW9M&list=PLE7DDD91010BC51F8&index=21)
22. [21. Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=cdZnhQjJu4I&list=PLE7DDD91010BC51F8&index=22)
23. [22. Diagonalization and Powers of A](https://www.youtube.com/watch?v=13r9QY6cmjc&list=PLE7DDD91010BC51F8&index=23)
24. [23. Differential Equations and exp(At)](https://www.youtube.com/watch?v=IZqwi0wJovM&list=PLE7DDD91010BC51F8&index=24)
25. [24. Markov Matrices; Fourier Series](https://www.youtube.com/watch?v=lGGDIGizcQ0&list=PLE7DDD91010BC51F8&index=25)
26. [24b. Quiz 2 Review](https://www.youtube.com/watch?v=QuZL5IKpO_U&list=PLE7DDD91010BC51F8&index=26)
27. [25. Symmetric Matrices and Positive Definiteness](https://www.youtube.com/watch?v=UCc9q_cAhho&list=PLE7DDD91010BC51F8&index=27)
28. [26. Complex Matrices; Fast Fourier Transform](https://www.youtube.com/watch?v=M0Sa8fLOajA&list=PLE7DDD91010BC51F8&index=28)
29. [27. Positive Definite Matrices and Minima](https://www.youtube.com/watch?v=vF7eyJ2g3kU&list=PLE7DDD91010BC51F8&index=29)
30. [28. Similar Matrices and Jordan Form](https://www.youtube.com/watch?v=TSdXJw83kyA&list=PLE7DDD91010BC51F8&index=30)
31. [29. Singular Value Decomposition](https://www.youtube.com/watch?v=TX_vooSnhm8&list=PLE7DDD91010BC51F8&index=31)
32. [30. Linear Transformations and Their Matrices](https://www.youtube.com/watch?v=Ts3o2I8_Mxc&list=PLE7DDD91010BC51F8&index=32)
33. [31. Change of Basis; Image Compression](https://www.youtube.com/watch?v=0h43aV4aH7I&list=PLE7DDD91010BC51F8&index=33)
34. [32. Quiz 3 Review](https://www.youtube.com/watch?v=HgC1l_6ySkc&list=PLE7DDD91010BC51F8&index=34)
35. [33. Left and Right Inverses; Pseudoinverse](https://www.youtube.com/watch?v=Go2aLo7ZOlU&list=PLE7DDD91010BC51F8&index=35)
36. [34. Final Course Review](https://www.youtube.com/watch?v=RWvi4Vx4CDc&list=PLE7DDD91010BC51F8&index=36)

</details>


## Books, notes and websites

- MIT 18.06 (Gilbert Strang) — OCW; 3Blue1Brown *Essence of Linear Algebra*
- ✅ NPTEL *Linear Algebra* (K.C. Sivakumar, IIT Madras) — nptel.ac.in/courses/111106051
- Harvard Stat 110 (Joe Blitzstein) — YouTube
- ✅ NPTEL *Probability and Statistics* (Somesh Kumar, IIT Kharagpur) — nptel.ac.in/courses/111105041

## Practice / proof of understanding

Implement PCA from SVD by hand; simulate a Markov chain and compare its stationary distribution to the eigenvector.

## Note

Do this before any ML course. It is a math base, not a CS course.

## What your IITM course sheet says

### From the PDF: CS6015

**Official description:** The course is intended to provide an extensive introduction to Linear Algebra and Probability theory relevant to  Computer Science with applications to real world problems. The course is divided into two themes: Linear  Algebra and Probability and Random Processes. The objective is to give the course a perspective from the point  of view of applications, especially in machine learning, data mining and pattern recognition.

**Official syllabus (trimmed):**

> Linear Algebra :
> Basic Topics: Fields, Vector Spaces, Basis, Subspaces. (1 week)
> Matrices: Matrices and Linear Transformations, Rank, Determinant (as a measure of volume of the space
> enclosed by the rows/columns of a matrix), trace of a matrix. Solving simultaneous equations using matrices:
> Gaussian Elimination. Overdetermined and underdetermine systems, Inverse, pseudo inverse. Condition
> number of a matrix, Eigenvalues, Eigenvectors, singular values, singular vectors. Computation of Eigenvalues and
> eigen vectors (physical significance of eigen vectors and singular vectors – e.g image as a matrix). Eigen vectors
> of a symmetric positive definite matrix and its meaning. Diagonalization of a matrix and applications. Derivatives
> of scalars w.r.t a vector. Jacobian (4 weeks)
> Short Exam on LA, Programming Assignment on Eigen/Singular values and vectors – e.g. image analysis and
> reconstruction using eigen decomposition.
> Orthogonality : Inner Product, Orthogonality, Gram-Schmidt Orthogonalization, Vector and Matrix Norms -
> Applications to optimization problems and graph theory, machine learning. (1 week)
> Probability and Random Processes:
> Basic Topics (recap) – Sample points and Sample spaces: Events, algebra of events, partitions, Bayes theorem,
> probability axioms, joint and conditional probability. (1 week)
> Short Exam and written assignment on basics.
> Introduction to random variables 

**Official textbooks:** 1. Linear Algebra and Its Applications - Gilbert Strang- Fourth Edition- Cengage Learning, 2006.  2. Probability, Random Variables and Stochastic Processes, Papoulis and Unnikrishnan, Fourth Edition, 2002,  available in paperback.  3. Probability and Random Processes – an introduction for application scientists and engineers, W B Davenport,  1970, McGraw Hill.

**Official references:** 1. Probability and Statistics with Reliability, Queuing, and Computer Science Applications - Kishore S Trivedi, PHI.  2. Linear Algebra (second edition )- Kenneth Hoffman and Ray Kunze, Prentice Hall India, 2013.  3. Linear Algebra (Second Edition) – Cheney and Kincaid, Jones and Bartlett learning, 2014 (Indian Edition  available)
