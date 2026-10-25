# CS6848 — Principles of Programming Languages

| | |
|---|---|
| Tier | B |
| Phase (order) | 6 |
| Do this first | CS2200, CS3300 |
| Estimated effort | 10-12 weeks |
| Unlocks | CS6225, CS6843 |

## Roadmap

1. Lambda calculus, evaluation strategies.
2. Type systems, polymorphism, subtyping.
3. Semantics (operational/denotational); write interpreters.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Computer Sc - Principles of Programming Languages](https://www.youtube.com/playlist?list=PLF7C73918190889CE) (40 videos). NPTEL *Principles of Programming Languages* (nptelhrd).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [MIT 6.001 Structure and Interpretation, 1986](https://www.youtube.com/playlist?list=PLE18841CABEA24090) (40 videos). MIT 6.001 *SICP* (Abelson & Sussman, 1986): the course that teaches what a programming language *is*.
- [Introduction To Haskell Programming](https://www.youtube.com/playlist?list=PLyqSpQzTE6M9whs2Vz_80ons0vRrvGMV5) (29 videos). NPTEL-NOC IITM *Introduction to Haskell Programming* (Madhavan Mukund/S.P. Suresh).
- [SML by Dan Grossman](https://www.youtube.com/playlist?list=PL-eVNDa9MNJczU4ZjhJDT8rIcCa12DyAx) (19 videos). Dan Grossman *Programming Languages* (SML part, re-upload of the Coursera course): types, closures, pattern matching.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=EbNJ05EVXs0&list=PLF7C73918190889CE&index=1)–[5](https://www.youtube.com/watch?v=4N14CdtvzqM&list=PLF7C73918190889CE&index=5) | Syntax, grammars, ambiguity, the PL0 language. |
| 2 | [6](https://www.youtube.com/watch?v=2uJUBQ2Iad8&list=PLF7C73918190889CE&index=6)–[9](https://www.youtube.com/watch?v=v9c8Nk5s0xM&list=PLF7C73918190889CE&index=9) | Semantics, syntactic classes, transition systems (operational semantics). |
| 3 | [10](https://www.youtube.com/watch?v=G3OwDpYTJPE&list=PLF7C73918190889CE&index=10)–[19](https://www.youtube.com/watch?v=AxxOaFJktQM&list=PLF7C73918190889CE&index=19) | Binding, environments, declarations, commands, stores, blocks. Write an interpreter for a small imperative language in Python/OCaml. |
| 4 | [20](https://www.youtube.com/watch?v=Bwo2oD8cu68&list=PLF7C73918190889CE&index=20)–[24](https://www.youtube.com/watch?v=mARX-dNTucY&list=PLF7C73918190889CE&index=24) | Data, structured data, sequences, control, non-determinism. |
| 5 | [25](https://www.youtube.com/watch?v=K9v1XXA5IQ8&list=PLF7C73918190889CE&index=25)–[31](https://www.youtube.com/watch?v=klG-YNuFQAk&list=PLF7C73918190889CE&index=31) | Lambda calculus: data as functions, fixpoints, normal forms. Implement a lambda-calculus evaluator. |
| 6 | [32](https://www.youtube.com/watch?v=lLVLjd3T_Sc&list=PLF7C73918190889CE&index=32)–[35](https://www.youtube.com/watch?v=VqMuQBIjwwE&list=PLF7C73918190889CE&index=35) | Monomorphism, polymorphism, type checking, contexts. Add type checking to your interpreter. |
| 7 | [36](https://www.youtube.com/watch?v=Gm66deL6yu0&list=PLF7C73918190889CE&index=36)–[40](https://www.youtube.com/watch?v=N1bvaR0o-TA&list=PLF7C73918190889CE&index=40) | Abstractions, procedures, parameter passing. Then Dan Grossman's SML lectures (alt) for hands-on functional programming. |

<details>
<summary>All lectures in <i>Computer Sc - Principles of Programming Languages</i> (40 videos)</summary>

1. [Lecture - 1 Introduction to programming languages](https://www.youtube.com/watch?v=EbNJ05EVXs0&list=PLF7C73918190889CE&index=1)
2. [Lecture - 2 Syntax](https://www.youtube.com/watch?v=RKmGoirsLDk&list=PLF7C73918190889CE&index=2)
3. [Lecture - 3 Grammars](https://www.youtube.com/watch?v=a6NJQ3AMcdo&list=PLF7C73918190889CE&index=3)
4. [Lecture - 4 Ambiguity](https://www.youtube.com/watch?v=nVPsqD1aI0Q&list=PLF7C73918190889CE&index=4)
5. [Lecture - 5 PLO:Syntax](https://www.youtube.com/watch?v=4N14CdtvzqM&list=PLF7C73918190889CE&index=5)
6. [Lecture - 6 Semantics](https://www.youtube.com/watch?v=2uJUBQ2Iad8&list=PLF7C73918190889CE&index=6)
7. [Lecture -7 Syntatic Classes](https://www.youtube.com/watch?v=buhZRdH58W0&list=PLF7C73918190889CE&index=7)
8. [Lecture -8 Transition Systems](https://www.youtube.com/watch?v=aahA0tNsko4&list=PLF7C73918190889CE&index=8)
9. [Lecture - 9 PL0 : Expressions](https://www.youtube.com/watch?v=v9c8Nk5s0xM&list=PLF7C73918190889CE&index=9)
10. [Lecture - 10 Binding](https://www.youtube.com/watch?v=G3OwDpYTJPE&list=PLF7C73918190889CE&index=10)
11. [Lecture -11 Environments](https://www.youtube.com/watch?v=WEOk6sFuILA&list=PLF7C73918190889CE&index=11)
12. [Lecture -12 Declarations](https://www.youtube.com/watch?v=_5HPxRnOVCQ&list=PLF7C73918190889CE&index=12)
13. [Lecture -13 Commands](https://www.youtube.com/watch?v=b4qgMrfFlKo&list=PLF7C73918190889CE&index=13)
14. [Lecture -14 Stores](https://www.youtube.com/watch?v=S6aQZsxTL6k&list=PLF7C73918190889CE&index=14)
15. [Lecture -15 Summary](https://www.youtube.com/watch?v=XZ8vB81-tV8&list=PLF7C73918190889CE&index=15)
16. [Lecture -16 Declarations and Commands](https://www.youtube.com/watch?v=WKkKYpRZDvk&list=PLF7C73918190889CE&index=16)
17. [Lecture -17 Blocks](https://www.youtube.com/watch?v=l-pE0baP4j0&list=PLF7C73918190889CE&index=17)
18. [Lecture -18 Qualification](https://www.youtube.com/watch?v=uZlSDHHyzoQ&list=PLF7C73918190889CE&index=18)
19. [Lecture -19 Pragmatics](https://www.youtube.com/watch?v=AxxOaFJktQM&list=PLF7C73918190889CE&index=19)
20. [Lecture -20 Data](https://www.youtube.com/watch?v=Bwo2oD8cu68&list=PLF7C73918190889CE&index=20)
21. [Lecture -21 Structured Data](https://www.youtube.com/watch?v=Axt036CObwA&list=PLF7C73918190889CE&index=21)
22. [Lecture - 22 Sequences](https://www.youtube.com/watch?v=MiCx2sawrL0&list=PLF7C73918190889CE&index=22)
23. [Lecture - 23 Control](https://www.youtube.com/watch?v=cjGEXrogv_g&list=PLF7C73918190889CE&index=23)
24. [Lecture - 24 Non- Determinacy](https://www.youtube.com/watch?v=mARX-dNTucY&list=PLF7C73918190889CE&index=24)
25. [Lecture - 25 Programming Languages](https://www.youtube.com/watch?v=K9v1XXA5IQ8&list=PLF7C73918190889CE&index=25)
26. [Lecture - 26 Programming Languages](https://www.youtube.com/watch?v=P4ggvQXUJuY&list=PLF7C73918190889CE&index=26)
27. [Lecture - 27 Programming Languages](https://www.youtube.com/watch?v=b7-9HFFUBPQ&list=PLF7C73918190889CE&index=27)
28. [Lecture - 28 Data as Functions](https://www.youtube.com/watch?v=Z-5ZKq0yEQI&list=PLF7C73918190889CE&index=28)
29. [Lecture - 29 Data and Fixpoints](https://www.youtube.com/watch?v=13UK1Uolyjo&list=PLF7C73918190889CE&index=29)
30. [Lecture - 30 Normal Forms](https://www.youtube.com/watch?v=QxSOh9PS5eU&list=PLF7C73918190889CE&index=30)
31. [Lecture - 31 Programming Languages](https://www.youtube.com/watch?v=klG-YNuFQAk&list=PLF7C73918190889CE&index=31)
32. [Lecture - 32 Monomorphism](https://www.youtube.com/watch?v=lLVLjd3T_Sc&list=PLF7C73918190889CE&index=32)
33. [Lecture - 33 Polymorphism](https://www.youtube.com/watch?v=A7OwKcXuoLs&list=PLF7C73918190889CE&index=33)
34. [Lecture - 34 Type Checking](https://www.youtube.com/watch?v=O05sURjRBOE&list=PLF7C73918190889CE&index=34)
35. [Lecture - 35 Contexts](https://www.youtube.com/watch?v=VqMuQBIjwwE&list=PLF7C73918190889CE&index=35)
36. [Lecture - 36 Abstracts](https://www.youtube.com/watch?v=Gm66deL6yu0&list=PLF7C73918190889CE&index=36)
37. [Lecture - 37 Procedures](https://www.youtube.com/watch?v=FKA794QD2fI&list=PLF7C73918190889CE&index=37)
38. [Lecture - 38 Meanings](https://www.youtube.com/watch?v=gngL5CXT7YE&list=PLF7C73918190889CE&index=38)
39. [Lecture - 39 Parameters](https://www.youtube.com/watch?v=9IJdUKbkj9A&list=PLF7C73918190889CE&index=39)
40. [Lecture - 40 The Future](https://www.youtube.com/watch?v=N1bvaR0o-TA&list=PLF7C73918190889CE&index=40)

</details>


## Books, notes and websites

- Book: *Programming Languages: Application and Interpretation* (Krishnamurthi, free)
- Book: *Structure and Interpretation of Computer Programs* (SICP, free)
- ✅ NPTEL *Introduction to Haskell Programming* (S.P. Suresh, CMI) — onlinecourses.nptel.ac.in/noc21_cs77/preview
- Dan Grossman's *Programming Languages* (Coursera)

## Practice / proof of understanding

Write interpreters for lambda calculus and a typed mini-language.

## What your IITM course sheet says

### From the PDF: CS6848

_The course sheet has no syllabus text for this course; the plan below is based on the standard content of this subject._
