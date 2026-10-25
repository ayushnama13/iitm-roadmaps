# DA3409+DA3410 — Deep Learning (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 4 |
| Do this first | DA2400, DA1000, DA1001 |
| Estimated effort | 12-14 weeks |
| Unlocks | DA3451, DA3452, DA6401, DA6800 |

## Roadmap

1. MLP and backprop; optimisers.
2. CNNs; RNNs; transformers.
3. PyTorch lab: reproduce each model.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Deep Learning](https://www.youtube.com/playlist?list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT) (100+ videos). NPTEL *Deep Learning* (Mitesh Khapra, IIT Madras).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Deep Learning](https://www.youtube.com/playlist?list=PLZ2ps__7DhBZVxMrSkTIcG6zZBDKUXCnM) (68 videos). IIT Madras BS *Deep Learning*: newer recording of the IITM course.
- [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) (10 videos). Karpathy *Neural Networks: Zero to Hero*: build backprop, MLPs and GPT in code. Best for the lab (DA3410).
- [MIT 6.S191: Introduction to Deep Learning](https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI) (90 videos). MIT 6.S191 *Introduction to Deep Learning* (official, updated yearly): fast survey.

### ⚡ Short videos for intuition and revision

- [Neural networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (10 videos). 3Blue1Brown *Neural networks*: watch first.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=aPfkYu_qiF4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=1)–[18](https://www.youtube.com/watch?v=CJr4Dst0uZE&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=18) | History, MP neuron, perceptron, convergence proof. Code a perceptron. |
| 2 | [19](https://www.youtube.com/watch?v=X4RmokyD3U8&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=19)–[34](https://www.youtube.com/watch?v=sbvv-uQmwVY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=34) | Sigmoid neurons, gradient descent, feedforward nets, backpropagation. Write backprop for an MLP in NumPy and check with numerical gradients. |
| 3 | [35](https://www.youtube.com/watch?v=joKs2EJ9Z8w&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=35)–[43](https://www.youtube.com/watch?v=-0ZMU-gnm2g&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=43) | Optimisers: momentum, NAG, SGD/mini-batch, learning-rate schedules, Adagrad/RMSProp/Adam. Compare them on MNIST. |
| 4 | [44](https://www.youtube.com/watch?v=BTzz3BuYuM8&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=44)–[51](https://www.youtube.com/watch?v=xV1Q3go0S1Y&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=51), [33](https://www.youtube.com/watch?v=mvljKZtGTj4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=33) | Linear algebra recap, PCA, SVD. |
| 5 | [52](https://www.youtube.com/watch?v=wPz3MPl5jvY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=52)–[57](https://www.youtube.com/watch?v=BW7P1fvnAWk&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=57) | Autoencoders (denoising, sparse, contractive). Train one in PyTorch. |
| 6 | [58](https://www.youtube.com/watch?v=Y0m136XU65o&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=58)–[69](https://www.youtube.com/watch?v=qfsacbIe9AI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=69) | Bias-variance, regularisation, augmentation, early stopping, dropout. |
| 7 | [70](https://www.youtube.com/watch?v=P2x8qi5xT-8&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=70)–[74](https://www.youtube.com/watch?v=1XMjfhEFbFA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=74) | Pre-training, activations, initialisation, batch norm. |
| 8 | [75](https://www.youtube.com/watch?v=M2T36PlRv1U&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=75)–[86](https://www.youtube.com/watch?v=MBcnPueElDU&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=86) | Word representations: word2vec, GloVe. |
| 9 | [87](https://www.youtube.com/watch?v=yw8xwS15Pf4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=87)–[100](https://www.youtube.com/watch?v=orTNf_R5odY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=100) | CNNs and visualising them. Train a CNN on CIFAR-10. |
| 10-12 | rest of playlist (after 100) | RNNs, LSTMs, seq2seq, attention, transformers: open the full playlist. Then Karpathy's GPT video (alt). |

<details>
<summary>All lectures in <i>Deep Learning</i> (100+ videos)</summary>

1. [Deep Learning - Course Introduction](https://www.youtube.com/watch?v=aPfkYu_qiF4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=1)
2. [Deep Learning(CS7015): Lec 1.1 Biological Neuron](https://www.youtube.com/watch?v=4TC5s_xNKSs&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=2)
3. [Deep Learning(CS7015): Lec 1.2 From Spring to Winter of AI](https://www.youtube.com/watch?v=WpR8eOLUo9Q&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=3)
4. [Deep Learning(CS7015): Lec 1.3 The Deep Revival](https://www.youtube.com/watch?v=DpK_i6iA0i0&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=4)
5. [Deep Learning(CS7015): Lec 1.4 From Cats to Convolutional Neural Networks](https://www.youtube.com/watch?v=6USgwLa-7ks&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=5)
6. [Deep Learning(CS7015): Lec 1.5 Faster, higher, stronger](https://www.youtube.com/watch?v=0DKOUFrP7xI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=6)
7. [Deep Learning(CS7015): Lec 1.6 The Curious Case of Sequences](https://www.youtube.com/watch?v=H_ptjlq8pH0&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=7)
8. [Deep Learning(CS7015): Lec 1.7 Beating humans at their own games (literally)](https://www.youtube.com/watch?v=_z27qjHjqiM&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=8)
9. [Deep Learning(CS7015): Lec 1.8 The Madness (2013-)](https://www.youtube.com/watch?v=-7l-Pl_pwu4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=9)
10. [Deep Learning(CS7015): Lec 1.9 (Need for) Sanity](https://www.youtube.com/watch?v=rSY5YLLcPs8&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=10)
11. [Deep Learning(CS7015): Lec 2.1 Motivation from Biological Neurons](https://www.youtube.com/watch?v=qQmMp8fL82w&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=11)
12. [Deep Learning(CS7015): Lec 2.2 McCulloch Pitts Neuron, Thresholding Logic](https://www.youtube.com/watch?v=6XhSJbfT1pk&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=12)
13. [Deep Learning(CS7015): Lec 2.3 Perceptrons](https://www.youtube.com/watch?v=XKnBn1XZpQI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=13)
14. [Deep Learning(CS7015): Lec 2.4 Error and Error Surfaces](https://www.youtube.com/watch?v=f8tod7wt2Vw&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=14)
15. [Deep Learning(CS7015): Lec 2.5 Perceptron Learning Algorithm](https://www.youtube.com/watch?v=VRcixOuG-TU&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=15)
16. [Deep Learning(CS7015): Lec 2.6 Proof of Convergence of Perceptron Learning Algorithm](https://www.youtube.com/watch?v=vAOI9kTDVoo&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=16)
17. [Deep Learning(CS7015): Lec 2.7 Linearly Separable Boolean Functions](https://www.youtube.com/watch?v=AjUgxQNZhck&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=17)
18. [Deep Learning(CS7015): Lec 2.8 Representation Power of a Network of Perceptrons](https://www.youtube.com/watch?v=CJr4Dst0uZE&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=18)
19. [Deep Learning(CS7015): Lec 3.1 Sigmoid Neuron](https://www.youtube.com/watch?v=X4RmokyD3U8&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=19)
20. [Deep Learning(CS7015): Lec 3.2 A typical Supervised Machine Learning Setup](https://www.youtube.com/watch?v=uDcU3ZzH7hs&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=20)
21. [Deep Learning(CS7015): Lec 3.3 Learning Parameters: (Infeasible) guess work](https://www.youtube.com/watch?v=HnaBcIL2shc&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=21)
22. [Deep Learning(CS7015): Lec 3.4 Learning Parameters: Gradient Descent](https://www.youtube.com/watch?v=giZD8yzXEZ4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=22)
23. [Deep Learning(CS7015): Lec 3.5 Representation Power of Multilayer Network of Sigmoid Neurons](https://www.youtube.com/watch?v=d1K-6b5guh0&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=23)
24. [Deep Learning(CS7015): Lec 4.1 Feedforward Neural Networks (a.k.a multilayered network of neurons)](https://www.youtube.com/watch?v=AASR9rOzhhA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=24)
25. [Deep Learning(CS7015): Lec 4.2 Learning Paramters of Feedforward Neural Networks (Intuition)](https://www.youtube.com/watch?v=4gm4sXPndUY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=25)
26. [Deep Learning(CS7015): Lec 4.3 Output functions and Loss functions](https://www.youtube.com/watch?v=hMkRDNzH9vs&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=26)
27. [Deep Learning(CS7015): Lec 4.4 Backpropagation (Intuition)](https://www.youtube.com/watch?v=DSqgn2lAN1M&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=27)
28. [Deep Learning(CS7015): Lec 4.5 Backpropagation: Computing Gradients w.r.t. the Output Units](https://www.youtube.com/watch?v=JSfRBOWp3Es&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=28)
29. [Deep Learning(CS7015): Lec 4.6 Backpropagation: Computing Gradients w.r.t. Hidden Units](https://www.youtube.com/watch?v=MDVVUY-sftQ&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=29)
30. [Deep Learning(CS7015): Lec 4.7 Backpropagation: Computing Gradients w.r.t. Parameters](https://www.youtube.com/watch?v=DirgOcmERwA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=30)
31. [Deep Learning(CS7015): Lec 4.8 Backpropagation: Pseudo code](https://www.youtube.com/watch?v=Qdh4NEkQRuo&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=31)
32. [Deep Learning(CS7015): Lec 4.9 Derivative of the activation function](https://www.youtube.com/watch?v=0OHLbVEOq04&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=32)
33. [Deep Learning(CS7015): Lec 6.6 PCA : Interpretation 3](https://www.youtube.com/watch?v=mvljKZtGTj4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=33)
34. [Deep Learning(CS7015): Lec 4.10 Information content, Entropy & cross entropy](https://www.youtube.com/watch?v=sbvv-uQmwVY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=34)
35. [Deep Learning(CS7015): Lec 5.1 & Lec 5.2 Recap: Learning Parameters: Guess Work, Gradient Descent](https://www.youtube.com/watch?v=joKs2EJ9Z8w&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=35)
36. [Deep Learning(CS7015): Lec 5.3 Contours Maps](https://www.youtube.com/watch?v=pHarJN7Wo0M&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=36)
37. [Deep Learning(CS7015): Lec 5.4 Momentum based Gradient Descent](https://www.youtube.com/watch?v=ewN0vFYFJ7A&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=37)
38. [Deep Learning(CS7015): Lec 5.5 Nesterov Accelerated Gradient Descent](https://www.youtube.com/watch?v=sV9aiEsXanE&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=38)
39. [Deep Learning(CS7015): Lec 5.6 Stochastic And Mini-Batch Gradient Descent](https://www.youtube.com/watch?v=Vc-jG_LdOLw&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=39)
40. [Deep Learning(CS7015): Lec 5.7 Tips for Adjusting Learning Rate and Momentum](https://www.youtube.com/watch?v=t5Q2z-MM1X4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=40)
41. [Deep Learning(CS7015): Lec 5.8 Line Search](https://www.youtube.com/watch?v=CxgYyBut6i0&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=41)
42. [Deep Learning(CS7015): Lec 5.9 Gradient Descent with Adaptive Learning Rate](https://www.youtube.com/watch?v=FKCV76N9Ys0&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=42)
43. [Deep Learning(CS7015): Lec 5.9 (Part-2) Bias Correction in Adam](https://www.youtube.com/watch?v=-0ZMU-gnm2g&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=43)
44. [Deep Learning(CS7015): Lec 6.1 Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=BTzz3BuYuM8&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=44)
45. [Deep Learning(CS7015): Lec 6.2 Linear Algebra : Basic Definitions](https://www.youtube.com/watch?v=FsWX2c7Q6Qg&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=45)
46. [Deep Learning(CS7015): Lec 6.3 Eigenvalue Decompositon](https://www.youtube.com/watch?v=mdZVysybPrk&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=46)
47. [Deep Learning(CS7015): Lec 6.4 Principal Component Analysis and its Interpretations](https://www.youtube.com/watch?v=5eEPs8XS5AQ&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=47)
48. [Deep Learning(CS7015): Lec 6.5 PCA : Interpretation 2](https://www.youtube.com/watch?v=_EwqeZcZ9KY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=48)
49. [Deep Learning(CS7015): Lec 6.6 (Part-2) PCA : Interpretation 3 (Contd.)](https://www.youtube.com/watch?v=tcR5I2pPk3o&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=49)
50. [Deep Learning(CS7015): Lec 6.7 PCA : Practical Example](https://www.youtube.com/watch?v=wHHxkWcqokY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=50)
51. [Deep Learning(CS7015): Lec 6.8 Singular Value Decomposition](https://www.youtube.com/watch?v=xV1Q3go0S1Y&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=51)
52. [Deep Learning(CS7015): Lec 7.1 Introduction to Autoncoders](https://www.youtube.com/watch?v=wPz3MPl5jvY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=52)
53. [Deep Learning(CS7015): Lec 7.2 Link between PCA and Autoencoders](https://www.youtube.com/watch?v=0ZQxPIwuA4o&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=53)
54. [Deep Learning(CS7015): Lec 7.3 Regularization in autoencoders (Motivation)](https://www.youtube.com/watch?v=mNUAt7umSiw&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=54)
55. [Deep Learning(CS7015): Lec 7.4 Denoising Autoencoders](https://www.youtube.com/watch?v=0n2x_D-ZmmU&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=55)
56. [Deep Learning(CS7015): Lec 7.5 Sparse Autoencoders](https://www.youtube.com/watch?v=REzrCEDMQws&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=56)
57. [Deep Learning(CS7015): Lec 7.6 Contractive Autoencoders](https://www.youtube.com/watch?v=BW7P1fvnAWk&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=57)
58. [Deep Learning(CS7015): Lec 8.1 Bias and Variance](https://www.youtube.com/watch?v=Y0m136XU65o&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=58)
59. [Deep Learning(CS7015): Lec 8.2 Train error vs Test error](https://www.youtube.com/watch?v=gyGMaNUaeic&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=59)
60. [Deep Learning(CS7015): Lec 8.2 (Part-2) Train error vs Test error (Recap)](https://www.youtube.com/watch?v=aVAs2YwiDoA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=60)
61. [Deep Learning(CS7015): Lec 8.3 True error and Model complexity](https://www.youtube.com/watch?v=y_tQBokE94s&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=61)
62. [Deep Learning(CS7015): Lec 8.4 L2 regularization](https://www.youtube.com/watch?v=lg4OLAjxRcQ&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=62)
63. [Deep Learning(CS7015): Lec 8.5 Dataset augmentation](https://www.youtube.com/watch?v=KHMHOieuJuw&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=63)
64. [Deep Learning(CS7015): Lec 8.6 Parameter sharing and tying](https://www.youtube.com/watch?v=EZ4X5rFzLFE&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=64)
65. [Deep Learning(CS7015): Lec 8.7 Adding Noise to the inputs](https://www.youtube.com/watch?v=agGUR06jM_g&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=65)
66. [Deep Learning(CS7015): Lec 8.8 Adding Noise to the outputs](https://www.youtube.com/watch?v=TtU9GhLeOk4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=66)
67. [Deep Learning(CS7015): Lec 8.9 Early stopping](https://www.youtube.com/watch?v=zm5cqvfKO-o&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=67)
68. [Deep Learning(CS7015): Lec 8.10 Ensemble Methods](https://www.youtube.com/watch?v=qlNDzNjR3eA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=68)
69. [Deep Learning(CS7015): Lec 8.11 Dropout](https://www.youtube.com/watch?v=qfsacbIe9AI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=69)
70. [Deep Learning(CS7015): Lec 9.1 A quick recap of training deep neural networks](https://www.youtube.com/watch?v=P2x8qi5xT-8&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=70)
71. [Deep Learning(CS7015): Lec 9.2 Unsupervised pre-training](https://www.youtube.com/watch?v=_GRvjpJVr5A&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=71)
72. [Deep Learning(CS7015): Lec 9.3 Better activation functions](https://www.youtube.com/watch?v=HxKaLyyGq50&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=72)
73. [Deep Learning(CS7015): Lec 9.4 Better initialization strategies](https://www.youtube.com/watch?v=1pgahpCZeF0&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=73)
74. [Deep Learning(CS7015): Lec 9.5 Batch Normalization](https://www.youtube.com/watch?v=1XMjfhEFbFA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=74)
75. [Deep Learning(CS7015): Lec 10.1 One-hot representations of words](https://www.youtube.com/watch?v=M2T36PlRv1U&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=75)
76. [Deep Learning(CS7015): Lec 10.2 Distributed Representations of words](https://www.youtube.com/watch?v=74clhgHhR2M&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=76)
77. [Deep Learning(CS7015): Lec 10.3 SVD for learning word representations](https://www.youtube.com/watch?v=SSpSk1Io52w&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=77)
78. [Deep Learning(CS7015): Lec 10.3 (Part-2) SVD for learning word representations (Contd.)](https://www.youtube.com/watch?v=05L1tSvzWHs&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=78)
79. [Deep Learning(CS7015): Lec 10.4 Continuous bag of words model](https://www.youtube.com/watch?v=yBmtXtVya9A&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=79)
80. [Deep Learning(CS7015): Lec 10.5 Skip-gram model](https://www.youtube.com/watch?v=XO2GHDm-ZoI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=80)
81. [Deep Learning(CS7015): Lec 10.5 (Part-2) Skip-gram model (Contd.)](https://www.youtube.com/watch?v=3F6KInYCJxI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=81)
82. [Deep Learning(CS7015): Lec 10.6 Contrastive estimation](https://www.youtube.com/watch?v=XZUGn36eAgA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=82)
83. [Deep Learning(CS7015): Lec 10.7 Hierarchical softmax](https://www.youtube.com/watch?v=ioe1eeEWU0I&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=83)
84. [Deep Learning(CS7015): Lec 10.8 GloVe representations](https://www.youtube.com/watch?v=zA0U8C_q04M&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=84)
85. [Deep Learning(CS7015): Lec 10.9 Evaluating word representations](https://www.youtube.com/watch?v=b0M0AzjpPqc&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=85)
86. [Deep Learning(CS7015): Lec 10.10 Relation between SVD and Word2Vec](https://www.youtube.com/watch?v=MBcnPueElDU&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=86)
87. [Deep Learning(CS7015): Lec 11.1 The convolution operation](https://www.youtube.com/watch?v=yw8xwS15Pf4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=87)
88. [Deep Learning(CS7015): Lec 11.2 Relation between input size, output size and filter size](https://www.youtube.com/watch?v=7eiYBFladus&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=88)
89. [Deep Learning(CS7015): Lec 11.3 Convolutional Neural Networks](https://www.youtube.com/watch?v=PmZp5VtMwLE&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=89)
90. [Deep Learning(CS7015): Lec 11.3 (Part-2) Convolutional Neural Networks (Contd.)](https://www.youtube.com/watch?v=9eZN8U-68eI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=90)
91. [Deep Learning(CS7015): Lec 11.4 CNNs (success stories on ImageNet)](https://www.youtube.com/watch?v=53ysOFHCaqI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=91)
92. [Deep Learning(CS7015): Lec 11.4 (Par-2) CNNs (success stories on ImageNet) (Contd.)](https://www.youtube.com/watch?v=mHhhXlEB32c&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=92)
93. [Deep Learning(CS7015): Lec 11.5 Image Classification continued (GoogLeNet and ResNet)](https://www.youtube.com/watch?v=UukbB6q6CTo&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=93)
94. [Deep Learning(CS7015): Lec 12.1 Visualizing patches which maximally activate a neuron](https://www.youtube.com/watch?v=nBxy_vzmO_M&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=94)
95. [Deep Learning(CS7015): Lec 12.2 Visualizing filters of a CNN](https://www.youtube.com/watch?v=XE8O5p5mceA&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=95)
96. [Deep Learning(CS7015): Lec 12.3 Occlusion experiments](https://www.youtube.com/watch?v=DaLZRH6D7wo&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=96)
97. [Deep Learning(CS7015): Lec 12.4 Finding influence of input pixels using backpropagation](https://www.youtube.com/watch?v=SPJnlFtw6h0&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=97)
98. [Deep Learning(CS7015): Lec 12.5 Guided Backpropagation](https://www.youtube.com/watch?v=rcXOEzAuvu4&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=98)
99. [Deep Learning(CS7015): Lec 12.6 Optimization over images](https://www.youtube.com/watch?v=a4k8YorzUdI&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=99)
100. [Deep Learning(CS7015): Lec 12.7 Create images from embeddings](https://www.youtube.com/watch?v=orTNf_R5odY&list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT&index=100)

_Only the first 100 are listed; see [the full playlist](https://www.youtube.com/playlist?list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT)._

</details>


## Books, notes and websites

- ✅ NPTEL *Deep Learning* (Khapra, IIT Madras) — nptel.ac.in/courses/106106201/
- d2l.ai; Karpathy *Zero to Hero*; Stanford CS231n
- Book: Prince, *Understanding Deep Learning* (free); Goodfellow *Deep Learning*

## Practice / proof of understanding

Backprop in NumPy, a ResNet on CIFAR-10, a small transformer language model.

## What your IITM course sheet says

### From the PDF: DA3409

**Official description:** : This course aims to introduce undergraduate students to the fundamental concepts of Deep Learning and their  practical applications. The course provides a conceptual and hands-on understanding of neural networks and  modern deep learning architectures. Students will learn how deep learning models are designed, trained, and  applied to solve problems in areas such as computer vision and natural language processing.

**Official syllabus (trimmed):**

> Foundations of Deep Learning: Brief history and motivation for deep learning. McCulloch–Pitts neuron model,
>  threshold logic, perceptron model, perceptron learning algorithm and convergence. Multilayer perceptrons (MLPs)
>  and the representation power of neural networks.
>  Training Neural Networks: Sigmoid and other activation functions, feedforward neural networks, loss functions, and
>  gradient descent. Automatic differentiation for gradient computation. Gradient-based optimization methods
>  including stochastic gradient descent, momentum, Nesterov accelerated gradient, AdaGrad, RMSProp, and Adam.
>  Regularization and Training Deep Networks: Regularization methods including L2 regularization, early stopping,
>  dataset augmentation, parameter sharing, dropout, and ensemble methods. Techniques for improving training
>  such as better activation functions, weight initialization, and batch/layer normalization.
>  Convolutional Neural Networks: Motivation for convolutional networks. Key architectures such as LeNet, AlexNet,
>  VGG, GoogLeNet, and ResNet.
>  Sequential Models: Recurrent neural networks (RNNs), backpropagation through time, vanishing and exploding
>  gradients. Advanced recurrent architectures including GRU and LSTM.
>  Attention and Modern Architectures: Encoder–decoder models and sequence-to-sequence learning. Attention
>  mechanisms in neural networks. Transformers and self-attentio

**Official textbooks:** 1. Charu C. Aggarwal. Neural Networks and Deep Learning: A Textbook. Springer. 2019.  2. Aston Zhang, Zachary C. Lipton, Mu Li, Alexander Smola. Dive into Deep Learning

**Official references:** 1. Ian Goodfellow and Yoshua Bengio and Aaron Courville. Deep Learning. An MIT Press book. 2016.  2. Simon J.D. Prince. Understanding Deep Learning. An MIT Press book. 2023.

### From the PDF: DA3410

**Official description:** The laboratory course is designed to complement the theory course on Deep Learning by providing hands-on  experience in implementing and experimenting with neural network models. The course aims to help students  understand how deep learning models are trained, evaluated, and improved in practice.  Students will learn to implement core deep learning algorithms using modern frameworks such as PyTorch or  TensorFlow, work with real world datasets, and gain practical exposure to model training, debugging, and  experimentation. The laboratory will emphasize experimentation, visualization, and analysis of model behavior

**Official syllabus (trimmed):**

> Introduction to Deep Learning Frameworks: Setting up Python environments for deep learning. Introduction to
>  libraries such as PyTorch or JAX. Working with tensors, automatic differentiation, and GPU acceleration.
>  Data Handling and Visualization: Loading and preprocessing datasets. Dataset splitting, normalization, and
>  augmentation. Visualization of data and training statistics using libraries such as matplotlib.
>  Implementation of Basic Neural Networks: Implementing perceptrons and multilayer perceptrons. Building
>  feedforward neural networks with and without using deep learning frameworks. Training models using gradient
>  descent and automatic differentiation..
>  Optimization and Training Experiments: Experimenting with optimization algorithms such as stochastic gradient
>  descent, momentum, RMSProp, and Adam. Studying learning rate schedules and convergence behavior.
>  Regularization and Model Improvement: Applying techniques such as L2 regularization, dropout, early stopping,
>  and data augmentation. Studying bias variance tradeoff through controlled experiments.
>  Convolutional Neural Networks: Implementing convolutional neural networks for image classification tasks.
>  Training and evaluating CNN models on standard image datasets. Visualizing learned filters and feature maps.
>  Sequential Models: Implementing recurrent neural networks for sequence prediction tasks. Training mod

**Official textbooks:** 1. Eli Stevens, Luca Antiga, and Thomas Viehmann. Deep Learning with PyTorch, Manning Publications, 2026.

**Official references:** 1. Ian Goodfellow and Yoshua Bengio and Aaron Courville. Deep Learning. An MIT Press book. 2016.  2. Simon J.D. Prince. Understanding Deep Learning. An MIT Press book. 2023.

### From the PDF: DA6401

**Official description:** 1. Understanding the Fundamentals of Deep Learning:  o To provide a comprehensive introduction to the core concepts and mathematical foundations of deep  learning.  o To equip students with an understanding of key neural network architectures, optimization techniques,  and the learning process.  2. Developing Practical Knowledge:  o To introduce students to advanced deep learning techniques, including Convolutional Neural  Networks (CNNs), Recurrent Neural Networks (RNNs), Long Short-Term Memory Networks (LSTMs),  and Transformer models.  3. Implementation and Analysis:  o To enable students to implement deep learning algorithms using frameworks like PyTorch or JAX.  o To evaluate the performance of neural networks and optimize them for various applications.

**Official syllabus (trimmed):**

> 1. Introduction and History of Deep Learning (3 Lectures):
>  o Overview of deep learning and its evolution.
>  o Success stories in modern AI.
>  2. Neural Network Fundamentals (6 Lectures):
>  o McCulloch Pitts Neuron, Thresholding Logic, Perceptrons. Perceptron Learning Algorithm, Multilayer
>  Perceptrons (MLPs), Representation Power of MLPs
>  3. Feedforward Neural Networks (6 Lectures):
>  o Sigmoid Neurons, Feedforward Neural Networks.Representation Power of Feedforward Networks,
>  automatic differentiation, stochastic optimisation.
>  4. Optimization Techniques (6 Lectures):
>  o Gradient Descent (GD), Momentum-based GD, Nesterov Accelerated GD, Stochastic GD, AdaGrad,
>  RMSProp, Adam.
>  5. Regularization Techniques (4 Lectures):
>  o Bias-Variance Tradeoff, L2 Regularization, Early Stopping, Dataset Augmentation. Ensemble
>  Methods, Dropout, and Injecting Noise.
>  6. Advanced Neural Network Training Methods (4 Lectures):
>  o Greedy Layerwise Pre-training, Improved Activation Functions, Batch Normalization.
>  7. Convolutional Neural Networks (CNNs) (3 Lectures):
>  o LeNet, AlexNet, ZFNet, VGGNet, GoogLeNet, ResNet.
>  8. Word Embeddings and Vector Representations (3 Lectures):
>  o Introduction to Word2Vec and Skip-gram models.
>  9. Recurrent Neural Networks (RNNs) (4 Lectures):
>  o Computations in a RNN, Backpropagation Through Time (BPTT), Vanishing and Exploding Gradients.
>  o Long Short-Term Memory C

**Official textbooks:** 1. Charu C. Aggarwal. Neural Networks and Deep Learning: A Textbook. Springer. 2019.  2. Aston Zhang, Zachary C. Lipton, Mu Li, Alexander Smola. Dive into Deep Learning.

**Official references:** 1. Ian Goodfellow and Yoshua Bengio and Aaron Courville. Deep Learning. An MIT Press book. 2016.  2. Simon J.D. Prince. Understanding Deep Learning. An MIT Press book. 2023.
