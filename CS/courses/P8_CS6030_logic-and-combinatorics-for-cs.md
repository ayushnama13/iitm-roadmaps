# CS6030 — Logic and Combinatorics for CS

| | |
|---|---|
| Tier | C |
| Phase (order) | 8 |
| Do this first | CS1200, CS1202 |
| Estimated effort | 10-12 weeks |
| Unlocks | CS5692, CS6850 |

## Roadmap

1. Propositional and first-order logic, resolution, SAT.
2. Advanced counting and probabilistic method.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Mathematics - Mathematical Logic](https://www.youtube.com/playlist?list=PL2EB5662A0D455A81) (42 videos). NPTEL *Mathematical Logic* (nptelhrd): propositional/first-order logic, soundness, completeness.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Computer Science - Combinatorics](https://www.youtube.com/playlist?list=PLbMVogVj5nJTvqxdydl8wRH_U1dNeVSOV) (41 videos). NPTEL *Combinatorics* (nptelhrd): counting, recurrences, generating functions, Polya.
- [Set Theory and Mathematical Logic](https://www.youtube.com/playlist?list=PLFW6lRTa1g83LYdhDkUQfkXs7EbMBwYuF) (52 videos). NPTEL *Set Theory and Mathematical Logic* (IIT Kanpur).
- [MIT 18.200 Principles of Discrete Applied Mathematics, Spring 2024](https://www.youtube.com/playlist?list=PLUl4u3cNGP61p2fXeXjNCrfNHFwyW-bl0) (20 videos). MIT 18.200 *Principles of Discrete Applied Mathematics* (Spring 2024, official OCW).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=ziID8gefa0g&list=PL2EB5662A0D455A81&index=1)–[6](https://www.youtube.com/watch?v=YSleI5KNrNo&list=PL2EB5662A0D455A81&index=6) | Propositional logic: syntax, unique parsing, semantics, consequence. |
| 2 | [7](https://www.youtube.com/watch?v=oWrwj03RTcg&list=PL2EB5662A0D455A81&index=7)–[14](https://www.youtube.com/watch?v=yyGtbgxhnIM&list=PL2EB5662A0D455A81&index=14) | Informal proofs, normal forms, SAT/3SAT, Horn-SAT, resolution. Write a DPLL SAT solver; try PySAT/MiniSat. |
| 3 | [15](https://www.youtube.com/watch?v=OBxprOjTjoM&list=PL2EB5662A0D455A81&index=15)–[21](https://www.youtube.com/watch?v=a8OXlUcbmEM&list=PL2EB5662A0D455A81&index=21) | Propositional calculus, adequacy, compactness, analytic tableaux. |
| 4 | [22](https://www.youtube.com/watch?v=FYaMsTxb7Lc&list=PL2EB5662A0D455A81&index=22)–[31](https://www.youtube.com/watch?v=rQRrMVCxV5M&list=PL2EB5662A0D455A81&index=31) | First-order logic: syntax, semantics, validity, quantifier laws, prenex form. |
| 5 | [32](https://www.youtube.com/watch?v=ca7su2T1vrA&list=PL2EB5662A0D455A81&index=32)–[38](https://www.youtube.com/watch?v=aqBf8N4cPCo&list=PL2EB5662A0D455A81&index=38) | Skolem form, Herbrand's theorem, unification, resolution. Implement unification. |
| 6 | [39](https://www.youtube.com/watch?v=woZn2S90048&list=PL2EB5662A0D455A81&index=39)–[42](https://www.youtube.com/watch?v=iqX8m3wBfSc&list=PL2EB5662A0D455A81&index=42) | Axiomatic system, semi-decidability, tableaux for FOL, Gödel's incompleteness. Combinatorics half: use the alt series. |

<details>
<summary>All lectures in <i>Mathematics - Mathematical Logic</i> (42 videos)</summary>

1. [Mod-01 Lec-01 Sets and Strings](https://www.youtube.com/watch?v=ziID8gefa0g&list=PL2EB5662A0D455A81&index=1)
2. [Mod-01 Lec-02 Lecture-02-Syntax of Propositional Logic](https://www.youtube.com/watch?v=2f5Z7OiZg6E&list=PL2EB5662A0D455A81&index=2)
3. [Mod-01 Lec-03 Lecture-03-Unique Parsing](https://www.youtube.com/watch?v=hTpIZ9F7fBQ&list=PL2EB5662A0D455A81&index=3)
4. [Mod-01 Lec-04 Lecture-04-Semantics of PL](https://www.youtube.com/watch?v=HmqdgK4xMrE&list=PL2EB5662A0D455A81&index=4)
5. [Mod-01 Lec-05 Lecture-05-Consequences and Equivalences](https://www.youtube.com/watch?v=KBKX0gvpvg8&list=PL2EB5662A0D455A81&index=5)
6. [Mod-01 Lec-06 Five results about PL](https://www.youtube.com/watch?v=YSleI5KNrNo&list=PL2EB5662A0D455A81&index=6)
7. [Mod-01 Lec-07 Lecture-07-Calculations and Informal Proofs](https://www.youtube.com/watch?v=oWrwj03RTcg&list=PL2EB5662A0D455A81&index=7)
8. [Mod-01 Lec-08 Lecture-08-More Informal Proofs](https://www.youtube.com/watch?v=0FeQDUzsvws&list=PL2EB5662A0D455A81&index=8)
9. [Mod-01 Lec-09 Lecture-09-Normal forms](https://www.youtube.com/watch?v=C5CFAKKS9Ag&list=PL2EB5662A0D455A81&index=9)
10. [Mod-01 Lec-10 Lecture-10-SAT and 3SAT](https://www.youtube.com/watch?v=3iolN4ntczg&list=PL2EB5662A0D455A81&index=10)
11. [Mod-01 Lec-11 Lecyture-11-Horn-SAT and Resolution](https://www.youtube.com/watch?v=Iy8t2SkFbJU&list=PL2EB5662A0D455A81&index=11)
12. [Mod-01 Lec-12 Lecture-12-Resolution](https://www.youtube.com/watch?v=2NiDdmOIJB4&list=PL2EB5662A0D455A81&index=12)
13. [Mod-01 Lec-13 Lecture-13-Adequacy of Resolution](https://www.youtube.com/watch?v=OUwwvsFSye8&list=PL2EB5662A0D455A81&index=13)
14. [Mod-01 Lec-14 Lecture-14-Adequacy and Resolution Strategies](https://www.youtube.com/watch?v=yyGtbgxhnIM&list=PL2EB5662A0D455A81&index=14)
15. [Mod-01 Lec-15 Lecture-15-Propositional Calculus (PC)](https://www.youtube.com/watch?v=OBxprOjTjoM&list=PL2EB5662A0D455A81&index=15)
16. [Mod-01 Lec-16 Lecture-16-Some Results about PC](https://www.youtube.com/watch?v=oJOK9ZVOrpk&list=PL2EB5662A0D455A81&index=16)
17. [Mod-01 Lec-17 Lecture-17-Arguing with Proofs](https://www.youtube.com/watch?v=SdSftqR0Pjg&list=PL2EB5662A0D455A81&index=17)
18. [Mod-01 Lec-18 Lecture-18-Adequacy of PC](https://www.youtube.com/watch?v=ScbRSyv0YtE&list=PL2EB5662A0D455A81&index=18)
19. [Mod-01 Lec-19 Lecture-19-Compactness & Analytic Tableau](https://www.youtube.com/watch?v=zzX-4QkM2cw&list=PL2EB5662A0D455A81&index=19)
20. [Mod-01 Lec-20 Lecture-20-Examples of Tableau Proofs](https://www.youtube.com/watch?v=PXNM5QxbESs&list=PL2EB5662A0D455A81&index=20)
21. [Mod-01 Lec-21 Lecture-21-Adequacy of Tableaux](https://www.youtube.com/watch?v=a8OXlUcbmEM&list=PL2EB5662A0D455A81&index=21)
22. [Mod-01 Lec-22 Lecture-22-Syntax of First order Logic (FL)](https://www.youtube.com/watch?v=FYaMsTxb7Lc&list=PL2EB5662A0D455A81&index=22)
23. [Mod-01 Lec-23 Lecture-23-Symbolization & Scope of Quantifiers](https://www.youtube.com/watch?v=vziZnasAgwo&list=PL2EB5662A0D455A81&index=23)
24. [Mod-01 Lec-24 Lecture-24-Hurdles in giving Meaning](https://www.youtube.com/watch?v=u97eawdg0Z8&list=PL2EB5662A0D455A81&index=24)
25. [Mod-01 Lec-25 Lecture-25-Semantics of FL](https://www.youtube.com/watch?v=-5bMMJs0ZPo&list=PL2EB5662A0D455A81&index=25)
26. [Mod-01 Lec-26 Lecture-26-Relevance Lemma](https://www.youtube.com/watch?v=ZIyvb3s4zDE&list=PL2EB5662A0D455A81&index=26)
27. [Mod-01 Lec-27 Lecture-27-Validity, Satisfiability & Equivalence](https://www.youtube.com/watch?v=kGlVe_VIU3g&list=PL2EB5662A0D455A81&index=27)
28. [Mod-01 Lec-28 Lecture-28-Six Results about FL](https://www.youtube.com/watch?v=Nj0mWmaVFBk&list=PL2EB5662A0D455A81&index=28)
29. [Mod-01 Lec-29 Lecture-29-Laws, Calculation & Informal Proof](https://www.youtube.com/watch?v=-OfCXFs51M4&list=PL2EB5662A0D455A81&index=29)
30. [Mod-01 Lec-30 Lecture-30-Quantifier Laws and Consequences](https://www.youtube.com/watch?v=9Xf5Q8rWZNo&list=PL2EB5662A0D455A81&index=30)
31. [Mod-01 Lec-31 Lecture-31-More Proofs and Prenex Form](https://www.youtube.com/watch?v=rQRrMVCxV5M&list=PL2EB5662A0D455A81&index=31)
32. [Mod-01 Lec-32 Lecture-32-Prenex Form Conversion](https://www.youtube.com/watch?v=ca7su2T1vrA&list=PL2EB5662A0D455A81&index=32)
33. [Mod-01 Lec-33 Lecture-33-Skolem Form](https://www.youtube.com/watch?v=ILpy0vDLGLA&list=PL2EB5662A0D455A81&index=33)
34. [Mod-01 Lec-34 Lecture-34-Syntatic Interpretation](https://www.youtube.com/watch?v=2Xhph31lS50&list=PL2EB5662A0D455A81&index=34)
35. [Mod-01 Lec-35 Lecture-35-Herbrand's Theorem](https://www.youtube.com/watch?v=iuZh96SJy-I&list=PL2EB5662A0D455A81&index=35)
36. [Mod-01 Lec-36 Lecture-36-Most General Unifiers](https://www.youtube.com/watch?v=1NFDhFky0lI&list=PL2EB5662A0D455A81&index=36)
37. [Mod-01 Lec-37 Lecture-37-Resolution Rules](https://www.youtube.com/watch?v=a6UJk0S6KvE&list=PL2EB5662A0D455A81&index=37)
38. [Mod-01 Lec-38 Lecture-38-Resolution Examples](https://www.youtube.com/watch?v=aqBf8N4cPCo&list=PL2EB5662A0D455A81&index=38)
39. [Mod-01 Lec-39 Lecture-39-Ariomatic System FC](https://www.youtube.com/watch?v=woZn2S90048&list=PL2EB5662A0D455A81&index=39)
40. [Mod-01 Lec-40 Lecture-40-FC and Semidecidability of FL](https://www.youtube.com/watch?v=ywPPNhkHdwE&list=PL2EB5662A0D455A81&index=40)
41. [Mod-01 Lec-41 Lecture-41-Analytic Tableau for FL](https://www.youtube.com/watch?v=Loskv9Dulmc&list=PL2EB5662A0D455A81&index=41)
42. [Mod-01-Lec-42 Lecture-42-Godels Incompleteness Theorems](https://www.youtube.com/watch?v=iqX8m3wBfSc&list=PL2EB5662A0D455A81&index=42)

</details>


## Books, notes and websites

- Book: Huth & Ryan, *Logic in Computer Science*
- Book: van Lint & Wilson, *A Course in Combinatorics*

## Practice / proof of understanding

Write a DPLL SAT solver.

## What your IITM course sheet says

### From the PDF: CS6030

**Official description:** The course is intended to provide the foundations to mathematical rigor that are used in most areas of Computer  Science and limitations of computation. The topics include Logic, Basic Combinatorics and elements of  Computability.

**Official syllabus (trimmed):**

> Language of Math – Sets, relations, functions (quick review) Logic : Propositional Logic, Predicate and First order
>  Logic, Examples, Soundness and Completeness. Second Order Logic. Incompleteness theorems. Further
>  extensions of logic (MSO, Temporal etc). Subsets of first order logic. Example Applications. Proofs: Mathematical
>  Arguments and Argument Forms, Inference Rules, Notion of a Proof and validity of an argument, Various Proof
>  techniques and examples, Identifying fallacies. Infinite Sets: Countable and uncountable sets, Cantor’s
>  diagonalization. Undecidability : Turing Machines, Church-Turing Thesis. Notion of Computation and decidability,
>  Undecidability of the Halting Problem. Consequences to the Program Verification Problem. Combinatorics
>  Basics: Pigeonhole Principle and applications (e.g., Ramsey Theorem) Counting methods: Principle of Inclusion
>  Exclusion, Proving Combinatorial Identities, Combinatorial Arguments, Permutations, Derangements. Recurrence:
>  Linear recurrences, method of roots. Generating Functions. Examples Structured Sets: Posets and Lattices, Fixed
>  Point Theorems (Knaster-Tarski and Polya), Monoids, Semigroups, Groupoids and Groups, Examples, Subgroups,
>  Cosets, Lagrange’s theorem. Introduction to Polya’s theory of counting.

**Official textbooks:** 1) Discrete Mathematics and its Applications – Kenneth H. Rosen 7th Edition -Tata McGraw Hill Publishers –  2007.2) Introduction to Automata Theory, Languages and Computation (third edition) - John Hopcroft, Rajeev  Motwani, and Jeffrey Ullman, Pearson Education Publishers, 2006.3) A Mathematical Introduction to Logic  (second edition) - Herbert B Enderton, Academic Press , 2001.

**Official references:** 1. Combinatorics: Topics, Techniques, Algorithms by Peter J. Cameron, Cambridge University Press, 1994 (reprint  1996).2. Concrete Mathematics – Ronald Graham, Donald Knuth, and Oren Patashnik, 2nd Edition - Pearson  Education Publishers - 1996.

### From the PDF: CS5692

**Official description:** Mathematical Logic forms the foundation of many theoretical and practical aspects of computer science. This  course aims to introduce the students to the foundations of Mathematical Logic and its applications in computer  science.

**Official syllabus (trimmed):**

> Module 1:Propositional Logic (PL) and First Order Logic (FOL) [3 Weeks]
>  Syntax
>  Structures and Semantics
>  Modeling various scenarios in these logics, Logical Paradoxes
>  Notions of Satisfiability, Model Checking, Validity
>  Compactness Theorem
>  Module 2 : Axiom Systems for PL and FOL [2 Weeks]
>  Hilbert style axiom system
>  Natural Deduction
>  Sequent Calculus
>  Module 3 : Modal Logic (ML) [3 Weeks]
>  Syntax
>  Kripke Structures and Semantics
>  Epistemic Logic, Temporal Logic, Doxastic Logic
>  Sound and Complete Axiom System
>  Bisimulation
>  Module 4 : Algorithms and Complexity [3 Weeks]
>  Satisfiability problem for PL, FOL and ML
>  Model Checking problem for PL, FOL and ML
>  Decidable fragments of FOL
>  (Un)decidability of various Theories
>  Module 5 : Applications (Some of the following topics depending on time) [3 Weeks]
>  Logic and Databases
>  Logic and Complexity
>  Logic and Automata Theory
>  Logic and Formal Verification
>  Logic and Artificial Intelligence

**Official textbooks:** A Mathematical Introduction to Logic by Herbert Enderton  Publication : Academic Press, Year : 2001  Modal Logic by Patrick Blackburn, Maarten de Rijke and, Yde Venema  Publisher : Cambridge University Press, 2nd Edition ; Year : 2014

**Official references:** Dynamic Epistemic Logic by Hans Ditmarsch , Wiebe Hoek , Barteld Kooi  Publication : Academic Press, Year : 2001  Principles of Databases by Marcelo Arenas, Pablo Barcelo ´, Leonid Libkin, Wim Marten and Andreas Pieris  Publication : Springer Year : 2008  The Classical Decision Problem by Egon Borger, Erich Gradel and Yuri Gurevic  Publication : Springer Year : 1997  Logic and Automata: History an
