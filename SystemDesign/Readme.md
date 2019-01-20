System Design Notes
===

Sharding
---
Pros:
* Split the burden of data storage
* ID generation is simplistic

Cons:
* send requests to all data resources to get the responses
* since the tables could be loaded into separate partitions sql joins would not work
* 


ACID
---
* Atomicity: either succeeds completely, or fails completely
* Consistentcy: valid transactions
* Isolation: concurrency control
* Durability: power outage

Consistency:
---
* Eventual consistency: eventually the system converges to the same state

Choices of NoSQL
---
HBase: 
* Frequent writes get cached and write once buffer is full (out-performs SQL and document-based NoSQL like MongoDB)

Cassendra:
* Wide-column data

CAP:
http://blog.nahurst.com/visual-guide-to-nosql-systems
* CA: RDBMS
* CP: BigTable, HBase, Redis, MongoDB
* AP: Dynamo, Cassendra
  * Dynamo is a key value store where cassandra is a column wide store

Cassendra
---
A must read for developers 
http://abiasforaction.net/cassandra-architecture/

Distributed Hash Table
---
Virtual Server Replicas and Keys are distributed on a Ring.

Google Project
---

* Hadoop <--> Mapreduce
* Hadoop Distributed File System (HDFS) <--> Google File System
* Hbase <--> Bigtable

Long Term Storage: Hive

Fan-out Write/Read
---
同样是timeline, twitter用fan-out-write（将new feed直接写到follower的timeline里），而Facebook却用fan-out-read（在读的时候实时抓取相关用户的feeds并merge/rank)。why？我的理解是，这两个timeline是有本质不同的，twitter的timeline是比较传统的按时间顺序呈现你follow的人的feeds，而Facebook的news feeds更像一个timeline + social graph search, 不仅有好友最新的post，还有基于social graph搜索之后的相关结果（可能是你朋友的朋友，或者朋友赞过的照片，等），并且可能会有个性化结果。回归到fan-out-read/fan-out-write一个本质区别是，如果request/answer pattern越不确定（比如web search就是一个极端例子，query pattern趋近无限），或者answer features需要agile的变化，那么用fan-out-read越好（read所有candidate后，灵活的组织结果）。 



