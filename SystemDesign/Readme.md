System Design Notes
===

Sharding
---
Pros:
* Split the burden of data storage

Cons:
* send requests to all data resources to get the responses

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
