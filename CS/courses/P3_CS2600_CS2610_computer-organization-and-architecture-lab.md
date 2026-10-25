# CS2600+CS2610 — Computer Organization and Architecture (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | CS2300 (or at least gates + assembly idea) |
| Estimated effort | 12 weeks |
| Unlocks | CS3500, CS4100, CS6600 |

## Roadmap

1. Instruction set architectures, addressing modes, function calls, stack frames (RISC-V/ARM/x86).
2. Single-cycle datapath and control; then pipelining and hazards.
3. Caches and memory hierarchy; virtual memory.
4. Superscalar, multithreaded, multicore basics.
5. Lab: assembly programs, multi-precision arithmetic, calling C from assembly, and a simulator for caches/branch predictors.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Computer Sc - Computer Organization](https://www.youtube.com/playlist?list=PL1A5A6AE8AFC187B7) (33 videos). NPTEL *Computer Organization* (nptelhrd, IIT Madras).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Livestream - Digital Design and Computer Architecture (Spring 2026)](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi-yo9kK-BKrq11ykNKkVEpd) (51 videos). Onur Mutlu *Digital Design and Computer Architecture* (ETH Zurich, Spring 2026 livestream). World-class; do the labs.
- [computer Organization](https://www.youtube.com/playlist?list=PLUQpHm_JtukJXJV6OekM0DZVnm0I5m5kk) (76 videos). IIT Madras BS *Computer Organization*.
- [Computer Architecture and Organisation](https://www.youtube.com/playlist?list=PL-8LShlBMIjUuI9beQJHZUF14we25NToB) (63 videos). NPTEL *Computer Architecture and Organisation* (IIT Kharagpur): very thorough on pipelines and memory.
- [[CS61C FA20] Lectures - Great Ideas in Computer Architecture | UC, Berkeley](https://www.youtube.com/playlist?list=PL0j-r-omG7i0-mnsxN5T4UcVS1Di0isqf) (100+ videos). Berkeley CS61C Fall 2020 (re-upload by a viewer, not the official channel): C + RISC-V + caches + parallelism.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1-2 | [1](https://www.youtube.com/watch?v=leWKvuZVUE8&list=PL1A5A6AE8AFC187B7&index=1)–[5](https://www.youtube.com/watch?v=piuWSMLNeco&list=PL1A5A6AE8AFC187B7&index=5) | Computing systems overview, processor activities, processor as a state machine. |
| 3-4 | [6](https://www.youtube.com/watch?v=ceuXLsuZhLE&list=PL1A5A6AE8AFC187B7&index=6)–[14](https://www.youtube.com/watch?v=hhvl7nbVpLo&list=PL1A5A6AE8AFC187B7&index=14) | Datapath, microprogrammed vs hardwired control, addressing modes. Write small RISC-V assembly programs (RARS simulator). |
| 5-6 | [15](https://www.youtube.com/watch?v=tas2eUavhRE&list=PL1A5A6AE8AFC187B7&index=15)–[18](https://www.youtube.com/watch?v=Opp-annh9sg&list=PL1A5A6AE8AFC187B7&index=18) | Memory system and caches. Simulate a direct-mapped cache in Python. |
| 7 | [19](https://www.youtube.com/watch?v=e9w_XERZ2UM&list=PL1A5A6AE8AFC187B7&index=19)–[23](https://www.youtube.com/watch?v=G0rbpTX_ytE&list=PL1A5A6AE8AFC187B7&index=23) | Virtual memory, segmentation, address translation. |
| 8-9 | [24](https://www.youtube.com/watch?v=aGvMubj8NXk&list=PL1A5A6AE8AFC187B7&index=24)–[33](https://www.youtube.com/watch?v=ZKBLirP5jo8&list=PL1A5A6AE8AFC187B7&index=33) | I/O: programmed, interrupt-driven, DMA, buses. |
| 10-12 | Mutlu ETH (alt) | Pipelining, hazards, branch prediction, out-of-order. Build a 5-stage pipelined RISC-V CPU in Verilog (lab). |

<details>
<summary>All lectures in <i>Computer Sc - Computer Organization</i> (33 videos)</summary>

1. [Lecture - 1 Introduction To Computing](https://www.youtube.com/watch?v=leWKvuZVUE8&list=PL1A5A6AE8AFC187B7&index=1)
2. [Lecture - 2 Introduction To System : Software](https://www.youtube.com/watch?v=VG9VopzV_T0&list=PL1A5A6AE8AFC187B7&index=2)
3. [Lecture - 3 Introduction To System : Hardware](https://www.youtube.com/watch?v=FOyuMclwymw&list=PL1A5A6AE8AFC187B7&index=3)
4. [Lecture - 4 Processor Activities](https://www.youtube.com/watch?v=Zm1saVDpS7g&list=PL1A5A6AE8AFC187B7&index=4)
5. [Lecture - 5 Processor As a State Machine](https://www.youtube.com/watch?v=piuWSMLNeco&list=PL1A5A6AE8AFC187B7&index=5)
6. [Lecture - 6 Data Path Architecture](https://www.youtube.com/watch?v=ceuXLsuZhLE&list=PL1A5A6AE8AFC187B7&index=6)
7. [Lecture - 7 Data Path Controller : Micro Programmed](https://www.youtube.com/watch?v=fo-yfZyrW4c&list=PL1A5A6AE8AFC187B7&index=7)
8. [Lecture - 8 State Machine Design](https://www.youtube.com/watch?v=hg2QxXeI_-8&list=PL1A5A6AE8AFC187B7&index=8)
9. [Lecture - 9 Controller Design: Microprogrammed and Hardwired](https://www.youtube.com/watch?v=6CCwWCstDGc&list=PL1A5A6AE8AFC187B7&index=9)
10. [Lecture - 10 Controller Design (Contd)](https://www.youtube.com/watch?v=QmVX73K_hyo&list=PL1A5A6AE8AFC187B7&index=10)
11. [Lecture - 11 Typical Micro Instructions](https://www.youtube.com/watch?v=UYv36HV3Sng&list=PL1A5A6AE8AFC187B7&index=11)
12. [Lecture - 12 Addressing Modes](https://www.youtube.com/watch?v=p9wxyIx-j-c&list=PL1A5A6AE8AFC187B7&index=12)
13. [Lecture - 13 Problem Exercise](https://www.youtube.com/watch?v=F5pU5LbmLVg&list=PL1A5A6AE8AFC187B7&index=13)
14. [Lecture - 14 Problem Exercise](https://www.youtube.com/watch?v=hhvl7nbVpLo&list=PL1A5A6AE8AFC187B7&index=14)
15. [Lecture 15 - Inroduction to memory system](https://www.youtube.com/watch?v=tas2eUavhRE&list=PL1A5A6AE8AFC187B7&index=15)
16. [Lecture - 16 CPU - Memory Interaction](https://www.youtube.com/watch?v=mAK9KklkRYY&list=PL1A5A6AE8AFC187B7&index=16)
17. [Lecture - 17 Cache Organization](https://www.youtube.com/watch?v=VcO3ja6WS2E&list=PL1A5A6AE8AFC187B7&index=17)
18. [Lecture - 18 Cache Organization](https://www.youtube.com/watch?v=Opp-annh9sg&list=PL1A5A6AE8AFC187B7&index=18)
19. [Lecture - 19 Virtual Memory](https://www.youtube.com/watch?v=e9w_XERZ2UM&list=PL1A5A6AE8AFC187B7&index=19)
20. [Lecture - 20  Virtual Memory](https://www.youtube.com/watch?v=3ye2OXj32DM&list=PL1A5A6AE8AFC187B7&index=20)
21. [Lecture - 21 Performance Calculation](https://www.youtube.com/watch?v=8s4b8mYCMAE&list=PL1A5A6AE8AFC187B7&index=21)
22. [Lecture - 22 Segmentation](https://www.youtube.com/watch?v=HWwNTWY1rxo&list=PL1A5A6AE8AFC187B7&index=22)
23. [Lecture - 23 Address Translation and Protection](https://www.youtube.com/watch?v=G0rbpTX_ytE&list=PL1A5A6AE8AFC187B7&index=23)
24. [Lecture - 24 Programmed I/O](https://www.youtube.com/watch?v=aGvMubj8NXk&list=PL1A5A6AE8AFC187B7&index=24)
25. [Lecture 25 - Interrupt Driven I/O](https://www.youtube.com/watch?v=C02weCM9yWA&list=PL1A5A6AE8AFC187B7&index=25)
26. [Lecture - 26 DMA : Direct Memory Access](https://www.youtube.com/watch?v=3RfqkVyvnnc&list=PL1A5A6AE8AFC187B7&index=26)
27. [Lecture - 27 Device Service Routines](https://www.youtube.com/watch?v=XIFbPXcG2W4&list=PL1A5A6AE8AFC187B7&index=27)
28. [Lecture - 28 Evolution Of I/O](https://www.youtube.com/watch?v=Zsr8kODwr08&list=PL1A5A6AE8AFC187B7&index=28)
29. [Lecture 29 - I/O devices](https://www.youtube.com/watch?v=AtfXJ0PNesk&list=PL1A5A6AE8AFC187B7&index=29)
30. [Lecture 30 - I/O Devices - Contd](https://www.youtube.com/watch?v=pW5QK6Fp8-g&list=PL1A5A6AE8AFC187B7&index=30)
31. [Lecture 31 - Buses](https://www.youtube.com/watch?v=fYl2PoGoQWY&list=PL1A5A6AE8AFC187B7&index=31)
32. [Lecture 32 - Buses Contd](https://www.youtube.com/watch?v=29SNQooq5wM&list=PL1A5A6AE8AFC187B7&index=32)
33. [Lecture - 33 Conclusion](https://www.youtube.com/watch?v=ZKBLirP5jo8&list=PL1A5A6AE8AFC187B7&index=33)

</details>


## Books, notes and websites

- ✅ NPTEL *Computer Organization and Architecture* (Kamakoti, IIT Madras) — nptel.ac.in/courses/106106166
- Book: Patterson & Hennessy, *Computer Organization and Design, RISC-V Edition*
- ETH Zurich *Digital Design and Computer Architecture* (Onur Mutlu) — YouTube
- Berkeley CS61C lectures; Ripes simulator for RISC-V
- Book: Bryant & O'Hallaron, *CS:APP*

## Practice / proof of understanding

Write a recursive factorial and a string-reverse in RISC-V assembly, trace a pipeline with hazards by hand, and run a cache simulator comparing associativities.

## What your IITM course sheet says

### From the PDF: CS2600

**Official description:** To learn about the internal organization of CPU and physical memory unit, different types of Instruction Set  Architecture (ISA) used in CPUs, ISA support for programming languages and operating system functions, cache  and memory hierarchy, architecture of scalar pipelined processor, and introduction to superscalar, multi-threaded,  and multi-core processors.

**Official syllabus (trimmed):**

> 1. Introduction to Structured Computer Organization: Digital hardware level, Microarchitecture level, Operating
>  system level, System programming level and Application programming level. Differences between computer
>  organization and computer architecture.
>  2. Instruction Set Architecture Support for Programming Languages: Arithmetic, logical, and comparison
>  instructions, Addressing modes, Data movement instructions, Control transfer instructions, Instruction
>  representation, Instruction decoding, Control unit, Atomic instructions, Stack frames, Function calls and parameter
>  passing, and CISC and RISC architectures.
>  3. CPU Subsystem Architecture: Design of a single cycle processor for basic instructions learnt in the previous
>  module, CPU System-on-Chip (SoC) architecture with core and memory mapped peripherals, Interrupt as a
>  means for peripherals to communicate with the core, Different types of interrupts, and Platform-level vs. core-level
>  interrupt controller. This module acts as a bridge between the earlier module on instruction set and the subsequent
>  module on ISA support for operating systems.
>  4. Instruction Set Architecture Support for Operating Systems: ISA support for handling interrupts, Software
>  interrupts, Nested interrupts, Using interrupts to support multi-tasking and the resulting challenges, Virtual
>  memory, Demand paging, Page table, Hierarchical page tr

**Official textbooks:** 1. J.L.Hennessy and D.A.Patterson, Computer Architecture -- A Quantitative Approach, 6th Ed., Morgan  Kaufmann, 2017.  2. J.P.Shen and M.H.Lipasti, Modern Processor Design -- Fundamentals of Superscalar Processors, Tata  McGraw-Hill, 2005  3. W.Stallings, Computer Organization and Architecture – Designing for Performance, 9th Edition, Pearson, 2013.

**Official references:** 1. C.Hamacher, Z.Vranesic, S.Zaky and N.Manjikian, Computer Organization and Embedded Systems, 6th  Edition, McGraw-Hill, 2012.

### From the PDF: CS2610

**Official description:** The primary objective of this course is to teach assembly language programming using the RISC-V or ARM or x86  Instruction Set Architecture (ISA), its support for translation of high-level programming language constructs and  data structures into assembly programs, and implementation of operating system related functions using assembly  programs. The secondary objective is to introduce students to custom-built or open-source architectural simulators  for analyzing the performance of pipelined processors, cache hierarchy, and branch predictors.

**Official syllabus (trimmed):**

> 1. Set up and understand the ISA simulator/emulator toolchain, compile sample assembly programs, and simulate
>  the executables using both normal and debug modes of operation.
>  2. Write assembly programs to perform arithmetic, logical, and data transfer operations, implement loops for array
>  traversal, and use branch instructions for flow control.
>  3. Write assembly program to perform multi-precision arithmetic operations. Such operations are used in
>  cryptographic algorithms like RSA that perform computations on 1024-bit integers or deep learning algorithms that
>  use IEEE full-precision/half-precision floating point or bfloat16 format (developed by Google).
>  4. Write recursive programs in assembly language to understand argument passing, stack maintenance, and local
>  variable allocation.
>  5. Understand how to access functions and variables defined in C from assembly programs and vice versa,
>  through proper use of assembler directives and calling conventions.
>  6. Learn how to switch privilege modes by programming the appropriate control and status registers.
>  7. Simulate a simple cooperative multitasking environment in assembly language by implementing a program with
>  two concurrently running tasks and a basic context switching mechanism triggered by timer interrupts.
>  8. Understand virtual memory management by switching between different privilege modes, setting up page
>  tables

**Official textbooks:** 1. Sivarama P. Dandamudi, Introduction to Assembly Language Programming for Pentium and RISC Processors,  Springer-Verlag, 2005.  2. Daniel Kusswurm, Modern x86 Assembly Language Programming: 32-bit, 64-bit, SSE, and AVX, Apress, 2014.  3. D.A. Patterson and J.L. Hennessy. Computer Organization and Design: The Hardware/Software Interface  (RISC-V Edition). Morgan Kaufmann Publishers, 2020.

**Official references:** 1. Igor Zhirkov, Low-Level Programming: C, Assembly, and Program Execution on Intel® 64 Architecture, Apress,  2017.
