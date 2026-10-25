# DA3408+DA5402 — AI Operations / MLOps Labs

| | |
|---|---|
| Tier | A |
| Phase (order) | 5 |
| Do this first | DA3406, DA3409 |
| Estimated effort | 10 weeks |
| Unlocks | Industry deployment |

## Roadmap

1. Experiment tracking (MLflow), data/version control (DVC), CI.
2. Distributed ETL (Spark), scaling (Ray), serving and monitoring.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Machine Learning Operations (MLOps) - Rangarajan Vasudevan](https://www.youtube.com/playlist?list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2) (55 videos). IIT Madras BS *Machine Learning Operations (MLOps)* (Rangarajan Vasudevan).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [MLOps Zoomcamp](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK) (43 videos). DataTalksClub *MLOps Zoomcamp*: experiment tracking, orchestration, deployment, monitoring. Free, project-based.
- [Full Stack Deep Learning - 2022](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) (18 videos). *Full Stack Deep Learning 2022*: the whole lifecycle of a deployed model.
- [Machine Learning Engineering for Production (MLOps)](https://www.youtube.com/playlist?list=PLkDaE6sCZn6GMoA0wbpJLi3t34Gd8l0aK) (40 videos). DeepLearning.AI *ML Engineering for Production (MLOps)* (Andrew Ng et al.).

### ⚡ Short videos for intuition and revision

- [Docker and Kubernetes Tutorial for Beginners](https://www.youtube.com/playlist?list=PLy7NrYWoggjwPggqtFsI_zMAwvG0SqYCb) (33 videos). TechWorld with Nana *Docker and Kubernetes*: the containers you will deploy with.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=LNtSRp1reos&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=1)–[4](https://www.youtube.com/watch?v=68YxDKlAdP4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=4) | MLOps landscape, DevOps vs MLOps, cloud set-up (any cloud or local is fine). |
| 2 | [5](https://www.youtube.com/watch?v=r2_bgMgP580&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=5)–[11](https://www.youtube.com/watch?v=fl6LKNr8gb4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=11) | Data management, data versioning with DVC, feature stores (Feast). |
| 3 | [12](https://www.youtube.com/watch?v=1PFfzJk2qCc&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=12)–[15](https://www.youtube.com/watch?v=sKWA2PGmg90&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=15) | CI/CD for ML, git, GitHub Actions/CML. |
| 4 | [16](https://www.youtube.com/watch?v=_Kg-a7iOK8g&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=16)–[20](https://www.youtube.com/watch?v=35Pv2OJ1QxU&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=20) | Model lifecycle, experiment tracking with MLflow, hyperparameter tuning. |
| 5 | [21](https://www.youtube.com/watch?v=Qor7iGXVKOA&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=21)–[27](https://www.youtube.com/watch?v=RJHQRKGixnY&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=27) | Serving with FastAPI, Docker, Kubernetes, deployment. Containerise a model behind a FastAPI endpoint. |
| 6 | [28](https://www.youtube.com/watch?v=83BSH01jWFw&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=28)–[32](https://www.youtube.com/watch?v=Ixi12t0VKOw&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=32) | Monitoring, observability, logging. |
| 7 | [33](https://www.youtube.com/watch?v=WJSTDenIqgs&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=33)–[42](https://www.youtube.com/watch?v=ab1hl2SH7q4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=42) | ML security, governance, drift detection, bias, explainability. |
| 8 | [43](https://www.youtube.com/watch?v=A3jFXa88a2k&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=43)–[52](https://www.youtube.com/watch?v=mEcY-CdAX1A&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=52) | LLMOps: versioning, testing, fine-tuning, serving, cost, observability. |

<details>
<summary>All lectures in <i>Machine Learning Operations (MLOps) - Rangarajan Vasudevan</i> (55 videos)</summary>

1. [W1_L1: Introduction to mlops](https://www.youtube.com/watch?v=LNtSRp1reos&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=1)
2. [W1_L2: Devops vs mlops](https://www.youtube.com/watch?v=c8HdgyG4Shg&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=2)
3. [W1_L3: Landscape of mlops](https://www.youtube.com/watch?v=5k485C-KPVQ&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=3)
4. [W1_L4: Hands-on: introduction to google cloud, vertex ai](https://www.youtube.com/watch?v=68YxDKlAdP4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=4)
5. [W2_L1: Data management for machine learning](https://www.youtube.com/watch?v=r2_bgMgP580&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=5)
6. [W2_L2: Data versioning](https://www.youtube.com/watch?v=7rW5OejBA28&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=6)
7. [W2_L3: Hands-on: DVC](https://www.youtube.com/watch?v=uweHNLtgxKg&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=7)
8. [W3_L1: Motivation for feature store](https://www.youtube.com/watch?v=bBztTeXW3ME&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=8)
9. [W3_L2: Feature store: overview, use cases](https://www.youtube.com/watch?v=87owqZ481nc&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=9)
10. [W3_L3: Feast: overview](https://www.youtube.com/watch?v=JtyLLJgvQKA&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=10)
11. [W3_L4: Hands-on: feast](https://www.youtube.com/watch?v=fl6LKNr8gb4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=11)
12. [W4_L1: CI/CD for machine learning](https://www.youtube.com/watch?v=1PFfzJk2qCc&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=12)
13. [W4_L2: Git 101 for machine learning](https://www.youtube.com/watch?v=h-4IH6-qJWY&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=13)
14. [W4_L3: Github and best practices](https://www.youtube.com/watch?v=9EtdVdkdce8&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=14)
15. [W4_L4: Hands-on: CI for machine learning using CML](https://www.youtube.com/watch?v=sKWA2PGmg90&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=15)
16. [W5_L1: Model lifecycle patterns](https://www.youtube.com/watch?v=_Kg-a7iOK8g&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=16)
17. [W5_L2: Execution environments](https://www.youtube.com/watch?v=DILHZrfJYzs&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=17)
18. [W5_L3: Introduction to machine learning flow](https://www.youtube.com/watch?v=aSKi2_DixX4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=18)
19. [W5_L4: Hyperparameter tuning](https://www.youtube.com/watch?v=aTUsX2_GttA&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=19)
20. [W5_L5: Handson: machine learning flow on GCP](https://www.youtube.com/watch?v=35Pv2OJ1QxU&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=20)
21. [W6_L1: Model serving using fastapi](https://www.youtube.com/watch?v=Qor7iGXVKOA&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=21)
22. [W6_L2: Handson: fastapi](https://www.youtube.com/watch?v=LJNEr8XtU-s&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=22)
23. [W6_L3: Model serving using containers](https://www.youtube.com/watch?v=w3SabCLrkzM&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=23)
24. [W6_L4: Handson: docker](https://www.youtube.com/watch?v=kV47H5b71Z8&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=24)
25. [W6_L5: Introduction to kubernetes](https://www.youtube.com/watch?v=H_pMolfm6s4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=25)
26. [W6_L6: Handson: kubernetes](https://www.youtube.com/watch?v=J3dWDVG_YJc&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=26)
27. [W6_L7: Model deployment, ci/cd for ml](https://www.youtube.com/watch?v=RJHQRKGixnY&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=27)
28. [W7_L1: Machine learning systems monitoring & performance tools](https://www.youtube.com/watch?v=83BSH01jWFw&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=28)
29. [W7_L2: Modern observability stack for ml](https://www.youtube.com/watch?v=IZsyl8wHrmQ&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=29)
30. [W7_L3: Response options for ml systems](https://www.youtube.com/watch?v=zafCZIDM9EM&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=30)
31. [W7_L4: Logging for machine learning systems](https://www.youtube.com/watch?v=yYkQNSTISaA&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=31)
32. [W7_L5: Handson: logging, monitoring, scaling using gcp-native tools](https://www.youtube.com/watch?v=Ixi12t0VKOw&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=32)
33. [W8_L1: Introduction to machine learning security with examples](https://www.youtube.com/watch?v=WJSTDenIqgs&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=33)
34. [W8_L2: Challenges in securing ml](https://www.youtube.com/watch?v=c_3s_QWonfs&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=34)
35. [W8_L3: MLsecOps](https://www.youtube.com/watch?v=4abLOEKaUn4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=35)
36. [W8_L4: Hand-son: security demonstration](https://www.youtube.com/watch?v=TrnP2RnlWXc&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=36)
37. [W9_L1: Machine learning governance and regulation](https://www.youtube.com/watch?v=73bGDGzMtQw&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=37)
38. [W9_L2: Governance failures and how to mitigate them](https://www.youtube.com/watch?v=R_dMiAjAdAM&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=38)
39. [W9_L3: Drift monitoring](https://www.youtube.com/watch?v=vL1XiVK9VPI&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=39)
40. [W9_L4: Detecting bias in machine learning](https://www.youtube.com/watch?v=bV9cjMkkzc8&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=40)
41. [W9_L5: Explaining machine learning models](https://www.youtube.com/watch?v=DRe02jFW2FU&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=41)
42. [W9_L6: Handson: governance tools](https://www.youtube.com/watch?v=ab1hl2SH7q4&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=42)
43. [W10_L1: LLMOps](https://www.youtube.com/watch?v=A3jFXa88a2k&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=43)
44. [W10_L2: LLMOps during pretraining](https://www.youtube.com/watch?v=N50zCNg1aAs&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=44)
45. [W10_L3: Versioning & testing in llms](https://www.youtube.com/watch?v=6RmfAyeAoYs&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=45)
46. [W10_L4: CI&CD for LLMs](https://www.youtube.com/watch?v=twJ7gRs7Dnc&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=46)
47. [W10_L5: Handson: LLM finetuning](https://www.youtube.com/watch?v=rCNNbpyULf0&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=47)
48. [W11_L1: LLM accuracy](https://www.youtube.com/watch?v=b7SQViYCcII&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=48)
49. [W11_L2: Proprietary LLMs](https://www.youtube.com/watch?v=xkOFdcnZcuE&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=49)
50. [W11_L3: LLM serving, cost control](https://www.youtube.com/watch?v=wNM4Y39D__U&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=50)
51. [W11_L4: LLM observability, security, governance & best practices](https://www.youtube.com/watch?v=I-Ju8sCARqo&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=51)
52. [W11_L5: Handson: LLM usage and security](https://www.youtube.com/watch?v=mEcY-CdAX1A&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=52)
53. [Machine Learning Operations (MLOps)](https://www.youtube.com/watch?v=Ub9pCxSFfgQ&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=53)
54. [Machine Learning Operations (MLOps)](https://www.youtube.com/watch?v=vEBahj6fOjE&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=54)
55. [Machine Learning Operations (MLOps)](https://www.youtube.com/watch?v=Eog1ssY-eLs&list=PLZ2ps__7DhBaAR2w3oX5yMIQA8pUo5zt2&index=55)

</details>


## Books, notes and websites

- Book: *Engineering MLOps* (Emmanuel Raj)
- madewithml.com
- DataTalksClub MLOps Zoomcamp
- Docker and MLflow docs

## Practice / proof of understanding

Take one earlier model and ship it: tracked experiments, containerised API, a monitoring dashboard.

## What your IITM course sheet says

### From the PDF: DA3408

**Official description:** This course addresses the "Production Gap" in Artificial Intelligence. While deep learning courses focus on model  architectures, AI Operations (AIOps/MLOps) focuses on the support ecosystem required to build seamless,  reproducible, fault-tolerant, and productive AI systems. Students will master the lifecycle of AI—from distributed  data processing and experiment tracking to scalable model serving using a strictly open-source ecosystem.  Course Objectives  ? To understand the technical debt and infrastructure challenges inherent in AI systems.  ? To master the automation of data pipelines, model training, and deployment (CI/CD/CT).  ? To design and manage the end-to-end lifecycle of machine learning and generative AI systems.  ? To implement distributed computing patterns for large-scale data and model training.  ? To ensure reproducibility through rigorous experiment tracking and versi

**Official syllabus (trimmed):**

> Module 1: Experiment Management & Reproducibility
> ? The "Hidden Technical Debt" in AI Systems.
> ? MLOps vs. DevOps: Data Gravity and Model Decay.
> ? Experiment Tracking: Logging parameters, metrics, and artifacts with MLflow.
> ? Reproducibility: Versioning code (Git), Data (DVC), and Models (MLflow Model Registry).
> ? Case Studies:
> ? Auditing a healthcare model's training history for regulatory compliance.
> ? Resolving "it worked on my machine" issues using environment versioning.
> Module 2: Distributed Computing for Data & Models
> ? Data at Scale: Distributed ETL and feature engineering with Apache Spark.
> ? Distributed Computing: Introduction to Ray for scaling Python workloads.
> ? Distributed Training: Data Parallelism vs. Model Parallelism (Ray Train).
> ? Feature Stores: Implementing an open-source feature layer with Feast.
> ? Data Quality Validation (Great Expectations).
> ? Case Studies:
> ? Scaling a recommendation engine's feature pipeline to handle millions of users.
> ? Training a Large Language Model across a multi-node GPU cluster.
> ? Handling "Data Drift" in a credit scoring system.
> ? Building a real-time feature pipeline for a recommendation engine.
> Module 3: Infrastructure & Containerization
> ? Building reproducible environments with Docker.
> ? Introduction to Kubernetes for AI workloads.
> ? GPU Scheduling and Resource Management.
> ? Containerization: Advanced Docker patterns for AI (

**Official textbooks:** Engineering MLOps: Rapidly build, test, and manage production-ready machine learning life cycles at scale  by Emmanuel Raj

**Official references:** ? Distributed Systems: Learning Ray by Max Pumperla, Edward Oakes, and Richard Liaw (O'Reilly).  ? Data Scaling: Spark: The Definitive Guide by Bill Chambers and Matei Zaharia.  ? Production AI: Reliable Machine Learning by Cathy Chen et al. (O'Reilly).  ? Open Source Documentation: MLflow, Kubeflow, Ray.io.

### From the PDF: DA5402

**Official description:** This course aims to give students a comprehensive understanding of Machine Learning Operations (MLOps).  MLOpsis an emerging discipline that deploys, manages, and optimizes machine learning models in production  environments.The course will cover various aspects of MLOps, including model development, version control,  testing, deployment,monitoring, and scaling. Students will gain hands-on experience with popular MLOps tools and  frameworks, enablingthem to manage machine learning workflows effectively and deliver robust and scalable ML  solutions.

**Official syllabus (trimmed):**

> 1. Introduction to MLOps: Overview of MLOps and its significance : Key challenges in deploying and managing
>  MLmodels in production, Comparison of traditional software development and MLOps, Key components of
>  MLOps,MLOps workflow, Landscape of MLOps tools and technologies, Practice: Build a simple scripts-based
>  automationpipeline for image classification2. Data Engineering for MLOps: Overviews of data engineering tools
>  and technologies, Data pipeline design andimplementation, Data quality and data governance, Data engineering
>  illustration through Apache Airflow, Beam,Flume, Kafka, Spark3. Version Control and Collaboration in MLOps:
>  Introduction to Git and GitHub/GitLab, Branching and mergingstrategies for ML projects, Managing large datasets
>  using Git LFS (Large File Storage), Introduction to DVC (DataVersion Control)4. Machine Learning Model
>  Development Pipelines: Overviews of popular machine learning frameworks and libraries,Data preprocessing and
>  feature engineering, Introduction to MLflow for model development and monitoring, Introductionto Ray for
>  distributed training and hyperparameter tuning5. Model Deployment and Serving: Overview of containerization and
>  orchestration technologies, Overview of cloudbaseddeployment options, Building Docker images for ML
>  applications, Deployment strategies for different environments(cloud, edge, on-premises), Deploying models u

**Official textbooks:** 1. Engineering MLOps – Emmanuel Raj – Packt publication2. Introducing MLOps – Mark Traveil & The Dataiku  Team – O’Reilly publication

**Official references:** 1. Engineering MLOps – Emmanuel Raj – Packt publication2. Introducing MLOps – Mark Traveil & The Dataiku  Team – O’Reilly publication
