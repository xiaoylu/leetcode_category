A case study of Pinterest system design
===

Smart Feed
---
https://medium.com/@Pinterest_Engineering/building-a-smarter-home-feed-ad1918fdfbe3

Smart Feed Worker
* Work collected repin, related pin and interest pin into three pools
* Each pool is a priority queue sorted on score and belongs to a single user. (via key-based sorting of HBase)

Smart Feed Content Generator
* fetch from each pool

Smart Feed Service
* the materialized feed represents a frozen view of the feed as it was the last time the user viewed it.
* when no new feed, the smart feed service will return the content contained in the materialized feed

Dynamic and Responsive Pinterest
---
https://medium.com/pinterest-engineering/building-a-dynamic-and-responsive-pinterest-7d410e99f0a9

Online: Display
Offline: Generating the recommendations
* find candidates
  * Feed Generator sends to Polaris the board list and the bloom filter consisting of the impression history of the user
  *
* find features
* scoring
* display

Pixie
---
https://medium.com/@Pinterest_Engineering/introducing-pixie-an-advanced-graph-based-recommendation-system-e7b4229b664b
* periodically loads into memory an offline-generated graph consisting of boards and Pins
* when recommended boards are requested for a user, a random walk is simulated in the Pixie graph by using the Pins engaged by the user as starting points.

Graph Convolutional Neural Networks for Web-Scale Recommender Systems (KDD 2018)
---
* PinSage algorithm performs efficient, localized convolutions by sampling the neighborhood around a node and dynamically constructing a computation graph from this sampled neighborhood.
* Basic idea: transform the representations of u’s neighbors through a dense neural network and then apply a aggregator/pooling fuction
* We then concatenate the aggregated neighborhood vector nu with u’s current representation and transform the **concatenated** vector through another dense
neural network layer
* Supervised algorithm: the goal of the training phase is to optimize the PinSage parameters so that the output embeddings of pairs in the labeled set are close together.


