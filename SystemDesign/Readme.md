System Design Notes
===

Sharding
---
Pros:
* 
Cons:
* Requests to all data resources to get all the responses

Choices of NoSQL
---
HBase: 
* Frequent writes get cached and write once buffer is full (out-performs SQL and document-based NoSQL like MongoDB)

Cassendra:
* Wide-column data
