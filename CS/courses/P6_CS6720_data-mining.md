# CS6720 — Data Mining

| | |
|---|---|
| Tier | B |
| Phase (order) | 6 |
| Do this first | CS3700, CS4011 |
| Estimated effort | 10 weeks |
| Unlocks | CS6745, CS5830 |

## Roadmap

1. Preprocessing, frequent patterns, clustering, classification, graph/web mining.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Data Mining for Decision Making](https://www.youtube.com/playlist?list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD) (35 videos). NPTEL-NOC IITM *Data Mining for Decision Making*: classification, clustering, association rules.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Data Mining](https://www.youtube.com/playlist?list=PLCQnw0zDwSUrB7xd3rKmt1bO7LQudolbd) (36 videos). NPTEL *Data Mining* (Pabitra Mitra, IIT Kharagpur, re-upload).
- [Stanford CS224W Machine Learning with Graphs I Jure Leskovec](https://www.youtube.com/playlist?list=PLoROMvodv4rOP-ImU-O1rYRg2RFxomvFp) (47 videos). Stanford CS224W *Machine Learning with Graphs* (Jure Leskovec, official): PageRank, communities, GNNs; Leskovec also wrote *Mining of Massive Datasets* (free at mmds.org).

### ⚡ Short videos for intuition and revision

- [Data Warehouse & Data Mining](https://www.youtube.com/playlist?list=PLxCzCOWd7aiHexyDzYgry0YZN29e7HdNB) (25 videos). Gate Smashers *Data Warehouse & Data Mining*: short exam-style revision.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=mTjG0xkNp9E&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=1)–[4](https://www.youtube.com/watch?v=TRLCtrjU-ws&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=4) | What data mining is, decision lists, association rules; install WEKA (you can do every exercise in Python/scikit-learn instead). |
| 2 | [5](https://www.youtube.com/watch?v=fR1sqq2jU_0&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=5)–[10](https://www.youtube.com/watch?v=4ef2pVKHOm8&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=10) | Naive Bayes (categorical and numeric), decision trees. Run both on the UCI Adult dataset. |
| 3 | [11](https://www.youtube.com/watch?v=EIlzTW7bGdY&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=11)–[18](https://www.youtube.com/watch?v=jBgIeRO7kXY&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=18) | Neural networks, clustering, PCA. |
| 4 | [19](https://www.youtube.com/watch?v=rQXb1uKL78U&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=19)–[29](https://www.youtube.com/watch?v=bJfTZQ6Wx74&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=29) | Linear and logistic regression, kNN, market-basket analysis (Apriori), LDA. Mine association rules from a groceries dataset. |
| 5 | [30](https://www.youtube.com/watch?v=uqTI6XX45e8&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=30)–[35](https://www.youtube.com/watch?v=HVaFsu_xXso&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=35) | Evaluation metrics, SVMs. Then the free book *Mining of Massive Datasets* (mmds.org) for scale: LSH, streams, PageRank. |

<details>
<summary>All lectures in <i>Data Mining for Decision Making</i> (35 videos)</summary>

1. [Data Mining for Decision Making | INTRO | NPTEL | 2026](https://www.youtube.com/watch?v=mTjG0xkNp9E&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=1)
2. [Data Mining Explained: Decision Lists & Association Rules Made Simple](https://www.youtube.com/watch?v=F_eleZ8go0A&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=2)
3. [How to Install WEKA: Step-by-Step Guide for Beginners](https://www.youtube.com/watch?v=niMoxQalEoc&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=3)
4. [Getting Started with WEKA: A Complete Beginner’s Overview](https://www.youtube.com/watch?v=TRLCtrjU-ws&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=4)
5. [Basics of Bayesian Classification: Understanding Probabilistic Learning](https://www.youtube.com/watch?v=fR1sqq2jU_0&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=5)
6. [A Deep Dive into Bayesian Classification: Concepts & Intuition building](https://www.youtube.com/watch?v=yGdG04NI8rI&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=6)
7. [Implementing Bayesian Classification Using WEKA](https://www.youtube.com/watch?v=XOZRLH9sK-U&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=7)
8. [Bayesian Classification with Numeric Data: Theory & Examples](https://www.youtube.com/watch?v=nx5wFYm6q0I&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=8)
9. [Decision Trees Explained: From Roots to Leaves](https://www.youtube.com/watch?v=jRN8_rSqDxk&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=9)
10. [Building Decision Trees in WEKA: Hands-On Tutorial](https://www.youtube.com/watch?v=4ef2pVKHOm8&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=10)
11. [Neural Networks Fundamentals: How Artificial Brains Learn](https://www.youtube.com/watch?v=EIlzTW7bGdY&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=11)
12. [Neural Networks Explained: Architecture & Learning](https://www.youtube.com/watch?v=Ex_lcn-6_ho&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=12)
13. [Implementing Neural Networks in WEKA](https://www.youtube.com/watch?v=3ptuS-7ZIg0&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=13)
14. [Clustering Basics: Grouping Data Without Labels](https://www.youtube.com/watch?v=Lpq7G8VWwIU&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=14)
15. [Clustering Algorithms in WEKA: Practical Demonstration](https://www.youtube.com/watch?v=kGXmrzpJU0c&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=15)
16. [Clustering Techniques Explained: Beyond the Basics](https://www.youtube.com/watch?v=MFsNpkqNP14&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=16)
17. [Principal Component Analysis (PCA): Dimensionality Reduction Explained](https://www.youtube.com/watch?v=6dC6rRgK3lU&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=17)
18. [Applying PCA in WEKA: Step-by-Step Walkthrough](https://www.youtube.com/watch?v=jBgIeRO7kXY&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=18)
19. [Linear Regression Explained: Modeling Relationships in Data](https://www.youtube.com/watch?v=rQXb1uKL78U&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=19)
20. [Linear Regression Using WEKA: Practical Implementation](https://www.youtube.com/watch?v=DMjuLIhHLFM&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=20)
21. [Logistic Regression Basics: Classification Made Easy](https://www.youtube.com/watch?v=JKjhjr75BEA&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=21)
22. [Logistic Regression in WEKA: Hands-On Classification](https://www.youtube.com/watch?v=tj0MuB4LsVI&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=22)
23. [Instance-Based Learning Explained: Learning from Examples](https://www.youtube.com/watch?v=_yAIugcDt8E&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=23)
24. [Instance-Based Learning in WEKA: KNN and Beyond](https://www.youtube.com/watch?v=EVET5XaOloA&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=24)
25. [Market Basket Analysis Explained: Discovering Hidden Patterns](https://www.youtube.com/watch?v=m88tjGit4c4&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=25)
26. [Market Basket Analysis Using WEKA](https://www.youtube.com/watch?v=tCGna4zqOAQ&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=26)
27. [Linear Discriminant Analysis (LDA): Classification Intuition](https://www.youtube.com/watch?v=_Maje_5rirI&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=27)
28. [Linear Discriminant Analysis Explained in Depth](https://www.youtube.com/watch?v=04ORUnkJf3U&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=28)
29. [Implementing LDA in WEKA](https://www.youtube.com/watch?v=bJfTZQ6Wx74&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=29)
30. [Model Evaluation Metrics Explained: Accuracy, Precision & More](https://www.youtube.com/watch?v=uqTI6XX45e8&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=30)
31. [Support Vector Machines Explained: Maximum Margin Learning](https://www.youtube.com/watch?v=s8fGErUar9w&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=31)
32. [Support Vector Machines Deep Dive: Kernels & Optimization](https://www.youtube.com/watch?v=N0gGY21PG64&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=32)
33. [Advanced SVM Concepts: Kernels, Margins & Hyperparameters](https://www.youtube.com/watch?v=xGtgFIHT_IU&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=33)
34. [Support Vector Machines in WEKA: Practical Tutorial](https://www.youtube.com/watch?v=ytHNjuXPW2U&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=34)
35. [Data Mining for Decision Making: Key Takeaways & Final Insights](https://www.youtube.com/watch?v=HVaFsu_xXso&list=PLyqSpQzTE6M9eHB0QosKobGRIo29eq0mD&index=35)

</details>


## Books, notes and websites

- Book: Han, Kamber, Pei; Tan, Steinbach, Kumar
- Mining of Massive Datasets — mmds.org (free)

## Practice / proof of understanding

Run Apriori and DBSCAN on real data and report results.

## What your IITM course sheet says

### From the PDF: CS6720

**Official description:** The field of data mining is fast evolving to address issues related to handling very large volumes of data. This  course aims to provide an introduction to some of the techniques for handling massive data sets as well as  in-depth exploration of some of the topics. The course will be at an advanced level and would require that the  students have done an preliminary course on machine learning or pattern recognition.

**Official syllabus (trimmed):**

> Basics: Introduction to machine learning - Bayesian Decision Theory, Maximum Likelihood Estimation; Feature
>  Selection - Information Gain, Derived features: Principal Component Analysis, Linear Discriminant Analysis &
>  Partial Least Squares, Aggregation/Coding; Handling Missing Values; Class Imbalance: Differentialloss functions,
>  differential slack, Sampling based approaches.Ensemble Methods: Boosting - Adaboost, LogitBoost, Gradient
>  Boosting; Bagging - Simple methods, Random Forest, Subsampling; Stacking; Decision Fusion.Scaling up:
>  Map-Reduce; Locality Sensitive Hashing; Large Scale optimization Clustering: Hierarchical Clustering; k-means;
>  CURE; DBScan; Non-Euclidean spaces; Spectral clusteringFrequent Pattern Mining: Apriori Algorithm; Large
>  datasets; Limited-pass algorithms; Frequent sub-sequence miningStream Mining: Stream Data Model; Filtering
>  and Sampling from stream; Bloom Filters; Canonical problems on streams - Counting unique elements, counting
>  ones, computing moments.Graph Mining: Frequent sub-graph mining; Classification on Graphs; Network
>  computations: Page Rank.Recommender Systems: Content based Recommendation; Collaborative Filtering;
>  Non-negative Matrix Factorization; Online advertising.Other Data Mining Tasks: Multi-label Classification; Learning
>  to rank; Multi-view Learning; Structured output prediction; Information Extraction.

**Official textbooks:** Mining of Massive Datasets. Anand Rajaraman, and Jeffrey D. Ullman. Cambridge. 2011.

**Official references:** 1.The Elements of Statistical Learning: Data Mining, Inference, and Prediction. 2nd Ed. Trevor Hastie, Robert  Tibshirani, Jerome Friedman. Springer. 2012.2. Pattern Recognition and Machine Learning. 2nd Ed. Christopher  Bishop. 20073. Data Mining: Concepts and Techniques, 3rd Edition. Jiawei Han, Michelline Kamber, Jian Pei.  Morgan Kauffman. 2011
