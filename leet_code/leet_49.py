from typing import List

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = collections.defaultdict(list)

        for str in strs:
            sort_str = sorted(str)
            #print(sort_str)
            ana_dict[''.join(sort_str)].append(str)

        return list(ana_dict.values())

Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])