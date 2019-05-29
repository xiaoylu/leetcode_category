Suffix Tree
===

A good post about suffix tree
[Ukkonen's suffix tree algorithm in plain English](https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english)

Suffix tree is a "trie" which stores all the suffices of a string.

The Ukkonen's construction algorithm insert one character at a time.

Implicit Tree
---
Given a string `A`, each leaf edge of the implicit tree represents `A[i:#]`, where `#` indicates the current last char; when we insert a new char, the leaf edges **implicitly** extend, no operation is needed.

Split
---
Example: `A=abcabx`

Inserting `abcab`: the second `ab` matches the first `ab`. So we just record the active point right after the first`b` as `ab|cab`.

![Imgur](https://i.imgur.com/n7c2xx8.png)

When we insert `x`, there is not matching letter, so we need to split
![Imgur](https://i.imgur.com/BGIgKA5.png)

We deal with `abx` already, it is the turn of `bx` and `x`.

Suffix link
---
To insert `bx`, a split at `b` is needed. After the insertion, the suffix link of the first split at `b` points to second split at the other `b`.

![Imgur](https://i.imgur.com/EmRp5Rf.png)


**Why suffix link?**

Imagine buliding suffix tree for `abcabxaby`. The `aby` part can actually **share** the prefix `ab` (which is a route in the suffix tree) from the `abx`, and the `by` and **borrow** the `b` from `bx`.

Insert `aby`
![Imgur](https://i.imgur.com/3OtL7xK.png)

then follow the suffix link to insert `by`
![Imgur](https://i.imgur.com/nr6LGOa.png)

(Many thanks to the [visualization](http://brenden.github.io/ukkonen-animation/) tool by Brendon)

C++ code can be found here.
https://github.com/ADJA/algos/blob/master/Strings/UkkonenSuffixTree.cpp
