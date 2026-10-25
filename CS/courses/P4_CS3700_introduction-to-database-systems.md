# CS3700 — Introduction to Database Systems

| | |
|---|---|
| Tier | A |
| Phase (order) | 4 |
| Do this first | CS2705, CS1200 |
| Estimated effort | 10-12 weeks |
| Unlocks | CS6550, CS6510, CS6220, DA3406 |

## Roadmap

1. ER modelling and the relational model; relational algebra.
2. SQL: select-from-where, joins, nested queries, aggregates.
3. Functional dependencies and normal forms (1NF-BCNF), decomposition.
4. Transactions, indexing, concurrency control, recovery.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Introduction to Database Systems](https://www.youtube.com/playlist?list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu) (41 videos). NPTEL-NOC IITM *Introduction to Database Systems* (IIT Madras).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Database Management Systems](https://www.youtube.com/playlist?list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU) (81 videos). IIT Madras BS *Database Management Systems* (Partha Pratim Das).
- [CMU Intro to Database Systems (15-445/645 - Fall 2024)](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYDBpQnSymaectKjxCy6BYq) (26 videos). CMU 15-445 Fall 2024 (Andy Pavlo, official CMU Database Group): how a DBMS is built inside. Do BusTub projects.

### ⚡ Short videos for intuition and revision

- [SQL Ultimate Course](https://www.youtube.com/playlist?list=PLNcg_FV9n7qZY_2eAtUzEUulNjTJREhQe) (56 videos). Data with Baraa *SQL Ultimate Course*: practical SQL from zero.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=sEaYXwmsLw0&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=1)–[3](https://www.youtube.com/watch?v=Co12LqzGpTA&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=3) | DB architecture. Install PostgreSQL; load a sample DB (e.g. pagila). |
| 2 | [4](https://www.youtube.com/watch?v=5TU7zH0Z8ps&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=4)–[7](https://www.youtube.com/watch?v=Z2Zx2G02aI4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=7), [12](https://www.youtube.com/watch?v=balW7pT7qP0&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=12) | ER modelling, weak entities, relational model, keys, ER -> tables. Design an ER schema for a college and create it in Postgres. |
| 3 | [8](https://www.youtube.com/watch?v=eEIRQT6b4bo&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=8)–[14](https://www.youtube.com/watch?v=GpN1qp-qtjw&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=14) | Relational algebra and tuple relational calculus. Write 15 queries in RA, then in SQL. |
| 4 | [15](https://www.youtube.com/watch?v=QYd6ZjHpzBg&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=15)–[20](https://www.youtube.com/watch?v=jb-7jDate8w&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=20) | SQL: DDL, subqueries, correlated subqueries, aggregates, views, programmatic access. Do 30 SQL problems (pgexercises.com / LeetCode SQL 50). |
| 5 | [21](https://www.youtube.com/watch?v=NfHGvgMi6rw&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=21)–[26](https://www.youtube.com/watch?v=wsY9YX6vL2Y&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=26) | Functional dependencies, Armstrong's axioms, 2NF/3NF/BCNF/4NF, decompositions. Normalise 5 schemas by hand. |
| 6 | [27](https://www.youtube.com/watch?v=7seiJ3R_PU4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=27)–[35](https://www.youtube.com/watch?v=_jou55svo1k&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=35) | File organisation, hashing, B+ trees, RAID, query evaluation, join algorithms, optimisation. Use EXPLAIN ANALYZE on your queries; add indexes and compare. |
| 7 | [36](https://www.youtube.com/watch?v=p4bA-gM8ulQ&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=36)–[41](https://www.youtube.com/watch?v=Gm4W6BNqDB4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=41) | Transactions, schedules, locking, undo/redo logging, isolation levels. Reproduce a lost-update anomaly in two psql sessions. |

<details>
<summary>All lectures in <i>Introduction to Database Systems</i> (41 videos)</summary>

1. [#1 Introduction to Database Systems](https://www.youtube.com/watch?v=sEaYXwmsLw0&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=1)
2. [#2 Database Architecture | Introduction to Database Systems](https://www.youtube.com/watch?v=AAKUqHBuzk4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=2)
3. [#3 RDBMS Architecture | Introduction to Database Systems](https://www.youtube.com/watch?v=Co12LqzGpTA&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=3)
4. [#4 Introduction to ER Model | Introduction to Database Systems](https://www.youtube.com/watch?v=5TU7zH0Z8ps&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=4)
5. [#5 Entities & Relationships | Introduction to Database Systems](https://www.youtube.com/watch?v=9wPWupdoXGM&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=5)
6. [#6 Modelling Weak Entities & Design Choices | Introduction to Database Systems](https://www.youtube.com/watch?v=IVyUx7HCls8&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=6)
7. [#7 Relational Data Model & Notion of Keys | Introduction to Database Systems](https://www.youtube.com/watch?v=Z2Zx2G02aI4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=7)
8. [#8 Introduction to Relational Algebra | Introduction to Database Systems](https://www.youtube.com/watch?v=eEIRQT6b4bo&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=8)
9. [#9 Operators in Relational Model | Introduction to Database Systems](https://www.youtube.com/watch?v=lDtl3xN-wm8&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=9)
10. [#10 Uses of Renaming, Join & Division in Relation Algebra | Introduction to Database Systems](https://www.youtube.com/watch?v=RlgvdfNqPhc&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=10)
11. [#11 Example Queries in Relational Model & Outer Join Operation | Introduction to Database Systems](https://www.youtube.com/watch?v=Kmp76uRHz9c&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=11)
12. [#12 Convert ER-Model to a Relational Model | Introduction to Database Systems](https://www.youtube.com/watch?v=balW7pT7qP0&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=12)
13. [#13 Introduction to Tuple Relational Calculus | Introduction to Database Systems](https://www.youtube.com/watch?v=V2iBuOtX458&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=13)
14. [#14 Example TRC Queries | Introduction to Database Systems](https://www.youtube.com/watch?v=GpN1qp-qtjw&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=14)
15. [#15 Data Definition using SQL | Introduction to Database Systems](https://www.youtube.com/watch?v=QYd6ZjHpzBg&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=15)
16. [#16 Basic SQL Query block & Subqueries | Introduction to Database Systems](https://www.youtube.com/watch?v=9oAWVvUfa-E&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=16)
17. [#17 Correlated Subqueries | Introduction to Database Systems](https://www.youtube.com/watch?v=CPcAX8CsiGo&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=17)
18. [#18 Aggregate Functions | Introduction to Database Systems](https://www.youtube.com/watch?v=PVE4e7_fU0U&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=18)
19. [#19 Views | Introduction to Database Systems](https://www.youtube.com/watch?v=HHled4HwuGg&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=19)
20. [#20 Programmatic Access of SQL | Introduction to Database Systems](https://www.youtube.com/watch?v=jb-7jDate8w&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=20)
21. [#21 Normal forms | Introduction | Introduction to Database Systems](https://www.youtube.com/watch?v=NfHGvgMi6rw&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=21)
22. [#22 Deriving New Functional Dependencies | Introduction to Database Systems](https://www.youtube.com/watch?v=Q5jbdZtnOjg&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=22)
23. [#23 Proving Soundness & Completeness of Armstrong's Axioms | Introduction to Database Systems](https://www.youtube.com/watch?v=Zz43we9bTOM&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=23)
24. [#24 Normal forms | 2NF, 3NF, BCNF | Introduction to Database Systems](https://www.youtube.com/watch?v=2tPNtnCfGzo&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=24)
25. [#25 Properties of Decompositions | Introduction to Database Systems](https://www.youtube.com/watch?v=7frdVKSgqek&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=25)
26. [#26 Normal forms | 4NF, 5NF | Introduction to Database Systems](https://www.youtube.com/watch?v=wsY9YX6vL2Y&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=26)
27. [#27 Introduction to File Orgranization | Introduction to Database Systems](https://www.youtube.com/watch?v=7seiJ3R_PU4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=27)
28. [#28 File Orgranization Methods | Introduction to Database Systems](https://www.youtube.com/watch?v=3l-hYcZgNYI&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=28)
29. [#29 Dynamic File Orgranization Using Hashing | Introduction to Database Systems](https://www.youtube.com/watch?v=VNTfgUGQHz4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=29)
30. [#30 Index Structures | Introduction to Database Systems](https://www.youtube.com/watch?v=F0vZhxIR3Jw&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=30)
31. [#31 B+Trees on Disks | Introduction to Database Systems](https://www.youtube.com/watch?v=tbIIu0mnsBM&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=31)
32. [#32 Performance & Reliability of Multiple Disks | Introduction to Database Systems](https://www.youtube.com/watch?v=08Y0eK3iPJo&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=32)
33. [#33 Relational Query Evaluation | Introduction to Database Systems](https://www.youtube.com/watch?v=y6Gj41xEQxM&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=33)
34. [#34 Join Operator Processing Algorithms | Introduction to Database Systems](https://www.youtube.com/watch?v=29ZGZ6l0kkg&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=34)
35. [#35 Query Optimization | Introduction to Database Systems](https://www.youtube.com/watch?v=_jou55svo1k&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=35)
36. [#36 ACID Properties & Operations in Transactions | Introduction to Database Systems](https://www.youtube.com/watch?v=p4bA-gM8ulQ&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=36)
37. [#37 Schedules | Introduction to Database Systems](https://www.youtube.com/watch?v=14GE2Z21Xgs&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=37)
38. [#38 Concurrency Control Using Locks | Introduction to Database Systems](https://www.youtube.com/watch?v=IQ01axFqz6U&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=38)
39. [#39 Recovery Using Undo Logging Method | Introduction to Database Systems](https://www.youtube.com/watch?v=kqO4nxPkjKw&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=39)
40. [#40 Recovery Using Redo & Undo-Redo Logging Methods | Introduction to Database Systems](https://www.youtube.com/watch?v=mxhNw8f0IaM&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=40)
41. [#41 Recoverable Schedules & Transaction Isolation Levels | Introduction to Database Systems](https://www.youtube.com/watch?v=Gm4W6BNqDB4&list=PLyqSpQzTE6M-xymXgqewlzcC3U4cdRoSu&index=41)

</details>


## Books, notes and websites

- ✅ NPTEL *Database Management System* (Partha Pratim Das, IIT Kharagpur) — onlinecourses.nptel.ac.in/noc21_cs58/preview
- CMU 15-445 *Database Systems* (Andy Pavlo) — YouTube
- Book: Silberschatz, Korth, Sudarshan, *Database System Concepts*
- Practice: SQLBolt, pgexercises.com, PostgreSQL docs

## Practice / proof of understanding

Design a normalised schema for a small app, load sample data in PostgreSQL, write 25 queries, and prove one decomposition lossless.

## What your IITM course sheet says

### From the PDF: CS3700

**Official description:** The objective of the course is to impart knowledge about fundamental ideas and techniques of relational database  systems.

**Official syllabus (trimmed):**

> Introduction - General introduction to database systems; Database - DBMS disctinction, approaches to building a
>  database, data models, database management system, three-schema architecture of a database, challenges in
>  building a DBMS, various components of a DBMS.E/R Model - Conceptual data modeling - motivation, entities,
>  entity types, various types of attributes, relationships, relationship types, E/R diagram notation,
>  examples.Relational Data Model - Concept of relations, schema-instance distinction, keys, referential integrity and
>  foreign keys, relational algebra operators: selection, projection, cross product, various types of joins, division,
>  example queries, tuple relation calculus, converting the database specification in E/R notation to the relational
>  schema.SQL - Introduction, data definition in SQL, table, key and foreign key definitions, update behaviors.
>  Querying in SQL - basic select-from-where block and its semantics, nested queries - correlated and uncorrelated,
>  notion of aggregation, aggregation functions group by and having clauses, embedded SQL.Dependencies and
>  Normal forms - Importance of a good schema design, problems encountered with bad schema designs, motivation
>  for normal forms, dependency theory - functional dependencies, Armstrong's axioms for FD's, closure of a set of
>  FD's, minimal covers, definitions of 1NF, 2NF, 3NF and BCNF, decomposit

**Official textbooks:** 1. Ramez Elmasri and Shamkant B Navathe, Fundamentals of Database Systems, 6th Edition, Pearson, 2013

**Official references:** 1. A Silberschatz, H F Korth and S Sudarshan, Database System Concepts, 6th Edition, McGraw Hill, 2011.  2. H Garcia-Molina, J D Ullman, and Jennifer Widom, Database Systems-The Complete Book, Pearson Education,  2004.  3. Raghu Ramakrishnan and Johannes Gehrke, Database Management Systems, 3rd Edition, McGraw Hill, 2003.
