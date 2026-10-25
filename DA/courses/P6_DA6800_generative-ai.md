# DA6800 — Generative AI

| | |
|---|---|
| Tier | B |
| Phase (order) | 6 |
| Do this first | DA3409 |
| Estimated effort | 8-10 weeks |
| Unlocks | DA7016, DA5453 |

## Roadmap

1. LLM architecture, prompting, RAG, fine-tuning; diffusion models; responsible AI.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Stanford CS236: Deep Generative Models I 2023 I Stefano Ermon](https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8) (18 videos). Stanford CS236 *Deep Generative Models* (Stefano Ermon, 2023, official): VAEs, flows, GANs, energy models, diffusion.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [MIT 6.S184: Flow Matching and Diffusion Models (2026)](https://www.youtube.com/playlist?list=PL57nT7tSGAAXwjhDYcxEycx5W7YoSrZyt) (6 videos). MIT 6.S184 *Flow Matching and Diffusion Models* (2026): the modern image/video generation maths, with labs.
- [Stanford CS25 - Transformers United](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM) (50 videos). Stanford CS25 *Transformers United* (official): guest lectures from the people who built the models.
- [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) (10 videos). Karpathy *Zero to Hero*: build a GPT from scratch.

### ⚡ Short videos for intuition and revision

- [Diffusion Models Course Event](https://www.youtube.com/playlist?list=PLo2EIpI_JMQtk-IGGzoRatuoyXHfSKc7L) (6 videos). Hugging Face *Diffusion Models Course* event talks.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=XZ0PMRWXBEU&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=1)–[4](https://www.youtube.com/watch?v=bt3dqcbMLa0&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=4) | Background, autoregressive models, maximum likelihood. Train a character-level autoregressive model. |
| 2 | [5](https://www.youtube.com/watch?v=MAGBUh77bNg&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=5)–[6](https://www.youtube.com/watch?v=8cO61e_8oPY&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=6) | VAEs. Train a VAE on MNIST. |
| 3 | [7](https://www.youtube.com/watch?v=m6dKKRsZwBQ&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=7)–[10](https://www.youtube.com/watch?v=M3Fkvu78ZXc&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=10) | Normalizing flows, GANs. Train a DCGAN. |
| 4 | [11](https://www.youtube.com/watch?v=m61KiAMCJ5Q&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=11)–[14](https://www.youtube.com/watch?v=E69Lp_T9nVg&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=14) | Energy-based and score-based models. |
| 5 | [15](https://www.youtube.com/watch?v=MJt_ahtO-to&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=15)–[18](https://www.youtube.com/watch?v=mCaRNnEnYwA&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=18) | Evaluation, score-based diffusion, discrete latent variables, discrete diffusion. Implement DDPM on MNIST. |

<details>
<summary>All lectures in <i>Stanford CS236: Deep Generative Models I 2023 I Stefano Ermon</i> (18 videos)</summary>

1. [Stanford CS236: Deep Generative Models I 2023 I Lecture 1 - Introduction](https://www.youtube.com/watch?v=XZ0PMRWXBEU&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=1)
2. [Stanford CS236: Deep Generative Models I 2023 I Lecture 2 - Background](https://www.youtube.com/watch?v=rNEujZmD2Tg&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=2)
3. [Stanford CS236: Deep Generative Models I 2023 I Lecture 3 - Autoregressive Models](https://www.youtube.com/watch?v=tRArbBf-AbI&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=3)
4. [Stanford CS236: Deep Generative Models I 2023 I Lecture 4 - Maximum Likelihood Learning](https://www.youtube.com/watch?v=bt3dqcbMLa0&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=4)
5. [Stanford CS236: Deep Generative Models I 2023 I Lecture 5 - VAEs](https://www.youtube.com/watch?v=MAGBUh77bNg&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=5)
6. [Stanford CS236: Deep Generative Models I 2023 I Lecture 6 - VAEs](https://www.youtube.com/watch?v=8cO61e_8oPY&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=6)
7. [Stanford CS236: Deep Generative Models I 2023 I Lecture 7 - Normalizing Flows](https://www.youtube.com/watch?v=m6dKKRsZwBQ&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=7)
8. [Stanford CS236: Deep Generative Models I 2023 I Lecture 8 - Normalizing Flows](https://www.youtube.com/watch?v=qgTvgBCOyn8&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=8)
9. [Stanford CS236: Deep Generative Models I 2023 I Lecture 9 - GANs](https://www.youtube.com/watch?v=3Zv-gokhLu8&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=9)
10. [Stanford CS236: Deep Generative Models I 2023 I Lecture 10 - GANs](https://www.youtube.com/watch?v=M3Fkvu78ZXc&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=10)
11. [Stanford CS236: Deep Generative Models I 2023 I Lecture 11 - Energy Based Models](https://www.youtube.com/watch?v=m61KiAMCJ5Q&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=11)
12. [Stanford CS236: Deep Generative Models I 2023 I Lecture 12 - Energy Based Models](https://www.youtube.com/watch?v=Nci1Bepcy0g&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=12)
13. [Stanford CS236: Deep Generative Models I 2023 I Lecture 13 - Score Based Models](https://www.youtube.com/watch?v=8G-OsDs1RLI&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=13)
14. [Stanford CS236: Deep Generative Models I 2023 I Lecture 14 - Energy Based Models](https://www.youtube.com/watch?v=E69Lp_T9nVg&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=14)
15. [Stanford CS236: Deep Generative Models I 2023 I Lecture 15 - Evaluation of Generative Models](https://www.youtube.com/watch?v=MJt_ahtO-to&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=15)
16. [Stanford CS236: Deep Generative Models I 2023 I Lecture 16 - Score Based Diffusion Models](https://www.youtube.com/watch?v=VsllsC2JMGY&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=16)
17. [Stanford CS236: Deep Generative Models I 2023 I Lecture 17 - Discrete Latent Variable Models](https://www.youtube.com/watch?v=vBv7Mf1zsg8&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=17)
18. [Stanford CS236: Deep Generative Models I 2023 I Lecture 18 - Diffusion Models for Discrete Data](https://www.youtube.com/watch?v=mCaRNnEnYwA&list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8&index=18)

</details>


## Books, notes and websites

- Karpathy *Zero to Hero*; Hugging Face courses; Stanford CS336
- Lilian Weng's blog; *Attention Is All You Need*

## Practice / proof of understanding

Build a RAG app over your own documents, and fine-tune a small model with LoRA.

## What your IITM course sheet says

### From the PDF: DA6800

**Official description:** Equip participants with the foundational knowledge, practical skills, and strategic insights to identify, build, and  deploy Generative AI solutions within their organizations

**Official syllabus (trimmed):**

> Module 1: Foundations of Generative AI
>  ? Core Concepts: Generative vs. Discriminative AI; key terminology; major categories; industry applications.
>  ? Responsible AI: Ethical considerations, bias, fairness, misinformation, data privacy.
>  ? Hands-on: Environment setup; first GenAI interactions (OpenAI API, Hugging Face Hub).
>  ? Module 2: Mastering Large Language Models (LLMs) for Text
>  ? LLM Architecture & Capabilities: Transformers; pre-training/fine-tuning; popular LLMs.
>  ? Prompt Engineering: Crafting effective prompts; zero-shot, few-shot, chain-of-thought.
>  ? Hands-on: Advanced prompt engineering exercises.
>  ? Building LLM Applications: Frameworks (LangChain/LlamaIndex); RAG.
>  ? Hands-on: Building a Q&A bot with RAG.
>  ? Fine-tuning LLMs: When to fine-tune; PEFT methods (LoRA).
>  ? Hands-on: Fine-tuning a smaller LLM or exploring LoRA.
>  ? Module 3: Generating and Manipulating Images & Multimodal AI
>  ? Image Generation Models: GANs overview; Diffusion Models (Stable Diffusion).
>  ? Hands-on: Text-to-image generation with Stable Diffusion; prompt engineering for images.
>  ? Hands-on: AI-powered image editing (inpainting, outpainting).
>  ? Multimodal AI: Combining text, image, audio; applications (captioning, VQA, TTS, STT).
>  ? Hands-on: Practical exercises with multimodal models (image captioning, TTS/STT).
>  ? Module 4: Advanced Topics & Industry Integration
>  ? GenAI for Code & O

**Official textbooks:** Primarily based on current research papers, and practical guides for tools such as Hugging Face (Transformers,  Diffusers), OpenAI API, LangChain, and LlamaIndex. Specific readings and  resources will be provided per module. No single textbook comprehensively covers the rapid evolution of this field.

**Official references:** Relevant research papers (e.g., "Attention Is All You Need", Denoising Diffusion Probabilistic Models).  ? Articles and publications from leading AI research labs and conferences (NeurIPS, ICML, CVPR etc.).  ? Online courses and tutorials from platforms like DeepLearning.AI, Coursera, and fast.ai.
