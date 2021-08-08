from typing import List

import collections
class Solution:
    def string_split(self,string,idx,lenth):
        return [string[i:i+lenth] for i in range(idx,len(string),lenth)]

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated_dna = collections.defaultdict(int)
        for i in range(10):
            split_dna_by10 = self.string_split(s,i,10)
            for dna in split_dna_by10:
                if len(dna) == 10:
                    repeated_dna[dna] += 1
        repeated = []
        for dna in repeated_dna:
            if repeated_dna[dna] > 1:
                repeated.append(dna)
        #print(repeated)
        return repeated

'''
class Solution:
def findRepeatedDnaSequences(self, s: str) -> List[str]:
    current=set()
    repeated=set()
    for i in range(len(s)-9):
        curr=s[i:i+10]
        if curr in current:
            repeated.add(curr)
        current.add(curr)
    return [*repeated]
모범코드


'''



Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA")
