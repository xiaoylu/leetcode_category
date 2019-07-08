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

Now, when we insert `x`, there is no matching letter, so we need to split at the current active point
![Imgur](https://i.imgur.com/BGIgKA5.png)

We maintain a variable `remainder` which tells us how many additional inserts we need to make.

Case in point: we deal with `abx` already, so `remainder = 2` because it is the turn of `bx` and `x`.

To insert `bx`, we restart from the root and move the active point to `b|cabx`.

Suffix link
---
Due to the `x`, a split at the active point `b` is needed. After the split, the previous active point is linked to the current active point at the second. This link illustrated by dashed line is called **suffix link**.

![Imgur](https://i.imgur.com/EmRp5Rf.png)


**Why suffix link?**

Consider building suffix tree for `abXabY` where `ab` are letters and `X`, `Y` are different strings. The substring `abY` actually **shares** the prefix `ab` with the substring `abXabY`; the substring `bY` **shares** the `b` with `bXabY`.

So, we create the suffix link dealing with `abXabY` and `bXabY`. 
When working on `abY` and `bY`, instead of restarting from the root to match `b`, we can follow the suffix link.

Insert `aby`

![Imgur](https://i.imgur.com/3OtL7xK.png)

then follow the suffix link to insert `by`

![Imgur](https://i.imgur.com/nr6LGOa.png)

Many thanks to the [visualization](http://brenden.github.io/ukkonen-animation/) tool by Brenden

Code
---
C++ code can be found here.
https://github.com/ADJA/algos/blob/master/Strings/UkkonenSuffixTree.cpp
