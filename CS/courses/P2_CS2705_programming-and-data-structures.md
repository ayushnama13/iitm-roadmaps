# CS2705 — Programming and Data Structures

| | |
|---|---|
| Tier | A |
| Phase (order) | 2 |
| Do this first | CS1111 |
| Estimated effort | 10-12 weeks, ~8 h/week |
| Unlocks | CS2800, CS3500, CS3700, CS3300 |

## Roadmap

1. Asymptotics (big-oh/omega/theta) and how to count steps.
2. Arrays: searching, then sorting (bubble, insertion, merge, counting, radix, bucket).
3. Linked lists, stacks, queues. Implement each from scratch in C.
4. Binary trees, traversals, BST, AVL; hashing and collision handling; binary heaps and priority queues.
5. Graph basics: adjacency list/matrix, BFS, DFS.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Computer Sc - Programming and Data Structure](https://www.youtube.com/playlist?list=PLD9781AC5EBC9FA16) (32 videos). NPTEL *Programming and Data Structure* (nptelhrd): C-based PDS, matches IITM CS2705's C focus.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Programming, Data Structures And Algorithms Using Python](https://www.youtube.com/playlist?list=PLyqSpQzTE6M_Fu6l8irVwXkUyC9Gwqr6_) (45 videos). NPTEL *Programming, Data Structures and Algorithms using Python* (Madhavan Mukund, CMI): the clearest PDS teacher in India.
- [MIT 6.006 Introduction to Algorithms, Spring 2020](https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY) (32 videos). MIT 6.006 *Introduction to Algorithms* (Spring 2020): data structures + algorithms, rigorous.

### ⚡ Short videos for intuition and revision

- [Algorithms](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O) (84 videos). Abdul Bari *Algorithms*: whiteboard explanations, perfect when a topic doesn't click.
- [Data structures playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu) (55 videos). WilliamFiset *Data structures*: animated, with code.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=S47aSEqm_0I&list=PLD9781AC5EBC9FA16&index=1)–[4](https://www.youtube.com/watch?v=YZ6ij0EUmKY&list=PLD9781AC5EBC9FA16&index=4) | C refresher at PDS speed. Re-do pointer exercises from CS1111. |
| 2 | [5](https://www.youtube.com/watch?v=lEvzwEcjQ54&list=PLD9781AC5EBC9FA16&index=5)–[11](https://www.youtube.com/watch?v=KrjWloKRE2U&list=PLD9781AC5EBC9FA16&index=11) | Data structuring case studies, recursion, mergesort/quicksort. Implement both sorts in C. |
| 3 | [12](https://www.youtube.com/watch?v=nc8FBHYrjVw&list=PLD9781AC5EBC9FA16&index=12)–[17](https://www.youtube.com/watch?v=K7VIKlUdo20&list=PLD9781AC5EBC9FA16&index=17) | Strings, arrays/addresses, structures, dynamic allocation, linked lists. Implement a singly + doubly linked list. |
| 4 | [18](https://www.youtube.com/watch?v=6VF2Q0pgUFI&list=PLD9781AC5EBC9FA16&index=18)–[21](https://www.youtube.com/watch?v=4ANuaW8s88s&list=PLD9781AC5EBC9FA16&index=21) | Complexity and asymptotic analysis. Time your sorts on 10^3..10^6 elements and plot. |
| 5 | [22](https://www.youtube.com/watch?v=g_IsQKCTB34&list=PLD9781AC5EBC9FA16&index=22)–[25](https://www.youtube.com/watch?v=rgf5vvhw0Vo&list=PLD9781AC5EBC9FA16&index=25) | Search trees, 2-3 trees. Implement a BST with insert/delete/inorder. |
| 6 | [26](https://www.youtube.com/watch?v=ilEbxao9p50&list=PLD9781AC5EBC9FA16&index=26)–[32](https://www.youtube.com/watch?v=ToYKf-jjW1U&list=PLD9781AC5EBC9FA16&index=32) | Algorithm design + graphs. Implement BFS/DFS on an adjacency list. Then stacks/queues/heaps/hashing from Mukund's Python course (alt playlist). |

<details>
<summary>All lectures in <i>Computer Sc - Programming and Data Structure</i> (32 videos)</summary>

1. [Lec-1 Introduction](https://www.youtube.com/watch?v=S47aSEqm_0I&list=PLD9781AC5EBC9FA16&index=1)
2. [Lec-2 C Programming-I](https://www.youtube.com/watch?v=3QiItmIWmOM&list=PLD9781AC5EBC9FA16&index=2)
3. [Lec-3 C Programming-II](https://www.youtube.com/watch?v=atfNaIY9WbQ&list=PLD9781AC5EBC9FA16&index=3)
4. [Lec-4 C Programming-III](https://www.youtube.com/watch?v=YZ6ij0EUmKY&list=PLD9781AC5EBC9FA16&index=4)
5. [Lec-5 Data Structuring: Case Study-I](https://www.youtube.com/watch?v=lEvzwEcjQ54&list=PLD9781AC5EBC9FA16&index=5)
6. [Lec-6 Data Structuring: Case Study-II](https://www.youtube.com/watch?v=t0ze7NJIh8M&list=PLD9781AC5EBC9FA16&index=6)
7. [Lec-7 Data Structuring: Case Study-III](https://www.youtube.com/watch?v=NU77XIX-wro&list=PLD9781AC5EBC9FA16&index=7)
8. [Lec-8 Problem Decomposition By Recursion-I](https://www.youtube.com/watch?v=AKOWGChr9iA&list=PLD9781AC5EBC9FA16&index=8)
9. [Lec-9 Problem Decomposition By Recursion-II](https://www.youtube.com/watch?v=5D5ierCsAkM&list=PLD9781AC5EBC9FA16&index=9)
10. [Lec-10 Problem Decomposition By Recursion-III](https://www.youtube.com/watch?v=TTQPvDs24Xk&list=PLD9781AC5EBC9FA16&index=10)
11. [Lec-11 Mergesort And Quicksort](https://www.youtube.com/watch?v=KrjWloKRE2U&list=PLD9781AC5EBC9FA16&index=11)
12. [Lec-12 Characters And Strings](https://www.youtube.com/watch?v=nc8FBHYrjVw&list=PLD9781AC5EBC9FA16&index=12)
13. [Lec-13 Arrays: Addresses And Contents](https://www.youtube.com/watch?v=3Xo6P_V-qns&list=PLD9781AC5EBC9FA16&index=13)
14. [Lec-14 Structures-I](https://www.youtube.com/watch?v=cCnYT5TSHSA&list=PLD9781AC5EBC9FA16&index=14)
15. [Lec-15 Structures-II](https://www.youtube.com/watch?v=Y0O52ijs13w&list=PLD9781AC5EBC9FA16&index=15)
16. [Lec-16 Dynamic Allocation Part-I](https://www.youtube.com/watch?v=69OzAUm_Mp0&list=PLD9781AC5EBC9FA16&index=16)
17. [Lec-17 Linked Lists-I](https://www.youtube.com/watch?v=K7VIKlUdo20&list=PLD9781AC5EBC9FA16&index=17)
18. [Lec-18 Complexity(Efficiency) of Algorithms](https://www.youtube.com/watch?v=6VF2Q0pgUFI&list=PLD9781AC5EBC9FA16&index=18)
19. [Lec-19 Asymptotic Growth Functions](https://www.youtube.com/watch?v=9Q_cJ78SQd4&list=PLD9781AC5EBC9FA16&index=19)
20. [Lec-20 Asymptotic Analysis of Algorithms](https://www.youtube.com/watch?v=2wT2xOZJFx8&list=PLD9781AC5EBC9FA16&index=20)
21. [Lec-21 Data Structuring](https://www.youtube.com/watch?v=4ANuaW8s88s&list=PLD9781AC5EBC9FA16&index=21)
22. [Lec-22 Search Trees](https://www.youtube.com/watch?v=g_IsQKCTB34&list=PLD9781AC5EBC9FA16&index=22)
23. [Lec-23 Search Trees-II](https://www.youtube.com/watch?v=5jQGqaAUzOI&list=PLD9781AC5EBC9FA16&index=23)
24. [Lec-24 Search Trees-III](https://www.youtube.com/watch?v=SWUypfRd604&list=PLD9781AC5EBC9FA16&index=24)
25. [Lec-25 2-3 Trees](https://www.youtube.com/watch?v=rgf5vvhw0Vo&list=PLD9781AC5EBC9FA16&index=25)
26. [Lec-26 Algorithm Design-I](https://www.youtube.com/watch?v=ilEbxao9p50&list=PLD9781AC5EBC9FA16&index=26)
27. [Lec-27 Algorithm Design-II](https://www.youtube.com/watch?v=r4jzPQfIuAY&list=PLD9781AC5EBC9FA16&index=27)
28. [Lec-28 Algorithm Design-III](https://www.youtube.com/watch?v=c3OLRBt8TI4&list=PLD9781AC5EBC9FA16&index=28)
29. [Lec-29 Graphs-I](https://www.youtube.com/watch?v=bLzn6RhSb6I&list=PLD9781AC5EBC9FA16&index=29)
30. [Lec-30 Graphs-II](https://www.youtube.com/watch?v=XSnvszUAARk&list=PLD9781AC5EBC9FA16&index=30)
31. [Lec-31 Graphs-III](https://www.youtube.com/watch?v=AOnQvbPbP4g&list=PLD9781AC5EBC9FA16&index=31)
32. [Lec-32 Conclusions](https://www.youtube.com/watch?v=ToYKf-jjW1U&list=PLD9781AC5EBC9FA16&index=32)

</details>


## Books, notes and websites

- ✅ NPTEL *Programming and Data Structures* (N.S. Narayanaswamy, IIT Madras) — nptel.ac.in/courses/106106130/
- ✅ NPTEL *Programming, DSA using Python* (Madhavan Mukund, CMI) — if you prefer Python
- Princeton *Algorithms, Part I* (Sedgewick & Wayne) — algs4.cs.princeton.edu (site was unreachable from my check; try again, or use Coursera)
- Book: *Data Structures and Algorithm Analysis in C++* (Weiss)
- Practice: LeetCode Easy->Medium, 3 problems/week by topic

## Practice / proof of understanding

Implement linked list, stack, queue, BST, AVL, hash table, binary heap and BFS/DFS from scratch, each with a test file.

## Note

Same ground as DA1300/DA5300 in the DA department, taught in C here.

## What your IITM course sheet says

### From the PDF: CS2705

**Official description:** The objective of the course is to teach programming with an emphasis on problem solving and introduce  elementary data structures. The student should be able to analyze computational efficiency.

**Official syllabus (trimmed):**

> Review of Problem Solving using computers, Abstraction, Elementary Data Types, Algorithm design (2 lectures)
>  Complexity and Efficiency via model of computation (notion of time and space), mathematical preliminaries,
>  Elementary asymptotics (big-oh, big-omega, and theta notations). (3 lectures)
>  ADT Array -- searching and sorting on arrays:Linear search, binary search on a sorted array. Bubble sort, Insertion
>  sort, Merge Sort and analysis; Emphasis on the comparison based sorting model. Counting sort, Radix sort,
>  bucket sort. (6 lectures)
>  ADT Linked Lists, Stacks, Queues:List manipulation, insertion, deletion, searching a key, reversal of a list, use of
>  recursion to reverse/search. Doubly linked lists and circular linked lists. (4 lectures)
>  Stacks and queues as dynamic data structures implemented using linked lists. Analyse the ADT operations when
>  implemented using arrays. (3 lectures)
>  ADT Binary Trees:Tree representation, traversal, application of binary trees in Huffman coding. Introduction to
>  expression trees: traversal vs post/pre/infix notation. Recursive traversal and other tree parameters (depth, height,
>  number of nodes etc.) (5 lectures)
>  ADT Dictionary: Binary search trees, balanced binary search trees - AVL Trees. Hashing - collisions, open and
>  closed hashing, properties of good hash functions. (3+3 lectures)
>  ADT Priority queues: Binary heaps with applicati

**Official textbooks:** Data Structures and Algorithm Analysis in C++, by Mark Allen Weiss (Pearson 2007).

**Official references:** Data structures and Algorithms in C++ -- by Adam Drozdek (1994 2001).  How to solve it by Computer -- by R G Dromey (PHI 1982, Paperback 2008).  Fundamentals of Data Structures in C -- by Horowitz, Sahni and Anderson-Freed (Silicon Press 2007).  Data Structure Using C and C++ -- by Y. Langsam, M. J. Augenstein and A. N. Tanenbaum (Pearson Education,  2nd Edition, 2015).
