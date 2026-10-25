# CS6700 — Reinforcement Learning

| | |
|---|---|
| Tier | B |
| Phase (order) | 7 |
| Do this first | CS4011, probability |
| Estimated effort | 12 weeks |
| Unlocks | DA7400, CS7011 |

## Roadmap

1. Bandits; MDPs; dynamic programming.
2. Monte Carlo, TD, Q-learning, SARSA.
3. Function approximation, DQN, policy gradients, actor-critic.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Reinforcement Learning](https://www.youtube.com/playlist?list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9) (64 videos). NPTEL *Reinforcement Learning* (Balaraman Ravindran, IIT Madras): this is CS6700's teacher.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [DeepMind x UCL | Introduction to Reinforcement Learning 2015](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ) (10 videos). DeepMind x UCL *Introduction to RL 2015* (David Silver, official Google DeepMind): the classic. Pair with Sutton & Barto.
- [Stanford CS234 I Reinforcement Learning I Spring 2024 I Emma Brunskill](https://www.youtube.com/playlist?list=PLoROMvodv4rN4wG6Nk6sNpTEbuOSosZdX) (16 videos). Stanford CS234 Spring 2024 (Emma Brunskill, official): modern, includes offline RL and RLHF.
- [Special topics in ML (Reinforcement Learning)](https://www.youtube.com/playlist?list=PLZ2ps__7DhBbDiVplM2I9q2XNso1Qfj62) (44 videos). IIT Madras BS *Special topics in ML (Reinforcement Learning)*.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=4CgVEt-BhLA&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=1)–[6](https://www.youtube.com/watch?v=ewkm38skUlY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=6) | Probability and linear algebra tutorials, RL framework. |
| 2-3 | [7](https://www.youtube.com/watch?v=nNK4xKkAapM&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=7)–[18](https://www.youtube.com/watch?v=K2Hh-ayvsJU&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=18) | Bandits: UCB, PAC bounds, median elimination, Thompson sampling, policy search, contextual bandits. Implement epsilon-greedy, UCB and Thompson on a 10-armed testbed (Sutton & Barto ch. 2). |
| 4 | [19](https://www.youtube.com/watch?v=yIdgKWFulNQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=19)–[27](https://www.youtube.com/watch?v=ybEyXc4hNuk&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=27) | MDPs, Bellman equations, contraction / Banach fixed point proofs. |
| 5 | [28](https://www.youtube.com/watch?v=F3DjpixO1bY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=28)–[30](https://www.youtube.com/watch?v=_0BQZyXx0eU&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=30) | Value iteration, policy iteration, DP. Solve FrozenLake with both. |
| 6 | [31](https://www.youtube.com/watch?v=DaxOiIdjQ4Y&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=31)–[38](https://www.youtube.com/watch?v=w3wGvwi336I&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=38) | Monte Carlo, off-policy MC, UCT, TD(0), SARSA, Q-learning. Implement Q-learning on CliffWalking (Gymnasium). |
| 7 | [39](https://www.youtube.com/watch?v=n0K83V1sCxc&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=39)–[42](https://www.youtube.com/watch?v=uGUAUkmqQtk&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=42) | Eligibility traces, TD(lambda). |
| 8 | [43](https://www.youtube.com/watch?v=gqSuPgrcVx8&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=43)–[49](https://www.youtube.com/watch?v=AohtWrJwvgg&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=49) | Function approximation, LSTD, LSPI, fitted Q, DQN. Train a DQN on CartPole. |
| 9 | [50](https://www.youtube.com/watch?v=f2l8bv8GH5U&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=50)–[53](https://www.youtube.com/watch?v=X6yCRaQa5FE&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=53) | Policy gradients, REINFORCE, actor-critic. Implement REINFORCE and A2C. |
| 10 | [54](https://www.youtube.com/watch?v=K5MlmO0UJtI&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=54)–[64](https://www.youtube.com/watch?v=dMOUp7YzUpQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=64) | Hierarchical RL (options, MAXQ), POMDPs. Then PPO from Spinning Up (OpenAI). |

<details>
<summary>All lectures in <i>Reinforcement Learning</i> (64 videos)</summary>

1. [Tutorial 1 - Probability Basics 1](https://www.youtube.com/watch?v=4CgVEt-BhLA&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=1)
2. [Tutorial 1 - Probability Basics 2](https://www.youtube.com/watch?v=NFQ94cd649M&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=2)
3. [Tutorial 2 - Linear Algebra 1](https://www.youtube.com/watch?v=lWSYxvJbf9E&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=3)
4. [Tutorial 2 - Linear Algebra   2](https://www.youtube.com/watch?v=wW4tIx9dOk8&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=4)
5. [Introduction to RL](https://www.youtube.com/watch?v=YaPSPu7K9S0&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=5)
6. [RL Framework and Applications](https://www.youtube.com/watch?v=ewkm38skUlY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=6)
7. [Introduction to Immediate RL](https://www.youtube.com/watch?v=nNK4xKkAapM&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=7)
8. [Bandit Optimalities](https://www.youtube.com/watch?v=AizR8uvhX-s&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=8)
9. [Value Function Based Methods](https://www.youtube.com/watch?v=iB4m-jP7blI&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=9)
10. [UCB 1](https://www.youtube.com/watch?v=TIlDzLZPyhY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=10)
11. [Concentration Bounds](https://www.youtube.com/watch?v=KB-ZDvLbuOQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=11)
12. [UCB 1 Theorem](https://www.youtube.com/watch?v=7IA6Zb7KZM0&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=12)
13. [PAC Bounds](https://www.youtube.com/watch?v=N_9HgdhXKIY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=13)
14. [Median Elimination](https://www.youtube.com/watch?v=3iNaR0Mq1ug&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=14)
15. [Thompson Sampling](https://www.youtube.com/watch?v=H2OWTxdauqA&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=15)
16. [Policy Search](https://www.youtube.com/watch?v=y3QEOmkxsQo&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=16)
17. [REINFORCE](https://www.youtube.com/watch?v=WIBWQ7lOXoA&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=17)
18. [Contextual Bandits](https://www.youtube.com/watch?v=K2Hh-ayvsJU&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=18)
19. [Full RL Introduction](https://www.youtube.com/watch?v=yIdgKWFulNQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=19)
20. [Returns, Value functions and MDPs](https://www.youtube.com/watch?v=BiY_X1c068U&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=20)
21. [MDP Modelling](https://www.youtube.com/watch?v=BpSNh1h4HeQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=21)
22. [Bellman Equation](https://www.youtube.com/watch?v=CTPHADvQxSs&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=22)
23. [Bellman Optimality Equation](https://www.youtube.com/watch?v=4S9aRrsP954&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=23)
24. [Lec 20 - Cauchy Sequence and Green's Equation](https://www.youtube.com/watch?v=THmztE-ghWc&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=24)
25. [Banach Fixed Point Theorem](https://www.youtube.com/watch?v=EKwc7rw9YCU&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=25)
26. [Convergence Proof](https://www.youtube.com/watch?v=9UhK8U6rEVY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=26)
27. [Lpi Convergence](https://www.youtube.com/watch?v=ybEyXc4hNuk&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=27)
28. [Value Iteration](https://www.youtube.com/watch?v=F3DjpixO1bY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=28)
29. [Policy Iteration](https://www.youtube.com/watch?v=09L0nqw9Vnc&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=29)
30. [Dynamic Programming](https://www.youtube.com/watch?v=_0BQZyXx0eU&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=30)
31. [Monte Carlo](https://www.youtube.com/watch?v=DaxOiIdjQ4Y&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=31)
32. [Control in Monte Carlo](https://www.youtube.com/watch?v=h7lfqnV-8Pc&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=32)
33. [Off Policy MC](https://www.youtube.com/watch?v=oHE7u15n7Qg&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=33)
34. [UCT](https://www.youtube.com/watch?v=unCdZCQS64g&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=34)
35. [TD(0)](https://www.youtube.com/watch?v=4KlVxH8wMWQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=35)
36. [TD(0) Control](https://www.youtube.com/watch?v=x3PgPnVC-bQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=36)
37. [Lec 33 - Q-Learning](https://www.youtube.com/watch?v=ioQz9Pkycb0&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=37)
38. [Lec 34 - Afterstate](https://www.youtube.com/watch?v=w3wGvwi336I&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=38)
39. [Eligibility Traces](https://www.youtube.com/watch?v=n0K83V1sCxc&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=39)
40. [Backward View of Eligibility Traces](https://www.youtube.com/watch?v=A1s3dc64uhE&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=40)
41. [Eligibility Trace Control](https://www.youtube.com/watch?v=OgKysheQJSQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=41)
42. [Thompson Sampling](https://www.youtube.com/watch?v=uGUAUkmqQtk&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=42)
43. [Function Approximation](https://www.youtube.com/watch?v=gqSuPgrcVx8&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=43)
44. [Linear Parameterization](https://www.youtube.com/watch?v=c4cvheE3diA&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=44)
45. [State Aggregation Methods](https://www.youtube.com/watch?v=wGPxro6C2ik&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=45)
46. [Function Approximation and Eligibility Traces](https://www.youtube.com/watch?v=N21zCqTwxbs&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=46)
47. [LSTD and LSTDQ](https://www.youtube.com/watch?v=zTFNYrYbvVE&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=47)
48. [LSPI and Fitted Q](https://www.youtube.com/watch?v=JmbN6XZ4Cro&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=48)
49. [DQN and Fitted Q Iteration](https://www.youtube.com/watch?v=AohtWrJwvgg&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=49)
50. [Policy Gradient Approach](https://www.youtube.com/watch?v=f2l8bv8GH5U&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=50)
51. [Actor Critic and REINFORCE](https://www.youtube.com/watch?v=sTZ4GyJ4FZU&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=51)
52. [REINFORCE (cont'd)](https://www.youtube.com/watch?v=BEhnse8cLDw&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=52)
53. [Policy Gradient with Function Approximation](https://www.youtube.com/watch?v=X6yCRaQa5FE&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=53)
54. [Hierarchical Reinforcement Learning](https://www.youtube.com/watch?v=K5MlmO0UJtI&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=54)
55. [Types of Optimality](https://www.youtube.com/watch?v=EbTIQqVDJsg&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=55)
56. [Semi Markov Decision Processes](https://www.youtube.com/watch?v=vdRG-EbcNGw&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=56)
57. [Options](https://www.youtube.com/watch?v=1eb4vECGKC4&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=57)
58. [Learning with Options](https://www.youtube.com/watch?v=6wH3yS07NTA&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=58)
59. [Hierarchical Abstract Machines](https://www.youtube.com/watch?v=rVhb6f6G-1M&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=59)
60. [MAXQ](https://www.youtube.com/watch?v=4mmW0kYmK3I&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=60)
61. [MAXQ Value Function Decomposition](https://www.youtube.com/watch?v=1iACStiJQBs&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=61)
62. [Option Discovery](https://www.youtube.com/watch?v=uJ0oNtDG6ro&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=62)
63. [POMDP Introduction](https://www.youtube.com/watch?v=9G_KevA8DFY&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=63)
64. [Solving POMDP](https://www.youtube.com/watch?v=dMOUp7YzUpQ&list=PLyqSpQzTE6M_FwzHFAyf4LSkz_IjMyjD9&index=64)

</details>


## Books, notes and websites

- ✅ NPTEL *Reinforcement Learning* (Balaraman Ravindran, IIT Madras) — onlinecourses.nptel.ac.in/noc20_cs74/preview
- Book: Sutton & Barto — incompleteideas.net/book (free; did not load from my check, search the title if it is down)
- David Silver's UCL lectures (YouTube); Hugging Face Deep RL course

## Practice / proof of understanding

Solve FrozenLake with value iteration, CartPole with DQN, and LunarLander with PPO using Gymnasium.

## What your IITM course sheet says

### From the PDF: CS6700

**Official description:** The Reinforcement Learning problem : evaluative feedback, non-associative  learning, Rewards and returns, Markov Decision Processes, Value functions, optimality and approximation.  Dynamic programming : value iteration, policy iteration, asynchronous  DP, generalized policy iteration.  Monta-Carlo methods : policy evaluation, roll outs, on policy and off policy  learning, importance sampling.  Temporal Difference learning : TD prediction, Optimality of TD(0), SARSA, Q-learning, R-learning, Games and  after states.  Eligibility traces : n-step TD prediction, TD (lambda), forward and  backward views, Q (lambda), SARSA (lambda), replacing traces and  accumulating traces.  Function Approximation : Value prediction, gradient descent methods,  linear function approximation, ANN based function approximation, lazy  learning, instability issues  Policy Gradient methods : non-associative learning 

**Official textbooks:** NIL
