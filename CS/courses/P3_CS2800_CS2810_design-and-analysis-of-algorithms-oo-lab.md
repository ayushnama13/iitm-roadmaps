# CS2800+CS2810 — Design and Analysis of Algorithms (+ OO lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | CS2705, CS1200, CS1202 |
| Estimated effort | 14 weeks, ~9 h/week |
| Unlocks | Everything from OS/compilers/ML on; CS6100, CS6130 etc. |

## Roadmap

1. Asymptotics and recurrences (master theorem, recursion tree).
2. Divide and conquer (merge sort, fast multiplication, linear-time median).
3. Graph algorithms: BFS/DFS applications, SCC, biconnected components.
4. Greedy: MST, Dijkstra, scheduling, Huffman. Prove correctness each time.
5. Dynamic programming (LCS, knapsack, edit distance, shortest paths).
6. NP-completeness and reductions, approximation ideas.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Design and analysis of algorithms](https://www.youtube.com/playlist?list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P) (56 videos). NPTEL *Design and Analysis of Algorithms* (Madhavan Mukund, CMI).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [MIT 6.046J Design and Analysis of Algorithms, Spring 2015](https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp) (34 videos). MIT 6.046J (Spring 2015): divide & conquer, greedy, DP, network flow, NP-completeness, randomized.
- [Algorithms](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O) (84 videos). Abdul Bari *Algorithms*: the most-watched algorithms course in India.
- [Programming Concepts using Java](https://www.youtube.com/playlist?list=PLZ2ps__7DhBaXTORd_OKXZRXCMh3dGnBZ) (66 videos). For the OO lab (CS2810): IIT Madras BS *Programming Concepts using Java* (Madhavan Mukund).

### ⚡ Short videos for intuition and revision

- [Graph Theory Playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P) (43 videos). WilliamFiset *Graph Theory*: BFS/DFS/Dijkstra/MST/flows with code.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=gY0MwGLq9W8&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=1)–[8](https://www.youtube.com/watch?v=xFRea6xyPgM&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=8) | Motivation, asymptotics, analysing iterative/recursive algorithms. Solve recurrences with the master theorem. |
| 2 | [9](https://www.youtube.com/watch?v=hT1dIbFQoGE&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=9)–[17](https://www.youtube.com/watch?v=owtilSaeNT4&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=17) | Searching and sorting; prove quicksort's expected O(n log n). |
| 3-4 | [18](https://www.youtube.com/watch?v=mi2Fd0W8TaM&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=18)–[27](https://www.youtube.com/watch?v=_4CGMB5j_CQ&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=27) | Graphs: BFS/DFS, topological sort, Dijkstra, Bellman-Ford, all-pairs. Implement each in C++/Java; solve 10 LeetCode graph problems. |
| 5 | [28](https://www.youtube.com/watch?v=rSEc5sIlwSA&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=28)–[35](https://www.youtube.com/watch?v=51pyj1NWEqI&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=35) | MST (Prim/Kruskal), union-find, priority queues, heaps. |
| 6 | [36](https://www.youtube.com/watch?v=938kjf_stNY&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=36)–[42](https://www.youtube.com/watch?v=yhPjST1w0mk&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=42) | Divide & conquer (inversions, closest pair), BSTs, greedy (scheduling, Huffman). |
| 7-8 | [43](https://www.youtube.com/watch?v=EF953Vafi5c&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=43)–[48](https://www.youtube.com/watch?v=xWni5uErQhI&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=48) | Dynamic programming: memoisation, grid paths, LCS, edit distance, matrix chain. Do 15 DP problems. |
| 9 | [49](https://www.youtube.com/watch?v=oktB3FeAkMQ&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=49)–[55](https://www.youtube.com/watch?v=iBX_3wLreWc&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=55) | LP, network flow, reductions, P vs NP. Then MIT 6.046 (alt) for randomized + amortized analysis. |

<details>
<summary>All lectures in <i>Design and analysis of algorithms</i> (56 videos)</summary>

1. [Course Outline](https://www.youtube.com/watch?v=gY0MwGLq9W8&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=1)
2. [Example: Air Travel](https://www.youtube.com/watch?v=55Ivl9pu_0U&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=2)
3. [Example: Xerox shop](https://www.youtube.com/watch?v=9yVJCCNFDUI&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=3)
4. [Example: Document similarity](https://www.youtube.com/watch?v=mYh2MaOusCk&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=4)
5. [Introduction and motivation](https://www.youtube.com/watch?v=JzjkWMTPkdA&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=5)
6. [Input size, worst case, average case](https://www.youtube.com/watch?v=Q0pWMzPAdYM&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=6)
7. [Quantifying efficiency: O( ), Omega( ), Theta( )](https://www.youtube.com/watch?v=msj_2TEzRP0&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=7)
8. [Examples: Analysis of iterative and recursive algorithms](https://www.youtube.com/watch?v=xFRea6xyPgM&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=8)
9. [Arrays and lists](https://www.youtube.com/watch?v=hT1dIbFQoGE&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=9)
10. [Searching in an array](https://www.youtube.com/watch?v=3XCGzrCxVkw&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=10)
11. [Selection Sort](https://www.youtube.com/watch?v=1nAgMQSc-4Q&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=11)
12. [Insertion sort](https://www.youtube.com/watch?v=_EV6xAXf5FA&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=12)
13. [Merge sort](https://www.youtube.com/watch?v=2UP-XMgOyNw&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=13)
14. [Merge sort - analysis](https://www.youtube.com/watch?v=Pzs15qv-xTk&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=14)
15. [Quicksort](https://www.youtube.com/watch?v=RajaRfMJF4I&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=15)
16. [Quicksort - analysis](https://www.youtube.com/watch?v=N8lzcGiQo9A&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=16)
17. [Sorting - Concluding remarks](https://www.youtube.com/watch?v=owtilSaeNT4&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=17)
18. [Introduction to graphs](https://www.youtube.com/watch?v=mi2Fd0W8TaM&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=18)
19. [Representing graphs](https://www.youtube.com/watch?v=Y-6IGzmlG4Y&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=19)
20. [Breadth first search (BFS)](https://www.youtube.com/watch?v=ahXszIXr1NE&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=20)
21. [Depth first search (DFS)](https://www.youtube.com/watch?v=0n4UtSm5HtE&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=21)
22. [Applications of BFS and DFS](https://www.youtube.com/watch?v=Ia6AgDENsf0&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=22)
23. [Directed acylic graphs: topological sort](https://www.youtube.com/watch?v=_9a95v2shgQ&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=23)
24. [Directed acylic graphs: longest paths](https://www.youtube.com/watch?v=jpIeCsX4oNo&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=24)
25. [Dijkstras algorithm: analysis](https://www.youtube.com/watch?v=nieg8XQQ7i0&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=25)
26. [Negative edge weights: Bellman-Ford algorithm](https://www.youtube.com/watch?v=YbbGemzQ5ok&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=26)
27. [All pairs shortest paths](https://www.youtube.com/watch?v=_4CGMB5j_CQ&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=27)
28. [Minimum Cost Spanning Trees](https://www.youtube.com/watch?v=rSEc5sIlwSA&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=28)
29. [Prims Algorithm](https://www.youtube.com/watch?v=-M6IzZMpm1Y&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=29)
30. [Kruskals algorithm](https://www.youtube.com/watch?v=b2-vAkasvD0&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=30)
31. [Union-Find using arrays](https://www.youtube.com/watch?v=6i0ZmTDqsXA&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=31)
32. [Union-Find using pointers](https://www.youtube.com/watch?v=5wA56Z0ngLU&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=32)
33. [Priority queues](https://www.youtube.com/watch?v=ImSRt7LxQnY&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=33)
34. [Heaps](https://www.youtube.com/watch?v=uQ3mBbvPToQ&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=34)
35. [Heaps: Updating values, sorting](https://www.youtube.com/watch?v=51pyj1NWEqI&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=35)
36. [Counting inversions](https://www.youtube.com/watch?v=938kjf_stNY&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=36)
37. [Closest pair of points](https://www.youtube.com/watch?v=6UBDkbVhJck&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=37)
38. [Binary Search Trees](https://www.youtube.com/watch?v=esvCwpyPh90&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=38)
39. [Balanced search trees](https://www.youtube.com/watch?v=Awkkz8UytZE&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=39)
40. [Interval scheduling](https://www.youtube.com/watch?v=Oe9bxU8lbxE&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=40)
41. [Scheduling with deadlines: minimizing lateness](https://www.youtube.com/watch?v=z2OXv1qaSFE&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=41)
42. [Huffman codes](https://www.youtube.com/watch?v=yhPjST1w0mk&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=42)
43. [Introduction to dynamic programming](https://www.youtube.com/watch?v=EF953Vafi5c&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=43)
44. [Memoization](https://www.youtube.com/watch?v=IxD1vRA0B4s&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=44)
45. [Grid paths](https://www.youtube.com/watch?v=yTKJcpitONQ&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=45)
46. [Common subwords and subsequences](https://www.youtube.com/watch?v=xdA41xLxwuM&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=46)
47. [Edit distance](https://www.youtube.com/watch?v=3KMX8tBToLA&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=47)
48. [Matrix multiplication](https://www.youtube.com/watch?v=xWni5uErQhI&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=48)
49. [Linear Programming](https://www.youtube.com/watch?v=oktB3FeAkMQ&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=49)
50. [LP modelling: Production Planning](https://www.youtube.com/watch?v=mWNBH1WvxtY&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=50)
51. [LP modelling: Bandwidth allocation](https://www.youtube.com/watch?v=BpRhXZC5tfU&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=51)
52. [Network Flows](https://www.youtube.com/watch?v=yxHDqjT6OQw&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=52)
53. [Reductions](https://www.youtube.com/watch?v=AhIzCq83c7Q&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=53)
54. [Checking Algorithms](https://www.youtube.com/watch?v=btytfRFySg0&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=54)
55. [P and NP](https://www.youtube.com/watch?v=iBX_3wLreWc&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=55)
56. [Single source shortest paths: Dijkstras algorithm](https://www.youtube.com/watch?v=OGsPQy-lM1w&list=PLyqSpQzTE6M9DKhN7z2fOpKTJWu-639_P&index=56)

</details>


## Books, notes and websites

- ✅ NPTEL *Design and Analysis of Algorithms* (Madhavan Mukund, CMI) — e.g. onlinecourses-archive.nptel.ac.in/noc19_cs11/
- MIT 6.006 *Introduction to Algorithms* and 6.046J *Design and Analysis of Algorithms* (OCW)
- Jeff Erickson, *Algorithms* — jeffe.cs.illinois.edu/teaching/algorithms (free)
- Book: CLRS; Kleinberg & Tardos; Dasgupta-Papadimitriou-Vazirani
- Roughgarden *Algorithms Specialization* (Stanford, Coursera audit)

## Practice / proof of understanding

Solve 60 problems: 15 greedy, 20 DP, 15 graph, 10 divide-and-conquer. Write a correctness proof for at least 10. Implement the lab list (balanced trees, hashing, DP, matrix ops) in C++.

## Note

This is the most important course on the CS side. Do not rush it.

## What your IITM course sheet says

### From the PDF: CS2800

**Official description:** The objective of the course is to teach techniques for effective problem solving incomputing. The use of different  paradigms of problem solving will be used to illustrate cleverand efficient ways to solve a given problem. In each  case emphasis will be placed onrigorously proving correctness of the algorithm. In addition, the analysis of the  algorithm will beused to show the efficiency of the algorithm over the naive techniques.

**Official syllabus (trimmed):**

> Introduction: Problem solving -- adding 2 n-bit numbers, multiplication as repeatedaddition.Running time analysis
>  -- recall of asymptotic notation, big-oh, theta, big-omega, andintroduce little-oh and little-omega. Worst case and
>  average case complexity (3 lectures+ 1 tutorial).Basic paradigms with illustrative examples -- incremental design
>  (e.g., incrementalsorting, interpolating polynomials), decremental design (e.g., GCD with discussion oninput size,
>  factorial), and pruning (e.g., order statistics).2. Divide and Conquer: Integer multiplication revisited with an efficient
>  algorithm thatmotivates and leads into recurrences. Solving recurrences using recurrence trees,repeated
>  substitution, statement of master theorem. Brief recall of merge sort and itsrecurrence. Median in worst case linear
>  time. (7+2)3. Application of Graph Traversal Techniques: Recall representation of graphs, BFS (asa method for
>  SSSP on unweighted graphs), DFS, connected components, topologicalsorting of DAGs, biconnected
>  components, and strongly connected components indirected graphs. (4+1)4. Greedy Algorithms: Greedy choice,
>  optimal substructure property, minimum spanningtrees -- Prims and Kruskals, Dijkstra’s shortest path using arrays
>  and heaps, fractionalknapsack, and Huffman coding (use of priority queue). (9+3)5. Dynamic Programming:
>  Integral knapsack (contrasted with the fractional varia

**Official textbooks:** 1. Introduction to Algorithms, by Cormen, Leiserson, Rivest, and Stein, MIT Press, Third Edition, 2009.

**Official references:** 1. Algorithms, by Dasgupta, Papadimitrou and Vazirani, McGraw-Hill Education, 2006.2. Computer Algorithms, by  Horowitz, Sahni, and Rajasekaran, Silicon Press, 2007.3. Algorithm Design, by Kleinberg and Tardos, Pearson,  2005.4. Algorithm Design, by Goodrich and Tamassia, Wiley, 2001.

### From the PDF: CS2810

**Official description:** teaching the fundamentals of object-oriented concepts and programming and implementation.

**Official syllabus (trimmed):**

> 1. Object Oriented Programming -- Objects, Operator Overloading, Function and Object Polymorphism,
>  Inheritance, Abstraction, Function Pointers, File I/O.2. Data Structures and Algorithms Implementation and
>  Analysis based on topics covered in CS2800. The following list is not exhaustive --Stacks, Queues, Searching and
>  Sorting (Internal and External), Graph Algorithms, Trees (including Balanced and In-Memory/In-Disk Storage),
>  Hash Tables, Dynamic Programming, Matrix Operations (including Multiplication, Transpose, Inverse, Gaussian
>  Elimination).

**Official textbooks:** Same as CS2800

**Official references:** 1. Data Structures and Algorithm Analysis in C++ Hardcover, by Mark A. Weiss, Jun 2013, Publisher: PHI; 4  edition, ISBN-10: 013284737X ISBN-13: 978-0132847377.2. Algorithms in C++ : Fundamentals, Data Structures,  Sorting, Searching, Parts 1-4, 3rd Edition (Paperback), Pearson India, ISBN-10 8131713059, 2009, ISBN-13  9788131713051.
