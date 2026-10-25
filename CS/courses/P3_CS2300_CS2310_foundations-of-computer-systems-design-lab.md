# CS2300+CS2310 — Foundations of Computer Systems Design (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | CS1111, CS1200 |
| Estimated effort | 12 weeks, ~8 h/week |
| Unlocks | CS2600, CS3500, CS3300 |

## Roadmap

1. Boolean algebra and combinational logic (encoder, mux, adders, ALU).
2. Sequential logic: flip-flops, registers, counters, memory.
3. Build the whole computer bottom-up: CPU (Hack), assembler, VM, compiler, OS, as the course does.
4. Do the lab in Verilog/SystemVerilog and finish Tetris on your own machine.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Foundations to Computer Systems Design](https://www.youtube.com/playlist?list=PLyqSpQzTE6M-JIlXDZF7wGz5thLz15xWA) (77 videos). NPTEL *Foundations to Computer Systems Design* (V. Kamakoti, IIT Madras): this IS the IITM course.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Electronics - Digital Circuits and Systems](https://www.youtube.com/playlist?list=PL803563859BF7ED8C) (40 videos). NPTEL *Digital Circuits and Systems* (nptelhrd): the logic-design half in more depth.
- [NOC Jan 2019: Digital Electronic Circuits](https://www.youtube.com/playlist?list=PLbRMhDVUMnge4gDT0vBWjCb3Lz0HnYKkX) (61 videos). NPTEL *Digital Electronic Circuits* (IIT Kharagpur, 2019).

### ⚡ Short videos for intuition and revision

- [Building an 8-bit breadboard computer!](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU) (44 videos). Ben Eater *Building an 8-bit breadboard computer*: you will finally *see* how a CPU works.

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

- ✅ NPTEL *Foundations to Computer Systems Design* (Kamakoti, IIT Madras) — onlinecourses.nptel.ac.in/noc20_cs34/preview
- nand2tetris.org — the official reference text is *The Elements of Computing Systems*; free Coursera Parts I and II
- HDLBits (hdlbits.01xz.net) for Verilog drills
- Book: *Code* (Charles Petzold) for intuition

## Practice / proof of understanding

Complete nand2tetris projects 1-12 (gates -> ALU -> CPU -> assembler -> VM -> compiler -> OS).

## What your IITM course sheet says

### From the PDF: CS2300

**Official description:** This course is intended to understand the different components of a computer system, namely, digital hardware,  the microarchitecture, the operating systems and the compilers, and their interconnection.

**Official syllabus (trimmed):**

> 1. Introduction: Functional components of a computer system, Interaction among functional components
>  2. Design of Arithmetic and Logic Unit: Digital logic gates, Boolean algebra, Simplification of Boolean
>  Expressions, Combinational logic circuits – Encoder, Decoder, Multiplexer and Demultiplexer; Representation of
>  integer data, Integer adders, Integer multipliers, Design of integer unit, Floating point representation of real data,
>  Floating-point adder/subtractor, Floating-point multiplier, Design of Floating point unit
>  3. Design of Register File and Memory Unit: Flip-flops, Synchronous sequential circuits – Registers and Counters;
>  Memory unit
>  4. Generation and Execution of Machine Code: Instruction set architecture of a simple CPU, Assembler, Code
>  generation, Application binary interface, Microarchitecture of CPU, Execution of machine code
>  5. Processing of High Level Language Code: Virtual machine, Interpreter, A simple compiler, Fundamentals of
>  operating system

**Official textbooks:** 1. C. H. Roth and L.L.Kinney, Fundamentals of Logic Design, 7th Edition, Cengage Learning, 2014.  2. C.Hamacher, Z.Vranesic, S.Zaky and N.Manjikian, Computer Organization and Embedded Systems, 6th  Edition, McGraw-Hill, 2012  3. N. Nisan and S. Schocken, The Elements of Computing Systems – Building a Modern Computer from First  Principles, The MIT Press, 2005

**Official references:** 1. V. P. Nelson, H.T. Nagle, E.D. Caroll and J.D. Irwin, Digital Logic Circuit Analysis and Design, Prentice Hall  International, 1995  2. S. Brown and Z Vranesic, Fundamentals of Logic Design with VHDL Design, Tata McGraw-Hill , 2000  4. F.J. Hill and G.R.Peterson, Computer Aided Logical Design with Emphasis on VLSI, John Wiley & Sons, 1993

### From the PDF: CS2310

**Official description:** This is the laboratory course, associated with CS2300 - Foundations of Computer Systems Design. In the lab part  – the components taught in the course shall be described using a suitable description language and integrated to  form a system; the assembler, compiler and OS concepts shall be ported on the system built above.

**Official syllabus (trimmed):**

> 1. Breadboard exercises
>  a. 4-to-2 bit Encoder
>  b. 1-bit, 4-to-1 Line Multiplexer
>  c. 4-bit ripple carry adder
>  2. Hardware Description Language (such as Verilog) based exercises:
>  a. 16-bit Adder/Subtractor using 4-bit Carry Look Ahead circuits
>  b. 16-bit Signed integer multiplier using Wallace tree multiplier
>  c. Arithmetic and Logic unit for 16-bit operands
>  d. Register file and Main memory
>  3. Implementation of microarchitecture a simple processor (such as Hack)
>  4. Interpreter for the language of a virtual machine (such as JACK)
>  5. Compiler for a simple language (such as JACK)
>  6. Compilation and execution of a complete application (such as Tetris game)

**Official textbooks:** S. Sutherland, S. Davidmann and P. Flake, SystemVerilog for Design - A Guide to Using System Verilog for  Hardware Design and Modeling, 2nd Edition, Springer, 2006.

**Official references:** N. Nisan and S. Schocken, The Elements of Computing Systems – Building a Modern Computer from First  Principles, The MIT Press, 2005
