# DA1001 — Applied Linear Algebra

| | |
|---|---|
| Tier | A |
| Phase (order) | 1 |
| Do this first | School maths |
| Estimated effort | 12 weeks, ~6 h/week |
| Unlocks | DA2400, DA3409, DA1002, DA6300 |

## Roadmap

1. Vectors, matrices, Gaussian elimination.
2. Vector spaces, basis, dimension, four fundamental subspaces.
3. Eigenvalues, diagonalisation, symmetric/PSD matrices, Jordan form, SVD.
4. Applications: image processing, networks.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Applied Linear Algebra](https://www.youtube.com/playlist?list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt) (48 videos). NPTEL-NOC IITM *Applied Linear Algebra*: IIT Madras, application-oriented, matches DA1001.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [MIT 18.06SC Linear Algebra, Fall 2011](https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C) (74 videos). MIT 18.06SC *Linear Algebra* (Strang, Fall 2011): lectures + recitations + problem sets.
- [Mathematics for Machine Learning - Linear Algebra](https://www.youtube.com/playlist?list=PLiiljHvN6z1_o1ztXTKWPrShrMrBLo5P3) (37 videos). Imperial College *Mathematics for ML: Linear Algebra* (official): short, ML-oriented.

### ⚡ Short videos for intuition and revision

- [Essence of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (16 videos). 3Blue1Brown *Essence of linear algebra*: watch all 16 first, for geometry.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=Ymn8rzTaEfk&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=1)–[6](https://www.youtube.com/watch?v=r-NCO2TE4Qg&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=6) | Vector spaces, span, linear independence, basis, dimension, Gaussian elimination. Pair with 3Blue1Brown Essence of Linear Algebra (short videos). |
| 2 | [7](https://www.youtube.com/watch?v=uyHo3eJNpSo&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=7)–[11](https://www.youtube.com/watch?v=tAHPESttoaU&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=11) | Linear maps, matrices, null space, range, rank-nullity, invertibility. |
| 3 | [12](https://www.youtube.com/watch?v=bERijv8R7gU&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=12)–[18](https://www.youtube.com/watch?v=MU2y_7oEeYQ&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=18) | Solving Ax=b, row operations, quotient spaces, row rank, determinants, change of basis. Implement row reduction to RREF in NumPy. |
| 4 | [19](https://www.youtube.com/watch?v=zesZj_TkjF4&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=19)–[23](https://www.youtube.com/watch?v=7GOVm99SO3A&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=23) | Polynomials, invariant subspaces, eigenvalues/eigenvectors, diagonalisation, upper-triangular form. |
| 5 | [24](https://www.youtube.com/watch?v=abDdEU7Jai0&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=24)–[27](https://www.youtube.com/watch?v=g_Ssc4NplFI&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=27) | Applications: linear dynamical systems, DFT, counting paths in graphs, PageRank. Implement PageRank by power iteration. |
| 6 | [28](https://www.youtube.com/watch?v=flRmVRbvO1o&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=28)–[34](https://www.youtube.com/watch?v=Z8cNLPWU5ck&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=34) | Inner products, Gram-Schmidt, orthogonal complements and projections, least squares, MMSE estimation. Fit a polynomial by least squares. |
| 7 | [35](https://www.youtube.com/watch?v=ATtAl3cJyPo&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=35)–[42](https://www.youtube.com/watch?v=bBaQz34Dj0A&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=42) | Adjoints, self-adjoint and normal operators, spectral theorems, positive operators. |
| 8 | [43](https://www.youtube.com/watch?v=ZSZPx8GmfDQ&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=43)–[48](https://www.youtube.com/watch?v=sFd-c6Zlr8c&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=48) | Quadratic forms, matrix norms, isometries, SVD, polar decomposition. Compress an image with truncated SVD. |

<details>
<summary>All lectures in <i>Applied Linear Algebra</i> (48 videos)</summary>

1. [Applied Linear Algebra _ Course Introduction](https://www.youtube.com/watch?v=Ymn8rzTaEfk&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=1)
2. [Vector Spaces: Introduction](https://www.youtube.com/watch?v=mSDU6PTFI3o&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=2)
3. [Linear Combinations and Span](https://www.youtube.com/watch?v=_TUbqEvdtPA&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=3)
4. [Subspaces, Linear Dependence and Independence](https://www.youtube.com/watch?v=zOoAUyZdgxA&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=4)
5. [Basis and Dimension](https://www.youtube.com/watch?v=Yiort0yZxmQ&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=5)
6. [Sums, Direct Sums and Gaussian Elimination](https://www.youtube.com/watch?v=r-NCO2TE4Qg&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=6)
7. [Linear Maps and Matrices](https://www.youtube.com/watch?v=uyHo3eJNpSo&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=7)
8. [Null space, Range, Fundamental theorem of linear maps](https://www.youtube.com/watch?v=iVTjMOFD3pc&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=8)
9. [Column space, null space and rank of a matrix](https://www.youtube.com/watch?v=F40D7DKNuo4&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=9)
10. [Algebraic operations on linear maps](https://www.youtube.com/watch?v=gRUgQgeZ9Eo&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=10)
11. [Invertible maps, Isomorphism, Operators](https://www.youtube.com/watch?v=tAHPESttoaU&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=11)
12. [Solving Linear Equations](https://www.youtube.com/watch?v=bERijv8R7gU&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=12)
13. [Elementary Row Operations](https://www.youtube.com/watch?v=QnWp4d0P3jc&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=13)
14. [Translates of a subspace, Quotient Spaces](https://www.youtube.com/watch?v=SK310vXubrU&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=14)
15. [Row space and rank of a matrix](https://www.youtube.com/watch?v=UhpWhH3EV3s&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=15)
16. [Determinants](https://www.youtube.com/watch?v=tTiDxsTjwkU&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=16)
17. [Coordinates and linear maps under a change of basis](https://www.youtube.com/watch?v=Jnh3fqsmZ9k&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=17)
18. [Simplifying matrices of linear maps by choice of basis](https://www.youtube.com/watch?v=MU2y_7oEeYQ&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=18)
19. [Polynomials and Roots](https://www.youtube.com/watch?v=zesZj_TkjF4&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=19)
20. [Invariant subspaces, Eigenvalues, Eigenvectors](https://www.youtube.com/watch?v=1WP7eam6S7Q&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=20)
21. [More on Eigenvalues, Eigenvectors, Diagonalization](https://www.youtube.com/watch?v=ZYhdrGB5iiw&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=21)
22. [Eigenvalues, Eigenvectors and Upper Triangularization](https://www.youtube.com/watch?v=dwe2EuL8VBk&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=22)
23. [Properties of Eigenvalues](https://www.youtube.com/watch?v=7GOVm99SO3A&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=23)
24. [Linear state space equations and system stability](https://www.youtube.com/watch?v=abDdEU7Jai0&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=24)
25. [Discrete-time Linear Systems and Discrete Fourier Transforms](https://www.youtube.com/watch?v=kfd71z-5JPQ&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=25)
26. [Sequences and counting paths in graphs](https://www.youtube.com/watch?v=vG2tGKhO-Lk&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=26)
27. [PageRank Algorithm](https://www.youtube.com/watch?v=g_Ssc4NplFI&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=27)
28. [Dot product and length in Cn, Inner product and norm in V over F](https://www.youtube.com/watch?v=flRmVRbvO1o&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=28)
29. [Orthonormal basis and Gram-Schmidt orthogonalisation](https://www.youtube.com/watch?v=lwkXgLDTs-4&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=29)
30. [Linear Functionals, Orthogonal Complements](https://www.youtube.com/watch?v=FY3IdwEbTRY&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=30)
31. [Orthogonal Projection](https://www.youtube.com/watch?v=IIa3A-NWSdU&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=31)
32. [Projection and distance from a subspace](https://www.youtube.com/watch?v=qR-YKak4LO0&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=32)
33. [Linear equations, Least squares solutions and Linear regression](https://www.youtube.com/watch?v=9RK9NIJMoWo&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=33)
34. [Minimum Mean Squared Error Estimation](https://www.youtube.com/watch?v=Z8cNLPWU5ck&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=34)
35. [Adjoint of a linear map](https://www.youtube.com/watch?v=ATtAl3cJyPo&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=35)
36. [Properties of Adjoint of a Linear Map](https://www.youtube.com/watch?v=u0l9hZ1Iv7c&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=36)
37. [Adjoint of an Operator and Operator-Adjoint Product](https://www.youtube.com/watch?v=hyEQRB5L_s0&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=37)
38. [Self-adjoint Operator](https://www.youtube.com/watch?v=7xDBO8yCPxg&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=38)
39. [Normal Operators](https://www.youtube.com/watch?v=1BuEmk3gFjs&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=39)
40. [Complex Spectral Theorem](https://www.youtube.com/watch?v=z1TrFh_KGYw&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=40)
41. [Real Spectral Theorem](https://www.youtube.com/watch?v=SUh_PDwBvss&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=41)
42. [Positive Operators](https://www.youtube.com/watch?v=bBaQz34Dj0A&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=42)
43. [Quadratic Forms, Matrix Norms and Optimization](https://www.youtube.com/watch?v=ZSZPx8GmfDQ&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=43)
44. [Isometries](https://www.youtube.com/watch?v=3m_zfC7BRaI&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=44)
45. [Classification of Operators](https://www.youtube.com/watch?v=EdGOWan4Wh4&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=45)
46. [Singular Values and Vectors of a Linear Map](https://www.youtube.com/watch?v=AYUhJyGcmak&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=46)
47. [Singular Value Decomposition](https://www.youtube.com/watch?v=aNBH1Ls4LQ8&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=47)
48. [Polar decomposition and some applications of SVD](https://www.youtube.com/watch?v=sFd-c6Zlr8c&list=PLyqSpQzTE6M912cneV79Cqsj88E3VBfxt&index=48)

</details>


## Books, notes and websites

- MIT 18.06 (Strang) — OCW; Strang's book (the course text)
- 3Blue1Brown *Essence of Linear Algebra*
- ✅ NPTEL *Linear Algebra* (K.C. Sivakumar, IIT Madras) — nptel.ac.in/courses/111106051
- Book: *Mathematics for Machine Learning* — mml-book.com (free)

## Practice / proof of understanding

Do the 18.06 problem sets; implement SVD-based image compression in NumPy.

## What your IITM course sheet says

### From the PDF: DA1001

**Official description:** Real-world systems or scenarios throw at us lot of information which needs to be understood and processed. This  analysis becomes easier when the available information is organised in a certain structure, which makes it easier  to understand the underlying information in a better way. This course on Linear Algebra provides us with  mathematical abstractions and structures to organize, analyze and interpret information and is one of the  fundamental tools in any engineering studies. The course will start with an introduction to vector spaces and  subspaces, linear functions, systems of linear equations, matrices as linear transformations, matrix algebra, with  engineering applications.

**Official syllabus (trimmed):**

> What is Linear Algebra: Vectors, dot products, linear combinations, linear functions, Matrices.
>  Systems of Linear Equations: Gaussian elimination, Elementary row operations
>  Vector spaces and subspaces: Spaces of vectors, span, basis, linear independence, dimension, rank nullity
>  theorem, four fundamental subspaces, change of basis, complete solution to a system of linear equations,
>  orthonormal bases.
>  Matrices: Eigenvalues and Eigenvectors, Diagonalisation of matrices, Symmetric matrices, Positive definite
>  matrices, generalized Eigenvectors, Jordan form, Singular value decomposition.
>  Linear transformation, matrix representation of a linear transformation.
>  Applications: Image processing, Optimisation, Networks,

**Official textbooks:** S. Lang, Linear Algebra, 3rd edition, Springer, 2004.  Gilbert Strang, Introduction to Linear Algebra, 3rd Edition.

**Official references:** K. Janich. Linear Algebra. Springer. 1994.  H. Anton. C. Rorres. Elementary Linear Algebra: Applications, Wiley; 11th edition, 2013
