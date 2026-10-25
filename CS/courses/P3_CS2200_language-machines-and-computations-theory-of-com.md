# CS2200 — Language, Machines and Computations (theory of computation)

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | CS1200 |
| Estimated effort | 12 weeks, ~7 h/week |
| Unlocks | CS3300 (parsing), CS6850, CS6840 |

## Roadmap

1. DFA/NFA, regular languages, closure, pumping lemma, Myhill-Nerode, minimisation.
2. Regular expressions and the NFA<->RE equivalence.
3. Context-free grammars, PDAs, CNF, CYK, pumping lemma for CFLs.
4. Turing machines, decidability, halting problem, reductions, intro to complexity (P, NP).

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Computer - Theory of Automata, Formal Languages and Computation](https://www.youtube.com/playlist?list=PL85CF9F4A047C7BF7) (42 videos). NPTEL *Theory of Automata, Formal Languages and Computation* (Kamala Krithivasan, IIT Madras).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Theory of Computation_Prof. Subrahmanyam Kalyanasundaram](https://www.youtube.com/playlist?list=PLyqSpQzTE6M9-v4V62bCygAVYGluaijyo) (70 videos). NPTEL-NOC IITM *Theory of Computation* (Subrahmanyam Kalyanasundaram, IIT Hyderabad): newer, cleaner.
- [MIT 18.404J Theory of Computation, Fall 2020](https://www.youtube.com/playlist?list=PLUl4u3cNGP60_JNv2MmK3wkOt9syvfQWY) (25 videos). MIT 18.404J (Fall 2020, Michael Sipser): taught by the author of the standard textbook.
- [Theory of Computation (Raghunath Tewari, IIT Kanpur, 2016)](https://www.youtube.com/playlist?list=PLidiQIHRzpXLOB6lg8hGUKLbbyekRz7JQ) (42 videos). Raghunath Tewari (IIT Kanpur, 2016) — the NPTEL ToC course, uploaded by a TCS channel.

### ⚡ Short videos for intuition and revision

- [Theory of Computation & Automata Theory](https://www.youtube.com/playlist?list=PLBlnK6fEyqRgp46KUv4ZY69yXmpwKOIev) (100+ videos). Neso Academy *Theory of Computation*: one short video per construction (DFA/NFA/PDA/TM).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [8](https://www.youtube.com/watch?v=_9fuEO5khrI&list=PL85CF9F4A047C7BF7&index=8)–[11](https://www.youtube.com/watch?v=HiN4b-dzie4&list=PL85CF9F4A047C7BF7&index=11) | DFA, NFA, epsilon-NFA, subset construction. Convert 5 NFAs to DFAs by hand; simulate a DFA in Python. |
| 2 | [12](https://www.youtube.com/watch?v=ExG0ToMUsEM&list=PL85CF9F4A047C7BF7&index=12)–[15](https://www.youtube.com/watch?v=Km45DNEa9mI&list=PL85CF9F4A047C7BF7&index=15) | Regular expressions <-> automata, regular grammars. Write a regex-to-NFA (Thompson) converter. |
| 3 | [16](https://www.youtube.com/watch?v=cyAMe39JQ3Y&list=PL85CF9F4A047C7BF7&index=16)–[19](https://www.youtube.com/watch?v=JbxIEzs8jBg&list=PL85CF9F4A047C7BF7&index=19) | Pumping lemma, Myhill-Nerode, DFA minimisation, Moore/Mealy machines. Prove 5 languages non-regular. |
| 4 | [1](https://www.youtube.com/watch?v=-aIRqNnUvEg&list=PL85CF9F4A047C7BF7&index=1)–[7](https://www.youtube.com/watch?v=uc9QZgWle8U&list=PL85CF9F4A047C7BF7&index=7) | Grammars, CFGs, ambiguity, simplification, Chomsky and Greibach normal forms. Convert 3 grammars to CNF. |
| 5 | [20](https://www.youtube.com/watch?v=8O6FUFwWt5A&list=PL85CF9F4A047C7BF7&index=20)–[25](https://www.youtube.com/watch?v=pGOPmYT-APQ&list=PL85CF9F4A047C7BF7&index=25) | Pushdown automata, CFG <-> PDA, pumping lemma for CFLs (16). Implement CYK parsing in Python. |
| 6-7 | [26](https://www.youtube.com/watch?v=IhyEGNn-7Uo&list=PL85CF9F4A047C7BF7&index=26)–[30](https://www.youtube.com/watch?v=XBLRdcGkxyM&list=PL85CF9F4A047C7BF7&index=30) | Turing machines and their variants. Write TMs in a simulator (turingmachine.io) for a^n b^n c^n and binary increment. |
| 8 | [31](https://www.youtube.com/watch?v=KJD_F-QGLmo&list=PL85CF9F4A047C7BF7&index=31)–[35](https://www.youtube.com/watch?v=9OSYj3GSvIA&list=PL85CF9F4A047C7BF7&index=35) | Decidability, universal TM, Rice's theorem, Post's correspondence problem. Then Sipser ch. 4-5 + MIT 18.404 (alt) lectures on reductions. |
| 9 | [36](https://www.youtube.com/watch?v=qpCvPS-WwGA&list=PL85CF9F4A047C7BF7&index=36)–[37](https://www.youtube.com/watch?v=-axSdJ6gpVc&list=PL85CF9F4A047C7BF7&index=37) | NP-completeness and Cook's theorem. 38-42 (L-systems, DNA computing) are optional. |

<details>
<summary>All lectures in <i>Computer - Theory of Automata, Formal Languages and Computation</i> (42 videos)</summary>

1. [Mod-01 Lec-01 GRAMMARS AND NATURAL LANGUAGE PROCESSING](https://www.youtube.com/watch?v=-aIRqNnUvEg&list=PL85CF9F4A047C7BF7&index=1)
2. [Mod-01 Lec-02 GRAMMARS AND LANGUAGES GENERATED](https://www.youtube.com/watch?v=rnGpW6RRAcw&list=PL85CF9F4A047C7BF7&index=2)
3. [Mod-01 Lec-03 GRAMMARS AND LANGUAGES GENERATED (Contd)](https://www.youtube.com/watch?v=A-cJBuwLUx8&list=PL85CF9F4A047C7BF7&index=3)
4. [Mod-01 Lec-04 AMBIGUITY IN CFG](https://www.youtube.com/watch?v=rjWqEI3HOD4&list=PL85CF9F4A047C7BF7&index=4)
5. [Mod-01 Lec-05 SIMPLICATION OF CFG](https://www.youtube.com/watch?v=Xk-MTgB68rQ&list=PL85CF9F4A047C7BF7&index=5)
6. [Mod-01 Lec-06 REMOVAL OF UNIT PRODUCTIONS , CHOMSKY NORMAL FORM FOR CFG](https://www.youtube.com/watch?v=AT0baggXDeA&list=PL85CF9F4A047C7BF7&index=6)
7. [Mod-01 Lec-07 GREIBACH NORMAL FORM FOR CFG](https://www.youtube.com/watch?v=uc9QZgWle8U&list=PL85CF9F4A047C7BF7&index=7)
8. [Mod-02 Lec-08 FINAL STATE AUTOMATA](https://www.youtube.com/watch?v=_9fuEO5khrI&list=PL85CF9F4A047C7BF7&index=8)
9. [Mod-02 Lec-09 NON-DETERMINISTIC FSA](https://www.youtube.com/watch?v=D3dc4dbBFGI&list=PL85CF9F4A047C7BF7&index=9)
10. [Mod-02 Lec-10 NON DETERMINISTIC FSA (Contd)](https://www.youtube.com/watch?v=hv_KHbK46Vc&list=PL85CF9F4A047C7BF7&index=10)
11. [Mod-02 Lec-11 NON DETERMINISTIC FSA WITH E(Epsilon)- MOVES](https://www.youtube.com/watch?v=HiN4b-dzie4&list=PL85CF9F4A047C7BF7&index=11)
12. [Mod-02 Lec-12 EQUIVALENCE BETWEEN FSA AND TYPE 3 GRAMMARS](https://www.youtube.com/watch?v=ExG0ToMUsEM&list=PL85CF9F4A047C7BF7&index=12)
13. [Mod-02 Lec-13 REGULAR EXPRESSIONS , REGULAR EXPRESSIONS TO NFSA](https://www.youtube.com/watch?v=NfhXY_nttSg&list=PL85CF9F4A047C7BF7&index=13)
14. [Mod-02 Lec-14 DFSA TO REGULAR EXPRESSIONS](https://www.youtube.com/watch?v=VA4kWwJc9Uo&list=PL85CF9F4A047C7BF7&index=14)
15. [Mod-02 Lec-15 PROBLEMS AND SOLUTIONS](https://www.youtube.com/watch?v=Km45DNEa9mI&list=PL85CF9F4A047C7BF7&index=15)
16. [Mod-02 Lec-16 PUMPING LEMMAS FOR REGULAR SETS AND CFL](https://www.youtube.com/watch?v=cyAMe39JQ3Y&list=PL85CF9F4A047C7BF7&index=16)
17. [Mod-02 Lec-17 MYHILL-NERODE THEOREM](https://www.youtube.com/watch?v=tPUWmgFw3QA&list=PL85CF9F4A047C7BF7&index=17)
18. [Mod-02 Lec-18 MINIMIZATION OF DFSA](https://www.youtube.com/watch?v=6c_LxYg_ImM&list=PL85CF9F4A047C7BF7&index=18)
19. [Mod-02 Lec-19 FSA WITH OUTPUT MOORE AND MEALY MACHINES](https://www.youtube.com/watch?v=JbxIEzs8jBg&list=PL85CF9F4A047C7BF7&index=19)
20. [Mod-03 Lec-20 PUSHDOWN AUTOMATA](https://www.youtube.com/watch?v=8O6FUFwWt5A&list=PL85CF9F4A047C7BF7&index=20)
21. [Mod-03 Lec-21 PUSHDOWN AUTOMATA,EQUIVALENCE BETWEEN ACCEPTANCE BY EMPTY STORE](https://www.youtube.com/watch?v=BnIlVgZbqV0&list=PL85CF9F4A047C7BF7&index=21)
22. [Mod-03 Lec-22 PUSHDOWN AUTOMATA CFG TO PDA](https://www.youtube.com/watch?v=MJ9xNavURY8&list=PL85CF9F4A047C7BF7&index=22)
23. [Mod-04 Lec-23 PUSHDOWN AUTOMATA PDA TO CFG](https://www.youtube.com/watch?v=b3OPl5wS4AQ&list=PL85CF9F4A047C7BF7&index=23)
24. [Mod-04 Lec-24 PROBLEMS AND SOLUTIONS-I](https://www.youtube.com/watch?v=V3sv_FRqRJ4&list=PL85CF9F4A047C7BF7&index=24)
25. [Mod-04 Lec-25 PROBLEMS AND SOLUTIONS - III](https://www.youtube.com/watch?v=pGOPmYT-APQ&list=PL85CF9F4A047C7BF7&index=25)
26. [Mod-05 Lec-26 TURING MACHINES](https://www.youtube.com/watch?v=IhyEGNn-7Uo&list=PL85CF9F4A047C7BF7&index=26)
27. [Mod-05 Lec-27 TURING MACHINES (Contd)](https://www.youtube.com/watch?v=1SOi9Zp4X3c&list=PL85CF9F4A047C7BF7&index=27)
28. [Mod-05 Lec-28 TURING MACHINE AS ACCEPTOR , TECHNIQUES FOR TM CONSTRUCTION](https://www.youtube.com/watch?v=vhSMp91tS6k&list=PL85CF9F4A047C7BF7&index=28)
29. [Mod-05 Lec-29 GENERALIZED VERSIONS OF TURING MACHINES](https://www.youtube.com/watch?v=8KuGjioBTIY&list=PL85CF9F4A047C7BF7&index=29)
30. [Mod-05 Lec-30 TURING MACHINE AS A GENERATING DEVICE](https://www.youtube.com/watch?v=XBLRdcGkxyM&list=PL85CF9F4A047C7BF7&index=30)
31. [Mod-06 Lec-31 RECURSIVE SETS , RECURSIVELY INNUMERABLE SETS , ENCODING OF TM , HALTING PROBLEM](https://www.youtube.com/watch?v=KJD_F-QGLmo&list=PL85CF9F4A047C7BF7&index=31)
32. [Mod-06 Lec-32 PROBLEMS AND INSTANCES , UNIVERSAL TM , DECIDABILITY](https://www.youtube.com/watch?v=3upnsi1kFl0&list=PL85CF9F4A047C7BF7&index=32)
33. [Mod-06 Lec-33 RICE'S THEOREM,LINEAR BOUNDED AUTOMATA,PROPERTIES OF TM](https://www.youtube.com/watch?v=kFH4X69L1JU&list=PL85CF9F4A047C7BF7&index=33)
34. [Mod-06 Lec-34 POST'S CORRESPONDENCE PROBLEMS](https://www.youtube.com/watch?v=YSr5zmVqZLI&list=PL85CF9F4A047C7BF7&index=34)
35. [Mod-07 Lec-35 POST'S CORRESPONDENCE PROBLEMS (Contd) TIME AND TAPE COMPLEXITY OT TM](https://www.youtube.com/watch?v=9OSYj3GSvIA&list=PL85CF9F4A047C7BF7&index=35)
36. [Mod-07 Lec-36 NP - COMPLETE PROBLEMS , COOK'S THEOREM](https://www.youtube.com/watch?v=qpCvPS-WwGA&list=PL85CF9F4A047C7BF7&index=36)
37. [Mod-07 Lec-37 NP - COMPLETE PROBLEMS (Contd)](https://www.youtube.com/watch?v=-axSdJ6gpVc&list=PL85CF9F4A047C7BF7&index=37)
38. [Mod-08 Lec-38 REGULATED REWRITING](https://www.youtube.com/watch?v=wsH2U7AVN9k&list=PL85CF9F4A047C7BF7&index=38)
39. [Mod-08 Lec-39 L - SYSTEMS](https://www.youtube.com/watch?v=ekLFTqNV_J4&list=PL85CF9F4A047C7BF7&index=39)
40. [Mod-08 Lec-40 GRAMMAR SYSTEMS](https://www.youtube.com/watch?v=tG3tUV5eUYQ&list=PL85CF9F4A047C7BF7&index=40)
41. [Mod-09 Lec-41 DNA COMPUTING](https://www.youtube.com/watch?v=CNu5RDittrE&list=PL85CF9F4A047C7BF7&index=41)
42. [Mod-09 Lec-42 MEMBRANE COMPUTING](https://www.youtube.com/watch?v=GQvNv9uhmbw&list=PL85CF9F4A047C7BF7&index=42)

</details>


## Books, notes and websites

- ✅ NPTEL *Theory of Computation* (Raghunath Tewari, IIT Kanpur) — see classcentral.com/mooc/6701/nptel-theory-of-computation
- Book: Michael Sipser, *Introduction to the Theory of Computation*
- Jeff Erickson, *Models of Computation* notes (free)
- JFLAP to simulate automata

## Practice / proof of understanding

Build a DFA minimiser and a CYK parser in code; prove 5 languages non-regular with the pumping lemma; reduce 3 problems to Halting.

## What your IITM course sheet says

### From the PDF: CS2200

**Official description:** To introduce students to the basic concepts in theoretical computer science, and the formal relationships among  machines, languages, grammars, and computational problems. After completing the course, the student will be  able to:  • Model, compare and analyse different computational models using combinatorial methods.  • Apply rigorously formal mathematical methods to prove properties of languages, grammars and automata.  • Construct algorithms for different problems and argue formally about correctness on different restricted  machine models of computation.  • Identify limitations of some computational models and possible methods of proving them.  • Have an overview of how the theoretical study in this course is applicable to and engineering application like  designing the compilers.

**Official syllabus (trimmed):**

> Four basic themes (but related in a flow) : 44L + 12T
>  Finite Automata & Regular Languages - 13L + 3T
>  Languages vs Problems. Finite State Automata, Regular Languages. Closure properties, Limitations, Pumping
>  Lemma, Myhill-Nerode relations, Quotient Construction. Minimization Algorithm.
>  Non-determinism & Regular Expressions - 8L + 2T
>  Notion of non-determinism. Acceptance condition. Subset construction. Pattern matching and regular
>  expressions. Regular Expressions and Regular languages. More closure properties of regular languages.
>  Grammars & Context-free Languages(CFLs) - 15L + 5T
>  Grammars and Chomsky Hierarchy, CFLs, Regular Grammars, Chomsky Normal Form, Pumping Lemma for
>  CFLs, Inherent Ambiguity of Context-Free Languages, Cock-Younger-Kasami Algorithm, Applications to Parsing.
>  Pushdown Automata(PDA), PDA vs CFLs. Deterministic CFLs.
>  Turing Machines & Computability - 9L + 2T
>  Introduction to Turing Machines, Configurations, Halting vs Looping. Multi-tape Turing machines. Recursive and
>  Recursively enumerable languages. Undecidability of Halting Problem. Reductions. Introduction to Theory of
>  NP-completeness.

**Official textbooks:** 1. Michael Sipser “Introduction to the Theory of Computation”, 3rd Edition, CENGAGE Learning, 2012.  2. Dexter Kozen “Automata and Computability” Springer-Verlag, 1997.

**Official references:** 1. J. E. Hopcroft, R. Motwani and J. D. Ullman, "Introduction to automata theory, languages and computation",  Pearson Education Asia, 2001  2. H. R. Lewis and C.H. papadinitriou, "Elements of the theory of computation", Prentice Hall International  Editions, 1981.
