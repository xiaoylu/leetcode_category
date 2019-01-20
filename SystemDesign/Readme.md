System Design Notes
===

Template
===
* Requirements and Goals of the System
    * Write Heavy or Read Heavy?
    * Please prioritize functionality
    * What is NOT in scope?
* Capacity Estimation and Constraints:
    * max requests/day, QPS (query per second)
    * storage size, latency, availability
* High Level
    * System APIs
        * who call it?
    * Data Model
        * what will be saved?
        * seperate meta-data and hosting data!
    * Workflow/User Case
        * go through the steps
* Details
    * Choice of database
        * Image/Video hosting: distributed file storage system (HDFS)
        * CA: RDBMS
        * CP: HBase, Redis, MongoDB 
        * AP: Cassendra(wide-column), Dynamno(key-value store)
    * Data Partition
        * How many shards we need?
        * Shard by which ID
        * when user/post/ become popular?
            * consistent hashing to balance the load between servers!!
        * 
    * Diagram:
        * seperate web server and application server
        
    * Cache
        * Memcached
    * Load Balancer

    



Domain Knowledge
===
http://www.mitbbs.com/article_t/JobHunting/32777529.html

Sharding
---
Pros:
* Split the burden of data storage
* ID generation is simplistic

Cons:
* send requests to all data resources to get the responses
* since the tables could be loaded into separate partitions sql joins would not work

ACID
---
* Atomicity: either succeeds completely, or fails completely
* Consistentcy: valid transactions
* Isolation: concurrency control
* Durability: power outage

Eventual vs Strong Consistency:
---
https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/
* Eventual consistency: eventually the system converges to the same state
* Strong consistency: data **viewed after an update** will be consistent for all observers of the entity

Choices of NoSQL via CAP
---

http://blog.nahurst.com/visual-guide-to-nosql-systems
* CA: RDBMS
* CP: BigTable, HBase, Redis, MongoDB
   * HBase gets frequent writes get cached and write only once when buffer is full (out-performs MongoDB)

* AP: Dynamo, Cassendra 
   * good for most content distribution platforms because consistency is not important here
   * Dynamo is a key value store where cassandra is a column wide store; Cassendra > Redis

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
* HBase <--> Bigtable

Long Term Storage: Hive

Fan-out Write/Read (Push or Pull)
---
http://massivetechinterview.blogspot.com/2015/06/itint5.html


同样是timeline, twitter用fan-out-write（将new feed直接写到follower的timeline里），而Facebook却用fan-out-read（在读的时候实时抓取相关用户的feeds并merge/rank)

Twitter has apparently seen great performance improvements by disabling fanout for high profile users and instead loading their tweets during reads (pull).

Redis Vs Cassandra
---
http://highscalability.com/blog/2013/10/28/design-decisions-for-scaling-your-high-traffic-feeds.html

Instagram started out with Redis but eventually switched to Cassandra.

Redis however has a few limitations:
* all of your data needs to be stored in RAM which eventually becomes expensive. 
* no support for sharding built into Redis. Sharding across nodes is quite easy, but moving data when you add or remove nodes is a pain.

CDN
---
Store data physcially close to its consumers

Read Heavy or Write Heavy
---
read heavy那么用cache会提升performance之类的 同时知道应该避免什
么东西 比如避免single point of failure 再比如时间和空间的tradeoff在read 
heavy的时候应该倾向于时间 Write heavy的时候倾向于空间等等




