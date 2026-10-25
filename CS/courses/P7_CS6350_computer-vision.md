# CS6350 — Computer Vision

| | |
|---|---|
| Tier | B |
| Phase (order) | 7 |
| Do this first | CS6910, linear algebra |
| Estimated effort | 12 weeks |
| Unlocks | CS6790, CS6777 |

## Roadmap

1. Image formation, filtering, features (SIFT/Harris).
2. Geometry (cameras, epipolar), then CNN-based detection and segmentation.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Stanford CS231N Deep Learning for Computer Vision I 2025](https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16) (18 videos). Stanford CS231N *Deep Learning for Computer Vision* 2025 (official Stanford Online).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [First Principles of Computer Vision: Introduction (Shree Nayar)](https://www.youtube.com/playlist?list=PL2zRqk16wsdoz4eycyq7EmeV2KpE6JN76) (7 videos). Shree Nayar *First Principles of Computer Vision* (Columbia): classical vision (image formation, features, stereo, flow). Other units are separate playlists on the same channel.
- [Deep Learning for Computer Vision](https://www.youtube.com/playlist?list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r) (22 videos). Michigan EECS 498 *Deep Learning for Computer Vision* (Justin Johnson): CS231n's successor, with assignments.
- [Deep Learning for Computer Vision](https://www.youtube.com/playlist?list=PLyqSpQzTE6M_PI-rIz4O1jEgffhJU9GgG) (100+ videos). NPTEL *Deep Learning for Computer Vision* (Vineeth Balasubramanian, IIT Hyderabad).
- [Computer Vision and Image Processing - Fundamentals and Applications](https://www.youtube.com/playlist?list=PLwdnzlV3ogoVsma5GmBSsgJM6gHv1QoAo) (42 videos). NPTEL *Computer Vision and Image Processing* (IIT Guwahati): classical image processing.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=2fq9wYslV0A&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=1)–[3](https://www.youtube.com/watch?v=dyNGd06MWn4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=3) | Image classification, linear classifiers, regularisation, optimisation. Assignment 1 (kNN, SVM, softmax) from cs231n.github.io. |
| 2 | [4](https://www.youtube.com/watch?v=25zD5qJHYsk&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=4)–[6](https://www.youtube.com/watch?v=aVJy4O5TOk8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=6) | Backprop, CNNs, CNN architectures (ResNet etc.). Assignment 2: CNN on CIFAR-10. |
| 3 | [7](https://www.youtube.com/watch?v=kG2lAPBF7zA&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=7)–[8](https://www.youtube.com/watch?v=RQowiOF_FvQ&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=8) | RNNs, attention, transformers. |
| 4 | [9](https://www.youtube.com/watch?v=PTypu6GqEd4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=9)–[10](https://www.youtube.com/watch?v=wElqklprhPE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=10) | Detection, segmentation, visualisation, video. Fine-tune a YOLO / Mask R-CNN model. |
| 5 | [11](https://www.youtube.com/watch?v=9MvD-XsowsE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=11)–[14](https://www.youtube.com/watch?v=Edr4uZFh4EE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=14) | Distributed training, self-supervised learning, generative models (VAE, GAN, diffusion). |
| 6 | [15](https://www.youtube.com/watch?v=7lxrKDKtykM&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=15)–[18](https://www.youtube.com/watch?v=g8UaBfj6Sh8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=18) | 3D vision, vision-language, robot learning, human-centred AI. For classical CV (filters, geometry, stereo) use Shree Nayar's series (alt). |

<details>
<summary>All lectures in <i>Stanford CS231N Deep Learning for Computer Vision I 2025</i> (18 videos)</summary>

1. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 1: Introduction](https://www.youtube.com/watch?v=2fq9wYslV0A&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=1)
2. [Stanford CS231N | Spring 2025 | Lecture 2: Image Classification with Linear Classifiers](https://www.youtube.com/watch?v=pdqofxJeBN8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=2)
3. [Stanford CS231N | Spring 2025 | Lecture 3: Regularization and Optimization](https://www.youtube.com/watch?v=dyNGd06MWn4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=3)
4. [Stanford CS231N | Spring 2025 | Lecture 4: Neural Networks and Backpropagation](https://www.youtube.com/watch?v=25zD5qJHYsk&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=4)
5. [Stanford CS231N | Spring 2025 | Lecture 5: Image Classification with CNNs](https://www.youtube.com/watch?v=f3g1zGdxptI&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=5)
6. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 6: CNN Architectures](https://www.youtube.com/watch?v=aVJy4O5TOk8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=6)
7. [Stanford CS231N | Spring 2025 | Lecture 7: Recurrent Neural Networks](https://www.youtube.com/watch?v=kG2lAPBF7zA&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=7)
8. [Stanford CS231N | Spring 2025 | Lecture 8: Attention and Transformers](https://www.youtube.com/watch?v=RQowiOF_FvQ&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=8)
9. [Stanford CS231N | Spring 2025 | Lecture 9: Object Detection, Image Segmentation, Visualizing](https://www.youtube.com/watch?v=PTypu6GqEd4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=9)
10. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 10: Video Understanding](https://www.youtube.com/watch?v=wElqklprhPE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=10)
11. [Stanford CS231N | Spring 2025 | Lecture 11: Large Scale Distributed Training](https://www.youtube.com/watch?v=9MvD-XsowsE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=11)
12. [Stanford CS231N | Spring 2025 | Lecture 12: Self-Supervised Learning](https://www.youtube.com/watch?v=4howBU7THbM&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=12)
13. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 13: Generative Models 1](https://www.youtube.com/watch?v=zbHXQRUNlH0&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=13)
14. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 14: Generative Models 2](https://www.youtube.com/watch?v=Edr4uZFh4EE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=14)
15. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 15: 3D Vision](https://www.youtube.com/watch?v=7lxrKDKtykM&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=15)
16. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 16: Vision and Language](https://www.youtube.com/watch?v=mQOK0Mfyrkk&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=16)
17. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 17: Robot Learning](https://www.youtube.com/watch?v=XSfmOH_xVSU&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=17)
18. [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 18: Human-Centered AI](https://www.youtube.com/watch?v=g8UaBfj6Sh8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=18)

</details>


## Books, notes and websites

- Szeliski, *Computer Vision: Algorithms and Applications* — szeliski.org/Book (free)
- Stanford CS231n; OpenCV tutorials

## Practice / proof of understanding

Build a panorama stitcher with OpenCV and train a small object detector.

## What your IITM course sheet says

### From the PDF: CS6350

**Official description:** Computer Vision focuses on development of algorithms and techniques to analyze and interpret the visible world  around us. This requires understanding of the fundamental concepts related to multi-dimensional signal  processing, feature extraction, pattern analysis visual geometric modeling, stochastic optimization etc. Knowledge  of these concepts is necessary in this field, to explore and contribute to research and further developments in the  field of computer vision. Applications range from Biometrics, Medical diagnosis, document processing, mining of  visual content, to surveillance, advanced rendering etc.

**Official syllabus (trimmed):**

> Syllabus:
>  • Digital Image Formation and low-level Processing: Overview and State-of-the-art, Fundamentals of Image
>  Formation, Transformation: Orthogonal, Euclidean, Affine, Projective, etc; Fourier Transform, Convolution and
>  Filtering, Image Enhancement, Restoration, Histogram Processing.
>  • Depth estimation and Multi-camera views: Perspective, Binocular Stereopsis: Camera and Epipolar Geometry;
>  Homography, Rectification, DLT, RANSAC, 3-D reconstruction framework; Auto-calibration.
>  • Feature Extraction: Edges – Canny, LOG, DOG; Line detectors (Hough Transform), Corners – Harris and
>  Hessian Affine, Orientation Histogram, SIFT, SURF, HOG, GLOH, Scale-Space Analysis- Image Pyramids and
>  Gaussian derivative filters, Gabor Filters and DWT.
>  • Image Segmentation: Region Growing, Edge Based approaches to segmentation, Graph-Cut, Mean-Shift,
>  MRFs, Texture Segmentation; Object detection.
>  • Pattern Analysis: Clustering: K-Means, K-Medoids, Mixture of Gaussians, Classification: Discriminant Function,
>  Supervised, Un-supervised, Semi-supervised; Classifiers: Bayes, KNN, ANN models; Dimensionality Reduction:
>  PCA, LDA, ICA; Non-parametric methods.
>  • Motion Analysis: Background Subtraction and Modeling, Optical Flow, KLT, Spatio-Temporal Analysis, Dynamic
>  Stereo; Motion parameter estimation.
>  • Object Recognition: Structural, model-based, appearance and shape-based methods; probabi

**Official textbooks:** 1. Richard Szeliski, Computer Vision: Algorithms and Applications, Springer-Verlag Limited, London, 2011.

**Official references:** 1. Richard Hartley and Andrew Zisserman, Multiple View Geometry in Computer Vision, Second Edition,  Cambridge University Press, March 2004.  2. K. Fukunaga; Introduction to Statistical Pattern Recognition, Second Edition, Academic Press, Morgan  Kaufmann, 1990.  3. R.C. Gonzalez and R.E. Woods, Digital Image Processing, Addison-Wesley, 1992.  4. IEEE Transactions on Pattern Analysis and Machine I
