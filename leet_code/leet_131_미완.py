from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return_list = []

        for window in range(1 , len(s) + 1):
            temp = []
            idx = 0
            while idx <= len(s) - window:
                sub_s = s[idx:idx+window]
                print(sub_s)
                if sub_s == sub_s[::-1]:
                    idx += window
                    temp.append(sub_s)
                else:
                    idx += 1


            return_list.append(temp)

        return return_list
print(Solution().partition("aab"))