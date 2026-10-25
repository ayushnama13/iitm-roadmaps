# CS3400+CS3410 — Principles of Software Engineering (+ lab)

| | |
|---|---|
| Tier | B |
| Phase (order) | 5 |
| Do this first | CS2705, CS1234 |
| Estimated effort | 8-10 weeks |
| Unlocks | Any large project |

## Roadmap

1. Process models, requirements, UML/modelling.
2. Design principles, patterns, refactoring.
3. Testing (unit, integration), debugging, CI.
4. Estimation, QA, configuration management.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Software Engineering by Prof. Rajib Mall](https://www.youtube.com/playlist?list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt) (60 videos). NPTEL *Software Engineering* (Rajib Mall, IIT Kharagpur): the standard Indian SE course, matches the IITM syllabus.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Software testing](https://www.youtube.com/playlist?list=PLyqSpQzTE6M-sBjDcT21Gpnj8grR2fDgc) (59 videos). NPTEL-NOC IITM *Software Testing* (Meenakshi D'Souza, IIIT Bangalore): for the testing half.
- [Object-Oriented Analysis and Design](https://www.youtube.com/playlist?list=PLJ5C_6qdAvBHslIkD7JB7kBdgv1SeXy3P) (52 videos). *Object-Oriented Analysis and Design* (NPTEL, IIT Kharagpur): UML and design patterns.

### ⚡ Short videos for intuition and revision

- [Missing Semester IAP 2020](https://www.youtube.com/playlist?list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J) (11 videos). Missing Semester lectures 6-8 (git, debugging, build systems/CI) for the lab.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=Ln_LP7c23WM&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=1)–[14](https://www.youtube.com/watch?v=gWYw4gKgmPk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=14) | Intro, life-cycle models, waterfall, incremental, agile, XP, Scrum. |
| 2 | [15](https://www.youtube.com/watch?v=l9XFipXoJb0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=15)–[18](https://www.youtube.com/watch?v=mND1i92IBps&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=18) | Requirements: gathering, SRS. Write an SRS for your project. |
| 3 | [19](https://www.youtube.com/watch?v=5q_KBeNlRFk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=19)–[30](https://www.youtube.com/watch?v=rjCYo81J0rU&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=30) | Design: cohesion, coupling, DFDs, structured design. |
| 4-5 | [31](https://www.youtube.com/watch?v=7wo9PHfkyik&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=31)–[42](https://www.youtube.com/watch?v=AFOIMsgpJP0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=42) | UML: use cases, class, sequence, state diagrams; OO design process. Draw UML for your project; read *Head First Design Patterns*. |
| 6-7 | [43](https://www.youtube.com/watch?v=_9bmWEMhGFU&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=43)–[60](https://www.youtube.com/watch?v=rG9wQvvJHYI&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=60) | Testing: unit, equivalence class, boundary, decision table, pairwise, white-box, MC/DC, path, dataflow and mutation testing. Write a pytest suite with coverage >80% and try mutmut. |

<details>
<summary>All lectures in <i>Software Engineering by Prof. Rajib Mall</i> (60 videos)</summary>

1. [Lecture 01: Introduction- I](https://www.youtube.com/watch?v=Ln_LP7c23WM&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=1)
2. [Lecture 02: Introduction- II](https://www.youtube.com/watch?v=PM73z4SwvIQ&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=2)
3. [Lecture 03: Introduction- III](https://www.youtube.com/watch?v=nM4O7S_ASSw&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=3)
4. [Lecture 04: Introduction- IV](https://www.youtube.com/watch?v=gvdgaJIUcMA&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=4)
5. [Lecture 05: Introduction- V](https://www.youtube.com/watch?v=cNG4KuoyfiI&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=5)
6. [Lecture 06: Life Cycle Model](https://www.youtube.com/watch?v=OT2O7uNldQk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=6)
7. [Lecture 07: Life Cycle Model (Contd.)](https://www.youtube.com/watch?v=_ziaLmfToSk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=7)
8. [Lecture 08: Waterfall Model](https://www.youtube.com/watch?v=zKWeXjpFeRw&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=8)
9. [Lecture 09: Waterfall Derivatives](https://www.youtube.com/watch?v=tF9Njt-XW3E&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=9)
10. [Lecture 10: Incremental Model](https://www.youtube.com/watch?v=xl9Rtc4Ga1U&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=10)
11. [Lecture 11: Evolutionary Model](https://www.youtube.com/watch?v=XKW9TWrxxPo&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=11)
12. [Lecture 12: Agile Model](https://www.youtube.com/watch?v=x90kIAFGYKE&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=12)
13. [Lecture 13: Extreme Programming and Scrum](https://www.youtube.com/watch?v=td7mY7x_Tk0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=13)
14. [Lecture 14: Scrum](https://www.youtube.com/watch?v=gWYw4gKgmPk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=14)
15. [Lecture 15: Introduction to requirement specification](https://www.youtube.com/watch?v=l9XFipXoJb0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=15)
16. [Lecture 16: Requirement gathering and analysis](https://www.youtube.com/watch?v=ul6nW1g3xK0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=16)
17. [Lecture 17: Functional requirements](https://www.youtube.com/watch?v=PR_ZwLfjWrA&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=17)
18. [Lecture 18: Representation of complex programming logic](https://www.youtube.com/watch?v=mND1i92IBps&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=18)
19. [Lecture 19: Design Fundamentals](https://www.youtube.com/watch?v=5q_KBeNlRFk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=19)
20. [Lecture 20: Modular Design](https://www.youtube.com/watch?v=FTyncRpLd5g&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=20)
21. [Lecture 21: Classification of Cohesion](https://www.youtube.com/watch?v=40Du7ear5v8&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=21)
22. [Lecture 22: Classification of Coupling](https://www.youtube.com/watch?v=OFxBjpE8mT0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=22)
23. [Lecture 23: Introduction to structured analysis and structured design](https://www.youtube.com/watch?v=69PIhEvYmm8&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=23)
24. [Lecture 24: Basics of Data Flow Diagrams (DFD)](https://www.youtube.com/watch?v=e6HjDcd4U6U&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=24)
25. [Lecture 25: Developing DFD Model](https://www.youtube.com/watch?v=PvYTyXJiwuo&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=25)
26. [Lecture 26: Examples of DFD Model development](https://www.youtube.com/watch?v=OAPV00_0hSk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=26)
27. [Lecture 27: DFD Model - More Examples](https://www.youtube.com/watch?v=qgWuZcnmVrk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=27)
28. [Lecture 28: Essentials of Structure Chart](https://www.youtube.com/watch?v=3253sqmQ6OA&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=28)
29. [Lecture 29: Structure Chart Development](https://www.youtube.com/watch?v=iskh2c4jAZE&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=29)
30. [Lecture 30: Structured Design Examples](https://www.youtube.com/watch?v=rjCYo81J0rU&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=30)
31. [Lecture 31: Use Case Modelling](https://www.youtube.com/watch?v=7wo9PHfkyik&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=31)
32. [Lecture 32: Factoring Use Cases](https://www.youtube.com/watch?v=lZMdb_RUmAQ&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=32)
33. [Lecture 33: Overview of Class diagram](https://www.youtube.com/watch?v=z5bsXJ5lnpk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=33)
34. [Lecture 34: Inheritance relationship](https://www.youtube.com/watch?v=wDRmM9LCLoE&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=34)
35. [Lecture 35: Association relationship](https://www.youtube.com/watch?v=7Pc5-birfmk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=35)
36. [Lecture 36: Aggregation/ Composition and dependency relations](https://www.youtube.com/watch?v=9KokDbcr6cM&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=36)
37. [Lecture 37: Interation Modelling](https://www.youtube.com/watch?v=azTLDkiqGVk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=37)
38. [Lecture 38: Development of Sequence diagrams](https://www.youtube.com/watch?v=RFosHwXYLg4&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=38)
39. [Lecture 39: State-Machine diagram](https://www.youtube.com/watch?v=RoQ__mLv1hM&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=39)
40. [Lecture 40: An Object-Oriented design process](https://www.youtube.com/watch?v=Ie7qzy3SY-E&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=40)
41. [Lecture 41: Domain Analysis](https://www.youtube.com/watch?v=15FYNqkKfrc&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=41)
42. [Lecture 42: Examples of object-oriented design](https://www.youtube.com/watch?v=AFOIMsgpJP0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=42)
43. [Lecture 43: Basic concepts in Testing-I](https://www.youtube.com/watch?v=_9bmWEMhGFU&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=43)
44. [Lecture 44: Basic concepts in Testing-II](https://www.youtube.com/watch?v=Su-bw6Of-g8&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=44)
45. [Lecture 45: Basic concepts in Testing-III](https://www.youtube.com/watch?v=TSacDWHGlWU&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=45)
46. [Lecture 46: Unit testing strategies-I](https://www.youtube.com/watch?v=reTh1y7ZH_A&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=46)
47. [Lecture 47: Unit testing strategies-II](https://www.youtube.com/watch?v=ZIUJDS3O0BQ&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=47)
48. [Lecture 48: Equivalance Class Testing-I](https://www.youtube.com/watch?v=QmBmRzzD2KM&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=48)
49. [Lecture 49: Equivalance Class Testing-II](https://www.youtube.com/watch?v=zH0zbNj1qZc&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=49)
50. [Lecture 50: Special Value Testing](https://www.youtube.com/watch?v=RkEEmrj5odE&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=50)
51. [Lecture 51: Combinatorial Testing](https://www.youtube.com/watch?v=BIA-kQjAkZI&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=51)
52. [Lecture 52: Decision Table Testing](https://www.youtube.com/watch?v=ds7MIuNdJz8&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=52)
53. [Lecture 53: Cause effect graphing](https://www.youtube.com/watch?v=QU_jI6F0ndQ&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=53)
54. [Lecture 54: Pairwise Testing](https://www.youtube.com/watch?v=PPojYKImWG8&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=54)
55. [Lecture 55: White box Testing](https://www.youtube.com/watch?v=pXkCkRgPFrc&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=55)
56. [Lecture 56: Condition Testing](https://www.youtube.com/watch?v=u43CvemmDEk&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=56)
57. [Lecture 57: MC/DC Coverage](https://www.youtube.com/watch?v=orwspdC4PC0&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=57)
58. [Lecture 58: MC/DC Testing](https://www.youtube.com/watch?v=lazvIT0jWD4&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=58)
59. [Lecture 59: Path Testing](https://www.youtube.com/watch?v=TAFhCV721tY&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=59)
60. [Lecture 60: Dataflow and Mutation Testing](https://www.youtube.com/watch?v=rG9wQvvJHYI&list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&index=60)

</details>


## Books, notes and websites

- MIT 6.031 *Software Construction* notes
- Book: *A Philosophy of Software Design* (Ousterhout)
- Book: *Design Patterns* (Gamma et al.)
- Pro Git; GitHub Actions docs

## Practice / proof of understanding

Build a medium app (about 2k lines) with tests, CI, issues and a design doc.

## What your IITM course sheet says

### From the PDF: CS3400

**Official description:** The process of software development - Process models.  Software measurement - Software process improvement by metrics- Size-oriented metrics and function point  metrics.  Engineering of software systems - Analysis concepts and principles - Analysis modeling - Data modeling -  Specification techniques for software.  Design concepts and principles - Abstraction - Refinement - Modularity - Architectural design - Cohesion coupling  concepts - Refactoring of designs.  O-O Approach to software design - Concepts - Design issues - Modeling techniques Design process - Design  patterns.  Software Testing - Principles - Designing test cases - Testing strategies - Debugging - Introduction to O-O testing.  Software project planning - Effort and cost estimation techniques - LOC-based and Function-point based  measures - The COCOMO model.  Software Quality Assurance(SQA) - Software Reliability - The IS

**Official textbooks:** NIL

**Official references:** 1. Software Engineering - A Practitioner's approach by Roger Pressman, 5e, 2001.  2. Software Engineering Economics by Barry Boehm.  3. Fundamentals of Software Engineering by Carlo Ghezzi, Mehdi Jazayeri, Dino Mandrioli.  4. IEEE Software Engineering Standards.  5. "Software Metrics : A rigorous and practical approach", 2nd edition, Norman E Fenton and Shari Lawrence  Pfleeger, Thomson Asia, 2002

### From the PDF: CS3410

**Official description:** System Requirement Specification (SRS) and related analysis documents as per the guidelines in ANSI/IEEE Std  830-1984.  Design documents representing the complete design of the software system.  The design can further be improved by the principles learned in this module.  Analysis and design for the same problem should be done using O-O approach.  Test documents as per ANSI/IEEE Std. 829/1983 Software Test Documentation.  Simple exercises in effort and cost estimation in COCOMO model.  Application of COCOMO and Function Point (FP) model for the actual project that has been chosen.  Familiarization of SCM tools with some public domain software like SCCS, CVS.  Familiarization of some reverse engineering tools available in the public domain.  At the end of the semester, there should be a presentation of the project with demonstration.  It is also advisable to have the students present the

**Official textbooks:** NIL
