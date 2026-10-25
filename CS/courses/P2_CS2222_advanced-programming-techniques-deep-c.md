# CS2222 — Advanced Programming Techniques (deep C)

| | |
|---|---|
| Tier | B |
| Phase (order) | 2 |
| Do this first | CS1111, CS1234 |
| Estimated effort | 6-8 weeks |
| Unlocks | CS2300 labs, CS3500, CS3300 |

## Roadmap

1. Pointers and pointer arithmetic, dynamic memory, debugging with gdb/valgrind.
2. Bit manipulation, variadic functions, command-line args, file and directory I/O.
3. Macros, separate compilation, makefiles; inline assembly basics.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [CS50x 2025 Lectures](https://www.youtube.com/playlist?list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R) (13 videos). CS50x 2025: lecture 4 (Memory) and 5 (Data Structures) are the best pointer/malloc intro.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Beginner C Videos](https://www.youtube.com/playlist?list=PL9IEJIKnBJjG5H0ylFAzpzs9gSmW_eICB) (46 videos). Jacob Sorber *Beginner C Videos*: pointers, memory, make, the details.
- [Debugging C Programs](https://www.youtube.com/playlist?list=PL9IEJIKnBJjHGWPN_S9NS_Ky1-tC8ZrUI) (38 videos). Jacob Sorber *Debugging C Programs*: gdb, valgrind, sanitizers.
- [Unix Processes in C](https://www.youtube.com/playlist?list=PLfqABt5AS4FkW5mOn2Tn9ZZLLDwA3kZUY) (27 videos). CodeVault *Unix Processes in C*: fork/exec/pipes (needed later in OS).

### ⚡ Short videos for intuition and revision

- [Unix Threads in C](https://www.youtube.com/playlist?list=PLfqABt5AS4FmuQf70psXrsMLEDQXNkLq2) (29 videos). CodeVault *Unix Threads in C*.
- [C Programming and Assembly Language](https://www.youtube.com/playlist?list=PLyqSpQzTE6M8O9Oy9t-yhiAUXOi-rmTp_) (32 videos). NPTEL-NOC IITM *C Programming and Assembly Language*: how C maps to assembly.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | CS50 lec 4-5 | Memory, pointers, malloc, linked lists, hash tables. Do CS50 problem sets *Recover* and *Speller*. |
| 2-3 | Jacob Sorber Beginner C (alt) | Pointers to pointers, function pointers, const, bit fields, variadic functions, the preprocessor. |
| 4 | Jacob Sorber Debugging C (alt) | gdb, valgrind, AddressSanitizer, core dumps. Fix 5 memory bugs on purpose. |
| 5-6 | CodeVault Unix Processes + Threads (alt) | fork/exec/wait/pipe, pthreads, mutexes. Write a mini shell supporting pipes. |
| 7 | K&R ch. 5-8 | Write your own malloc (free-list allocator) and a generic hash map with void*. |

<details>
<summary>All lectures in <i>CS50x 2025 Lectures</i> (13 videos)</summary>

1. [CS50x 2025 - Introduction](https://www.youtube.com/watch?v=h6lqxDwUmJQ&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=1)
2. [CS50x 2025 - Lecture 0 - Scratch](https://www.youtube.com/watch?v=2WtPyqwTLKM&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=2)
3. [CS50x 2025 - Lecture 1 - C](https://www.youtube.com/watch?v=89cbCbWrM4U&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=3)
4. [CS50x 2025 - Lecture 2 - Arrays](https://www.youtube.com/watch?v=Y8qnryVy5sQ&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=4)
5. [CS50x 2025 - Lecture 3 - Algorithms](https://www.youtube.com/watch?v=iCx3zwK8Ms8&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=5)
6. [CS50x 2025 - Lecture 4 - Memory](https://www.youtube.com/watch?v=kcRdFGbzR1I&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=6)
7. [CS50x 2025 - Lecture 5 - Data Structures](https://www.youtube.com/watch?v=aV8LlSmd1E8&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=7)
8. [CS50x 2025 - Lecture 6 - Python](https://www.youtube.com/watch?v=0eNc5lJfZFM&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=8)
9. [CS50x 2025 - Artificial Intelligence](https://www.youtube.com/watch?v=1HuD2ryeOLg&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=9)
10. [CS50x 2025 - Lecture 7 - SQL](https://www.youtube.com/watch?v=ZA25WHO62ZA&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=10)
11. [CS50x 2025 - Lecture 8 - HTML, CSS, JavaScript](https://www.youtube.com/watch?v=xiWUL3M9D8c&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=11)
12. [CS50x 2025 - Lecture 9 - Flask](https://www.youtube.com/watch?v=1r-dFbPQ7Z8&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=12)
13. [CS50x 2025 - Lecture 10 - The End](https://www.youtube.com/watch?v=WGEy-Bu5Hos&list=PLhQjrBD2T383q7Vn8QnTsVgSvyLpsqL_R&index=13)

</details>


## Books, notes and websites

- K&R, *The C Programming Language* (the course's own text)
- Kernighan & Pike, *The Practice of Programming*
- *Modern C* (Jens Gustedt, free PDF)
- Beej's Guide to C

## Practice / proof of understanding

Write your own `malloc` wrapper with leak tracking, a bit-vector library, and a tiny `grep` clone.

## Note

Optional, but excellent preparation for OS and compilers.

## What your IITM course sheet says

### From the PDF: CS2222

**Official description:** - To be comprehensive in an imperative programming language  - To learn more and deeper problem solving  - To improve coding confidence

**Official syllabus (trimmed):**

> Overview of an Imperative Programming Language [1 week]
>  Topics from the Programming Language such as [8 weeks]
>  - pointers and pointer arithmetic, memory management, debugging
>  - byte and bit manipulations, bit fields, string tokenization
>  - variable number of arguments, command-line arguments, environment variables
>  - file / directory operations, records, profiling, time utilities
>  - macros, user-defined header files, separate compilation, makefiles
>  - writing assembly code, exception handling, assertions
>  - optimizing code for time and memory usage
>  Library Usage and Problem Solving related to Various Domains such as [4 weeks]
>  - numerical computing, crypto functions (math library, complex numbers, GNU scientific library)
>  - string manipulations (string library)
>  - geometry
>  - matrix operations, linear algebra (random numbers)
>  - logical thinking, puzzles
>  Developing an Application [1--2 weeks]
>  - putting the above learning together.

**Official textbooks:** Kernighan and Ritchie, "The C Programming Language", (2nd ed.) Prentice-Hall, 1988

**Official references:** C: How to program, H. M. Deitel, P. J. Deitel, 7th edition, Pearson Education, 2010.  The Practice of Programming, Brian Kernighan and Robert Pike, Addison-Wesley Inc., 1999.
