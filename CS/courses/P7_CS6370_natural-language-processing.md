# CS6370 — Natural Language Processing

| | |
|---|---|
| Tier | B |
| Phase (order) | 7 |
| Do this first | CS4011, CS6910 |
| Estimated effort | 12 weeks |
| Unlocks | DA6800, CS7016 |

## Roadmap

1. Tokenisation, n-grams, edit distance, language models.
2. Embeddings, sequence models, attention.
3. Transformers, pretraining and fine-tuning, evaluation.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Stanford CS224N Natural Language Processing with Deep Learning I Spring 2024 I Professor Christopher Manning](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D) (23 videos). Stanford CS224N *NLP with Deep Learning* (official Stanford Online): word vectors to transformers and LLMs.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Introduction to Natural Language Processing (i-NLP)](https://www.youtube.com/playlist?list=PLZ2ps__7DhBY8Mbke8rzGsACDQlIOcCqH) (61 videos). IIT Madras BS *Introduction to Natural Language Processing*: classical NLP (n-grams, POS, parsing) the IITM course also covers.
- [Introduction to large language models](https://www.youtube.com/playlist?list=PLZ2ps__7DhBbaMNZoyW2Hizl8DG6ikkjo) (55 videos). IIT Madras BS *Introduction to Large Language Models* (Mitesh Khapra).
- [Introduction to Large Language Models (LLMs)](https://www.youtube.com/playlist?list=PLp6ek2hDcoNDDRINFiWGDlPKUwW-g1Hjk) (38 videos). NPTEL *Introduction to Large Language Models* (IIT Delhi).

### ⚡ Short videos for intuition and revision

- [Hugging Face Course](https://www.youtube.com/playlist?list=PLo2EIpI_JMQvWfQndUesu0nPBAtZ9gP1o) (80 videos). Hugging Face *Course* videos: the practical transformers library side.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=DzpHeXVSC5I&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=1)–[2](https://www.youtube.com/watch?v=nBor4jfWetQ&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=2) | Word vectors and language models. Assignment 1 (word2vec). |
| 2 | [3](https://www.youtube.com/watch?v=HnliVHU2g9U&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=3)–[4](https://www.youtube.com/watch?v=KVKvde-_MYc&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=4), [21](https://www.youtube.com/watch?v=8j4wpU98Q74&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=21)–[22](https://www.youtube.com/watch?v=Uv0AIRr3ptg&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=22) | Backprop, dependency parsing; Python and PyTorch tutorials. Assignment 2: neural dependency parser. |
| 3 | [5](https://www.youtube.com/watch?v=fyc0Jzr74y4&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=5)–[7](https://www.youtube.com/watch?v=J7ruSOIzhrE&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=7) | RNNs, LSTMs, seq2seq, attention. Assignment 3: NMT with attention. |
| 4 | [8](https://www.youtube.com/watch?v=LWMzyfvuehA&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=8)–[9](https://www.youtube.com/watch?v=DGfCRXuNA2w&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=9), [23](https://www.youtube.com/watch?v=b80by3Xk_A8&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=23) | Transformers and pretraining; Hugging Face tutorial. Fine-tune BERT on a classification task. |
| 5 | [10](https://www.youtube.com/watch?v=N9L32bFieEY&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=10)–[13](https://www.youtube.com/watch?v=UVX7SYGCKkA&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=13) | Generation, post-training, benchmarking, efficient training. |
| 6 | [14](https://www.youtube.com/watch?v=tfVgHsKpRC8&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=14)–[20](https://www.youtube.com/watch?v=cd3pRpEtjLs&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=20) | Reasoning and agents, DPO, multimodal, interpretability, linguistics. Final project: build and evaluate a small RAG or fine-tuning project. |

<details>
<summary>All lectures in <i>Stanford CS224N Natural Language Processing with Deep Learning I Spring 2024 I Professor Christopher Manning</i> (23 videos)</summary>

1. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 1 - Intro and Word Vectors](https://www.youtube.com/watch?v=DzpHeXVSC5I&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=1)
2. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 2 - Word Vectors and Language Models](https://www.youtube.com/watch?v=nBor4jfWetQ&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=2)
3. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 3 - Backpropagation, Neural Network](https://www.youtube.com/watch?v=HnliVHU2g9U&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=3)
4. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 4 - Dependency Parsing](https://www.youtube.com/watch?v=KVKvde-_MYc&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=4)
5. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 5 - Recurrent Neural Networks](https://www.youtube.com/watch?v=fyc0Jzr74y4&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=5)
6. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 6 - Sequence to Sequence Models](https://www.youtube.com/watch?v=Ba6Fn1-Jsfw&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=6)
7. [Stanford CS224N: NLP w/ DL | Spring 2024 | Lecture 7 - Attention, Final Projects and LLM Intro](https://www.youtube.com/watch?v=J7ruSOIzhrE&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=7)
8. [Stanford CS224N NLP with Deep Learning | 2023 | Lecture 8 - Self-Attention and Transformers](https://www.youtube.com/watch?v=LWMzyfvuehA&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=8)
9. [Stanford CS224N NLP with Deep Learning | 2023 | Lecture 9 - Pretraining](https://www.youtube.com/watch?v=DGfCRXuNA2w&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=9)
10. [Stanford CS224N NLP with Deep Learning | 2023 | Lecture 11 - Natural Language Generation](https://www.youtube.com/watch?v=N9L32bFieEY&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=10)
11. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 10 - Post-training by Archit Sharma](https://www.youtube.com/watch?v=35X6zlhoCy4&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=11)
12. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 11 - Benchmarking by Yann Dubois](https://www.youtube.com/watch?v=TO0CqzqiArM&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=12)
13. [Stanford CS224N: NLP w/ DL | Spring 2024 | Lecture 12 - Efficient Training, Shikhar Murty](https://www.youtube.com/watch?v=UVX7SYGCKkA&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=13)
14. [Stanford CS224N: NLP w/ DL| Spring 2024 | Lecture 13 - Brain-Computer Interfaces, Chaofei Fan](https://www.youtube.com/watch?v=tfVgHsKpRC8&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=14)
15. [Stanford CS224N: NLP w/ DL | Spring 2024 | Lecture 14 - Reasoning and Agents by Shikhar Murty](https://www.youtube.com/watch?v=I0tj4Y7xaOQ&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=15)
16. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 15 - After DPO by Nathan Lambert](https://www.youtube.com/watch?v=dnF463_Ar9I&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=16)
17. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 16 - ConvNets and TreeRNNs](https://www.youtube.com/watch?v=S8d-7v3f5MQ&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=17)
18. [Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 18 - NLP, Linguistics, Philosophy](https://www.youtube.com/watch?v=NxH0Y78xcF4&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=18)
19. [Stanford CS224N NLP with Deep Learning | 2023 | Lecture 16 - Multimodal Deep Learning, Douwe Kiela](https://www.youtube.com/watch?v=5vfIT5LOkR0&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=19)
20. [Stanford CS224N NLP with Deep Learning | 2023 | Lec. 19 - Model Interpretability & Editing, Been Kim](https://www.youtube.com/watch?v=cd3pRpEtjLs&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=20)
21. [Stanford CS224N NLP with Deep Learning | 2023 | Python Tutorial, Manasi Sharma](https://www.youtube.com/watch?v=8j4wpU98Q74&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=21)
22. [Stanford CS224N NLP with Deep Learning | 2023 | PyTorch Tutorial,  Drew Kaul](https://www.youtube.com/watch?v=Uv0AIRr3ptg&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=22)
23. [Stanford CS224N NLP with Deep Learning | 2023 | Hugging Face Tutorial, Eric Frankel](https://www.youtube.com/watch?v=b80by3Xk_A8&list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D&index=23)

</details>


## Books, notes and websites

- Jurafsky & Martin, *Speech and Language Processing* — web.stanford.edu/~jurafsky/slp3 (free)
- Stanford CS224n; Hugging Face NLP course
- Karpathy's `nanoGPT`

## Practice / proof of understanding

Build a spell-corrector, a sentiment classifier, and fine-tune a small transformer on a text task.

## What your IITM course sheet says

### From the PDF: CS6370

**Official description:** Introduction to NLP; Computational models of language; Organization of  NLP systems. Syntax; Linguistic background; Elements of simple  sentences; Parsing techniques; Features and augmented grammars;  Deterministic parsing. Semantics; Logical form; Case relations; Semantic  networks; Basic operations for semantic interpretation; Strategies and  issues. Context and world knowledge; Knowledge representation;  Reference; question; Answering systems; Natural language generation;  Typical NLP systems and their architectures; cognitive aspects of natural  languages. Indian language processing; Approach to machine translation;  Typical case studies

**Official syllabus (trimmed):**

> The objective of this course is to introduce central challenges in making machines analyze, understand and
>  generate natural languages, and present computational approaches to address some of these foundational
>  problems. The thrust would be on empirical (statistical) methods, though we will contrast the same with
>  rationalistic (symbolic) approaches in the context of our discussion.

**Official textbooks:** 1. JM Daniel Jurafsky and James H. Martin, Speech and Language Processing. Prentice Hall, 2000 (as well as  later editions of the book available online) Christopher D. Manning and Hinrich Schutze, Foundations of Statistical  Natural Language Processing, MIT Press, 1999

**Official references:** 1. Material from the following books may be used as necessary. CHA Eugene Charniak, Statistical language  learning. MIT Press, 1993 BKL S. Bird, E. Klein and E. Loper, Natural language processing with Python, O’Reilly,  2009 The course relies a lot on survey and research papers, tutorial material and workbooks.
