Suffix Tree
===

A good post about suffix tree
[Ukkonen's suffix tree algorithm in plain English](https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english)

Suffix tree is a "trie" which stores all the suffices of a string.

The Ukkonen's construction algorithm insert one character at a time (from left to right).

Implicit Tree
---
Given a string `A`, each leaf edge of the implicit tree represents `A[i:#]`, where `#` indicates the current last char; when we insert a new char, the leaf edges **implicitly** extend, no operation is needed.

Split
---
Example: `A=abcabx`

Inserting `abcab`: the implicit tree automatically grows the edges `abcab`, `bcab`, `cab` from root.

Note the second `ab` matches the first `ab`. So we just move the active point to `ab|cab`.

![Imgur](https://i.imgur.com/n7c2xx8.png)

Now, when we insert `x`, there is no matching letter, so we need to split
![Imgur](https://i.imgur.com/BGIgKA5.png)

We deal with `abx` already, it is the turn of `bx` and `x`.

Suffix link
---
To insert `bx`, we restart from the root, then a split at the `b` is needed. After the insertion, the first split at `b` points to second split point at the second `b`. This link is called suffix link.

![Imgur](https://i.imgur.com/EmRp5Rf.png)


**Why suffix link?**

Imagine building suffix tree for `abcabxaby`. The substring `aby` actually **shares** the prefix `ab` with `abx`; and the substring `by` **shares** the `b` with `bx`. 

So, we can follow the suffix link from `aby` to `by` directly. We do not need to restart from the root to match `by`. Because any suffix `ab..` would indicate that a suffix `b..` already exist in the tree.

Insert `aby`

![Imgur](https://i.imgur.com/3OtL7xK.png)

then follow the suffix link to insert `by`

![Imgur](https://i.imgur.com/nr6LGOa.png)

(Many thanks to the [visualization](http://brenden.github.io/ukkonen-animation/) tool by Brenden)

C++ code can be found here.
https://github.com/ADJA/algos/blob/master/Strings/UkkonenSuffixTree.cpp
