# CS6886 — Systems Engineering for Deep Learning

| | |
|---|---|
| Tier | C |
| Phase (order) | 8 |
| Do this first | CS6910, CS2600, CS3500 |
| Estimated effort | 10-12 weeks |
| Unlocks | Research in ML systems |

## Roadmap

1. GPU architecture, efficient training/inference, quantisation, distributed training.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [EfficientML.ai Course | 2023 Fall | MIT 6.5940](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) (45 videos). MIT 6.5940 *EfficientML.ai* (Fall 2023, Song Han, official MIT HAN Lab): pruning, quantisation, distillation, efficient LLM serving.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Stanford CS336 Language Modeling from Scratch I 2025](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) (17 videos). Stanford CS336 *Language Modeling from Scratch* (2025, official): GPUs, kernels, parallelism, scaling. Do the assignments.
- [CMU Deep Learning Systems 10-414/714](https://www.youtube.com/playlist?list=PLGzYMymX8amNyGPuJ35YWdq59eQ5jYCZ1) (24 videos). CMU 10-414 *Deep Learning Systems* (Tianqi Chen & Zico Kolter, re-upload): build your own autodiff framework (needle).

### ⚡ Short videos for intuition and revision

- [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) (10 videos). Karpathy *Zero to Hero*: the last video, *Let's reproduce GPT-2*, is a hands-on systems lesson (mixed precision, DDP, FlashAttention).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=rCFvPEQTxKI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=1)–[4](https://www.youtube.com/watch?v=ieg0RJb7TeI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=4) | Intro, NN basics (each lecture appears as two consecutive videos; they are parts of the same lecture). |
| 2 | [5](https://www.youtube.com/watch?v=w5WiUcDJosM&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=5)–[12](https://www.youtube.com/watch?v=n72ndSimkB8&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=12) | Pruning, sparsity, quantisation. Labs 1-2 from efficientml.ai: prune and quantise a CNN. |
| 3 | [13](https://www.youtube.com/watch?v=gFi29IEHRGc&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=13)–[18](https://www.youtube.com/watch?v=dSDW_c789zI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=18) | Neural architecture search, knowledge distillation. |
| 4 | [19](https://www.youtube.com/watch?v=l7RdJRYl7ZY&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=19)–[22](https://www.youtube.com/watch?v=gGcbn0ISOJM&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=22) | TinyML, MCUNet, TinyEngine, parallel processing. |
| 5 | [23](https://www.youtube.com/watch?v=A12m85vbZro&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=23)–[32](https://www.youtube.com/watch?v=7s2YAGoLcCA&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=32) | Efficient transformers and LLMs, vision transformers, GANs/video/point clouds, diffusion. Lab: quantise an LLM (AWQ) and run it on a laptop. |
| 6 | [33](https://www.youtube.com/watch?v=0vdzBAms8mE&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=33)–[40](https://www.youtube.com/watch?v=uI4HWD8U6-4&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=40) | Distributed training, on-device training, efficient fine-tuning (LoRA). |
| 7 | [41](https://www.youtube.com/watch?v=Z8GKkgE2840&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=41)–[45](https://www.youtube.com/watch?v=kCTzlodCZII&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=45) | Quantum ML (optional). |

<details>
<summary>All lectures in <i>EfficientML.ai Course | 2023 Fall | MIT 6.5940</i> (45 videos)</summary>

1. [EfficientML.ai Lecture 1 - Introduction (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=rCFvPEQTxKI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=1)
2. [EfficientML.ai Lecture 1 - Introduction (MIT 6.5940, Fall 2023, Zoom recording)](https://www.youtube.com/watch?v=6cAmS-_vEh8&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=2)
3. [EfficientML.ai Lecture 2 - Basics of Neural Networks (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=Q9bdjoVx_m4&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=3)
4. [EfficientML.ai Lecture 2 - Basics of Neural Networks (MIT 6.5940, Fall 2023, Zoom recording)](https://www.youtube.com/watch?v=ieg0RJb7TeI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=4)
5. [EfficientML.ai Lecture 3 - Pruning and Sparsity (Part I) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=w5WiUcDJosM&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=5)
6. [EfficientML.ai Lecture 3 - Pruning and Sparsity (Part I) (MIT 6.5940, Fall 2023, Zoom recording)](https://www.youtube.com/watch?v=95JFZPoHbgQ&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=6)
7. [EfficientML.ai Lecture 4 - Pruning and Sparsity (Part II) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=3t9aGLLaCqs&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=7)
8. [EfficientML.ai Lecture 4 - Pruning and Sparsity (Part II) (MIT 6.5940, Fall 2023, Zoom recording)](https://www.youtube.com/watch?v=sDJymyfAOKY&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=8)
9. [EfficientML.ai Lecture 5 - Quantization (Part I) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=TSc_BibWRhM&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=9)
10. [EfficientML.ai Lecture 5 - Quantization (Part I) (MIT 6.5940, Fall 2023, Zoom recording)](https://www.youtube.com/watch?v=MK4k64vY3xo&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=10)
11. [EfficientML.ai Lecture 6 - Quantization (Part II) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=g-TzDApaE88&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=11)
12. [EfficientML.ai Lecture 6 - Quantization (Part II) (MIT 6.5940, Fall 2023, Zoom recording)](https://www.youtube.com/watch?v=n72ndSimkB8&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=12)
13. [EfficientML.ai Lecture 7 - Neural Architecture Search (Part I) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=gFi29IEHRGc&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=13)
14. [EfficientML.ai Lecture 7 - Neural Architecture Search (Part I) (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=W84MKJSg90A&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=14)
15. [EfficientML.ai Lecture 8 - Neural Architecture Search (Part II) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=EFpGQoDQ7JI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=15)
16. [EfficientML.ai Lecture 8 - Neural Architecture Search (Part II) (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=MOMc8KkGwCc&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=16)
17. [EfficientML.ai Lecture 9 - Knowledge Distillation (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=EkjVHToId7U&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=17)
18. [EfficientML.ai Lecture 9 - Knowledge Distillation (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=dSDW_c789zI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=18)
19. [EfficientML.ai Lecture 10 - MCUNet: TinyML on Microcontrollers (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=l7RdJRYl7ZY&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=19)
20. [EfficientML.ai Lecture 10 - MCUNet: TinyML on Microcontrollers (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=zJ3ZDZXD_zw&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=20)
21. [EfficientML.ai Lecture 11 - TinyEngine and Parallel Processing (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=HGsvWHqU29Y&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=21)
22. [EfficientML.ai Lecture 11 - TinyEngine and Parallel Processing (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=gGcbn0ISOJM&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=22)
23. [EfficientML.ai Lecture 12 - Transformer and LLM (Part I) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=A12m85vbZro&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=23)
24. [EfficientML.ai Lecture 12 - Transformer and LLM (Part I) (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=mR4u6ZaCYe4&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=24)
25. [EfficientML.ai Lecture 13 - Transformer and LLM (Part II) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=7WeraZ0LLlg&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=25)
26. [EfficientML.ai Lecture 13 - Transformer and LLM (Part II) (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=caEDCA3Jo_4&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=26)
27. [EfficientML.ai Lecture 14 - Vision Transformer (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=QQY24LLww1A&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=27)
28. [EfficientML.ai Lecture 14 - Vision Transformer (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=fcmOYHd57Dk&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=28)
29. [EfficientML.ai Lecture 15 - GAN, Video, and Point Cloud (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=W3WwxI0M-hI&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=29)
30. [EfficientML.ai Lecture 15 - GAN, Video, and Point Cloud (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=WU7tpyesm68&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=30)
31. [EfficientML.ai Lecture 16 - Diffusion Model (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=nFE1euQ_Wtw&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=31)
32. [EfficientML.ai Lecture 16 - Diffusion Model (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=7s2YAGoLcCA&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=32)
33. [EfficientML.ai Lecture 17: Distributed Training (Part I) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=0vdzBAms8mE&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=33)
34. [EfficientML.ai Lecture 17: Distributed Training (Part I) (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=u6NEbhNiyAE&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=34)
35. [EfficientML.ai Lecture 18: Distributed Training (Part II) (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=mP4BL6URdxc&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=35)
36. [EfficientML.ai Lecture 18: Distributed Training (Part II) (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=ZSZQL0q8eYY&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=36)
37. [EfficientML.ai Lecture 19: On-Device Training and Transfer Learning (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=PArGX623PvA&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=37)
38. [EfficientML.ai Lecture 19: On-Device Training and Transfer Learning (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=0YABI9mxG60&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=38)
39. [EfficientML.ai Lecture 20: Efficient Fine-tuning and Prompt Engineering (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=vOPwwRCZ8q8&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=39)
40. [EfficientML.ai Lecture 20: Efficient Fine-tuning and Prompt Engineering (MIT 6.5940,Fall 2023,Zoom)](https://www.youtube.com/watch?v=uI4HWD8U6-4&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=40)
41. [EfficientML.ai Lecture 21: Basics of Quantum Computing (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=Z8GKkgE2840&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=41)
42. [EfficientML.ai Lecture 21: Basics of Quantum Computing (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=xu_6Tz5DPOw&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=42)
43. [EfficientML.ai Lecture 22: Quantum Machine Learning (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=eDtzfMRJg_Y&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=43)
44. [EfficientML.ai Lecture 22: Quantum Machine Learning (MIT 6.5940, Fall 2023, Zoom)](https://www.youtube.com/watch?v=36S3yCY193M&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=44)
45. [EfficientML.ai Lecture 23: Noise Robust Quantum ML (MIT 6.5940, Fall 2023)](https://www.youtube.com/watch?v=kCTzlodCZII&list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB&index=45)

</details>


## Books, notes and websites

- Papers and docs: PyTorch internals, Megatron-LM, FlashAttention
- Stanford CS336 *Language Modeling from Scratch*

## Practice / proof of understanding

Profile a PyTorch model, then speed it up with mixed precision and a compiled kernel.

## What your IITM course sheet says

### From the PDF: CS6886

**Official description:** The course will provide a comprehensive and current view of systems challenges to execute workloads from Deep  Learning (DL). This will include three major areas: hardware design, security, and safety-critical execution. All  these three areas will be studied covering both training and inference methods and spanning from edge to cloud  devices. At the end of the course, the students should appreciate the significance of systems thinking in enabling  efficient DL, and be equipped to implement and optimize large systems for real-world application of DL.

**Official syllabus (trimmed):**

> - Introduction to the course; overview of computer architecture and deep learning (2.5 weeks)
>  - Evolution of platforms for Deep Learning: CPUs, GPUs, FPGAs, DSPs, accelerators; Hardware considerations in
>  inference and training, Case study of an accelerator: Google TPU v1-3 (2.5 weeks)
>  - Accelerating the convolution operation: Algorithms, Data flow patterns, Memory reuse (1.5 week)
>  - Case-study on writing a custom GPU kernel for accelerating convolution (2 weeks)
>  - Optimizing networks: Weight quantization, network compression, sparse operations, zero forwarding, learning
>  with hardware in the loop, learning and inference on low-memory devices (2 weeks)
>  - Case-study on hardware design of small modules with Bluespec BSV. Alternatively, implementing a
>  state-of-the-art DL model on an embedded device such as Raspberry Pi / Arduino (1.5 weeks)
>  - Security for DL: side channel attacks on devices, secure enclaves, privacy during learning and inference (1.5
>  weeks)
>  - Safety-critical deployment of DL: Inference under timing deadlines, Minimizing latency (0.5 week)
>  The following topics will be covered based on available time and student interest
>  - Neuromorphic computing, Spiking neurons, Signaling in time, In-memory compute, Memristors, Current industry
>  pursuits
>  - Security for DL: adversarial learning, shared learning on confidential data, DL on encrypted data, homomorphic
>  mod

**Official textbooks:** There is no prescribed textbook for this course

**Official references:** - Recent papers from top venues especially ML systems workshops at NIPS, ICML, SOSP  - Stoica, Ion, et al. "A Berkeley view of systems challenges for AI." arXiv preprint arXiv:1712.05855 (2017).  - Sze, Vivienne, et al. "Efficient processing of deep neural networks: A tutorial and survey." Proceedings of the  IEEE105.12 (2017): 2295-2329.
