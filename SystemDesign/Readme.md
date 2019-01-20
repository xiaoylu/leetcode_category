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

* Consistent Hashing (both virtual server replicas and keys are mapped to a ring.)
    * determining a node on which a specific piece of data should reside on
    * minimising data movement when adding or removing nodes.

* Gossip Protocol – exchanging state information about themselves and a maximum of 3 other nodes they know about. Over a period of time state information about every node propagates throughout the cluster. The gossip protocol facilitates failure detection.

Google Project
---

* Hadoop <--> Mapreduce
* Hadoop Distributed File System (HDFS) <--> Google File System
* Hbase <--> Bigtable

Long Term Storage: Hive

Fan-out Write/Read (Push or Pull)
---
http://massivetechinterview.blogspot.com/2015/06/itint5.html


同样是timeline, twitter用fan-out-write（将new feed直接写到follower的timeline里），而Facebook却用fan-out-read（在读的时候实时抓取相关用户的feeds并merge/rank)

Twitter has apparently seen great performance improvements by disabling fanout for high profile users and instead loading their tweets during reads (pull).



