# CS6847 — Cloud Computing + Distributed Computing

| | |
|---|---|
| Tier | B |
| Phase (order) | 7 |
| Do this first | CS3500, CS3205, CS3700 |
| Estimated effort | 12 weeks |
| Unlocks | CS6440, CS6851 |

## Roadmap

1. Virtualisation, containers, orchestration.
2. Distributed systems: time, consensus (Raft), replication, fault tolerance.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [MIT 6.824 Distributed Systems (Spring 2020)](https://www.youtube.com/playlist?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB) (20 videos). MIT 6.824 *Distributed Systems* (Spring 2020, Robert Morris, official course channel): MapReduce, Raft, GFS, Spanner. Do the Go labs.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Distributed Systems lecture series](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB) (23 videos). Martin Kleppmann *Distributed Systems*: short, rigorous, free lecture notes.
- [Cloud Computing and Distributed Systems - Prof. Rajiv Misra](https://www.youtube.com/playlist?list=PLFW6lRTa1g82dte3YD_7-GoZXcBiK6K9G) (21 videos). NPTEL *Cloud Computing and Distributed Systems* (Rajiv Misra, IIT Patna).
- [Big Data Computing.:-Prof. Rajiv Misra](https://www.youtube.com/playlist?list=PLFW6lRTa1g813IyYHLRP_bWJEKQDeEcSP) (35 videos). NPTEL *Big Data Computing* (Rajiv Misra): Hadoop/Spark/Kafka.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=1)–[2](https://www.youtube.com/watch?v=gA4YXUJX7t8&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=2) | Intro, RPC, threads in Go. Lab 1: MapReduce (pdos.csail.mit.edu/6.824). |
| 2 | [3](https://www.youtube.com/watch?v=EpIgvowZr00&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=3)–[4](https://www.youtube.com/watch?v=M_teob23ZzY&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=4) | GFS, primary-backup replication. |
| 3-4 | [5](https://www.youtube.com/watch?v=UzzcUS2OHqo&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=5)–[7](https://www.youtube.com/watch?v=4r8Mz3MMivY&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=7) | Raft. Lab 2: implement Raft (the hardest and most valuable part). |
| 5 | [8](https://www.youtube.com/watch?v=pbmyrNjzdDk&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=8)–[11](https://www.youtube.com/watch?v=-pKNCjUhPjQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=11) | ZooKeeper, CRAQ, Aurora, Frangipani. Lab 3: fault-tolerant key/value store on Raft. |
| 6 | [12](https://www.youtube.com/watch?v=aDp99WDIM_4&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=12)–[14](https://www.youtube.com/watch?v=Cw6Nj2evjSs&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=14) | Distributed transactions, Spanner, optimistic concurrency control. |
| 7 | [15](https://www.youtube.com/watch?v=mzIoSW-cInA&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=15)–[20](https://www.youtube.com/watch?v=XvXK_vZ0BNw&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=20) | Spark, Memcache at Facebook, causal consistency, certificate transparency, Bitcoin, Blockstack. |

<details>
<summary>All lectures in <i>MIT 6.824 Distributed Systems (Spring 2020)</i> (20 videos)</summary>

1. [Lecture 1: Introduction](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=1)
2. [Lecture 2: RPC and Threads](https://www.youtube.com/watch?v=gA4YXUJX7t8&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=2)
3. [Lecture 3: GFS](https://www.youtube.com/watch?v=EpIgvowZr00&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=3)
4. [Lecture 4: Primary-Backup Replication](https://www.youtube.com/watch?v=M_teob23ZzY&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=4)
5. [Lecture 5: Go, Threads, and Raft](https://www.youtube.com/watch?v=UzzcUS2OHqo&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=5)
6. [Lecture 6: Fault Tolerance: Raft (1)](https://www.youtube.com/watch?v=64Zp3tzNbpE&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=6)
7. [Lecture 7: Fault Tolerance: Raft (2)](https://www.youtube.com/watch?v=4r8Mz3MMivY&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=7)
8. [Lecture 8: Zookeeper](https://www.youtube.com/watch?v=pbmyrNjzdDk&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=8)
9. [Lecture 9: More Replication, CRAQ](https://www.youtube.com/watch?v=IXHzbCuADt0&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=9)
10. [Lecture 10: Cloud Replicated DB, Aurora](https://www.youtube.com/watch?v=jJSh54J1s5o&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=10)
11. [Lecture 11: Cache Consistency: Frangipani](https://www.youtube.com/watch?v=-pKNCjUhPjQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=11)
12. [Lecture 12: Distributed Transactions](https://www.youtube.com/watch?v=aDp99WDIM_4&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=12)
13. [Lecture 13: Spanner](https://www.youtube.com/watch?v=4eW5SWBi7vs&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=13)
14. [Lecture 14: Optimistic Concurrency Control](https://www.youtube.com/watch?v=Cw6Nj2evjSs&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=14)
15. [Lecture 15: Big Data: Spark](https://www.youtube.com/watch?v=mzIoSW-cInA&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=15)
16. [Lecture 16: Cache Consistency: Memcached at Facebook](https://www.youtube.com/watch?v=Myp8z0ybdzM&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=16)
17. [Lecture 17: COPS, Causal Consistency](https://www.youtube.com/watch?v=fR_NB714EAI&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=17)
18. [Lecture 18: Fork Consistency, Certificate Transparency](https://www.youtube.com/watch?v=UKdLJ7-0iFM&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=18)
19. [Lecture 19: Bitcoin](https://www.youtube.com/watch?v=K_euhRou98Y&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=19)
20. [Lecture 20: Blockstack](https://www.youtube.com/watch?v=XvXK_vZ0BNw&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=20)

</details>


## Books, notes and websites

- MIT 6.5840 (formerly 6.824) *Distributed Systems* labs + lectures
- Book: Kleppmann, *Designing Data-Intensive Applications*
- Docker and Kubernetes official tutorials

## Practice / proof of understanding

Implement Raft (MIT 6.5840 lab 2) and deploy a 3-service app with Docker Compose.

## What your IITM course sheet says

### From the PDF: CS6847

**Official description:** NIL

**Official syllabus (trimmed):**

> Introduction to Cloud Computing: Cluster Computing, Grid Computing, Utility Computing, Cloud Computing,-
>  Concepts of virtualization, Pay-as-you go model
>  Basics of Service-oriented Computing: Web services, Web Service Description Languages, SOAP and REST
>  services, service composition, service match-making, service mashups
>  Public Clouds: concepts of IaaS, PaaS, SaaS, Amazon case study: EC2, S3, Amazon SQS, Simple DB, etc.,
>  cloud security
>  Private Clouds: Eucalyptus architecture, Device clouds, Internet of Things (IOT)
>  Hybrid clouds: issues with data-intensive applications, cloud bursting algorithms
>  Working with Big Data: Big Table, Google File System, Hadoop Distributed File System (HDFS), Map-reduce on
>  Hadoop, Elastic Map-reduce in Amazon, Iterative machine-learning applications with Mahout, Iterative/Recursive
>  applications with Generate-Map-Reduce, Graph applications, Dryad, DryadLINQ, HBase, Pig, Hive, etc., key-value
>  stores with relaxed consistency models – Amazon Dynamo, Virat

**Official textbooks:** NIL

**Official references:** 1. Hadoop: The Definitive Guide, O’Reilly, 2009  2. Grid Computing – A research Monograph, D. Janakiram, McGraw-Hill  3. Selected research papers

### From the PDF: CS6440

**Official description:** Notion of time in distributed systems; Logical clocks, vector clocks,  bitmatrix clocks, virtual clocks; Shared memory vs. message passing;  Consensus; Byzantine agreement, agreement protocols, commit  protocols; Mutual exclusion in distributed systems; Distributed algorithms;  2, 3 tier c/s architectures; Languages for distributed computing; Linda,  CSP, DP, SR; Distributed operating systems; Distributed file systems;  Distributed databases; Distributed objects -DCOM, CORBA, Java.

**Official textbooks:** NIL
