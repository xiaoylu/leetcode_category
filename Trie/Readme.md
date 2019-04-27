## Trie

Trie a tree structure which faciliates searching and storing prefixes. Given a set of strings, we can store the i-th letter as a node on the i-th layers of the tree.

1. Easy creation of Prefix Tree
```
    self.root = {}
    node = self.root
    for c in word+"$":
        node = node.setdefault(c, {})
```
where the `$` symbol indicates the end of a string `word`. Or equivalently
```
	T = lambda: collections.defaultdict(T)
        self.root = T()
        reduce(dict.__getitem__, word, self.root)['$'] = True
```

2. Easy travesal of Prefix Tree
```
    # Recursive
    def visit(node, word, prefix):
         if not word:
	    # Do sth.
         if '$' in node:
	    # Do sth.
	 c, w = word[0], word[1:] 
	 if c in node:
	    # Do sth.
	    visit(node[c], w, prefix+c)
```
Note that within any recursion call, `prefix+word` is the complete input string.

3. C++ short implementation, using a counter `next` to create new nodes.
```
    map<int, map<char, int> > x;
    int next = 1;

    void build(const string& w) {
        int cur = 0;
        for (const auto& ch : w) {
            if (x[cur].find(ch) == x[cur].end()) cur = x[cur][ch] = next++;
            else cur = x[cur][ch];
        }
        x[cur]['#'] = -1;
    }
```

**LC 336. Palindrome Pairs**

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. `words[i] + words[j]` is a palindrome.

The idea is to use a Trie storing all the prefixes, a pair of strings `ab???` and `ba` matches, so you can reverse `ba` into `ab`, and search Trie to end up with some suffix `???`. If `???` is palindrome, then `ab???` and `ba` make a pair.

```
class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = -1
        self.pal = []
    
    # create the Trie, recording the index of a string in case of palindrome suffix
    def insert(self, i, s):
        if not s:
            self.end = i
        else:
            if s[::-1] == s:
                self.pal += i,
            if s[0] not in self.kids:
                self.kids[s[0]] = TrieNode()
            self.kids[s[0]].insert(i, s[1:])
    
    # search the Trie, collect the pairs of strings if concatenation is palindrome string
    def collect(self, i, s, ret):
        if not s:
            # Reach `ab?` with the input `ab`
            ret.extend([j, i] for j in self.pal)
            # Reach `ab` with the input `ab`
            if self.end not in [-1, i]:
                ret.append([self.end, i])
        else:
            # Reach `ab` with the input `abs`
            if self.end != -1 and s[::-1] == s:
                ret.append([self.end, i])
            if s[0] in self.kids:
                self.kids[s[0]].collect(i, s[1:], ret)
        
class Solution(object):
    def palindromePairs(self, words):
        root = TrieNode()
        for i, w in enumerate(words):
            root.insert(i, w)
        ret = []
        for i, w in enumerate(words):
            root.collect(i, w[::-1], ret)
        return ret
```

**LC 676. Implement Magic Dictionary**
Find a string in the given dict which becomes the input string after modifying exact one character.
We traverse the Trie recursively with a `flag` storing the state if a character has been modified.
 
Pay attention to the two termination states: (i) run out of the input string (ii) reach the bottom of Trie

```
class MagicDictionary {
public:
    map<int, map<char, int> > x;
    int next = 1;
    
    /** Initialize your data structure here. */
    MagicDictionary() {
        next = 1;
        x.clear();
    }
    void build(const string& w) {
        int cur = 0;
        for (const auto& ch : w) {
            if (x[cur].find(ch) == x[cur].end()) cur = x[cur][ch] = next++;
            else cur = x[cur][ch];
        }
        x[cur]['#'] = -1;
    }
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        for (const auto& w : dict) build(w);
    }
    
    bool _search(string word, int cur, int i, bool flag) {
        //cout << word << "," << word[i] << "," << flag << endl;
        
        if (i == word.size()) {
            if (!flag && x[cur].find('#') != x[cur].end()) return true;
            return false;
        }
        
        if (flag) {
            for (auto it : x[cur]) if (it.first != '#') {
                if (_search(word, it.second, i + 1, (word[i] == it.first))) 
                    return true;
            }
            return false;
        }
        else {
            return x[cur].find(word[i]) == x[cur].end() ?
                false : _search(word, x[cur][word[i]], i + 1, false);
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        if (word.empty()) return false;
        return _search(word, 0, 0, true);
    }
};
```
