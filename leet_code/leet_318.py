from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        total = []
        for i in range(len(words) - 1):
            word1 = words[i]
            word1_len = len(word1)
            max_len = 0
            for j in range(i + 1, len(words)):
                word2 = words[j]
                word2_len = len(word2)

                if len(set(list(word1)).intersection(list(word2))) == 0:
                    max_len = max(word1_len * word2_len,max_len)
            total.append(max_len)

        return max(total)

Solution().maxProduct( ["abcw","baz","foo","bar","xtfn","abcdef"])