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



