# DA2304 — Introduction to Computer Systems

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | DA1300 |
| Estimated effort | 12 weeks |
| Unlocks | DA3408, DA5402, ML systems work |

## Roadmap

1. Logic gates to ALU and CPU (nand2tetris style).
2. Assembly, machine code, intro to compilers and OS.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Foundations to Computer Systems Design](https://www.youtube.com/playlist?list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA) (77 videos). NPTEL *Foundations to Computer Systems Design* (V. Kamakoti, IIT Madras): from gates to a working computer, nand2tetris style.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [cmu 15-213/18-213/15-513: Introduction to Computer Systems, Fall 2017](https://www.youtube.com/playlist?list=PLtv4PQFH2yMas_SCMTEaE4eUIWWWiwISj) (29 videos). CMU 15-213 *Introduction to Computer Systems* (Fall 2017, re-upload): data representation, assembly, caches, linking, processes, virtual memory. Do the CS:APP labs.
- [Computer Sc - Computer Organization](https://www.youtube.com/playlist?list=PL1A5A6AE8AFC187B7) (33 videos). NPTEL *Computer Organization* (nptelhrd, IIT Madras).
- [System Commands](https://www.youtube.com/playlist?list=PLZ2ps__7DhBajgl-4et7X2BjOIObqlp81) (33 videos). IIT Madras BS *System Commands*: Linux shell, the practical side.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=IZ5dicfkIP4&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=1)–[6](https://www.youtube.com/watch?v=2IaqLJRovig&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=6) | CMOS, gates, HDL simulator. Do nand2tetris Project 1. |
| 2 | [7](https://www.youtube.com/watch?v=fNWda_fTozQ&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=7)–[13](https://www.youtube.com/watch?v=Qm_ZI9WxArQ&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=13) | Number systems, adders, the HACK ALU. Project 2. |
| 3 | [14](https://www.youtube.com/watch?v=G-dczzI-fJM&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=14)–[22](https://www.youtube.com/watch?v=ZWn_IKYhm4k&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=22) | Sequential logic, memory, PC, memory-mapped I/O. Projects 3 and 4 (machine language). |
| 4 | [23](https://www.youtube.com/watch?v=TyU-nnf28oU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=23)–[28](https://www.youtube.com/watch?v=r6HZLtQ0UkU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=28) | HACK CPU micro-architecture and the full computer. Project 5: build the CPU. |
| 5 | [29](https://www.youtube.com/watch?v=LEKDkhvUKjA&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=29)–[34](https://www.youtube.com/watch?v=deXI_iYTzNo&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=34) | Assembler. Project 6: write the assembler in Python/C. |
| 6-7 | [35](https://www.youtube.com/watch?v=xCsOs4LRm6c&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=35)–[47](https://www.youtube.com/watch?v=x1e-ZTGJCco&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=47) | Virtual machine I and II. Projects 7-8: VM translator. |
| 8-9 | [48](https://www.youtube.com/watch?v=32vaatTEnDc&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=48)–[65](https://www.youtube.com/watch?v=M0pck8nW2kI&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=65) | Jack language + compiler front end. Projects 9-10. |
| 10-12 | [66](https://www.youtube.com/watch?v=M9R6tUX6cyU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=66)–[77](https://www.youtube.com/watch?v=25w1j_M42po&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=77) | Compiler back end + OS. Projects 11-12. You now built a computer from NAND to a compiled program. |

<details>
<summary>All lectures in <i>Foundations to Computer Systems Design</i> (77 videos)</summary>

1. [Module 1.1: Introduction to the Course](https://www.youtube.com/watch?v=IZ5dicfkIP4&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=1)
2. [Module 1.2: CMOS Transistors and Gates](https://www.youtube.com/watch?v=qj3kNYxkt1s&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=2)
3. [Module 1.3: Basic Gates](https://www.youtube.com/watch?v=ZYtFwSSAHgY&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=3)
4. [Module 1.4: Building Gates Using Simulator](https://www.youtube.com/watch?v=2Xca-xQ7NK4&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=4)
5. [Module 1.5: Hierarchical Design and Verification](https://www.youtube.com/watch?v=THiJwj3zKZU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=5)
6. [Module 1.6: Building Blocks of a Digital Computer](https://www.youtube.com/watch?v=2IaqLJRovig&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=6)
7. [Module 2.1: Binary Number Systems](https://www.youtube.com/watch?v=fNWda_fTozQ&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=7)
8. [Module 2.2: Signed Number Systems](https://www.youtube.com/watch?v=SejfGPywmI0&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=8)
9. [Module 2.3: Two’s Complement Number System](https://www.youtube.com/watch?v=aizebIJn7hM&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=9)
10. [Module 2.4: Binary Adder Circuits](https://www.youtube.com/watch?v=hoJum-2ZWqc&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=10)
11. [Module 2.5: Building the ALU of HACK](https://www.youtube.com/watch?v=4jdoX64gUXo&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=11)
12. [Module 2.6: HACK ALU Functionality](https://www.youtube.com/watch?v=dYjKa5Gucfk&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=12)
13. [Module P1: Tips for Project P01](https://www.youtube.com/watch?v=Qm_ZI9WxArQ&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=13)
14. [Module 3.1: Sequential Logic Design](https://www.youtube.com/watch?v=G-dczzI-fJM&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=14)
15. [Module 3.2: Latches and Flipflops](https://www.youtube.com/watch?v=YeAf3DlylyA&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=15)
16. [Module 3.3: The Memory Hierarchy](https://www.youtube.com/watch?v=__Cs4PWT3fs&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=16)
17. [Module 3.4: Design of Program Counter](https://www.youtube.com/watch?v=3ueOkmBETqY&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=17)
18. [Module 3.5: Introduction to Computer Organization: The HACK Instruction Set Architecture (ISA)](https://www.youtube.com/watch?v=AumPb6aHdIg&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=18)
19. [Module 3.6 Memory Mapped I/O](https://www.youtube.com/watch?v=OeXq2HdO_00&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=19)
20. [Module P2: Tips for Projects P02 and P03](https://www.youtube.com/watch?v=JCcXtl5VyCQ&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=20)
21. [Module P3: Tips for Project 04](https://www.youtube.com/watch?v=RDZCQXZ6j4M&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=21)
22. [Module P4: Tips for Project 04](https://www.youtube.com/watch?v=ZWn_IKYhm4k&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=22)
23. [Module 4.1: Introduction to Computer Architecture](https://www.youtube.com/watch?v=TyU-nnf28oU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=23)
24. [Module 4.2: The HACK Microarchitecture](https://www.youtube.com/watch?v=KjjUZWSJKss&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=24)
25. [Module 4.3: The HACK CPU - A Deep Dive: Part 1](https://www.youtube.com/watch?v=IfZ-I5AgmaY&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=25)
26. [Module 4.4: The HACK CPU - A Deep Dive: Part 2](https://www.youtube.com/watch?v=QAbhHIB2NoA&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=26)
27. [Module 4.5: The Data Memory](https://www.youtube.com/watch?v=WgNuHHNS4Pw&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=27)
28. [Module 4.6: The HACK Computer](https://www.youtube.com/watch?v=r6HZLtQ0UkU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=28)
29. [Module 5.1: The Assembler Construction](https://www.youtube.com/watch?v=LEKDkhvUKjA&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=29)
30. [Module 5.2: Understanding the Working of Assembler](https://www.youtube.com/watch?v=CF9DI6-dMc4&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=30)
31. [Module 5.3: Assembler: Symbol Table Construction](https://www.youtube.com/watch?v=r2gvItxDyL8&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=31)
32. [Module 5.4: Assembler: Pass 1](https://www.youtube.com/watch?v=CHb6GPGmUi8&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=32)
33. [Module 5.5: Assembler: Pass 2](https://www.youtube.com/watch?v=2dBcwaiDedk&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=33)
34. [Module 5.6: Project 06 - Demonstration](https://www.youtube.com/watch?v=deXI_iYTzNo&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=34)
35. [Module 6.1: Virtual Machines - What and Why?](https://www.youtube.com/watch?v=xCsOs4LRm6c&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=35)
36. [Module 6.2: The VM Instruction Set Architecture](https://www.youtube.com/watch?v=_Fc8ucMx_eE&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=36)
37. [Module 6.3: The execution of a VM Program](https://www.youtube.com/watch?v=k25WpN-KXcU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=37)
38. [Module 6.4: How powerful is the VM?](https://www.youtube.com/watch?v=ctdPTHxfKrk&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=38)
39. [Module P5: Project 07: VM ISA to HACK Mnemonic Translation](https://www.youtube.com/watch?v=6yrMUNZ9vyE&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=39)
40. [Module 6.6: Project 07: Demo](https://www.youtube.com/watch?v=jrUjY8B6q1A&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=40)
41. [Module 6.5: Deep Understanding of VM ISA using VM Emulator](https://www.youtube.com/watch?v=4nD-dnZrTL8&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=41)
42. [Module 7.1: Virtual Machine II - Program flow commands and Introduction to Function Calls](https://www.youtube.com/watch?v=tgQ7f9V7HJQ&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=42)
43. [Module 7.2: Implementation of Function Call](https://www.youtube.com/watch?v=UlDaq4EPYTI&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=43)
44. [Module 7.3: Working of the Virtual Machine](https://www.youtube.com/watch?v=PClRENhTY84&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=44)
45. [Module 7.4: Project 08: Translation of Program Flow and Function Call to HACK Mnemonic](https://www.youtube.com/watch?v=d-rBsTKZkls&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=45)
46. [Module 7.5: Handling Static Variables](https://www.youtube.com/watch?v=aolU_Y9JagM&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=46)
47. [Module 7.6: Project 08: Implementation tips in a Nut Shell](https://www.youtube.com/watch?v=x1e-ZTGJCco&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=47)
48. [Module 8.1: Introduction to The JACK Programming Language](https://www.youtube.com/watch?v=32vaatTEnDc&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=48)
49. [Module 8.2: Project 09: Basic Steps](https://www.youtube.com/watch?v=s6TMBs64gNo&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=49)
50. [Module 8.3: Understanding Syntax of JACK using Examples](https://www.youtube.com/watch?v=wchfXltvoqg&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=50)
51. [Module 8.4: Project 09: More Examples](https://www.youtube.com/watch?v=4ENCotWmAC8&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=51)
52. [Module 8.5: The JACK Syntax - Language Specification](https://www.youtube.com/watch?v=l5wwijVum84&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=52)
53. [Module 8.6: Application Development using JACK](https://www.youtube.com/watch?v=_-U8ztP5Pbo&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=53)
54. [Module 9.1: JACK Compiler: Lexical Analysis - Tokenization](https://www.youtube.com/watch?v=CuidLyXedVs&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=54)
55. [Module 9.2: Project 10: Compiler for JACK - Part-1 Demo](https://www.youtube.com/watch?v=h38JY91Orxg&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=55)
56. [Module 9.3: The JACK Grammar](https://www.youtube.com/watch?v=89dlq_AEZsk&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=56)
57. [Module 9.4: Compiler for JACK: Parsing the JACK Program](https://www.youtube.com/watch?v=UhbDJcoUosw&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=57)
58. [Module 9.5: Project 10: Part 2: The Token Analyzer](https://www.youtube.com/watch?v=TcQsJzMPeGA&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=58)
59. [Module 9.6: Project 10: Part 3: Testing the Correctness](https://www.youtube.com/watch?v=AvhA5e68-Kk&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=59)
60. [Mod 10 1](https://www.youtube.com/watch?v=TM2kLowau2w&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=60)
61. [Mod 10 2](https://www.youtube.com/watch?v=wdha8s39Jmk&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=61)
62. [Mod 10 3](https://www.youtube.com/watch?v=0gSCEyY2d4E&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=62)
63. [Mod 10 4](https://www.youtube.com/watch?v=dkMSfoVGChA&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=63)
64. [Mod 10 5](https://www.youtube.com/watch?v=jy6nQ5TgykY&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=64)
65. [Mod 10 6](https://www.youtube.com/watch?v=M0pck8nW2kI&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=65)
66. [Module 11.1: The Jack Compiler Backend: An XML guided approach](https://www.youtube.com/watch?v=M9R6tUX6cyU&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=66)
67. [Module 11.2: The Jack Compiler Backend: Populating the Class and Subroutine Symbol tables.](https://www.youtube.com/watch?v=Qal-0AOkE1U&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=67)
68. [Module 11.3: The Jack Compiler Backend: Code Generation - 1](https://www.youtube.com/watch?v=xNVb9JWt17E&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=68)
69. [Module 11.4: The Jack Compiler Backend: Code Generation - 2](https://www.youtube.com/watch?v=NOQIMPVqrJE&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=69)
70. [Module 11.5: The Jack Compiler Backend: Code Generation - 3](https://www.youtube.com/watch?v=bAEpBuMqtgA&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=70)
71. [Module 11.6: The Jack Compiler Backend: Code Generation - 4](https://www.youtube.com/watch?v=rgDAvlCfShQ&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=71)
72. [Module 12.1: Jack Compiler: Code Generation - 5](https://www.youtube.com/watch?v=INVxYRKuNiY&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=72)
73. [Module 12.2: Jack Compiler: Code Generation - 6](https://www.youtube.com/watch?v=IHz_18rAt8c&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=73)
74. [Module 12.3: Jack Compiler: Code Generation - 7](https://www.youtube.com/watch?v=gbJ53hLjONs&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=74)
75. [Module 12.4: Understand the Operating System - Compiler Interactions](https://www.youtube.com/watch?v=_LLgxMIwL_A&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=75)
76. [Module 12.5: Project - 12: One sample journey from Jack to Hack](https://www.youtube.com/watch?v=rbusPfxJD9A&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=76)
77. [Module 12.6: Concluding Remarks](https://www.youtube.com/watch?v=25w1j_M42po&list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA&index=77)

</details>


## Books, notes and websites

- nand2tetris.org (the course text) — free Coursera Parts I and II
- Book: Patterson & Hennessy, RISC-V edition; Petzold, *Code*
- ✅ NPTEL *Foundations to Computer Systems Design* (Kamakoti)
- CMU 15-213 *CS:APP*

## Practice / proof of understanding

Build the Hack computer in nand2tetris projects 1-6, then an assembler.

## What your IITM course sheet says

### From the PDF: DA2304

**Official description:** Modern systems consist of multiple entities such as basic logic gates, which form the building blocks of most  modern hardware systems, application programs that enable the user to interact with the system, and Operating  Systems, which help coordinate between users’ inputs, application programs, and the underlying hardware.  It is crucial in today’s world to have a proper understanding of each of these components and their interactions.  Improper understanding or calibration of one or more of these components can lead to suboptimal performance  and, in some cases, catastrophic consequences.  This course aims to provide the students with the following outcomes:  • A hands-on understanding of how computer systems work by adopting a bottom-up approach.  • An insight into how the different components, viz, hardware, software, compilers, and OS, interact and the  various optimizations and th

**Official syllabus (trimmed):**

> 1. Introduction and Outline (1 week )
>  2. Basics of Digital Design. (1 week) Boolean logic, boolean arithmetic, memory, logic gates, sequential vs
>  combinational logic, basics of RTL design - designing basic arithmetic circuits
>  3. Computer Organization and Architecture(3 weeks) Instruction Set Architecture, Various elements of a mi-
>  croprocessor, I/O logic, Interrupts, Memory-mapped vs interrupt-driven I/O, Computer Architecture: assembling a
>  processor, design of memory elements, optimizations
>  4. Assembly Language and Introduction to Compilers (5 weeks) Understanding machine code, writing low- level
>  machine programs: challenges and advantages, symbolic instruction code and micro-ops, translating high-level
>  programs to low-level machine code: grammar, parsing, syntax-checking, code-generation, linking static and
>  dynamic libraries.
>  5. Operating Systems and Virtual Machines (3 weeks) understanding memory management, data handling, and
>  I/O interactions such as graphics, understanding the need and challenges of Virtual Machines, Handling program
>  emulation in VMs.

**Official textbooks:** 1. The Elements of Computing Systems: Building a Modern Computer from First Principles. Noam Nisan and  Shimon Schocken (MIT Press)  2. Computer Organization and Design RISC-V Edition. David Patterson.  3. Code: The Hidden Language of Computer Hardware and Software, 2nd edition, by Charles Petzold, published  by Pearson Education

**Official references:** 1. The Elements of Computing Systems: Building a Modern Computer from First Principles. Noam Nisan and  Shimon Schocken (MIT Press)  2. Computer Organization and Design RISC-V Edition. David Patterson.  3. Code: The Hidden Language of Computer Hardware and Software, 2nd edition, by Charles Petzold, published  by Pearson Education
