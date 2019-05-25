Suffix Tree
===

A good post about suffix tree
[Ukkonen's suffix tree algorithm in plain English](https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english)

Suffix tree is a tries storing all the suffices of a string.

The Ukkonen's construction algorithm insert one character at a time.

* Implicit Tree: each leaf edge of the tree represents `A[i:#]`, where `#` indicates the last char; when we insert a new char, the leaf edges **implicitly** extend, no operation is needed.

* Split:
[Imgur](https://i.imgur.com/n7c2xx8.png)
[Imgur](https://i.imgur.com/BGIgKA5.png)

* Suffix link:
