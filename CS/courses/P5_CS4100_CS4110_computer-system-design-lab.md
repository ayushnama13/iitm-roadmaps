# CS4100+CS4110 — Computer System Design (+ lab)

| | |
|---|---|
| Tier | B |
| Phase (order) | 5 |
| Do this first | CS2600, CS3500 |
| Estimated effort | 10-12 weeks |
| Unlocks | CS6886, CS6847 |

## Roadmap

1. Building blocks: CPU, storage, I/O.
2. Performance specification and measurement.
3. Integration and distributed resources.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Livestream - Computer Architecture - ETH Zürich (Fall 2023)](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe) (32 videos). Onur Mutlu *Computer Architecture* (ETH Zurich, Fall 2023): memory systems, caches, prefetching, multicore.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Advanced Computer Architecture](https://www.youtube.com/playlist?list=PLwdnzlV3ogoWJhBxBYu-K4l-q-nNHd24D) (34 videos). NPTEL *Advanced Computer Architecture* (IIT Guwahati).
- [Advanced Computer Architecture](https://www.youtube.com/playlist?list=PL1iLu2CSC9EWZMIh4_V5dGroMAwA84Lmz) (58 videos). Smruti Sarangi (IIT Delhi) *Advanced Computer Architecture*: he also wrote a free textbook.
- [Spring 2015 -- Computer Architecture Lectures -- Carnegie Mellon](https://www.youtube.com/playlist?list=PL5PHm2jkkXmi5CxxI7b3JCL1TWybTDtKq) (39 videos). CMU 18-447 Spring 2015 (Onur Mutlu): official CMU recording.

### ⚡ Short videos for intuition and revision

- [Multi-Core Computer Architecture](https://www.youtube.com/playlist?list=PLwdnzlV3ogoUT7g3BySY2QQesG3eB4dss) (49 videos). NPTEL *Multi-Core Computer Architecture* (IIT Guwahati).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=6CNeDUk3fJA&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=1)–[2](https://www.youtube.com/watch?v=fqWNVGcVL2o&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=2) | Intro + memory systems challenges. |
| 2-3 | [9](https://www.youtube.com/watch?v=HToR2HGyCeU&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=9), [12](https://www.youtube.com/watch?v=UpBs8kvbqDI&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=12)–[14](https://www.youtube.com/watch?v=BgF9DsdLtHM&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=14), [31](https://www.youtube.com/watch?v=rXGGSYYYwh8&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=31)–[32](https://www.youtube.com/watch?v=BGaLNhyr-2Q&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=32) | Memory latency, memory controllers, prefetching, virtual memory, cache design. Write a cache simulator (or use gem5). |
| 4 | [18](https://www.youtube.com/watch?v=r1GmCoVQ_hA&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=18)–[21](https://www.youtube.com/watch?v=bAYoGl042JE&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=21) | Parallelism, multiprocessors, cache coherence, interconnects. |
| 5 | [27](https://www.youtube.com/watch?v=nHHsYp7ZkHQ&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=27)–[30](https://www.youtube.com/watch?v=xz9DO-4Pkko&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=30) | VLIW, systolic arrays (TPU-style), SIMD and GPU architecture, GPU programming. |
| 6 | [3](https://www.youtube.com/watch?v=GTLhs7SIVtE&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=3), [5](https://www.youtube.com/watch?v=WPSd93rOXqs&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=5), [15](https://www.youtube.com/watch?v=ylqDue6XFeM&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=15)–[17](https://www.youtube.com/watch?v=mxyEqvemQ90&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=17) | Processing-in-memory, emerging memories, flash/SSDs. |
| 7 | [22](https://www.youtube.com/watch?v=5lybMDZHBBQ&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=22), [26](https://www.youtube.com/watch?v=6abzvI9xzRI&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=26) | Simulation and on-chip networks. Project: extend your RISC-V CPU (CS2600 lab) with a cache and branch predictor. |

<details>
<summary>All lectures in <i>Livestream - Computer Architecture - ETH Zürich (Fall 2023)</i> (32 videos)</summary>

1. [Computer Architecture - Lecture 1: Introduction and Basics (Fall 2023)](https://www.youtube.com/watch?v=6CNeDUk3fJA&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=1)
2. [Computer Architecture - Lecture 2: Memory Systems: Challenges and Opportunities (Fall 2023)](https://www.youtube.com/watch?v=fqWNVGcVL2o&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=2)
3. [Computer Architecture - Lecture 3: Processing near Memory (Fall 2023)](https://www.youtube.com/watch?v=GTLhs7SIVtE&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=3)
4. [Computer Architecture - Lecture 4: Programming a Real-world PIM Arch. and Enabling PIM (Fall 2023)](https://www.youtube.com/watch?v=FBV579jtxj8&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=4)
5. [Computer Architecture - Lecture 5: Processing using Memory (Fall 2023)](https://www.youtube.com/watch?v=WPSd93rOXqs&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=5)
6. [Computer Architecture - Lecture 6: Memory Security, Reliability Problems and Solutions (Fall 2023)](https://www.youtube.com/watch?v=PTDjgPUB8tQ&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=6)
7. [Computer Architecture - Lecture 7: Cutting Edge Research on DRAM Read Disturbance (Fall 2023)](https://www.youtube.com/watch?v=O3IXOFsyvFo&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=7)
8. [Computer Architecture - Lecture 8: Data Retention and Memory Refresh (Fall 2023)](https://www.youtube.com/watch?v=XKNU0A2GAnM&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=8)
9. [Computer Architecture - Lecture 9: Memory Latency (Fall 2023)](https://www.youtube.com/watch?v=HToR2HGyCeU&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=9)
10. [Computer Architecture - Lecture 10: Genome Analysis (Fall 2023)](https://www.youtube.com/watch?v=EH5EfcE-lSI&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=10)
11. [Computer Architecture - Lecture 11: Cutting-Edge Research in Computer Architecture (Fall 2023)](https://www.youtube.com/watch?v=tzyPB20NfaI&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=11)
12. [Computer Architecture - Lecture 12: Memory Controllers (Fall 2023)](https://www.youtube.com/watch?v=UpBs8kvbqDI&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=12)
13. [Computer Architecture - Lecture 13: Memory Controllers II & Prefetching (Fall 2023)](https://www.youtube.com/watch?v=FvP2tmVvNSM&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=13)
14. [Computer Architecture - Lecture 14: Prefetching II (Fall 2023)](https://www.youtube.com/watch?v=BgF9DsdLtHM&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=14)
15. [Computer Architecture - Lecture 15: Emerging Memory Technologies (Fall 2023)](https://www.youtube.com/watch?v=ylqDue6XFeM&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=15)
16. [Computer Architecture - Lecture 16: Flash Memory and Solid-State Drives (Fall 2023)](https://www.youtube.com/watch?v=lzC-choGjgo&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=16)
17. [Computer Architecture - Lecture 17: Flash Memory and Solid-State Drives II (Fall 2023)](https://www.youtube.com/watch?v=mxyEqvemQ90&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=17)
18. [Computer Architecture - Lecture 18: Parallelism & Heterogeneity (Fall 2023)](https://www.youtube.com/watch?v=r1GmCoVQ_hA&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=18)
19. [Computer Architecture - Lecture 19: Multiprocessors and Memory Ordering (Fall 2023)](https://www.youtube.com/watch?v=xQjyaQtAZCg&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=19)
20. [Computer Architecture - Lecture 20: Cache Coherence (Fall 2023)](https://www.youtube.com/watch?v=lt0bUdwW1II&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=20)
21. [Computer Architecture - Lecture 21: Interconnects (Fall 2023)](https://www.youtube.com/watch?v=bAYoGl042JE&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=21)
22. [Computer Architecture - Lecture 22: Simulation (Fall 2023)](https://www.youtube.com/watch?v=5lybMDZHBBQ&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=22)
23. [Computer Architecture - Lecture 23: Cutting-Edge Research in Computer Architecture  (Fall 2023)](https://www.youtube.com/watch?v=teb8jc3U1JY&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=23)
24. [Computer Architecture - Lecture 24: Discussion Session (Fall 2023)](https://www.youtube.com/watch?v=wrUMqaydnWc&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=24)
25. [Computer Architecture - Lecture 25: Cutting-Edge Research in Computer Architecture  (Fall 2023)](https://www.youtube.com/watch?v=jzcQ0KBxI3s&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=25)
26. [Computer Architecture - Lecture 26: On-Chip Networks (Fall 2023)](https://www.youtube.com/watch?v=6abzvI9xzRI&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=26)
27. [Computer Architecture - Lecture 27: VLIW Architectures (Fall 2023)](https://www.youtube.com/watch?v=nHHsYp7ZkHQ&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=27)
28. [Computer Architecture - Lecture 28: Systolic Array Architectures (Fall 2023)](https://www.youtube.com/watch?v=XkgtANeDrm8&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=28)
29. [Computer Architecture - Lecture 29: SIMD & GPU Architectures (Fall 2023)](https://www.youtube.com/watch?v=Kj8Hgc80VYo&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=29)
30. [Computer Architecture - Lecture 30: GPU Programming (Fall 2023)](https://www.youtube.com/watch?v=xz9DO-4Pkko&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=30)
31. [Computer Architecture - Lecture 31: Virtual Memory (Fall 2023)](https://www.youtube.com/watch?v=rXGGSYYYwh8&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=31)
32. [Computer Architecture - Lecture 32: Cache Design and Management (Fall 2023)](https://www.youtube.com/watch?v=BGaLNhyr-2Q&list=PL5Q2soXY2Zi9UFWwfRtSjpKX_IRF0lPSe&index=32)

</details>


## Books, notes and websites

- Book: Wolf, *Computers as Components*
- Book: Heuring & Jordan, *Computer Systems Design and Architecture*
- Book: Bryant & O'Hallaron, *CS:APP*; CMU 15-213 lectures

## Practice / proof of understanding

Profile a program with `perf`, find the bottleneck, and improve it by 2x.

## What your IITM course sheet says

### From the PDF: CS4100

**Official description:** Basic principles of System Design: system components in simple system; Workstations, servers.  Building blocks for Computer Systems; CPU, Storage, I/O, Multimedia devices The hardware-software interface,  Hardware features influenced by software requirements.  Specifications of the performance of a system.  How to effectively utilize the strength of a component to get improvement in performance?  Testing systems for performance.  Computing with distributed resources.  Basic principles of system integration, when building larger systems.

**Official textbooks:** 1. Wayne Hendrix Wolf, "Computers as Components: Principles of Embedded Computer Systems Design",  Academic Press 2001.  2. Vincent P. Heuring and Harry F. Jordan, "Computer Systems Design and Architecture", Pearson Education Asia,  2001.

### From the PDF: CS4110

**Official description:** Students are expected to design modules and sub-systems which may be put together to form computers. Several  experiments are included for software design for computer systems. These will be based on workstations and  development systems working in a networked environment.  The laboratory experiments will supplement the lectures given in the course CS 410.

**Official textbooks:** NIL
