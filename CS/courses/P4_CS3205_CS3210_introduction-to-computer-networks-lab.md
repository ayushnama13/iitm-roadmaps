# CS3205+CS3210 — Introduction to Computer Networks (+ lab)

| | |
|---|---|
| Tier | A |
| Phase (order) | 4 |
| Do this first | CS2705, CS3500 helps |
| Estimated effort | 12 weeks |
| Unlocks | CS6500, CS6048, CS6847 |

## Roadmap

1. Layered model, application layer (HTTP, DNS), sockets.
2. Transport: TCP, UDP, congestion control.
3. Network layer: IP, routing; link layer: Ethernet, ARP.
4. Hands-on: Wireshark captures, and a socket-based client/server.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Computer Networks and Internet Protocol](https://www.youtube.com/playlist?list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up) (61 videos). NPTEL *Computer Networks and Internet Protocol* (Soumya Kanti Ghosh & Sandip Chakraborty, IIT Kharagpur): has socket-programming demos.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Computer Networks](https://www.youtube.com/playlist?list=PLZ2ps__7DhBaKdpWeU8cn9czsZVCRUT0s) (34 videos). IIT Madras BS *Computer Networks*.
- [Computer Networking: A Top-Down Approach - Jim Kurose](https://www.youtube.com/playlist?list=PL1ya5dD_M8uX-BLUF1FEvUNsYWQL5_l0O) (47 videos). Jim Kurose's own lectures for *Computer Networking: A Top-Down Approach* (collected by a viewer): matches the course textbook chapter by chapter.

### ⚡ Short videos for intuition and revision

- [Computer Networks](https://www.youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx) (100+ videos). Neso Academy *Computer Networks*: subnetting/addressing drills.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [2](https://www.youtube.com/watch?v=lnU-Zw3NEEQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=2)–[6](https://www.youtube.com/watch?v=5AHp0f0489E&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=6) | History, circuit vs packet switching, the protocol stack. Install Wireshark and capture your own traffic. |
| 2 | [16](https://www.youtube.com/watch?v=JsUzPkOxZfA&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=16)–[20](https://www.youtube.com/watch?v=YkE2ps9IcUQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=20) | Application layer: DNS, FTP, HTTP, SMTP. Use dig/curl -v; write a tiny HTTP server in Python with raw sockets. |
| 3-4 | [7](https://www.youtube.com/watch?v=8-3CSAkscYU&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=7)–[15](https://www.youtube.com/watch?v=c8Wv3b7f9XY&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=15), [21](https://www.youtube.com/watch?v=VUdfS70puWI&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=21)–[24](https://www.youtube.com/watch?v=f1y25BfOH9I&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=24) | Transport: reliability, sliding window, TCP connection/flow/congestion control, UDP. (The playlist order is shuffled; follow the lecture numbers in the titles.) Do the Kurose Wireshark TCP lab. |
| 5 | [25](https://www.youtube.com/watch?v=x7obJLN7FcQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=25)–[26](https://www.youtube.com/watch?v=JExfKvUgrtI&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=26) | Socket programming. Build a multi-client chat server in C or Python. |
| 6-7 | [27](https://www.youtube.com/watch?v=aP346youQOk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=27)–[42](https://www.youtube.com/watch?v=9HgkQN7u7-8&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=42) | Network layer: IPv4/CIDR/NAT, IPv6, QoS, routing tables, intra/inter-domain routing, BGP, routers. Subnetting exercises; simulate Dijkstra/distance-vector. |
| 8 | [43](https://www.youtube.com/watch?v=Bc-qdRPqY_o&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=43)–[46](https://www.youtube.com/watch?v=MsJU8gZbDfk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=46) | Software-defined networking. Try Mininet. |
| 9 | [47](https://www.youtube.com/watch?v=rGWPOm3ectk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=47)–[56](https://www.youtube.com/watch?v=i6wlR8dmw1k&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=56), [59](https://www.youtube.com/watch?v=_HoeO1jw1Lo&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=59) | Data link and physical layer: Ethernet, error control, ARP/DHCP, VLANs, wireless LANs. |
| 10 | [57](https://www.youtube.com/watch?v=P1uAtSaHfHU&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=57)–[58](https://www.youtube.com/watch?v=Mfwu4ZwAvos&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=58), [60](https://www.youtube.com/watch?v=gyCj3Psau-g&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=60) | Network security overview. Then TLS from Kurose ch. 8. |

<details>
<summary>All lectures in <i>Computer Networks and Internet Protocol</i> (61 videos)</summary>

1. [Prof  Soumya Kanti Ghosh & Prof  Sandip Chakraborty](https://www.youtube.com/watch?v=O--rkQNKqls&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=1)
2. [Lecture 1:Introduction to Computer Networks – A brief history](https://www.youtube.com/watch?v=lnU-Zw3NEEQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=2)
3. [Lecture 2:Data Networks – from Circuit Switching Network to Packet Switching Network](https://www.youtube.com/watch?v=29Qdz0FmvmQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=3)
4. [Lecture 3:Network Protocol Stack](https://www.youtube.com/watch?v=b6f9vh3cd6w&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=4)
5. [Lecture 4:Services at the Different Layers of the Protocol Stack](https://www.youtube.com/watch?v=8BK70UDgyrc&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=5)
6. [Lecture 5:Application Layer I – Different Protocols at the Application Layer](https://www.youtube.com/watch?v=5AHp0f0489E&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=6)
7. [Lecture 11:Transport Layer I – Services](https://www.youtube.com/watch?v=8-3CSAkscYU&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=7)
8. [Lecture 12:Transport Layer II - Connection](https://www.youtube.com/watch?v=fBPDLGwfSUM&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=8)
9. [Lecture 14:Transport Layer IV – Reliability](https://www.youtube.com/watch?v=qclg6FY-FGM&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=9)
10. [Lecture 16:Transport Layer Performance](https://www.youtube.com/watch?v=bKHRbqwkMkg&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=10)
11. [Lecture 17:Buffer Management and Congestion Control](https://www.youtube.com/watch?v=b-nCA0tZU-0&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=11)
12. [Lecture 18:Transport Layer Primitives](https://www.youtube.com/watch?v=EqzDTO9tdqs&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=12)
13. [Lecture 19:Transmission Control Protocol I – Basics](https://www.youtube.com/watch?v=5ex1s4lURto&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=13)
14. [Lecture 20:Transmission Control Protocol II – Connections](https://www.youtube.com/watch?v=xS202cWCc2Q&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=14)
15. [Lecture 13:Transport Layer II - Connection (Contd.)](https://www.youtube.com/watch?v=c8Wv3b7f9XY&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=15)
16. [Lecture 6:Application Layer II – Domain Name Systems](https://www.youtube.com/watch?v=JsUzPkOxZfA&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=16)
17. [Lecture 7:Application Layer III – File Transfer (FTP)](https://www.youtube.com/watch?v=6uzEsZNUfmk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=17)
18. [Lecture 8:Application Layer IV – Hypertext Transfer Protocol (HTTP), HTML, Telnet  Part-I](https://www.youtube.com/watch?v=qZlMS4yJM-E&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=18)
19. [Lecture 9:Application Layer IV – Hypertext Transfer Protocol (HTTP), HTML, Telnet   Part-II](https://www.youtube.com/watch?v=rNhTsdxHeXI&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=19)
20. [Lecture 10:Application Layer V – Internet Mail Transfer (SMTP), Network Management (SNMP)](https://www.youtube.com/watch?v=YkE2ps9IcUQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=20)
21. [Lecture 15: Transport Layer V  – Sliding Window Protocols](https://www.youtube.com/watch?v=VUdfS70puWI&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=21)
22. [Lecture 21: Transmission Control Protocol III – Flow Control](https://www.youtube.com/watch?v=8NxJGHXDOGc&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=22)
23. [Lecture 22: Transmission Control Protocol IV – Congestion Control](https://www.youtube.com/watch?v=SHO9eeWxPxY&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=23)
24. [Lecture 23: User Datagram Protocol](https://www.youtube.com/watch?v=f1y25BfOH9I&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=24)
25. [Lecture 24 : Socket Programming – I](https://www.youtube.com/watch?v=x7obJLN7FcQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=25)
26. [Lecture 25: Socket Programming – II](https://www.youtube.com/watch?v=JExfKvUgrtI&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=26)
27. [Lecture 26: Network Layer I – Introduction](https://www.youtube.com/watch?v=aP346youQOk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=27)
28. [Lecture 27: IP Addressing (IPv4) I – Classful addressing](https://www.youtube.com/watch?v=5vbPS-KnhvI&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=28)
29. [Lecture 28: IP Addressing (IPv4) II - CIDR](https://www.youtube.com/watch?v=H-R3KUPX1v4&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=29)
30. [Lecture 29: IP Addressing (IPv4) III – Network Address Translation (NAT)](https://www.youtube.com/watch?v=_MZbwHyE0Ck&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=30)
31. [Lecture 30: IPv6 Addressing](https://www.youtube.com/watch?v=FkaFr3cpg6U&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=31)
32. [Lecture 31: Internet QoS - I (What is QoS)](https://www.youtube.com/watch?v=WM1OXVMetkE&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=32)
33. [Lecture 32: Internet QoS - II (Basic QoS Architecture)](https://www.youtube.com/watch?v=Y9CxqQcMydg&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=33)
34. [Lecture 33: Internet QoS - III (Traffic Policing and Traffic Shaping)](https://www.youtube.com/watch?v=TlB_ML2zAD8&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=34)
35. [Lecture 34: Internet QoS - IV (Traffic Scheduling)](https://www.youtube.com/watch?v=fbZTrHN2oXQ&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=35)
36. [Lecture 35: Internet QoS - V (Integrated and Differentiated Service Architecture)](https://www.youtube.com/watch?v=utvwelCCfas&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=36)
37. [Lecture 36: IP Routing Table](https://www.youtube.com/watch?v=IfzGf4kI2a8&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=37)
38. [Lecture 37: Routing in the Internet I – Intra-domain routing](https://www.youtube.com/watch?v=n9VmkVnc0rI&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=38)
39. [Lecture 38: Routing in the Internet II -  Routing protocols](https://www.youtube.com/watch?v=yQBuCHG5co0&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=39)
40. [Lecture 39: Routing in the Internet III – Inter-domain Routing](https://www.youtube.com/watch?v=U7Stg2reaLg&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=40)
41. [Lecture 40: Routing in the Internet IV – Border Gateway Protocol](https://www.youtube.com/watch?v=J0KNWNm_m7U&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=41)
42. [Lecture 41 : IP Routers](https://www.youtube.com/watch?v=9HgkQN7u7-8&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=42)
43. [Lecture 42 : IP Routers Demo](https://www.youtube.com/watch?v=Bc-qdRPqY_o&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=43)
44. [Lecture 43 : Software Defined Networking - I (Basics)](https://www.youtube.com/watch?v=CaukSKg_sI0&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=44)
45. [Lecture 44 : Software Defined Networking - II (Open Flow)](https://www.youtube.com/watch?v=l3E-C1j-SJg&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=45)
46. [Lecture 45 : Software Defined Networking - III (Demo)](https://www.youtube.com/watch?v=MsJU8gZbDfk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=46)
47. [Lecture 46: Data Link Layer - Overview](https://www.youtube.com/watch?v=rGWPOm3ectk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=47)
48. [Lecture 47: Data Link Layer - Basic Concept](https://www.youtube.com/watch?v=jMvA9mSIwtk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=48)
49. [Lecture 48: Data Link Layer - Ethernet](https://www.youtube.com/watch?v=WXiGbQa-5F4&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=49)
50. [Lecture 49: Data Link Layer - Ethernet (Contd.)](https://www.youtube.com/watch?v=GmrbL1-7qyU&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=50)
51. [Lecture 50: Data Link Layer - Flow and Error Control](https://www.youtube.com/watch?v=TrgZ7_L525w&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=51)
52. [Lecture 51: ARP-RAPP-BOOTP-DHCP](https://www.youtube.com/watch?v=JkqgkN_j6Lo&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=52)
53. [Lecture 52: ARP-RAPP-BOOTP-DHCP(Contd.)](https://www.youtube.com/watch?v=8LeqAH_ppsA&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=53)
54. [Lecture 54: Wireless LANs](https://www.youtube.com/watch?v=6SWBxiPeSqk&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=54)
55. [Lecture 53: Connectiing LANs,VLAN](https://www.youtube.com/watch?v=zVdyKTQyvVY&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=55)
56. [Lecture 56:Layer 1: Physical Layer-II](https://www.youtube.com/watch?v=i6wlR8dmw1k&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=56)
57. [Lecture 58:Network Security-Overview](https://www.youtube.com/watch?v=P1uAtSaHfHU&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=57)
58. [Lecture 59:Network Security-III(TCP?IPSecurity)](https://www.youtube.com/watch?v=Mfwu4ZwAvos&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=58)
59. [Lecture 55: Layer 1: Physical Layer](https://www.youtube.com/watch?v=_HoeO1jw1Lo&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=59)
60. [Lecture 60: Network Security-III(TCP/IP Security)](https://www.youtube.com/watch?v=gyCj3Psau-g&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=60)
61. [mod12Lec57](https://www.youtube.com/watch?v=erynt60b6LU&list=PLbRMhDVUMngf-peFloB7kyiA40EptH1up&index=61)

</details>


## Books, notes and websites

- Book: Kurose & Ross, *Computer Networking: A Top-Down Approach* (listed as the course text) + its free Wireshark labs
- ✅ NPTEL *Computer Networks* (Hema A Murthy, IIT Madras) — nptel.ac.in/courses/106106091; alternatives: IIT Kharagpur 106105081 (Sujoy Ghosh), 106105080 (Ajit Pal)
- Stanford CS144 *Introduction to Computer Networking*
- Beej's Guide to Network Programming — beej.us/guide/bgnet
- Book: Peterson & Davie, *Computer Networks: A Systems Approach* (free online)

## Practice / proof of understanding

Write a TCP echo server and a multi-client chat server in C; capture and annotate a TCP handshake and an HTTP request in Wireshark.

## What your IITM course sheet says

### From the PDF: CS3205

**Official description:** Concepts and implementation of computer networks; architecture,  protocol layers, inter-networking and addressing; network application development.

**Official syllabus (trimmed):**

> This course builds a practical and analytical foundation in computer networking, from layered Internet design and
>  transport behavior to hands-on packet capture, measurement, debugging, and socket-based application
>  development.

**Official textbooks:** 1. (Any one of these will suffice)  2. Kurose and Ross, "Computer Networking - A top-down approach", Seventh Edition, Pearson, 2017.  3. Andrew S. Tanenbaum, "Computer Networks", Fifth Edition, Pearson Education India, 2013.  4. Peterson and Davie, "Computer Networks, A Systems Approach'', 5th ed., Elsevier, 2011.

**Official references:** 1. Ying-Dar Liu, Ren-Hung Hwang, Fred Baker, "Computer Networks: An Open Source Approach", McGraw-Hill,  2011.  2. W. Richard Stevens, Bill Fenner and Andrew Rudoff, "Unix Network Programming", Volumes 1 and 2, Third  Edition, Addison-Wesley Professional, 2003.  3. Michael Donahoo, Ken Calvert, Pocket Guide to TCP/IP Socket Programming in C, Morgan Kaufmann Series in  Networking, 2000.

### From the PDF: CS3210

**Official description:** Configuration of networking in Linux using ifconfig, route, bind, etc.; configuration of firewall and masquerading in  Linux; network trouble-shooting and performance monitoring using netstat, ping, tcpdump, etc.  Configuration and performance measurement of commonly-used Linux servers such as E-Mail (sendmail,  pop3/imap) and Web (Apache).  Socket programming - TCP and UDP, peer-to-peer applications; reliable communications using unreliable  datagrams; client-server using RPC; concurrent servers using threads or processes.

**Official textbooks:** NIL

**Official references:** 1. "Linux Network Administrators Guide": http://tldp.org/LDP/nag2/index.html.  2. W.R. Stevens, "Unix Network Programming, Vol 1", 2nd ed., Prentice-Hall Inc., 1998.
