Suffix Tree
===

A good post about suffix tree
[Ukkonen's suffix tree algorithm in plain English](https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english)

Suffix tree is a "trie" which stores all the suffices of a string.

The Ukkonen's construction algorithm insert one character at a time (from left to right).

Many thanks to the [visualization](http://brenden.github.io/ukkonen-animation/) tool by Brenden

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
Due to the `x`, a split at the active point `b` is needed. After the split, the previous active point is linked to the current active point. The link illustrated by the dashed line below is called **suffix link**.

![Imgur](https://i.imgur.com/EmRp5Rf.png)


**Why suffix link?**

Suffix links enable us to reset the active point so we can make the next remaining insert

For example, when dealing with suffix `abc...` and `bc..`, we know that, if a split occurs at `ab|...`, then another split must be done at `b|...`.

Instead of restarting from the root to match the `b`, we can follow the suffix link.

For example: insert the remaining `by` for `abcabxaby`.

we also have the suffix link

![Imgur](https://i.imgur.com/3OtL7xK.png)

Follow the suffix link to insert `by`
* set the node to which suffix link points as the active point
* make a split there

![Imgur](https://i.imgur.com/nr6LGOa.png)

Code
---
C++ code can be found here.
https://github.com/ADJA/algos/blob/master/Strings/UkkonenSuffixTree.cpp

Java code
https://gist.github.com/makagonov/22ab3675e3fc0031314e8535ffcbee2c
