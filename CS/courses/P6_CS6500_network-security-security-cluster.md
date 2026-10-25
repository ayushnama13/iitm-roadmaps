# CS6500 — Network Security / security cluster

| | |
|---|---|
| Tier | B |
| Phase (order) | 6 |
| Do this first | CS3205, CS1202 |
| Estimated effort | 10-12 weeks |
| Unlocks | CS6530, CS6570 |

## Roadmap

1. Cryptography basics, TLS, authentication, firewalls and attacks.
2. Secure systems engineering (CS6570) and applied crypto (CS6530) as follow-ups.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Computer - Cryptography and Network Security](https://www.youtube.com/playlist?list=PL71FE85723FD414D7) (41 videos). NPTEL *Cryptography and Network Security* (Debdeep Mukhopadhyay, IIT Kharagpur).

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Introduction to Cryptography Lectures](https://www.youtube.com/playlist?list=PL3boZvi-wmN6r4HUGUpRSk5uhEcTNfjSS) (27 videos). Christof Paar *Introduction to Cryptography* (official channel): the clearest crypto lecturer; uses his free-chapter textbook.
- [MIT 6.858 Computer Systems Security, Fall 2014](https://www.youtube.com/playlist?list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh) (22 videos). MIT 6.858 *Computer Systems Security* (Fall 2014, official OCW): buffer overflows, web security, sandboxing.
- [Information Security 5 Secure Systems Engineering | IIT Madras](https://www.youtube.com/playlist?list=PLyqSpQzTE6M-q0Xgn0icEHvUS7WQxvenv) (59 videos). NPTEL *Secure Systems Engineering* (Chester Rebeiro, IIT Madras): IITM's own systems security course.

### ⚡ Short videos for intuition and revision

- [Cryptography & Network Security](https://www.youtube.com/playlist?list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII) (83 videos). Neso Academy *Cryptography & Network Security*: short revision videos.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=Q-HugPvA7GQ&list=PL71FE85723FD414D7&index=1)–[9](https://www.youtube.com/watch?v=ihEJGRA0n2Q&list=PL71FE85723FD414D7&index=9) | Overview, number theory, probability, classical ciphers, Shannon's theory. Do Cryptopals set 1. |
| 2 | [10](https://www.youtube.com/watch?v=QbczPuEphUY&list=PL71FE85723FD414D7&index=10)–[18](https://www.youtube.com/watch?v=FJNAokhimfg&list=PL71FE85723FD414D7&index=18) | Block ciphers, DES, AES, linear and differential cryptanalysis, modes of operation. Break ECB in Cryptopals set 2. |
| 3 | [19](https://www.youtube.com/watch?v=BKkpEjbD8xM&list=PL71FE85723FD414D7&index=19)–[26](https://www.youtube.com/watch?v=lECb8emmN0M&list=PL71FE85723FD414D7&index=26) | Stream ciphers, pseudorandomness, hash functions, MACs. |
| 4 | [27](https://www.youtube.com/watch?v=t_dMrgAmDd0&list=PL71FE85723FD414D7&index=27)–[33](https://www.youtube.com/watch?v=2kfAga111ls&list=PL71FE85723FD414D7&index=33) | RSA, primality, factoring, discrete log, Diffie-Hellman, ElGamal. Implement textbook RSA and a small-exponent attack. |
| 5 | [34](https://www.youtube.com/watch?v=2RVLBUncHJk&list=PL71FE85723FD414D7&index=34)–[37](https://www.youtube.com/watch?v=j7Ngtl1cCpY&list=PL71FE85723FD414D7&index=37) | Elliptic curves, secret sharing. |
| 6 | [38](https://www.youtube.com/watch?v=TbRVJKDC1rM&list=PL71FE85723FD414D7&index=38)–[41](https://www.youtube.com/watch?v=P-JK4hBPBYI&list=PL71FE85723FD414D7&index=41) | Network protocols, system security, firewalls, IDS, side channels. Then web/TLS security from MIT 6.858 (alt); set up a firewall with nftables. |

<details>
<summary>All lectures in <i>Computer - Cryptography and Network Security</i> (41 videos)</summary>

1. [Introduction](https://www.youtube.com/watch?v=Q-HugPvA7GQ&list=PL71FE85723FD414D7&index=1)
2. [Overview on Modern Cryptography](https://www.youtube.com/watch?v=B-Xe7_mf2CY&list=PL71FE85723FD414D7&index=2)
3. [Introduction to Number Theory](https://www.youtube.com/watch?v=SCvtxjpVQms&list=PL71FE85723FD414D7&index=3)
4. [Probability and Information Theory](https://www.youtube.com/watch?v=dkAr9ThdSUU&list=PL71FE85723FD414D7&index=4)
5. [Classical Cryptosystems](https://www.youtube.com/watch?v=Vazi_07u_ck&list=PL71FE85723FD414D7&index=5)
6. [Cryptanalysis of Classical Ciphers](https://www.youtube.com/watch?v=x2ojdYS5FF8&list=PL71FE85723FD414D7&index=6)
7. [Shannons Theory](https://www.youtube.com/watch?v=VK5vv8fi2dY&list=PL71FE85723FD414D7&index=7)
8. [Shannons Theory (Contd...1)](https://www.youtube.com/watch?v=utRt_XCi1Hg&list=PL71FE85723FD414D7&index=8)
9. [Shannons Theory (Contd...2)](https://www.youtube.com/watch?v=ihEJGRA0n2Q&list=PL71FE85723FD414D7&index=9)
10. [Symmetric Key Ciphers](https://www.youtube.com/watch?v=QbczPuEphUY&list=PL71FE85723FD414D7&index=10)
11. [Block Cipher Standards (DES)](https://www.youtube.com/watch?v=eCAHcfA-2c8&list=PL71FE85723FD414D7&index=11)
12. [Block Cipher Standards (AES)](https://www.youtube.com/watch?v=fMJl01wbmWE&list=PL71FE85723FD414D7&index=12)
13. [Block Cipher Standards (AES) (Contd.)](https://www.youtube.com/watch?v=Xg7BhVHXqLo&list=PL71FE85723FD414D7&index=13)
14. [Linear Cryptanalysis](https://www.youtube.com/watch?v=93PD9CqcZTg&list=PL71FE85723FD414D7&index=14)
15. [Differential Cryptanalysis](https://www.youtube.com/watch?v=xcBqraHhcJU&list=PL71FE85723FD414D7&index=15)
16. [Few other Cryptanalytic Techniques](https://www.youtube.com/watch?v=nRTvB51PLHk&list=PL71FE85723FD414D7&index=16)
17. [Overview on S-Box Design Principles](https://www.youtube.com/watch?v=cJ7hmwHVwtc&list=PL71FE85723FD414D7&index=17)
18. [Modes of Operation of Block Ciphers](https://www.youtube.com/watch?v=FJNAokhimfg&list=PL71FE85723FD414D7&index=18)
19. [Stream Ciphers](https://www.youtube.com/watch?v=BKkpEjbD8xM&list=PL71FE85723FD414D7&index=19)
20. [Stream Ciphers (Contd...1)](https://www.youtube.com/watch?v=xWzFuDtfX_M&list=PL71FE85723FD414D7&index=20)
21. [Stream Ciphers (Contd...2)](https://www.youtube.com/watch?v=tPcTenIPQm4&list=PL71FE85723FD414D7&index=21)
22. [Pseudorandomness](https://www.youtube.com/watch?v=JYIdqzMYb60&list=PL71FE85723FD414D7&index=22)
23. [Cryptographic Hash Functions](https://www.youtube.com/watch?v=9XZ45SAnJnk&list=PL71FE85723FD414D7&index=23)
24. [Cryptographic Hash Functions (Contd...1)](https://www.youtube.com/watch?v=iMJ1qWKmZXE&list=PL71FE85723FD414D7&index=24)
25. [Cryptographic Hash Functions (Contd...2)](https://www.youtube.com/watch?v=BGos-qLuPVs&list=PL71FE85723FD414D7&index=25)
26. [Message Authentication Codes](https://www.youtube.com/watch?v=lECb8emmN0M&list=PL71FE85723FD414D7&index=26)
27. [More Number Theoretic Results](https://www.youtube.com/watch?v=t_dMrgAmDd0&list=PL71FE85723FD414D7&index=27)
28. [The RSA Cryptosystem](https://www.youtube.com/watch?v=cOpYHlqis3o&list=PL71FE85723FD414D7&index=28)
29. [Primality Testing](https://www.youtube.com/watch?v=_7F8tVeOgZE&list=PL71FE85723FD414D7&index=29)
30. [Factoring Algorithms](https://www.youtube.com/watch?v=9zvjv2Bf4Xk&list=PL71FE85723FD414D7&index=30)
31. [Some Comments on the Security of RSA](https://www.youtube.com/watch?v=sSbbEyV29PQ&list=PL71FE85723FD414D7&index=31)
32. [Discrete Logarithm Problem (DLP)](https://www.youtube.com/watch?v=1cun1fVnDNE&list=PL71FE85723FD414D7&index=32)
33. [The Diffie-Hellman Problem and Security of ElGamal Systems](https://www.youtube.com/watch?v=2kfAga111ls&list=PL71FE85723FD414D7&index=33)
34. [An Introduction to Elliptic Curve Cryptography](https://www.youtube.com/watch?v=2RVLBUncHJk&list=PL71FE85723FD414D7&index=34)
35. [Application of Elliptic Curves to Cryptography](https://www.youtube.com/watch?v=keL8Gb38pVw&list=PL71FE85723FD414D7&index=35)
36. [Implementation of Elliptic Curve Cryptography](https://www.youtube.com/watch?v=_BCYCNYgXm8&list=PL71FE85723FD414D7&index=36)
37. [Secret Sharing Schemes](https://www.youtube.com/watch?v=j7Ngtl1cCpY&list=PL71FE85723FD414D7&index=37)
38. [A Tutorial on Network Protocols](https://www.youtube.com/watch?v=TbRVJKDC1rM&list=PL71FE85723FD414D7&index=38)
39. [System Security](https://www.youtube.com/watch?v=GqLKpi7k_BQ&list=PL71FE85723FD414D7&index=39)
40. [Firewalls and Intrusion Detection Systems](https://www.youtube.com/watch?v=2YGUvopGkQc&list=PL71FE85723FD414D7&index=40)
41. [Side Channel Analysis of Cryptographic Implementations](https://www.youtube.com/watch?v=P-JK4hBPBYI&list=PL71FE85723FD414D7&index=41)

</details>


## Books, notes and websites

- Book: Boneh & Shoup, *A Graduate Course in Applied Cryptography* (free)
- Stanford Cryptography I (Dan Boneh)
- Book: Katz & Lindell, *Introduction to Modern Cryptography*
- cryptopals.com, picoCTF, OverTheWire

## Practice / proof of understanding

Complete cryptopals sets 1-2 and 10 picoCTF challenges.

## What your IITM course sheet says

### From the PDF: CS6500

**Official description:** Objectives: The objective of this course is to teach the concepts of securing computer network protocols, based on  the application of cryptography techniques.

**Official syllabus (trimmed):**

> 1. Basics of cryptography, including conventional and public-key cryptography, hash functions, authentication, and
>  digital signatures. (4 hrs)
>  2. Key Management and Distribution: Symmetric Key Distribution, Distribution of Public Keys, X.509 Certificates,
>  Public-Key Infrastructure. (2 hrs)
>  3. User Authentication: Remote User-Authentication Principles, Remote User-Authentication Using Symmetric
>  Encryption, Kerberos Systems, Remote User Authentication Using Asymmetric Encryption. (2 hrs)
>  4. Malicious Software: Viruses, Worms, System Corruption, Attack Agents, Information Theft — Keyloggers,
>  Phishing, Spyware Payload Stealthing, Backdoors, Rootkits, Distributed Denial of Service
>  Attacks. (4 hrs)
>  5. Network Access Control: Network Access Control, Extensible Authentication Protocol, IEEE 802.1X Port-Based
>  Network Access Control. (3 hrs)
>  6. IP Security: IP Security Overview, IP Security Policy, Encapsulating Security Payload, Combining Security
>  Associations, Internet Key Exchange (IKE). (5 hrs)
>  7. Transport-Level Security: Web Security Considerations, Secure Sockets Layer, Transport Layer Security,
>  HTTPS standard, Secure Shell (SSH) application. (4 hrs)
>  8. Electronic Mail Security: Pretty Good Privacy, S/MIME, DomainKeys Identified Mail. (4 hrs)
>  9. Wireless Network Security: Mobile Device Security, IEEE 802.11i Wireless LAN Security. (4 hrs)
>  10. Firewalls and Intrusi

**Official textbooks:** 1. Cryptography and Network Security: Principles and Practice, 6th Edition, William Stallings, 2014, Pearson,  ISBN13: 9780133354690.

**Official references:** 1. Network Security: Private Communications in a Public World, M. Speciner, R. Perlman, C. Kaufman, Prentice  Hall, 2002.  2. Linux iptables Pocket Reference, Gregor N. Purdy, O'Reilly, 2004, ISBN-13: 978-0596005696.  3. Linux Firewalls, by Michael Rash, No Starch Press, October 2007, ISBN: 978-1-59327-141-1.  4. Network Security, Firewalls And VPNs, J. Michael Stewart, Jones & Bartlett Learning, 

### From the PDF: CS6530

**Official description:** The objectives of the course include learning the basic principles of applied cryptography and the commonly used  cryptographic algorithms for encryption, message authentication and integrity, and digital signatures.

**Official syllabus (trimmed):**

> Unit 1:
>  NUMBER THEORY BASICS: Modular arithmetic, primes, GCD and Chinese reminder theorems.
>  BLOCK CIPHERS: DES, AES; ECB, CBC, OFB,CFB, CTR and GCM modes, Double and triple encryptions.
>  STREAM CIPHERS: Encryption and decryption with Stream ciphers, Shift-register based stream ciphers,
>  Currently used Stream Ciphers.
>  Unit 2:
>  PUBLIC KEY CRYPTOGRAPHY: RSA, ElGamal, Rabins encryption schemes, Diffe-Hellman Key exchange,
>  practical digital signatures.
>  ELLIPTIC CURVE CRYPTOLOGY: definitions, group properties and basic algorithms for group operations.
>  Unit 3:
>  HASH FUNCTIONS: oneway, collision resistant, preimage resistant HASH functions, Real-world examples.
>  Random Number Generation and Secret Sharing.
>  MESSAGE AUTHENTICATION CODES: MAC from Hash functions, MAC from block ciphers.
>  KEY ESTABLISHMENT PROTOCOLS: Diffie-Hellman Protocol, Man-in-the-middle Attack, certificates, Public Key
>  Infrastructure and PKI based crypto systems.

**Official textbooks:** 1. Christof Paar, Jan Pelzl, Understanding Cryptography, A text book for students and practitioners, Springer  Verlag, India, 2010 { INDIAN EDITION}  2. Alfred Menezes. et al, Handbook of Applied Cryptography, CRC Press, USA. { Entire book available for free  download in PDF form from authors homepage}  3. William Stallings, “Cryptography and Network Security”, Pearson, 2014.

**Official references:** None.

### From the PDF: CS6111

**Official description:** 1. Build a solid mathematical basis to understand foundations of cryptography  2. Formally understand the notions related to security authentication and privacy.  3. Provide a rigorous treatment of the emerging and key subject subarea of CSE - security.

**Official textbooks:** Oded Goldreich, The Foundations of Cryptography: VOL 1 Cambridge university Press, USA. 2001.  Oded Goldreich, The Foundations of Cryptography: VOL 2 Cambridge university Press, USA. 2004.  ( Indian print for both volumes are available).

**Official references:** J.Katz, Y.Lindell, Introduction to Modern Cryptography, Chapman Hall, USA 2007.  Wen Bo Mao, Modern cryptography - Theory and practice, Prentice Hall, USA, 2003 ( Indian edition available)

### From the PDF: NUS180

_The course sheet has no syllabus text for this course; the plan below is based on the standard content of this subject._
