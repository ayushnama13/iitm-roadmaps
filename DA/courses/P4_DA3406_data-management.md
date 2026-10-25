# DA3406 — Data Management

| | |
|---|---|
| Tier | A |
| Phase (order) | 4 |
| Do this first | DA2303, DA2402 |
| Estimated effort | 10-12 weeks |
| Unlocks | DA3408, DA5402 |

## Roadmap

1. Relational model, ER, normalisation, SQL.
2. Transactions, indexing; data for AI workloads.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Database Management Systems](https://www.youtube.com/playlist?list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU) (81 videos). IIT Madras BS *Database Management Systems* (Partha Pratim Das).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [CMU Intro to Database Systems (15-445/645 - Fall 2025)](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYMAgsGH-GtY5rJYZ6zjsd5) (25 videos). CMU 15-445 *Intro to Database Systems* (Fall 2025, Andy Pavlo): how a database is built inside.

### ⚡ Short videos for intuition and revision

- [SQL Ultimate Course](https://www.youtube.com/playlist?list=PLNcg_FV9n7qZY_2eAtUzEUulNjTJREhQe) (56 videos). Data with Baraa *SQL Ultimate Course*: hands-on SQL from zero to window functions.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=OMHbGm9SQuE&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=1)–[10](https://www.youtube.com/watch?v=AaKMO4-g_zw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=10) | Why DBMS, data models, relational model, intro to SQL. Install PostgreSQL. |
| 2 | [13](https://www.youtube.com/watch?v=UTvCO2YaPxA&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=13)–[19](https://www.youtube.com/watch?v=Y4iDP3E7JxI&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=19) | Running SQL in PostgreSQL, joins, views, transactions, constraints, functions, procedures, triggers. Do 30 SQL problems (pgexercises.com). |
| 3 | [20](https://www.youtube.com/watch?v=VfQcP-2VdLc&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=20)–[25](https://www.youtube.com/watch?v=DMiZPUjRls0&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=25), [77](https://www.youtube.com/watch?v=CkL5StNIla8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=77) | Relational algebra, tuple relational calculus, ER modelling, division. |
| 4-5 | [26](https://www.youtube.com/watch?v=Am4ZVa1Filk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=26)–[35](https://www.youtube.com/watch?v=4iOin7ls0Uk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=35), [71](https://www.youtube.com/watch?v=0B6Yd7RhBX4&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=71)–[74](https://www.youtube.com/watch?v=3hCfuG-E0jk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=74), [78](https://www.youtube.com/watch?v=hEsWAya9PHM&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=78), [80](https://www.youtube.com/watch?v=2RyQBcD6kIs&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=80)–[81](https://www.youtube.com/watch?v=ODqghQdR4KY&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=81) | Functional dependencies, closures, keys, canonical cover, decompositions, normal forms up to 4NF. Normalise 5 schemas by hand. |
| 6 | [36](https://www.youtube.com/watch?v=yh6yhQj4Ncg&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=36)–[40](https://www.youtube.com/watch?v=KgK3Kz8BlmA&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=40), [69](https://www.youtube.com/watch?v=ZiO7YhTHuyQ&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=69) | Application development: web apps, SQL from Python. Build a small Flask + Postgres app. |
| 7 | [41](https://www.youtube.com/watch?v=uqpA6wySe8o&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=41)–[50](https://www.youtube.com/watch?v=oZetRAwYmrw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=50), [75](https://www.youtube.com/watch?v=bIUCShynysk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=75) | Storage, file structures, indexing, B+ trees, hashing. Compare query plans with and without indexes using EXPLAIN ANALYZE. |
| 8 | [51](https://www.youtube.com/watch?v=MwdAkFhR_I8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=51)–[60](https://www.youtube.com/watch?v=YYl4onLINRY&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=60) | Transactions, serialisability, locking, backup and recovery. |
| 9 | [61](https://www.youtube.com/watch?v=VQrqJafvnzY&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=61)–[65](https://www.youtube.com/watch?v=lgiN8paqhjw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=65), [76](https://www.youtube.com/watch?v=K8ngtaPkpFU&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=76) | Query processing and optimisation, NoSQL, revision. |

<details>
<summary>All lectures in <i>Database Management Systems</i> (81 videos)</summary>

1. [L1: Course overview with applications prerequisites & structure of database management systems](https://www.youtube.com/watch?v=OMHbGm9SQuE&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=1)
2. [L2: Why DBMS? /1 | evolution, importance, & modern applications](https://www.youtube.com/watch?v=BS0-7KJdopY&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=2)
3. [L3:Why DBMS? /2 | file based data management vs sql databases](https://www.youtube.com/watch?v=9SrBrnIoCjc&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=3)
4. [L4: Introduction to DBMS/1: data abstraction, schema vs instance & models](https://www.youtube.com/watch?v=s1Jb-NJNpT4&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=4)
5. [L5: Introduction to DBMS/2 | data models, architecture & design principles](https://www.youtube.com/watch?v=MDQxqYVXiVU&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=5)
6. [L6: Introduction to relational model/1 attributes schemas keys](https://www.youtube.com/watch?v=B3cCQagcoao&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=6)
7. [L7: Introduction to relational model/2 with relational algebra](https://www.youtube.com/watch?v=D8e1-apWxo8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=7)
8. [L8: Introduction to sql/1 | basics of data definition language & data manipulation language](https://www.youtube.com/watch?v=Wv6vM5rGCw0&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=8)
9. [L9: Introduction to SQL/2 | understanding query structure in DBMS](https://www.youtube.com/watch?v=hEgb_76wz1s&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=9)
10. [L10: Introduction to sql/3 | advanced sql concepts, set operations](https://www.youtube.com/watch?v=AaKMO4-g_zw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=10)
11. [L11: Binary numbers & character encoding part 1 | basics of binary](https://www.youtube.com/watch?v=7yzUtikAvsk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=11)
12. [L12: Binary numbers & character encoding part 2 | ASCII unicode boolean operations](https://www.youtube.com/watch?v=9vD-GAyfmv8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=12)
13. [L13: Running SQL commands in PostgreSQL | beginner guide to psql shell](https://www.youtube.com/watch?v=UTvCO2YaPxA&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=13)
14. [L14: SQL examples made easy | introduction to query building](https://www.youtube.com/watch?v=j6v3lL5xbao&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=14)
15. [L15: Intermediate sql/1 | data manipulation & nested subqueries](https://www.youtube.com/watch?v=Pk1j1UE3JLI&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=15)
16. [L16: Intermediate sql/2 | mastering joins & views](https://www.youtube.com/watch?v=_-JZS7mqo6k&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=16)
17. [L17: Intermediate sql/3 | transactions, constraints, data types & authorization](https://www.youtube.com/watch?v=JtCk6DurR8k&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=17)
18. [L18: Advanced sql | functions, procedures & triggers explained](https://www.youtube.com/watch?v=f0hK7aMloI0&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=18)
19. [L19: Database triggers explained with case studies | functionality vs performance](https://www.youtube.com/watch?v=Y4iDP3E7JxI&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=19)
20. [L20: Formal relational query languages/1: introduction to relational algebra](https://www.youtube.com/watch?v=VfQcP-2VdLc&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=20)
21. [L21: Formal relational query languages/2 | tuple relational calculus](https://www.youtube.com/watch?v=WjlbMfEqom8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=21)
22. [L22: Entity-relationship model/1 | fundamentals of database design & e-r concepts](https://www.youtube.com/watch?v=EGAQdgim3IA&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=22)
23. [L23: Entity-relationship model/2 | advanced E-R diagrams & relational schema](https://www.youtube.com/watch?v=Gfcm-A-MpO4&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=23)
24. [L24: Entity-relationship model/3 | ternary relationships, specialization, and aggregation](https://www.youtube.com/watch?v=WOWKszMjmgE&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=24)
25. [L25: Division operation in SQL with examples](https://www.youtube.com/watch?v=DMiZPUjRls0&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=25)
26. [L26: Relational database design/1 | principles, normalization & first normal form](https://www.youtube.com/watch?v=Am4ZVa1Filk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=26)
27. [L27: Relational database design/2 | understanding functional dependencies and keys](https://www.youtube.com/watch?v=iW5C0g8fhx4&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=27)
28. [L28: Relational database design/3 | functional dependency theory and database normalization](https://www.youtube.com/watch?v=gFJuNh63MGw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=28)
29. [L29: Relational database design/4 | functional dependencies, attribute](https://www.youtube.com/watch?v=6AZlp7EcmiQ&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=29)
30. [L30: Relational database design/5 | dependency preservation algorithms in relational database](https://www.youtube.com/watch?v=WWI4ACyTneI&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=30)
31. [L31: Relational database design/6 | normal forms in database normalization](https://www.youtube.com/watch?v=BQex0zbsMwg&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=31)
32. [L32: Relational database design/7 | higher-level normal forms explained](https://www.youtube.com/watch?v=4Vn2-tcg21c&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=32)
33. [L33: Relational database design/8 | case study in database normalization](https://www.youtube.com/watch?v=uOxY9Hn8yz4&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=33)
34. [L34: Relational database design/9 | multivalued dependencies (MVD) and Fourth Normal Form (4NF)](https://www.youtube.com/watch?v=pf7ws6WgklU&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=34)
35. [L35: Relational database design/10 | database design summary and handling temporal data](https://www.youtube.com/watch?v=4iOin7ls0Uk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=35)
36. [L36: Application design & development/1 | application architecture and design principles](https://www.youtube.com/watch?v=yh6yhQj4Ncg&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=36)
37. [L37: Application design & development/2 | web applications and database integration](https://www.youtube.com/watch?v=Uk8x3XvG3dA&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=37)
38. [L38: Application design & development/3 | sql and native language database connectivity](https://www.youtube.com/watch?v=ElkvZWTN9J8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=38)
39. [L39: Application design & development/4| building database applications with python and PostgreSQL](https://www.youtube.com/watch?v=uLbMLfUuAxQ&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=39)
40. [L40: Application design & development/5 | rapid application development and mobile app design](https://www.youtube.com/watch?v=KgK3Kz8BlmA&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=40)
41. [L41: Algorithms & data structures/1 | algorithms basics & complexity analysis](https://www.youtube.com/watch?v=uqpA6wySe8o&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=41)
42. [L42: Algorithms & data structures/2 | data structures | arrays,queues](https://www.youtube.com/watch?v=vY6MnadNvUk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=42)
43. [L43: Algorithms & data structures/3 | data structures and search techniques](https://www.youtube.com/watch?v=OgXyMwjD6Nk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=43)
44. [L44: Storage & file structure/1 | physical storage media in database systems](https://www.youtube.com/watch?v=tbCDTfpOC6Q&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=44)
45. [L45: Storage & file structure/2 | file structure | records, slotted pages](https://www.youtube.com/watch?v=7Y3z_iqTYbg&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=45)
46. [L46: Indexing & hashing/1 | introduction to indexing in databases](https://www.youtube.com/watch?v=fY-EC1dknnQ&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=46)
47. [L47: Indexing & hashing/2 | indexing/2 | balanced trees, 2-3-4 trees](https://www.youtube.com/watch?v=pZ9aUJUzFhg&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=47)
48. [L48: Indexing & hashing/3 | indexing Part 3 | b plus trees, search & insert](https://www.youtube.com/watch?v=7fhN_zacwK0&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=48)
49. [L49: Indexing & hashing/4 | static hashing, dynamic hashing, and bitmap indices](https://www.youtube.com/watch?v=yXK6yYwNJFw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=49)
50. [L50: Indexing & hashing/5 | index design | locks](https://www.youtube.com/watch?v=oZetRAwYmrw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=50)
51. [L51: Transactions/1 | acid & concurrency](https://www.youtube.com/watch?v=MwdAkFhR_I8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=51)
52. [L52: Transactions/2 | serializability | conflict serializability](https://www.youtube.com/watch?v=MNXTL69Ud9A&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=52)
53. [L53: Transactions/3 | recoverability | tcl, conflict checks](https://www.youtube.com/watch?v=tlnEqRcVB5s&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=53)
54. [L54: Concurrency control/1 | lock-based protocols](https://www.youtube.com/watch?v=VcYdCPbyWX0&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=54)
55. [L55: Concurrency control/2 | techniques & protocols](https://www.youtube.com/watch?v=OYbfDSxrEKI&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=55)
56. [L56: Backup & recovery/1 | backup/1](https://www.youtube.com/watch?v=7oNFney4vhc&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=56)
57. [L57: Backup & recovery/2 | recovery/1](https://www.youtube.com/watch?v=2BkGxLntkBc&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=57)
58. [L58: Backup & recovery/3 | recovery techniques with logging](https://www.youtube.com/watch?v=41cWyckqqRc&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=58)
59. [L59: Backup & recovery/4 | logical lndo & early lock release](https://www.youtube.com/watch?v=zliL6LlKiNs&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=59)
60. [L60: Backup & recovery/5 | backup/2 | redundant array of independent disks](https://www.youtube.com/watch?v=YYl4onLINRY&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=60)
61. [L61: Query processing & optimization/1 | processing](https://www.youtube.com/watch?v=VQrqJafvnzY&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=61)
62. [L62: Query processing & optimization/2 | query optimization strategies](https://www.youtube.com/watch?v=pAonkbv10ak&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=62)
63. [L63: Relational database systems performance & architecture](https://www.youtube.com/watch?v=MGJaOVjdHvs&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=63)
64. [L64: Non-relational database management systems | nosql & cap theorem](https://www.youtube.com/watch?v=sLapLg_dZ9c&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=64)
65. [L65: Widely used database management systems & course summarization](https://www.youtube.com/watch?v=lgiN8paqhjw&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=65)
66. [L66: Case study on entity relationship diagram:pharmacy database building design](https://www.youtube.com/watch?v=Gd9ZEFy3H-k&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=66)
67. [L67: Translation of entity relation diagram into relational schema](https://www.youtube.com/watch?v=w_7Q_P8ODNk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=67)
68. [L68: Entity-relationship model/2 | schema translation](https://www.youtube.com/watch?v=In_PYLgZvKo&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=68)
69. [L69: Application design & development/4 | apps with python & postgresql](https://www.youtube.com/watch?v=ZiO7YhTHuyQ&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=69)
70. [L70: Algorithms & data structures/2 | data structures](https://www.youtube.com/watch?v=P0SxHRCjlV8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=70)
71. [L71: Lossless join decomposition | examples & conditions](https://www.youtube.com/watch?v=0B6Yd7RhBX4&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=71)
72. [L72: Dependency presevation](https://www.youtube.com/watch?v=h-SO2pc9_0k&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=72)
73. [L73: Closure of attributes | superkeys & functional dependencies](https://www.youtube.com/watch?v=VC9WPXylUq4&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=73)
74. [L74: Super keys & candidate keys](https://www.youtube.com/watch?v=3hCfuG-E0jk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=74)
75. [L75: Indexing & hashing/3 | indexing/3 | b-tree index files](https://www.youtube.com/watch?v=bIUCShynysk&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=75)
76. [L76: DBMS summary tutorial | quick revision tutorial](https://www.youtube.com/watch?v=K8ngtaPkpFU&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=76)
77. [L77: Tuple relational calculus | non-procedural queries](https://www.youtube.com/watch?v=CkL5StNIla8&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=77)
78. [L78: Canonical cover | simplifying functional dependencies](https://www.youtube.com/watch?v=hEsWAya9PHM&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=78)
79. [L79: comprehensive case study on entity-relationship (ER) diagrams](https://www.youtube.com/watch?v=cS1hL-TjyA0&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=79)
80. [L80: Multivalued dependency & fourth normal form](https://www.youtube.com/watch?v=2RyQBcD6kIs&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=80)
81. [L81: Normalization techniques & problem solving on relational schema](https://www.youtube.com/watch?v=ODqghQdR4KY&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=81)

</details>


## Books, notes and websites

- ✅ NPTEL *Database Management System* (Partha Pratim Das)
- CMU 15-445
- Book: Silberschatz (course text); Kleppmann

## Practice / proof of understanding

Design a schema + 25 SQL queries over a dataset; build a feature store table in PostgreSQL.

## What your IITM course sheet says

### From the PDF: DA3406

**Official description:** . Objectives: This course provides a comprehensive foundation in data management tailored for artificial  intelligence and data analytics workloads. Building on introductory machine learning and data preprocessing,  students will explore the complete lifecycle of structured and scalable data. The curriculum spans logical database  design, relational algebra, and SQL, before diving into the internal mechanics of database systems, including  storage, indexing, query optimization, and transaction processing. To address the demands of modern analytics,  the course concludes with large-scale distributed architectures, big data paradigms (DISC and NoSQL), and  emerging AI-driven database trends such as vector search and learned indexes.  Upon successful completion of this course, students will be able to:  • Design and Query Relational Systems: Translate conceptual data models into normalized 

**Official syllabus (trimmed):**

> 2. Course contents:
>  Module 1: Data modeling and relational foundations (3 weeks): Role of databases in AI and data analytics; Data
>  abstraction, schemas, instances, metadata, and data independence; Conceptual modeling using entities,
>  attributes, relationships, keys, constraints, and weak entities; ER to relational mapping; Functional dependencies
>  and normalization, 1NF, 2NF, 3NF, BCNF; Relational model fundamentals, tuples, domains, keys, integrity
>  constraints; Relational algebra, selection, projection, union, difference, Cartesian product, join, division,
>  aggregation; SQL basics, DDL, DML, constraints, joins, subqueries, views, grouping, ordering, set operations.
>  Module 2: Storage and indexing (2 weeks): DBMS storage architecture and memory hierarchy; Disk structure,
>  pages, blocks, records, spanned and unspanned storage; File organizations, heap files, sorted files, clustered
>  storage, hashing; Buffer manager concepts and page replacement intuition; Cost of disk I/O and basic access path
>  analysis; Single-level and multi-level indexes; B-tree and B+ tree indexes; Static hashing and dynamic hashing,
>  including extendible or linear hashing; Dense and sparse indexes, clustered and non-clustered indexes;
>  Composite indexes and introductory index selection guidelines.
>  Module 3: Query processing and transaction management (3 weeks): Query execution architecture; Evaluation o

**Official textbooks:** 1. Silberschatz, Abraham, Henry F. Korth, and S. Sudarshan. Database System Concepts. 7th ed. New York:  McGraw-Hill Education, 2019

**Official references:** 1. Ramakrishnan, Raghu, and Johannes Gehrke. Database Management Systems. 3rd ed. New York:  McGraw-Hill, 2002.  2. Kleppmann, Martin. Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and  Maintainable Systems. Sebastopol, CA: O'Reilly Media, 2017.  3. Various research papers.
