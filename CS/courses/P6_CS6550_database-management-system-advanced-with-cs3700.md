# CS6550 — Database Management System (advanced, with CS3700)

| | |
|---|---|
| Tier | B |
| Phase (order) | 6 |
| Do this first | CS3700 |
| Estimated effort | 10-12 weeks |
| Unlocks | CS6510, CS5830 |

## Roadmap

1. Query processing and optimisation, indexes (B+-tree, hash).
2. Transactions, concurrency control, recovery (ARIES).

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [CMU Advanced Database Systems (15-721 / Spring 2024)](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ) (22 videos). CMU 15-721 *Advanced Database Systems* (Spring 2024, Andy Pavlo): modern OLAP/column-store internals.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [CMU Intro to Database Systems (15-445/645 - Fall 2025)](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYMAgsGH-GtY5rJYZ6zjsd5) (25 videos). CMU 15-445 Fall 2025: the intro course if you skipped it.
- [Distributed Systems lecture series](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB) (23 videos). Martin Kleppmann *Distributed Systems* (Cambridge): replication + consistency for distributed databases.

### ⚡ Short videos for intuition and revision

- [Designing Data Intensive Applications](https://www.youtube.com/playlist?list=PLhgFs9q2EVg_rB-XT1zaJ3k9z0KVGrR2h) (11 videos). *Designing Data-Intensive Applications* chapter walkthroughs (Ben Dicken).

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=NLycrsJ1jI8&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=1)–[4](https://www.youtube.com/watch?v=h3EOs7GH7hM&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=4) | Modern OLAP systems, columnar storage and encoding. Read the Parquet format docs. |
| 2 | [5](https://www.youtube.com/watch?v=tsbbwiWw9VE&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=5)–[9](https://www.youtube.com/watch?v=VZjzKVfU46k&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=9) | Query execution, vectorisation with SIMD, JIT compilation, scheduling. |
| 3 | [10](https://www.youtube.com/watch?v=S40K8iGa8Ek&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=10)–[12](https://www.youtube.com/watch?v=FaS-E-oq-X4&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=12) | Parallel hash joins, worst-case optimal joins, UDF optimisation. |
| 4 | [13](https://www.youtube.com/watch?v=0tfDldfzlR8&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=13)–[16](https://www.youtube.com/watch?v=anVC4AJeXqw&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=16) | Networking protocols, query optimiser implementation. |
| 5 | [17](https://www.youtube.com/watch?v=VOZax1tbvxw&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=17)–[22](https://www.youtube.com/watch?v=T9-MM8oHzsM&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=22) | System case studies: BigQuery, Photon, Snowflake, DuckDB, Yellowbrick, Redshift. Read one paper per system; benchmark DuckDB vs Postgres on TPC-H. |

<details>
<summary>All lectures in <i>CMU Advanced Database Systems (15-721 / Spring 2024)</i> (22 videos)</summary>

1. [S2024 #00 - Course Overview & Logistics (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=NLycrsJ1jI8&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=1)
2. [S2024 #01 - Modern OLAP Database Systems (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=5J-I8Mj8tss&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=2)
3. [S2024 #02 - Data Formats & Encoding Part 1 (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=1hdynBJo3ew&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=3)
4. [S2024 #03 - Data Formats & Encoding Part 2 (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=h3EOs7GH7hM&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=4)
5. [S2024 #04 - Query Execution & Processing Part 1 (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=tsbbwiWw9VE&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=5)
6. [S2024 #05 - Query Execution & Processing Part 2 (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=et54i_Rplik&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=6)
7. [S2024 #06 - Vectorized Query Execution Using SIMD (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=yU1S8gwjGEw&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=7)
8. [S2024 #07 - JIT Query Compilation & Code Generation (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=UPQ53hM6AWE&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=8)
9. [S2024 #08 - Query Scheduling & Coordination (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=VZjzKVfU46k&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=9)
10. [S2024 #09 - Parallel Hash Join Algorithms (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=S40K8iGa8Ek&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=10)
11. [S2024 #10 - Multi-Way Join Algorithms / Worst-Case Optimal Joins (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=1aHT3KitTYo&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=11)
12. [S2024 #11 - User-Defined Function Optimizations (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=FaS-E-oq-X4&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=12)
13. [S2024 #12 - Database Networking Protocols (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=0tfDldfzlR8&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=13)
14. [S2024 #13 - Query Optimizer Implementation 1 (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=DwX0X8CyBSg&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=14)
15. [S2024 #14 - Query Optimizer Implementation 2 (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=B9gJa5ZLg8s&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=15)
16. [S2024 #15 - Query Optimizer Implementation 3 (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=anVC4AJeXqw&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=16)
17. [S2024 #17 - Google BigQuery / Dremel (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=VOZax1tbvxw&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=17)
18. [S2024 #18 - Databricks Photon / Spark SQL (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=PwnUf6_0H0k&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=18)
19. [S2024 #19 - Snowflake Data Warehouse Internals (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=NhWp1bTG0Cw&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=19)
20. [S2024 #20 - DuckDB Embedded Database System (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=4iD4h4sGLz4&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=20)
21. [S2024 #21 - Yellowbrick Data Warehouse System (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=hkTK6Auh5vE&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=21)
22. [S2024 #22 - Amazon Redshift Data Warehouse System (CMU Advanced Database Systems)](https://www.youtube.com/watch?v=T9-MM8oHzsM&list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ&index=22)

</details>


## Books, notes and websites

- CMU 15-445 / 15-721 lectures
- Book: *Designing Data-Intensive Applications* (Kleppmann)
- Book: Ramakrishnan & Gehrke

## Practice / proof of understanding

Build a toy key-value store with a B+-tree and a write-ahead log.

## What your IITM course sheet says

### From the PDF: CS6550

**Official description:** Need for database approach; data independence; data models;  hierarchical, network and relational; TMS architecture; network approach;  DBTG report, scheme and subscheme, currency, data manipulation  language; relational models; join and projection operations, relational  algebra and calculus, normalization, query languages, database  administrator, security and integrity considerations, compression  techniques.

**Official textbooks:** NIL
