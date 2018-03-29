class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = i2 = -len(words)
        ret = len(words)
        for idx, word in enumerate(words):
            if word1==word:
                ret = min(ret, idx-i2)
                i1 = idx
            elif word2==word:
                ret = min(ret, idx-i1)
                i2 = idx
        return ret
