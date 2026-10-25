# CS2320 — Introduction to Graph Theory

| | |
|---|---|
| Tier | B |
| Phase (order) | 4 |
| Do this first | CS1202 |
| Estimated effort | 10 weeks |
| Unlocks | CS6130, CS6240, CS2800 graph algorithms |

## Roadmap

1. Follow Bondy-Murty chapters in order: basics, trees, connectivity, matchings, planarity, colouring, digraphs.
2. Write every proof out; this course trains proof writing.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Computer - Graph Theory](https://www.youtube.com/playlist?list=PL612CE2AB6F38DF9A) (40 videos). NPTEL *Graph Theory* (nptelhrd).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Graph Theory part-1](https://www.youtube.com/playlist?list=PLGxuz-nmYlQOiIOriTXMEoGoybUC3Jmrn) (9 videos). Sarada Herke *Graph Theory* (part 1 of her series; parts 2-10 are on her channel): proof-focused, matches Bondy-Murty.

### ⚡ Short videos for intuition and revision

- [Graph Theory Playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P) (43 videos). WilliamFiset *Graph Theory*: the algorithmic side, with code.
- [Network Flow playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDj3NzHbbFIC58etjZhiGcG) (11 videos). WilliamFiset *Network Flow*.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1-2 | [1](https://www.youtube.com/watch?v=Gc8emFk-2vc&list=PL612CE2AB6F38DF9A&index=1)–[8](https://www.youtube.com/watch?v=1-NW2fKIyLQ&list=PL612CE2AB6F38DF9A&index=8) | Vertex cover, matchings, Konig, Hall, Tutte, Gallai-Milgram, Dilworth. Implement bipartite matching (Hopcroft-Karp). |
| 3 | [9](https://www.youtube.com/watch?v=mNzg7CoF3r0&list=PL612CE2AB6F38DF9A&index=9)–[12](https://www.youtube.com/watch?v=6SP09ZdV9uQ&list=PL612CE2AB6F38DF9A&index=12) | Connectivity, Menger's theorem, minors. |
| 4-5 | [13](https://www.youtube.com/watch?v=dwR1R-L9HEU&list=PL612CE2AB6F38DF9A&index=13)–[22](https://www.youtube.com/watch?v=OkgIaXhVVnc&list=PL612CE2AB6F38DF9A&index=22) | Vertex/edge colouring, Brooks, Vizing, planarity, Kuratowski, list colouring, chromatic polynomials. |
| 6 | [23](https://www.youtube.com/watch?v=hJfHRbReGt4&list=PL612CE2AB6F38DF9A&index=23)–[30](https://www.youtube.com/watch?v=S1KgOr7sr6g&list=PL612CE2AB6F38DF9A&index=30) | Perfect graphs, chordal/interval graphs, Hamiltonicity. |
| 7 | [31](https://www.youtube.com/watch?v=Y9Ll0Ttfqzs&list=PL612CE2AB6F38DF9A&index=31)–[34](https://www.youtube.com/watch?v=VuMVg1-QPhc&list=PL612CE2AB6F38DF9A&index=34) | Network flows, max-flow min-cut. Implement Edmonds-Karp. |
| 8 | [35](https://www.youtube.com/watch?v=wrskjcV7cW0&list=PL612CE2AB6F38DF9A&index=35)–[40](https://www.youtube.com/watch?v=zZbkLIWoIjc&list=PL612CE2AB6F38DF9A&index=40) | Probabilistic method, random graphs, graph minors. |

<details>
<summary>All lectures in <i>Computer - Graph Theory</i> (40 videos)</summary>

1. [Mod-01 Lec-01 Introduction: Vertex cover and independent set](https://www.youtube.com/watch?v=Gc8emFk-2vc&list=PL612CE2AB6F38DF9A&index=1)
2. [Mod-01 Lec-02 Matchings: Konig's theorem and Hall's theorem](https://www.youtube.com/watch?v=IRbggk6J0TA&list=PL612CE2AB6F38DF9A&index=2)
3. [Mod-01 Lec-03 More on Hall's theorem and some applications](https://www.youtube.com/watch?v=BGCqWa33OD8&list=PL612CE2AB6F38DF9A&index=3)
4. [Mod-01 Lec-04 Tutte's theorem on existence of a perfect matching](https://www.youtube.com/watch?v=PM1FncPlXnM&list=PL612CE2AB6F38DF9A&index=4)
5. [Mod-01 Lec-05 More on Tutte's theorem](https://www.youtube.com/watch?v=_SOZz_aqRP4&list=PL612CE2AB6F38DF9A&index=5)
6. [Mod-01 Lec-06 More on Matchings](https://www.youtube.com/watch?v=7UZGUiG-UCw&list=PL612CE2AB6F38DF9A&index=6)
7. [Mod-01 Lec-07 Dominating set, path cover](https://www.youtube.com/watch?v=xi_f8TfH_qM&list=PL612CE2AB6F38DF9A&index=7)
8. [Mod-01 Lec-08 Gallai -- Millgram theorem, Dilworth's theorem](https://www.youtube.com/watch?v=1-NW2fKIyLQ&list=PL612CE2AB6F38DF9A&index=8)
9. [Mod-02 Lec-09 Connectivity: 2-connected and 3- connected graphs](https://www.youtube.com/watch?v=mNzg7CoF3r0&list=PL612CE2AB6F38DF9A&index=9)
10. [Mod-02 Lec-10 Menger's theorem](https://www.youtube.com/watch?v=4XC1tt80Eg8&list=PL612CE2AB6F38DF9A&index=10)
11. [Mod-02 Lec-11 More on connectivity: k- linkedness](https://www.youtube.com/watch?v=eJmbXo1P6E4&list=PL612CE2AB6F38DF9A&index=11)
12. [Mod-02 Lec-12 Minors, topological minors and more on k- linkedness](https://www.youtube.com/watch?v=6SP09ZdV9uQ&list=PL612CE2AB6F38DF9A&index=12)
13. [Mod-03 Lec-13 Vertex coloring: Brooks theorem](https://www.youtube.com/watch?v=dwR1R-L9HEU&list=PL612CE2AB6F38DF9A&index=13)
14. [Mod-03 Lec-14 More on vertex coloring](https://www.youtube.com/watch?v=EfZs9VDYeiU&list=PL612CE2AB6F38DF9A&index=14)
15. [Mod-03 Lec-15 Edge coloring: Vizing's theorem](https://www.youtube.com/watch?v=Ea3DlCoc0NQ&list=PL612CE2AB6F38DF9A&index=15)
16. [Mod-03 Lec-16 Proof of Vizing's theorem, Introduction to planarity](https://www.youtube.com/watch?v=TBYNkgvnU2s&list=PL612CE2AB6F38DF9A&index=16)
17. [Mod-03 Lec-17  5- coloring planar graphs, Kuratowsky's theorem](https://www.youtube.com/watch?v=kubJIJMOS8I&list=PL612CE2AB6F38DF9A&index=17)
18. [Mod-03 Lec-18 Proof of Kuratowsky's theorem, List coloring](https://www.youtube.com/watch?v=vEmogts6yg0&list=PL612CE2AB6F38DF9A&index=18)
19. [Mod-03 Lec-19 List chromatic index](https://www.youtube.com/watch?v=GAlD0t25LYI&list=PL612CE2AB6F38DF9A&index=19)
20. [Mod-03 Lec-20 Adjacency polynomial of a graph and combinatorial Nullstellensatz](https://www.youtube.com/watch?v=DliIdpEWSTE&list=PL612CE2AB6F38DF9A&index=20)
21. [Mod-03 Lec-21 Chromatic polynomial, k - critical graphs](https://www.youtube.com/watch?v=oFOPRPufisk&list=PL612CE2AB6F38DF9A&index=21)
22. [Mod-03 Lec-22 Gallai-Roy theorem, Acyclic coloring, Hadwiger's conjecture](https://www.youtube.com/watch?v=OkgIaXhVVnc&list=PL612CE2AB6F38DF9A&index=22)
23. [Mod-04 Lec-23 Perfect graphs: Examples](https://www.youtube.com/watch?v=hJfHRbReGt4&list=PL612CE2AB6F38DF9A&index=23)
24. [Mod-04 Lec-24 Interval graphs, chordal graphs](https://www.youtube.com/watch?v=Tg2_YO4CCNc&list=PL612CE2AB6F38DF9A&index=24)
25. [Mod-04 Lec-25 Proof of weak perfect graph theorem (WPGT)](https://www.youtube.com/watch?v=R1zyCMv03tk&list=PL612CE2AB6F38DF9A&index=25)
26. [Mod-04 Lec-26 Second proof of WPGT, Some non-perfect graph classes](https://www.youtube.com/watch?v=OBp8klRZdDw&list=PL612CE2AB6F38DF9A&index=26)
27. [Mod-04 Lec-27 More special classes of graphs](https://www.youtube.com/watch?v=TIeeu9aDifA&list=PL612CE2AB6F38DF9A&index=27)
28. [Mod-04 Lec-28 Boxicity,Sphericity, Hamiltonian circuits](https://www.youtube.com/watch?v=n9FWAVIQ-oM&list=PL612CE2AB6F38DF9A&index=28)
29. [Mod-04 Lec-29 More on Hamiltonicity: Chvatal's theorem](https://www.youtube.com/watch?v=VugQE-SRHa0&list=PL612CE2AB6F38DF9A&index=29)
30. [Mod-04 Lec-30 Chvatal's theorem, toughness, Hamiltonicity and 4-color conjecture](https://www.youtube.com/watch?v=S1KgOr7sr6g&list=PL612CE2AB6F38DF9A&index=30)
31. [Mod-05 Lec-31 Network flows: Max flow mincut theorem](https://www.youtube.com/watch?v=Y9Ll0Ttfqzs&list=PL612CE2AB6F38DF9A&index=31)
32. [Mod-05 Lec-32 More on network flows: Circulations](https://www.youtube.com/watch?v=ghtFBZPRfxg&list=PL612CE2AB6F38DF9A&index=32)
33. [Mod-05 Lec-33 Circulations and tensions](https://www.youtube.com/watch?v=VmnzH3GZiKw&list=PL612CE2AB6F38DF9A&index=33)
34. [Mod-05 Lec-34 More on circulations and tensions, flow number and Tutte's flow conjectures](https://www.youtube.com/watch?v=VuMVg1-QPhc&list=PL612CE2AB6F38DF9A&index=34)
35. [Mod-06 Lec-35 Random graphs and probabilistic method: Preliminaries](https://www.youtube.com/watch?v=wrskjcV7cW0&list=PL612CE2AB6F38DF9A&index=35)
36. [Mod-06 Lec-36 Probabilistic method: Markov's inequality, Ramsey number](https://www.youtube.com/watch?v=BM24sU2Xm7w&list=PL612CE2AB6F38DF9A&index=36)
37. [Mod-06 Lec-37 Probabilistic method: Graphs of high girth and high chromatic number](https://www.youtube.com/watch?v=XRaDIbBAb98&list=PL612CE2AB6F38DF9A&index=37)
38. [Mod-06 Lec-38 Probabilistic method: Second moment method, Lovasz local lemma](https://www.youtube.com/watch?v=of3sPOMJb2I&list=PL612CE2AB6F38DF9A&index=38)
39. [Mod-07 Lec-39 Graph minors and Hadwiger's conjecture](https://www.youtube.com/watch?v=ZD3Ai0BHYAQ&list=PL612CE2AB6F38DF9A&index=39)
40. [Mod-07 Lec-40 More on graph minors, tree decompositions](https://www.youtube.com/watch?v=zZbkLIWoIjc&list=PL612CE2AB6F38DF9A&index=40)

</details>


## Books, notes and websites

- Book: Bondy & Murty, *Graph Theory* (the course text)
- Diestel, *Graph Theory* — diestel-graph-theory.com (free electronic edition)
- ✅ NPTEL *Graph Theory* (L. Sunil Chandran, IISc) — nptel.ac.in/courses/106108054 (nearest full-course match; uses Diestel)
- William Fiset's graph theory videos for algorithmic intuition

## Practice / proof of understanding

Prove Cayley's formula, Hall's theorem and the 5-colour theorem; code a bipartite matching.

## What your IITM course sheet says

### From the PDF: CS2320

**Official description:** The goal of this course is to introduce students to Graph Theory (a topic that finds many applications in various  areas of  computer science and other fields such as electrical engineering). Apart from learning different graph theoretical  concepts, the students will also receive further training in writing rigorous proofs. Several of these proofs are  constructive,  and thus intrinsically related to algorithms.

**Official syllabus (trimmed):**

> I. Basics (6 lectures): graphs and subgraphs; isomorphisms and automorphisms; representations
>  of graphs; degrees and degree sequences; walks, trails, paths and cycles; connected
>  graphs; Eulerian and Hamilton graphs.
>  II. Trees and bipartite graphs (5 lectures): characterizations and properties; spanning trees; Cay-
>  ley's formula.
>  III. Connectivity (7 lectures): edge connectivity, vertex connectivity, ear decompositions, block
>  decomposition, Menger's Theorems.
>  IV. Matchings and Covers (6 lectures): matchings and augmenting paths, Hall's Theorem, Konig's
>  Theorem, Tutte's Theorem (without proof).
>  V. Planarity (5 lectures): Euler's Formula and its consequences, Planar duality, Kuratowski's
>  Theorem (without proof).
>  VI. Colorings (7 lectures): Edge-colorings of bipartite graphs; Vizing's Theorem (without proof); coloring number
>  and
>  degeneracy; chromatic number and clique number; Brooks' Theorem; Four color problem (with brief history);
>  6-color and
>  5-color theorems.
>  VII. Directed graphs (4 lectures): Basics, DAGs, tournaments.

**Official textbooks:** Graph Theory by J. A. Bondy and U. S. R. Murty (Springer 2008)

**Official references:** 1. Graph Theory with Applications by J. A. Bondy and U. S. R. Murty (Macmillan 1976)  2. Introduction to Graph Theory by D. B. West (Prentice Hall 1999)
