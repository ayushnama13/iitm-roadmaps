# CS3500+CS3510 — Operating Systems (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 4 |
| Do this first | CS2705, CS2600, CS2222 (C) |
| Estimated effort | 14 weeks, ~9 h/week |
| Unlocks | CS4100, CS6847, CS6440, CS6868 |

## Roadmap

1. Processes, threads, scheduling.
2. Synchronisation: locks, semaphores, condition variables, deadlocks.
3. Memory: paging, virtual memory, page replacement.
4. File systems, I/O, and (in the lab) system calls.
5. Read and modify xv6 along the way.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Introduction to Operating Systems | IIT Madras](https://www.youtube.com/playlist?list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk) (39 videos). NPTEL *Introduction to Operating Systems* (Chester Rebeiro, IIT Madras): xv6-based, this is the IITM OS course.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Operating Systems - Prof. Chester](https://www.youtube.com/playlist?list=PLZ2ps__7DhBYcwlZ7GPCBzbowmiiF4BYR) (50 videos). IIT Madras BS *Operating Systems* (Chester Rebeiro): newer recording of the same teacher.
- [CS 537: OS | University of Wisconsin-Madison](https://www.youtube.com/playlist?list=PLzBbfbHQmjyuqBFJ8KpDdcvnLNkvPXbS-) (26 videos). Wisconsin CS 537 (OSTEP-based) — pairs with the free OSTEP book.
- [UC Berkeley CS162 Operating Systems and System Programming, Fall 2020](https://www.youtube.com/playlist?list=PLRNgaiQ-qhKbYG-JkCv6am7LxhMMa_enm) (27 videos). Berkeley CS162 Fall 2020 (re-upload): deeper on synchronisation and file systems.
- [MIT 6.S081](https://www.youtube.com/playlist?list=PLTsf9UeqkReZHXWY9yJvTwLJWYYPcKEqK) (21 videos). MIT 6.S081 xv6 lectures (re-upload): do the labs at pdos.csail.mit.edu/6.S081.

### ⚡ Short videos for intuition and revision

- [Operating System](https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O) (77 videos). Neso Academy *Operating System*: short, exam-style revision.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=jciGIvn7UfM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=1)–[4](https://www.youtube.com/watch?v=jENkpxUOoXM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=4), [12](https://www.youtube.com/watch?v=JaW0kBhAFh8&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=12) | What an OS does, PC hardware, programs -> processes, booting. Set up xv6 (MIT 6.1810 site) and boot it in QEMU. |
| 2 | [6](https://www.youtube.com/watch?v=pdmDeWCHaH0&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=6)–[11](https://www.youtube.com/watch?v=2OobPx246zg&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=11) | CPU sharing, memory management, virtual memory, MMU, segmentation, xv6 memory. Read xv6 book ch. 3; trace a page-table walk. |
| 3 | [13](https://www.youtube.com/watch?v=g_kLI2pkNC4&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=13)–[19](https://www.youtube.com/watch?v=TgIIOp3l1DQ&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=19) | Processes, fork/exec/exit, system calls, interrupts, context switch. Add a new system call to xv6. |
| 4 | [20](https://www.youtube.com/watch?v=4hCih9eLc7M&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=20)–[24](https://www.youtube.com/watch?v=MkJfuI5_hjc&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=24) | Scheduling: priority, multiprocessor, Linux CFS. Implement a priority or lottery scheduler in xv6. |
| 5-6 | [25](https://www.youtube.com/watch?v=fYv_sLu-1uE&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=25)–[34](https://www.youtube.com/watch?v=8ZS7xzWPo5A&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=34) | IPC, synchronisation, Peterson/Bakery, hardware locks, mutexes, semaphores, dining philosophers, deadlocks. Solve producer-consumer and readers-writers with pthreads. |
| 7 | [35](https://www.youtube.com/watch?v=qkMk3k15PPA&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=35)–[36](https://www.youtube.com/watch?v=UKD0QC_nTkY&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=36) | Threads. Write a user-level threads library (the xv6 *uthread* lab). |
| 8 | [37](https://www.youtube.com/watch?v=8hkvMRGTzCM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=37)–[39](https://www.youtube.com/watch?v=ozJ-Y91igqw&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=39), [5](https://www.youtube.com/watch?v=btkuAEbcQ80&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=5) | OS security, information flow, buffer overflows. Then file systems from OSTEP ch. 39-42 (not in this playlist). |

<details>
<summary>All lectures in <i>Introduction to Operating Systems | IIT Madras</i> (39 videos)</summary>

1. [#1 Introduction to the Course | Introduction to Operating Systems](https://www.youtube.com/watch?v=jciGIvn7UfM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=1)
2. [#2 Introduction to Operating Systems](https://www.youtube.com/watch?v=a2B69vCtjOU&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=2)
3. [#3 PC Hardware | Introduction to Operating Systems](https://www.youtube.com/watch?v=ZDSzcs6NXx8&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=3)
4. [#4 From Programs to Processes | Introduction to Operating Systems](https://www.youtube.com/watch?v=jENkpxUOoXM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=4)
5. [#38 Buffer Overflows | Introduction to Operating Systems](https://www.youtube.com/watch?v=btkuAEbcQ80&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=5)
6. [#5 Sharing the CPU | Introduction to Operating Systems](https://www.youtube.com/watch?v=pdmDeWCHaH0&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=6)
7. [#6 Memory Management Introduction | Introduction to Operating Systems](https://www.youtube.com/watch?v=_pKbqFyG03s&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=7)
8. [#7 Virtual Memory | Introduction to Operating Systems](https://www.youtube.com/watch?v=kQKpJ4bD8TA&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=8)
9. [#8 MMU Mapping | Introduction to Operating Systems](https://www.youtube.com/watch?v=hhKRbc1QAjs&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=9)
10. [#9 Segmentation | Introduction to Operating Systems](https://www.youtube.com/watch?v=GoI8xYCESiw&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=10)
11. [#10 Memory Management in xv6 | Introduction to Operating Systems](https://www.youtube.com/watch?v=2OobPx246zg&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=11)
12. [#11 PC Booting | Introduction to Operating Systems](https://www.youtube.com/watch?v=JaW0kBhAFh8&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=12)
13. [#12 Introduction to Processes | Introduction to Operating Systems](https://www.youtube.com/watch?v=g_kLI2pkNC4&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=13)
14. [#13 Create, Execute & Exit from a Process | Introduction to Operating Systems](https://www.youtube.com/watch?v=a2LQbb82EZM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=14)
15. [#14 System Calls for Process Management | Introduction to Operating Systems](https://www.youtube.com/watch?v=JOaBNuXgqqw&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=15)
16. [#15 Interrupts | Introduction to Operating Systems](https://www.youtube.com/watch?v=xRaApI85Zqo&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=16)
17. [#16 Interrupt Handling | Introduction to Operating Systems](https://www.youtube.com/watch?v=1M5qXXlap0U&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=17)
18. [#17 Software Interrupts & System Calls | Introduction to Operating Systems](https://www.youtube.com/watch?v=Oo1xvseldwU&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=18)
19. [#18 CPU Context Switching | Introduction to Operating Systems](https://www.youtube.com/watch?v=TgIIOp3l1DQ&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=19)
20. [#19 CPU Scheduling | Introduction to Operating Systems](https://www.youtube.com/watch?v=4hCih9eLc7M&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=20)
21. [#20 Priority Based Scheduling Algorithms | Introduction to Operating Systems](https://www.youtube.com/watch?v=fJEVP91dXaE&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=21)
22. [#21 Multi-Processor Scheduling | Introduction to Operating Systems](https://www.youtube.com/watch?v=4FO7WlYOBP4&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=22)
23. [#22 Scheduling in Linux | Introduction to Operating Systems](https://www.youtube.com/watch?v=bsjOY7pjQII&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=23)
24. [#23 Completely Fair Scheduling | Introduction to Operating Systems](https://www.youtube.com/watch?v=MkJfuI5_hjc&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=24)
25. [#24 Inter Process Communication | Introduction to Operating Systems](https://www.youtube.com/watch?v=fYv_sLu-1uE&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=25)
26. [#25 Synchronization | Introduction to Operating Systems](https://www.youtube.com/watch?v=qKPCfuZAAEc&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=26)
27. [#26 Software Solutions for Critical Sections | Introduction to Operating Systems](https://www.youtube.com/watch?v=UuSswiH7jpE&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=27)
28. [#27 Bakery Algorithm | Introduction to Operating Systems](https://www.youtube.com/watch?v=3pUScfud9Sg&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=28)
29. [#28 Hardware Locks | Introduction to Operating Systems](https://www.youtube.com/watch?v=_RJILvSGqYY&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=29)
30. [#29 Mutexes | Introduction to Operating Systems](https://www.youtube.com/watch?v=yxVeUSkGeao&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=30)
31. [#30 Semaphores | Introduction to Operating Systems](https://www.youtube.com/watch?v=I-xQpuZ_UFM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=31)
32. [#31 Dining Philosophers Problem | Introduction to Operating Systems](https://www.youtube.com/watch?v=dOVdsd31WNg&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=32)
33. [#32 Deadlocks | Introduction to Operating Systems](https://www.youtube.com/watch?v=UczJ7misUEk&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=33)
34. [#33 Dealing with Deadlocks | Introduction to Operating Systems](https://www.youtube.com/watch?v=8ZS7xzWPo5A&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=34)
35. [#34 Threads | Part 1 | Introduction to Operating Systems](https://www.youtube.com/watch?v=qkMk3k15PPA&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=35)
36. [#35 Threads | Part 2 | Introduction to Operating Systems](https://www.youtube.com/watch?v=UKD0QC_nTkY&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=36)
37. [#36 Operating System Security | Introduction to Operating Systems](https://www.youtube.com/watch?v=8hkvMRGTzCM&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=37)
38. [#37 Information Flow Policies | Introduction to Operating Systems](https://www.youtube.com/watch?v=6w4bpIm8oSE&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=38)
39. [#39 Preventing Buffer Overflow Attacks | Introduction to Operating Systems](https://www.youtube.com/watch?v=ozJ-Y91igqw&list=PLyqSpQzTE6M9SYI5RqwFYtFYab94gJpWk&index=39)

</details>


## Books, notes and websites

- ✅ NPTEL *Introduction to Operating Systems* (Chester Rebeiro, IIT Madras) — nptel.ac.in/courses/106106144 (uses xv6)
- *Operating Systems: Three Easy Pieces* — ostep.org (free)
- MIT 6.S081 (xv6) — pdos.csail.mit.edu/6.S081
- Book: Tanenbaum, *Modern Operating Systems* (the course text)

## Practice / proof of understanding

Do the OSTEP projects or xv6 labs (add a syscall, implement a scheduler, copy-on-write fork). Write a tiny shell in C.

## What your IITM course sheet says

### From the PDF: CS3500

**Official description:** The course introduces operations systems (OS) to under graduates. The students would be able to understand the  working of an operating system, how it interfaces with computer hardware, and the various interfaces which  software can use. Additionally students will learn to appreciate design aspects of the OS.

**Official textbooks:** 1. Modern Operating Systems- Andrew S Tanenbaum, Prentice Hall2. Design of the Unix Operating System -  Maurice Bach, Prentice Hall.

**Official references:** 1. Operating System Concepts - Operating System Concepts, Sixth Edition, Abraham Silberschatz, Peter Baer  Galvin, Greg Gagne, John Wiley & Sons Inc.2. Operating Systems - Principles and Practice : Thomas Anderson  and Michael Dahlin, Recursive Books, 2014.

### From the PDF: CS3510

**Official description:** 1. Implementation of a command shell.  2. Implementation of Synchronization constructs.  3. Study of scheduling algorithms  4. Implementation of File system constructs  5. Advanced file system constructs  Currently, the whole set of five experiments are done in Java, on top of a java minikernel. A Nachos based solution  may also be used. For parts (4) and (5) Unix file system is used as a case study.

**Official textbooks:** NIL
