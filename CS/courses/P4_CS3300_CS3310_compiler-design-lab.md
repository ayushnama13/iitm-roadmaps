# CS3300+CS3310 — Compiler Design (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 4 |
| Do this first | CS2200, CS2705, CS2600 |
| Estimated effort | 14 weeks, ~9 h/week |
| Unlocks | CS6848, CS6013, CS6843 |

## Roadmap

1. Lexing: regular expressions to tokens (flex).
2. Parsing: top-down and LALR (bison); resolve conflicts.
3. Syntax-directed translation, semantic analysis, type checking.
4. Intermediate code, runtime environments, simple optimisation and register allocation.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [NOC Jan 2019: Compiler Design](https://www.youtube.com/playlist?list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP) (62 videos). NPTEL *Compiler Design* (Santanu Chattopadhyay, IIT Kharagpur, 2019).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Computer Science - Principles of Compiler Design](https://www.youtube.com/playlist?list=PLbMVogVj5nJQNjkHZgwuAlfQ9tzmQDxjA) (40 videos). NPTEL *Principles of Compiler Design* (Y.N. Srikant, IISc): strongest on optimisation and code generation.
- [Compiler Design by Sorav Bansal - IIT Delhi](https://www.youtube.com/playlist?list=PLf3ZkSCyj1tf3rPAkOKY5hUzDrDoekAc7) (100+ videos). Sorav Bansal (IIT Delhi) *Compiler Design*: modern, project-driven.
- [Stanford CS143: Compilers](https://www.youtube.com/playlist?list=PLUznfNKscdcMzIV_9WtSgtmVemc0JoJhn) (19 videos). Stanford CS143 (Alex Aiken) re-upload: the classic COOL-compiler course.

### ⚡ Short videos for intuition and revision

- [Compiler Design](https://www.youtube.com/playlist?list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q) (42 videos). Neso Academy *Compiler Design*: parsing tables step by step.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=_ck1Lnm28hQ&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=1)–[7](https://www.youtube.com/watch?v=kJlOkN1iBHQ&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=7) | Compiler structure and phases. Read the Crafting Interpreters intro; pick your project language (a tiny C subset). |
| 2-3 | [8](https://www.youtube.com/watch?v=xBQEqI91cJM&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=8)–[16](https://www.youtube.com/watch?v=A7BvcTuk1V0&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=16) | Lexical analysis: regex, finite automata, lex/flex. Write a hand-coded lexer, then the same with flex. |
| 4-7 | [17](https://www.youtube.com/watch?v=IdCT0KgUZXU&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=17)–[39](https://www.youtube.com/watch?v=Lfv89iS-qmw&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=39) | Parsing: top-down (LL(1), recursive descent), bottom-up (SLR, LR(1), LALR), yacc/bison. Write a recursive-descent parser producing an AST; then one grammar in bison. |
| 8 | [40](https://www.youtube.com/watch?v=9gbZ_DlG7CY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=40)–[43](https://www.youtube.com/watch?v=Wz_R0PMXfPE&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=43) | Type checking. Add a type checker pass to your AST. |
| 9 | [44](https://www.youtube.com/watch?v=FQb0hQ6Bgp8&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=44)–[50](https://www.youtube.com/watch?v=3kKCeIwHUHY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=50) | Symbol tables and runtime environments (activation records, stack layout). Implement scoped symbol tables. |
| 10-12 | [51](https://www.youtube.com/watch?v=Gc6PpW_SxKY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=51)–[62](https://www.youtube.com/watch?v=GCE20jvFv5k&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=62) | Intermediate code generation (three-address code). Emit TAC, then generate x86-64 or RISC-V assembly and run real programs. Code optimisation: Sorav Bansal (alt) lectures. |

<details>
<summary>All lectures in <i>NOC Jan 2019: Compiler Design</i> (62 videos)</summary>

1. [Compiler Design](https://www.youtube.com/watch?v=_ck1Lnm28hQ&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=1)
2. [Lecture : 01 Introduction](https://www.youtube.com/watch?v=7Nb-NTGbe-Q&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=2)
3. [Lecture 02: Introduction (Contd.)](https://www.youtube.com/watch?v=aa2ZdZXnGeY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=3)
4. [Lecture : 03 Introduction (Contd.)](https://www.youtube.com/watch?v=L7B7b9phxV8&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=4)
5. [Lecture : 04 Introduction (Contd.)](https://www.youtube.com/watch?v=IstUr884mnA&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=5)
6. [Lecture : 05 Introduction (Contd.)](https://www.youtube.com/watch?v=vcVHjoSYU_M&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=6)
7. [Lecture 06: Introduction (Contd.)](https://www.youtube.com/watch?v=kJlOkN1iBHQ&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=7)
8. [Lecture 07: Lexical Analysis](https://www.youtube.com/watch?v=xBQEqI91cJM&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=8)
9. [Lecture 08: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=5Vv3HHSeJUA&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=9)
10. [Lecture 09: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=EBTK19pGYiQ&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=10)
11. [Lecture 10: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=zpuouhg1NWM&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=11)
12. [Lecture 11: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=HVkeeVNs1Ws&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=12)
13. [Lecture 12: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=MjTdYxEF0Ug&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=13)
14. [Lecture 13: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=NoLQWQZGmWs&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=14)
15. [Lecture 14: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=IWBCw2CYswg&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=15)
16. [Lecture 15: Lexical Analysis (Contd.)](https://www.youtube.com/watch?v=A7BvcTuk1V0&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=16)
17. [Lecture 16: Parser](https://www.youtube.com/watch?v=IdCT0KgUZXU&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=17)
18. [Lecture 17: Parser (Contd.)](https://www.youtube.com/watch?v=qB3rcEdutFs&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=18)
19. [Lecture 18: Parser (Contd.)](https://www.youtube.com/watch?v=Hpn9rv60NlQ&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=19)
20. [Lecture 19: Parser (Contd.)](https://www.youtube.com/watch?v=yE8JXOwWo5I&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=20)
21. [Lecture 20: Parser (Contd.)](https://www.youtube.com/watch?v=P9uw8XyVtF8&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=21)
22. [Lecture 21: Parser (Contd.)](https://www.youtube.com/watch?v=T8Kmq-4O4hA&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=22)
23. [Lecture 22: Parser (Contd.)](https://www.youtube.com/watch?v=PEWYrFEZBTg&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=23)
24. [Lecture 23: Parser (Contd.)](https://www.youtube.com/watch?v=fz343jMkztY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=24)
25. [Lecture 24: Parser (Contd.)](https://www.youtube.com/watch?v=1cS7MMI7AW0&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=25)
26. [Lecture 25: Parser (Contd.)](https://www.youtube.com/watch?v=mXJ6Ega1olM&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=26)
27. [Lecture 26: Parser (Contd.)](https://www.youtube.com/watch?v=G4LKvUireu4&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=27)
28. [Lecture 27: Parser (Contd.)](https://www.youtube.com/watch?v=tvNy8-oqoq0&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=28)
29. [Lecture 28: Parser (Contd.)](https://www.youtube.com/watch?v=W9ZYZpcB74c&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=29)
30. [Lecture 29: Parser (Contd.)](https://www.youtube.com/watch?v=QFVorwdIZRg&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=30)
31. [Lecture 30: Parser (Contd.)](https://www.youtube.com/watch?v=LRyPoWMHlm0&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=31)
32. [Lecture 31: Parser (Contd.)](https://www.youtube.com/watch?v=TytQ3XsDGWk&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=32)
33. [Lecture 32: Parser (Contd.)](https://www.youtube.com/watch?v=Uzlslklu8ck&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=33)
34. [Lecture 33: Parser (Contd.)](https://www.youtube.com/watch?v=av1hcgGIynE&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=34)
35. [Lecture 34: Parser (Contd.)](https://www.youtube.com/watch?v=CsO7ZC9kSPI&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=35)
36. [Lecture 35: Parser (Contd.)](https://www.youtube.com/watch?v=w7TX9qwbS30&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=36)
37. [Lecture 36: Parser (Contd.)](https://www.youtube.com/watch?v=XeK5bq6AHhc&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=37)
38. [Lecture 37: Parser (Contd.)](https://www.youtube.com/watch?v=trApFScoviI&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=38)
39. [Lecture 38: Parser (Contd.)](https://www.youtube.com/watch?v=Lfv89iS-qmw&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=39)
40. [Lecture 39: Type Checking](https://www.youtube.com/watch?v=9gbZ_DlG7CY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=40)
41. [Lecture 40: Type Checking(Contd.)](https://www.youtube.com/watch?v=p-hJBrfmPGU&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=41)
42. [Lecture 41: Type Checking(Contd.)](https://www.youtube.com/watch?v=AtGkOBVNjV0&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=42)
43. [Lecture 42: Type Checking(Contd.)](https://www.youtube.com/watch?v=Wz_R0PMXfPE&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=43)
44. [Lecture 43: Symbol Table](https://www.youtube.com/watch?v=FQb0hQ6Bgp8&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=44)
45. [Lecture 44: Symbol Table (Contd.)](https://www.youtube.com/watch?v=Rcw2Iy5Mfso&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=45)
46. [Lecture 45: Symbol Table (Contd.)](https://www.youtube.com/watch?v=nWXL0EBITbE&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=46)
47. [Lecture 46: Symbol Table (Contd.) and Runtime Environment](https://www.youtube.com/watch?v=uVaY1eKI2WY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=47)
48. [Lecture 47: Runtime Environment](https://www.youtube.com/watch?v=RS822U7naxQ&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=48)
49. [Lecture 48: Runtime Environment (Contd.)](https://www.youtube.com/watch?v=-G5aPgAgZxU&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=49)
50. [Lecture 49: Runtime Environment (Contd.)](https://www.youtube.com/watch?v=3kKCeIwHUHY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=50)
51. [Lecture 50: Intermediate Code Generation](https://www.youtube.com/watch?v=Gc6PpW_SxKY&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=51)
52. [Lecture 51: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=QgqgAfSR-1g&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=52)
53. [Lecture 52: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=yVLRP_dBpHI&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=53)
54. [Lecture 53: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=1vgrUXhrlm0&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=54)
55. [Lecture 54: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=vWU2QQp0HBk&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=55)
56. [Lecture 55: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=brrgSY-hhZA&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=56)
57. [Lecture 56: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=iI83JmuR73o&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=57)
58. [Lecture 57: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=np4vX8ADNHI&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=58)
59. [Lecture 58: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=udKNLaK1dqM&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=59)
60. [Lecture 59: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=GOqV7x45eqs&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=60)
61. [Lecture 60: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=rRW0NkJgBbo&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=61)
62. [Lecture 61: Intermediate Code Generation (Contd.)](https://www.youtube.com/watch?v=GCE20jvFv5k&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=62)

</details>


## Books, notes and websites

- Book: Aho, Lam, Sethi, Ullman, *Compilers: Principles, Techniques, and Tools* (the course text)
- ✅ NPTEL *Compiler Design* (Santanu Chattopadhyay, IIT Kharagpur) — onlinecourses.nptel.ac.in/noc22_cs14/preview
- ✅ Prof. Krishna Nandivada's own CS3300 slides — cse.iitm.ac.in/~krishna/cs3300
- *Crafting Interpreters* — craftinginterpreters.com (free)
- Stanford CS143 *Compilers* (online)

## Practice / proof of understanding

Build a compiler for a small language (variables, ints, if/while, functions) that emits assembly or LLVM IR.

## What your IITM course sheet says

### From the PDF: CS3300

**Official description:** The objectives are to teach students a understanding of some of the standard passes in a general purpose  compiler and to provide hands-on experience in implementing a compiler for a subset of a high-level language  such as Java.

**Official syllabus (trimmed):**

> Introduction to language translators and overview of the compilation process.
>  Lexical analysis: specification of tokens, token recognition, conflict resolution
>  Parsing: Overview of CFG, Parse trees and derivations, left recursion, left factoring, top-down parsing, LALR
>  parsing, conflict resolution, dangling-else.
>  Syntax directed translation.
>  Semantic analysis, Type checking, intermediate code generation.
>  Runtime environments: activation records, heap management
>  Code optimization: basic blocks, liveness, register allocation.
>  Advanced topics: Overview of machine dependent and independent optimizations.

**Official textbooks:** 1. Alfred V. Aho, Monica Lam, Ravi Sethi and Jeffrey D. Ullman, "Compilers: Principles, Techniques, and Tools",  second edition, Pearson Education, 2007  2. Modern compiler implementation in Java, Second Edition, Andrew W. Appel, Jens Palsberg, Cambridge  University Press, 2002.

**Official references:** 1. Computer Organization and Design: The Hardware/Software Interface, David Patterson and John Hennessy,  Morgan Kaufmann, 1998  2. The Java programming language, Ken Arnold, James Gosling and David Holmes, Addison-Wesley, 2000.

### From the PDF: CS3310

**Official description:** A language subset will be defined and used during the lab course. The programming exercises here consist of  implementing the basic components of a compiler. The constructs in this subset are found in most programming  languages. They allow programs such as recursive and non-recursive sorting, and matrix multiplication to be  expressed.

**Official syllabus (trimmed):**

> Lexing, Parsing, type checking, intermediate code generation, register allocation, simple optimizations, code
>  generation.

**Official textbooks:** NIL

**Official references:** 1. Modern compiler implementation in Java, Second Edition, Andrew W. Appel, Jens Palsberg, Cambridge  University Press, 2002. 2. A.T. Schreiner and H.G. Friedman, Jr., "Introduction to Compiler construction with  UNIX", Prentice Hall, 1985.
