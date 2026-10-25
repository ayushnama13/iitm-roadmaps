# CS1111 — Problem Solving using Computers

| | |
|---|---|
| Tier | A |
| Phase (order) | 1 |
| Do this first | Nothing |
| Estimated effort | 6-8 weeks, ~6 h/week |
| Unlocks | CS1234, CS2705, CS2222 |

## Roadmap

1. Install gcc, make and gdb on Linux (you already have Linux).
2. Work through the C basics in the order of the course's own weeks: variables, loops, arrays, strings, 2-D arrays, functions, recursion.
3. Solve each course-style problem (weighted marks, encrypt/decrypt a string, tic-tac-toe) yourself before looking at any solution.
4. Finish with pointers and structs, since every later course (OS, compilers, systems) assumes them.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Introduction to C Programming](https://www.youtube.com/playlist?list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN) (60 videos). IIT Madras's own C course (BS Electronic Systems). Same style as your IITM course.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [CS50x 2025 Lectures](https://www.youtube.com/playlist?list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R) (13 videos). CS50x 2025: watch lectures 1-5 (C, arrays, algorithms, memory). Best-produced intro anywhere.
- [Problem solving through Programming In C](https://www.youtube.com/playlist?list=PLJ5C_6qdAvBFzL9su5J-FX8x80BMhkPy1) (61 videos). NPTEL *Problem Solving through Programming in C* (Anupam Basu, IIT Kharagpur).

### ⚡ Short videos for intuition and revision

- [C Programming](https://www.youtube.com/playlist?list=PLBlnK6fEyqRggZZgYpPMUxdY1CYkZtARR) (100+ videos). Neso Academy C: short topic videos, good for revising one concept.
- [Programming in C](https://www.youtube.com/playlist?list=PLdo5W4Nhv31a8UcMN9-35ghv8qyFWD9_S) (100+ videos). Jenny's Lectures C (Indian-English, exam style).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=9wqvDPfjGvo&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=1)–[14](https://www.youtube.com/watch?v=uWRDJjtKsnA&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=14) | How a computer works, number representation, compilation. Install gcc/gdb, write and compile hello-world by hand. |
| 2 | [15](https://www.youtube.com/watch?v=m7d2z6FJ2tk&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=15)–[22](https://www.youtube.com/watch?v=aMdnav33Jns&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=22) | First programs, variables, operators, control flow, loops. Solve 10 small loop problems (patterns, primes, digit sums). |
| 3 | [23](https://www.youtube.com/watch?v=oDQ_DJku0iU&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=23)–[27](https://www.youtube.com/watch?v=D9JiFNNNSMg&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=27) | Functions, runtime stack, recursion, scope. Write factorial/fibonacci/power recursively and iteratively. |
| 4 | [28](https://www.youtube.com/watch?v=XZXJfnwQi30&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=28)–[38](https://www.youtube.com/watch?v=omXPrhA9CQI&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=38) | Pointers, endianness, arrays, pointer arithmetic, strings. Re-implement strlen/strcpy/strcmp yourself. |
| 5 | [39](https://www.youtube.com/watch?v=iC3-KAzHdcA&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=39)–[49](https://www.youtube.com/watch?v=C19W3F-p6YY&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=49) | struct/typedef/union/enum, stack vs heap, malloc/free, 2-D arrays. Build a student-records program with a dynamic array. |
| 6 | [50](https://www.youtube.com/watch?v=irn29Wp1-I4&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=50)–[60](https://www.youtube.com/watch?v=d3rhPqci9zo&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=60) | Files, bit manipulation, macros, multi-file projects. Final: tic-tac-toe + caesar cipher split across .c/.h files with a Makefile. |

<details>
<summary>All lectures in <i>Introduction to C Programming</i> (60 videos)</summary>

1. [1.1 : How a Computer works](https://www.youtube.com/watch?v=9wqvDPfjGvo&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=1)
2. [1.2 : Generalized Memory and Computations](https://www.youtube.com/watch?v=hdtqc7-0l4U&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=2)
3. [1.3 : Split Memory Architecture](https://www.youtube.com/watch?v=RLcZ_YHLw74&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=3)
4. [1.4 : Loops, Conditions & Branches](https://www.youtube.com/watch?v=NMpHjyxbxPE&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=4)
5. [1.5 : Communication between Computer Memory 
and Outside World](https://www.youtube.com/watch?v=CSbL-EQwUM8&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=5)
6. [1.6 : What is Programming?](https://www.youtube.com/watch?v=1rF20ho8XaU&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=6)
7. [1.7 : Introduction to C Language](https://www.youtube.com/watch?v=SpE0zpWZp2w&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=7)
8. [2.1 : Number Representation in a Computer](https://www.youtube.com/watch?v=tDPXMnXrq-c&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=8)
9. [2.2 : Negative Number and Hexadecimal Representation](https://www.youtube.com/watch?v=93WWfR_9zJs&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=9)
10. [2.3 : Floating Point Representation](https://www.youtube.com/watch?v=ubaynZnDMA8&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=10)
11. [2.4 : Character Representation and Encoding](https://www.youtube.com/watch?v=w2MiuRz960E&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=11)
12. [2.5 : Instructions Encoding](https://www.youtube.com/watch?v=dbSztDmtCEQ&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=12)
13. [2.6 : Program Compilation](https://www.youtube.com/watch?v=kXRAgDAvQOk&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=13)
14. [2.7 : Role of Operating System in a Computer](https://www.youtube.com/watch?v=uWRDJjtKsnA&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=14)
15. [3.1 : Writing First C Program](https://www.youtube.com/watch?v=m7d2z6FJ2tk&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=15)
16. [3.2 : Structure of a C program](https://www.youtube.com/watch?v=7sXNH0lZsMU&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=16)
17. [3.3 : Variables in C](https://www.youtube.com/watch?v=2MCz0tuGtpI&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=17)
18. [3.4 : Operators in C](https://www.youtube.com/watch?v=uC-LSJnjt7g&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=18)
19. [4.1 : Structured Programming](https://www.youtube.com/watch?v=7JG8FHBsfvs&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=19)
20. [4.2 : Introduction to Control Flow in C](https://www.youtube.com/watch?v=Le3kXqlKG0o&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=20)
21. [4.3 : Control Flow in C - Examples](https://www.youtube.com/watch?v=FYhBZ2D7_FI&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=21)
22. [4.4 : Loops in C](https://www.youtube.com/watch?v=aMdnav33Jns&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=22)
23. [5.1 : Why Functions?](https://www.youtube.com/watch?v=oDQ_DJku0iU&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=23)
24. [5.2 : Functions in C](https://www.youtube.com/watch?v=tkNOz7RY81w&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=24)
25. [5.3 : What is a Runtime](https://www.youtube.com/watch?v=_F60bmId1RA&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=25)
26. [5.4 : Recursion](https://www.youtube.com/watch?v=zijXoNIQbpY&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=26)
27. [5.5 : Scopes in C](https://www.youtube.com/watch?v=D9JiFNNNSMg&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=27)
28. [6.1 : Introduction to Pointers](https://www.youtube.com/watch?v=XZXJfnwQi30&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=28)
29. [6.2 : Endianness](https://www.youtube.com/watch?v=ZWI4ha4JqTw&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=29)
30. [6.3 : Alignment](https://www.youtube.com/watch?v=95tBsqFTZys&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=30)
31. [6.4 : Pointers & Variables](https://www.youtube.com/watch?v=wqAkkwLRy80&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=31)
32. [6.5 : Compiler Optimizations](https://www.youtube.com/watch?v=SLyTtM7rEDA&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=32)
33. [7.1 : Introduction to Arrays - Part I](https://www.youtube.com/watch?v=QeEHp8Xe8vI&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=33)
34. [7.2 : Introduction to Arrays - Part II](https://www.youtube.com/watch?v=89JZIMiGkE0&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=34)
35. [7.3 : Pointer Arithmetic](https://www.youtube.com/watch?v=gTw8n8VARU0&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=35)
36. [7.4 : Examples of Pointer Arithmetic](https://www.youtube.com/watch?v=VOAnRvqHXuw&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=36)
37. [7.5 : Strings in C](https://www.youtube.com/watch?v=cWRpV52eDw8&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=37)
38. [7.6 : String Functions](https://www.youtube.com/watch?v=omXPrhA9CQI&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=38)
39. [8.1 : Introduction to Struct in C](https://www.youtube.com/watch?v=iC3-KAzHdcA&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=39)
40. [8.2 : Examples of Struct - I](https://www.youtube.com/watch?v=5pUSWyZwk3k&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=40)
41. [8.3 : Examples of Struct - II](https://www.youtube.com/watch?v=ftPM3sMTsio&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=41)
42. [8.4 : Typedef in C](https://www.youtube.com/watch?v=OUqwsQxciFk&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=42)
43. [8.5 : Union in C](https://www.youtube.com/watch?v=ezY1rQph94I&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=43)
44. [8.6: Enum in C](https://www.youtube.com/watch?v=t0PNLfaQOw8&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=44)
45. [9.1 : Heap and Stack Frames](https://www.youtube.com/watch?v=ruHSOURbGiM&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=45)
46. [9.2 : Dynamic Memory Allocation in C](https://www.youtube.com/watch?v=eUSzDTn3dVw&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=46)
47. [9.3 : Examples of Dynamic Memory Allocation - I](https://www.youtube.com/watch?v=tSxaHyukmIU&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=47)
48. [9.4 : Examples of Dynamic Memory Allocation - II](https://www.youtube.com/watch?v=9COFiApM42U&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=48)
49. [9.5 : Multidimensional Arrays in C](https://www.youtube.com/watch?v=C19W3F-p6YY&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=49)
50. [10.1 : Introduction to File Handling in C](https://www.youtube.com/watch?v=irn29Wp1-I4&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=50)
51. [10.2 : File Handling in Text Mode - I](https://www.youtube.com/watch?v=Amxdt5PX0DM&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=51)
52. [10.3 : File Handling in Text Mode - II](https://www.youtube.com/watch?v=Ml9CmSF75Rk&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=52)
53. [10.4 : File Handling in Binary Mode](https://www.youtube.com/watch?v=duMTAG3dj88&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=53)
54. [10.5 : Bit Manipulation](https://www.youtube.com/watch?v=L04QHh3o92A&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=54)
55. [11.1 : Introduction to Macros in C](https://www.youtube.com/watch?v=uzPDh6dfkxs&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=55)
56. [11.2 : Examples of Macros - I](https://www.youtube.com/watch?v=PyNb6l2d1LM&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=56)
57. [11.3 : Examples of Macros - II](https://www.youtube.com/watch?v=8OMrDwJ6o-M&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=57)
58. [11.4 : Include File in C](https://www.youtube.com/watch?v=5bSpysATt10&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=58)
59. [11.5 : Multifile Projects in C](https://www.youtube.com/watch?v=SzJpousu_c0&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=59)
60. [11.6 : Compilation Process of C Programs](https://www.youtube.com/watch?v=d3rhPqci9zo&list=PLUQpHm_JtukKo2fvS9d8hqc7n1dgAyXBN&index=60)

</details>


## Books, notes and websites

- CS50x (Harvard), weeks 1-5 — cs50.harvard.edu/x
- Book: *The C Programming Language* (Kernighan & Ritchie) — also the CS2222 text
- Book: *C Programming: A Modern Approach* (K.N. King) — slower and gentler than K&R
- Beej's Guide to C — beej.us/guide/bgc (free)
- Practice: exercism.org C track, HackerRank C

## Practice / proof of understanding

Write a tic-tac-toe, a caesar cipher and a matrix multiplication program in C with no copy-paste, compile with `-Wall -Wextra`, and run them under `valgrind`.

## What your IITM course sheet says

### From the PDF: CS1111

**Official description:** The course aims to provide exposure to problem-solving through programming. It aims to train the student to the  basic concepts of the C programming language. This course involves a lab component which is designed to give  the student hands-on experience with the concepts.

**Official syllabus (trimmed):**

> The course is structured around 8--10 Problems that will be solved throughout the semester. For each problem the
> necessary language constructs will be introduced.
> Week 1 and 2: Introduction and getting started
> Motivation of the course, fundamentals of computing, historical perspective, writing the first C program. Phases of
> developing and running a program in C.
> Statements, declarations, variables, basic data types (int, char), basic arithmetic and logical operators, if-else and
> loop construct.
> Week 3: Input from user (scanf), output to screen (printf), Arithmetic operators, precedence of operators.
> Sample Problem: Weighted sum of assignment marks for a single student.
> Week 4: Introduction to arrays, use of loops, need for different loop structures like while, do-while
> Sample Problem: Weighted sum of assignment marks for several students.
> Week 5: Introduction to character arrays, manipulating character arrays, motivate need for functions.
> Sample Problem: Encrypt and Decrypt a string.
> Week 6: 2-D arrays, use of loops, user input, input validation.
> Sample Problem: Tic-Tac-Toe program (2 users)
> Week 7: Functions. The prototype declaration, Function definition. Function call - Passing arguments to a function,
> by value, by reference. Scope of variable names.
> Week 8: Recursion, recursive formulas, factorial, Hemachandra (aka Fibonacci) numbers, recursive functions in
> C, sum, max of i

**Official textbooks:** C: How to program, H. M. Deitel, P. J. Deitel, 7th edition, Pearson Education, 2010.

**Official references:** R. G. Dromey, "How to Solve It By Computer", Pearson, 1982  A.R. Bradley, "Programming for Engineers", Springer, 2011  A.G. Ranade, "An Introduction to Programming through C++", McGraw Hill, 2014  Kernighan and Ritchie, "The C Programming Language", (2nd ed.) Prentice-Hall, 1988

### From the PDF: CS1100

**Official description:** The students should be able to write basic C programs comfortably. They should develop the logic building ability  to solve real word problems.

**Official syllabus (trimmed):**

> Module 1 : (Introduction to Computing) - 6 lectures
>  Fundamentals of Computing, Historical perspective, Early computers. Computing machine. Problems,
>  Pseudo-code and flowcharts. Memory, Variables, Values, Instructions, Programs.
>  Module 2 : (Introduction to C) 10 lectures
>  The language of C : Phases of developing a running computer program in C.
>  Data concepts in C :Constants, Variables, Expressions, Operators, and operator precedence in C.
>  Statements : Declarations, Input-Output Statements, Compound statements, Selection Statements.
>  Conditions, Logical operators, Precedences. Repetitive statements, While construct, Do-while Construct, For
>  construct.
>  Data types, size and values. Char, Unsigned and Signed data types. Number systems and representations.
>  Constants, Overflow.
>  Arrays. Strings. Multidimensional arrays and matrices.
>  Module 3 : (Modular Programming and Example Problems) : 10 lecture
>  Functions :The prototype declaration, Function definition.
>  Function call : Passing arguments to a function, by value, by reference. Scope of variable names. Recursive
>  function calls, Tail recursion. Analysing recursion, Tree of recursion, linear recursion.
>  Sorting problem : Selection Sort, Insertion Sort, Comparison between sorting algorithms. Sorting in
>  multidimensional arrays. Sorting in strings.
>  Search problem : Linear search and binary search. Comparison between search pro

**Official textbooks:** 1. Text Book 1: C: How to Program, P. Dietel and H. Dietel, 7th edition, Pearson Education, 2010

**Official references:** 1. Reference Book 1: Computer Programming in C, V. Rajaraman, 2nd edition, PHI Learning, 2008  2. Reference Book 1: How to solve it by Computer?, R. G. Dromey, 2nd edition, Pearson Education, 2008  3. Reference Book 1: The C Programming Language, B. W. Kernighan and D. M. Ritchie, 2nd Edition, Prentice  Hall, 1998
