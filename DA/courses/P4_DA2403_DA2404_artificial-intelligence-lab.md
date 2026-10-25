# DA2403+DA2404 — Artificial Intelligence (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 4 |
| Do this first | DA2400, DA2303 |
| Estimated effort | 12 weeks |
| Unlocks | DA7400, reinforcement learning |

## Roadmap

1. Agents; search (BFS, A*), CSP, games.
2. Probabilistic models: HMMs, graphical models.
3. Planning and an intro to RL.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Artificial Intelligence Search Methods For Problem Solving](https://www.youtube.com/playlist?list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc) (95 videos). NPTEL *AI: Search Methods for Problem Solving* (Deepak Khemani, IIT Madras).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [[CS188 SP24] Lectures](https://www.youtube.com/playlist?list=PLp8QV47qJEg67UTShQ4er4RYQ3rOeDKxv) (27 videos). Berkeley CS188 *Intro to AI* (Spring 2024, official course channel): search, CSPs, games, MDPs, Bayes nets. Do the Pac-Man projects.
- [MIT 6.034 Artificial Intelligence, Fall 2010](https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi) (30 videos). MIT 6.034 *Artificial Intelligence* (Patrick Winston, Fall 2010, official OCW).
- [CS50's Introduction to Artificial Intelligence with Python 2023](https://www.youtube.com/playlist?list=PLhQjrBD2T381PopUTYtMSstgk-hsTGkVm) (8 videos). Harvard CS50 AI (official): 7 lectures with Python projects, good for the lab (DA2404).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=NCq26BvEYIg&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=1)–[16](https://www.youtube.com/watch?v=QveMYBQGsT8&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=16) | Philosophy and history of AI (watch at 1.5x). |
| 2 | [17](https://www.youtube.com/watch?v=TVUkCyJygPE&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=17)–[22](https://www.youtube.com/watch?v=C1lxCf3XhCk&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=22) | State space search, DFS/BFS, iterative deepening. Implement them for the 8-puzzle. |
| 3 | [23](https://www.youtube.com/watch?v=2-4w7LZ-l_Q&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=23)–[33](https://www.youtube.com/watch?v=ZR2t5qFmxv8&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=33) | Heuristic search, local search, TSP, simulated annealing, genetic algorithms, ant colony. Solve a TSP instance with hill climbing and a GA. |
| 4-5 | [34](https://www.youtube.com/watch?v=ccxQZyVOn-w&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=34)–[49](https://www.youtube.com/watch?v=OhBpJEmmflQ&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=49) | Optimal paths: branch & bound, A*, admissibility, monotone condition, memory-bounded variants. Implement A* on a grid; compare heuristics. |
| 6 | [50](https://www.youtube.com/watch?v=a0WNihfI7as&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=50)–[57](https://www.youtube.com/watch?v=Tui1bAuDJ9w&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=57) | Game playing: minimax, alpha-beta, SSS*. Write a tic-tac-toe / Connect-4 AI with alpha-beta. |
| 7-8 | [58](https://www.youtube.com/watch?v=jjxywg1-dw0&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=58)–[71](https://www.youtube.com/watch?v=JdxyVLKsyPU&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=71) | Planning: STRIPS, goal stack, plan-space, Graphplan, AO*. Write a blocks-world planner. |
| 9 | [72](https://www.youtube.com/watch?v=e5R-CnyKB8I&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=72)–[79](https://www.youtube.com/watch?v=jT908a0eD50&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=79) | Rule-based systems, Rete algorithm. |
| 10 | [80](https://www.youtube.com/watch?v=0f-HqOc0FYI&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=80)–[87](https://www.youtube.com/watch?v=-vDk_IIl81Q&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=87) | Logic: inference, forward/backward chaining, FOL. |
| 11 | [88](https://www.youtube.com/watch?v=fEImACP5nmM&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=88)–[95](https://www.youtube.com/watch?v=vWBf5yphFBY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=95) | Constraint satisfaction, arc consistency, lookahead. Write a sudoku solver with AC-3 + backtracking. |
| 12 | Berkeley CS188 (alt) | Probabilistic half (Bayes nets, MDPs, RL) that this playlist does not cover. Do the Pac-Man projects. |

<details>
<summary>All lectures in <i>Artificial Intelligence Search Methods For Problem Solving</i> (95 videos)</summary>

1. [Prologue](https://www.youtube.com/watch?v=NCq26BvEYIg&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=1)
2. [The Winograd Schema Challenge](https://www.youtube.com/watch?v=OA5c7qMKz3M&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=2)
3. [Introduction (2013 version)](https://www.youtube.com/watch?v=9LbmroSa2cE&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=3)
4. [Can Machines Think?](https://www.youtube.com/watch?v=BrjxjKnqasg&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=4)
5. [The Turing Test](https://www.youtube.com/watch?v=2XXVjVqU2Nk&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=5)
6. [Language and Thought](https://www.youtube.com/watch?v=LTkfWMUTZFg&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=6)
7. [The Willing Suspension of Disbelief](https://www.youtube.com/watch?v=7UDLqICZg2c&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=7)
8. [Machines with Wheels and Gears](https://www.youtube.com/watch?v=zSNiDYc9gCg&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=8)
9. [The Notion of Mind in Philosophy](https://www.youtube.com/watch?v=NYVAoYwxO5c&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=9)
10. [Reasoning = Computation](https://www.youtube.com/watch?v=aDPu39j-mBY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=10)
11. [Concepts and Categories](https://www.youtube.com/watch?v=2k9VLLWMGos&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=11)
12. [How did AI get its name?](https://www.youtube.com/watch?v=tJVVNzn89pM&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=12)
13. [The Chess Saga](https://www.youtube.com/watch?v=CivOz_IABLc&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=13)
14. [A Brief History of AI](https://www.youtube.com/watch?v=VTCMp_HtEaU&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=14)
15. [The Worlds in our Minds](https://www.youtube.com/watch?v=pv40kt9x0zk&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=15)
16. [Epiphemona in Computers](https://www.youtube.com/watch?v=QveMYBQGsT8&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=16)
17. [State Space Search](https://www.youtube.com/watch?v=TVUkCyJygPE&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=17)
18. [Domain Independent Algorithms](https://www.youtube.com/watch?v=gP8o2mY9ffY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=18)
19. [Deterministic Search](https://www.youtube.com/watch?v=VUXpn2dp8-o&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=19)
20. [DFS and BFS](https://www.youtube.com/watch?v=QqdN7LH3jeA&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=20)
21. [Comparing DFS and BFS](https://www.youtube.com/watch?v=PV0dMkYwr3Y&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=21)
22. [Depth First Iterative Deepening](https://www.youtube.com/watch?v=C1lxCf3XhCk&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=22)
23. [Heuristic Search](https://www.youtube.com/watch?v=2-4w7LZ-l_Q&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=23)
24. [Heuristic Functions and the Search Landscape](https://www.youtube.com/watch?v=Rahq1F-n650&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=24)
25. [Solution Space Search](https://www.youtube.com/watch?v=int1tjmwjwY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=25)
26. [The Traveling Salesman Problem](https://www.youtube.com/watch?v=g29Mkpam4EQ&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=26)
27. [Escaping Local Optima](https://www.youtube.com/watch?v=6977W5xy9B8&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=27)
28. [Stochastic Local Search](https://www.youtube.com/watch?v=_w0r-YsMIjs&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=28)
29. [Genetic Algorithms: Survival of the Fittest](https://www.youtube.com/watch?v=uvp0otoY7Kc&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=29)
30. [Genetic Algorithms and SAT](https://www.youtube.com/watch?v=nUYRHVh8TdU&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=30)
31. [Genetic Algorithms for the TSP](https://www.youtube.com/watch?v=3lc_Fcga5z8&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=31)
32. [Emergent Systems](https://www.youtube.com/watch?v=YqXNY9Vs7Vs&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=32)
33. [Ant Colony Optimization](https://www.youtube.com/watch?v=ZR2t5qFmxv8&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=33)
34. [Finding Optimal Paths](https://www.youtube.com/watch?v=ccxQZyVOn-w&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=34)
35. [Branch & Bound](https://www.youtube.com/watch?v=ZF8xhXE0P20&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=35)
36. [Algorithm A*](https://www.youtube.com/watch?v=JY1IHmFJyfI&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=36)
37. [A*: An illustrated example](https://www.youtube.com/watch?v=G8CQHguhqr4&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=37)
38. [Is A* Admissible?](https://www.youtube.com/watch?v=EfvwZZmSF48&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=38)
39. [Admissibility of A*](https://www.youtube.com/watch?v=Fk9xZc2msoI&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=39)
40. [Higher, Faster ...](https://www.youtube.com/watch?v=XvAfVgmx-i4&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=40)
41. [B&B - A* -  wA* - Best First](https://www.youtube.com/watch?v=3aaRyk7ls3k&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=41)
42. [A*: Leaner Admissible Variations](https://www.youtube.com/watch?v=qgy-PvoFFFA&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=42)
43. [The Monotone Condition](https://www.youtube.com/watch?v=bauEiTvxo-A&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=43)
44. [DNA Sequence Alignment](https://www.youtube.com/watch?v=vzOoLMCyG4w&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=44)
45. [Divide & Conquer Frontier Search.](https://www.youtube.com/watch?v=s1SfTCLyGKA&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=45)
46. [Smart Memory Graph Search](https://www.youtube.com/watch?v=oGbkzHoz47M&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=46)
47. [Variations on A*: The story so far](https://www.youtube.com/watch?v=GNQ0nDSshuY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=47)
48. [Breadth First Heuristic Search](https://www.youtube.com/watch?v=8JhPT5ShEcY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=48)
49. [Beam Stack Search](https://www.youtube.com/watch?v=OhBpJEmmflQ&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=49)
50. [Game Theory](https://www.youtube.com/watch?v=a0WNihfI7as&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=50)
51. [Popular Recreational Games](https://www.youtube.com/watch?v=TFt2r81fe1c&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=51)
52. [Board Games and Game Trees](https://www.youtube.com/watch?v=SzziJsmVhzY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=52)
53. [The Evaluation Function in Board Games](https://www.youtube.com/watch?v=55TAcdQ4uEc&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=53)
54. [Algorithm Minimax and Alpha-Beta Pruning](https://www.youtube.com/watch?v=Vus2I9NVNzc&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=54)
55. [A Cluster of Strategies](https://www.youtube.com/watch?v=2lLJ9DSrGgw&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=55)
56. [SSS*: A Best First Algorithm](https://www.youtube.com/watch?v=Am9Ts9IWTOE&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=56)
57. [SSS*: A Detailed Example](https://www.youtube.com/watch?v=Tui1bAuDJ9w&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=57)
58. [Automated Domain Independent Planning](https://www.youtube.com/watch?v=jjxywg1-dw0&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=58)
59. [The Blocks World Domain](https://www.youtube.com/watch?v=XkEXV5ztwy0&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=59)
60. [State Space Planning: Forward and Backward](https://www.youtube.com/watch?v=Mjr_V9KVo74&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=60)
61. [Goal Stack Planning (GSP)](https://www.youtube.com/watch?v=w5vm3TxRpaQ&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=61)
62. [GSP: A Detailed Example](https://www.youtube.com/watch?v=slFpEvL4W2U&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=62)
63. [Plan Space Planning (PSP)](https://www.youtube.com/watch?v=jfi6hDO7KUY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=63)
64. [PSP: A Tiny Example](https://www.youtube.com/watch?v=AEXZXB5-jUU&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=64)
65. [Multi-Armed Robots](https://www.youtube.com/watch?v=jQvHXVHRn-Q&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=65)
66. [Means-Ends Analysis](https://www.youtube.com/watch?v=cVjCr8olwdk&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=66)
67. [The Planning Graph](https://www.youtube.com/watch?v=xANSo6_vsNo&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=67)
68. [Algorithm Graphplan](https://www.youtube.com/watch?v=Tvtms7L6YcA&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=68)
69. [Problem Decomposition.](https://www.youtube.com/watch?v=IhqzAsXccuw&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=69)
70. [Algorithm AO*](https://www.youtube.com/watch?v=DT0Lmv8Ypjw&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=70)
71. [AO*: An Illustration](https://www.youtube.com/watch?v=JdxyVLKsyPU&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=71)
72. [Rule Based Expert Systems](https://www.youtube.com/watch?v=e5R-CnyKB8I&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=72)
73. [The Inference Engine](https://www.youtube.com/watch?v=K1vqFx_5yic&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=73)
74. [The OPS5 Language](https://www.youtube.com/watch?v=UiawzptqU5Q&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=74)
75. [Conflict Resolution](https://www.youtube.com/watch?v=PpDngLCiTHo&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=75)
76. [Business Rule Management Systems](https://www.youtube.com/watch?v=V4nl_v85sNA&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=76)
77. [The Rete Net](https://www.youtube.com/watch?v=dv0YntxGdxk&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=77)
78. [Rete Algorithm: Optimizing the Match](https://www.youtube.com/watch?v=lCzEPLxt7f4&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=78)
79. [Rete Algorithm: Conflict Resolution](https://www.youtube.com/watch?v=jT908a0eD50&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=79)
80. [Reasoning in Logic](https://www.youtube.com/watch?v=0f-HqOc0FYI&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=80)
81. [Rules of Inference](https://www.youtube.com/watch?v=DEJf8Xn3g0g&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=81)
82. [Forward Reasoning](https://www.youtube.com/watch?v=vyU4EoxwXJE&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=82)
83. [First Order Logic](https://www.youtube.com/watch?v=WJNmTGjr1qs&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=83)
84. [Implicit Quantifier Notation](https://www.youtube.com/watch?v=MsuaWozZowg&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=84)
85. [Backward Reasoning](https://www.youtube.com/watch?v=6vNskRcabP4&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=85)
86. [Depth First Search on Goal Trees](https://www.youtube.com/watch?v=sxgCcuXhekI&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=86)
87. [Incompleteness...](https://www.youtube.com/watch?v=-vDk_IIl81Q&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=87)
88. [Constraint Satisfaction Problems](https://www.youtube.com/watch?v=fEImACP5nmM&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=88)
89. [Binary Constraint Networks](https://www.youtube.com/watch?v=N32HOW7BOv0&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=89)
90. [Interpreting Line Drawings](https://www.youtube.com/watch?v=bsk2B1KFev8&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=90)
91. [Model Based Diagnosis](https://www.youtube.com/watch?v=t5UQTnT6g88&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=91)
92. [Solving CSPs](https://www.youtube.com/watch?v=IOFARrkvOjg&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=92)
93. [Arc Consistency](https://www.youtube.com/watch?v=jyWpapbBWLQ&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=93)
94. [Propagation = Reasoning](https://www.youtube.com/watch?v=7WaB2hJLFAQ&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=94)
95. [Lookahead Search](https://www.youtube.com/watch?v=vWBf5yphFBY&list=PLyqSpQzTE6M8N9lDWllq6NqB5dmpy6gtc&index=95)

</details>


## Books, notes and websites

- Book: Russell & Norvig, *AIMA* (the course text); Sutton & Barto; Bishop
- ✅ NPTEL *AI: Search Methods* (Khemani, IIT Madras)
- Berkeley CS188

## Practice / proof of understanding

Solve Pacman-style search, CSP and an HMM filter in Python.

## What your IITM course sheet says

### From the PDF: DA2403

**Official description:** The students should be able to  1. Formulate the given AI task at hand in the rational agents and environments framework.  2. Construct basic algorithms for the most common type of AI tasks.  3. Implement these algorithms on the computer for a variety of settings.

**Official syllabus (trimmed):**

> 1. Introduction (2 weeks). Strong and weak AI, rational agents and environments, descriptive, predictive and
>  prescriptive/control tasks, multi-agent cooperative and adversarial tasks.
>  2. Description, Prediction, Modelling and Decisions (3 weeks) Clustering, prediction, classification vs regression,
>  sequential prediction, hidden Markov models, probabilistic graphical models: inference and learning.
>  3. Search (4 weeks) Deterministic control, single and multiple agents, BFS, DFS, uniform cost, A*, heuristics,
>  constraint satisfaction problems. Games, adversarial search, minimax value, a - ß pruning.
>  4. Logic and Planning (3 weeks) Logical agents, first-order logic, planning, knowledge representation.
>  5. Stochastic Control (2 weeks) Markov Decision Processes, formulation, value Iteration, Q-learning, partially
>  obsevable MDPs, Reinforcement learning.
>  6. Advanced Topics (1 week) Generative AI, robotics, real world impact. Fairness, accountability and transparency
>  in AI.

**Official textbooks:** 1. Artificial Intelligence : A Modern Approach (Paperpack). Stuart Russell and Peter Norvig. Pearson; 3 edition.  2010 ISBN-13: 978-0132071482  2. Reinforcement Learning: An Introduction. Richard S. Sutton Andrew G. Barto . MIT Press, 2017. ISBN-13:  9780262332767  3. Pattern Recognition and Machine Learning. Christopher Bishop. Springer. 2006. ISBN-13 978-0-387-31073-2.

**Official references:** 1. Artificial Intelligence : A Modern Approach (Paperpack). Stuart Russell and Peter Norvig. Pearson; 3 edition.  2010 ISBN-13: 978-0132071482  2. Reinforcement Learning: An Introduction. Richard S. Sutton Andrew G. Barto . MIT Press, 2017. ISBN-13:  9780262332767  3. Pattern Recognition and Machine Learning. Christopher Bishop. Springer. 2006. ISBN-13 978-0-387-31073-2.

### From the PDF: DA2404

**Official description:** The students should be able to  1. Construct basic AI algorithms for the most common type of AI tasks.  2. Implement these algorithms on the computer for a variety of settings.

**Official syllabus (trimmed):**

> 1. Description, Prediction, Modelling and Decisions (3 weeks) Clustering, prediction, classification vs regres-
>  sion, sequential prediction, hidden Markov models, probabilistic graphical models: inference and learning.
>  2. Search (4 weeks) Deterministic control, single and multiple agents, BFS, DFS, uniform cost, A*, heuristics,
>  constraint satisfaction problems. Games, adversarial search, minimax value, a - ß pruning.
>  3. Stochastic Control (2 weeks) Markov Decision Processes, formulation, value Iteration, Q-learning, partially
>  obsevable MDPs.
>  4. Mini-projects (5 weeks) Develop AI based solutions to complex problems on various environments. Build game
>  solvers.

**Official textbooks:** 1. Artificial Intelligence : A Modern Approach (Paperpack). Stuart Russell and Peter Norvig. Pearson; 3 edition.  2010 ISBN-13: 978-0132071482  2. Reinforcement Learning: An Introduction. Richard S. Sutton and Andrew G. Barto . MIT Press, 2017.  ISBN-13: 9780262332767  3. Pattern Recognition and Machine Learning. Christopher Bishop. Springer. 2006. ISBN-13 978-0-387-31073-2.

**Official references:** 1. Artificial Intelligence : A Modern Approach (Paperpack). Stuart Russell and Peter Norvig. Pearson; 3 edition.  2010 ISBN-13: 978-0132071482  2. Reinforcement Learning: An Introduction. Richard S. Sutton and Andrew G. Barto . MIT Press, 2017.  ISBN-13: 9780262332767  3. Pattern Recognition and Machine Learning. Christopher Bishop. Springer. 2006. ISBN-13 978-0-387-31073-2.
