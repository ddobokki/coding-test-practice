'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"


Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.

'''
import collections


class Solution:
    '''
    파이썬 알고리즘 인터뷰 참고 page 576
    '''

    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽으로 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            # 필요문자가 0이면 왼쪽 포인터 이동판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]


# 시간 초과
# import collections
# class Solution:
#     def check(self,s,t): # s가 t를 포함하는지 확인하는 함수
#         char_cnt = collections.Counter(s)
#         need_t = collections.Counter(t)
#         for char in need_t.keys():
#             if char in char_cnt:
#                 char_cnt[char] -= need_t[char]
#                 if char_cnt[char] < 0:
#                     return False
#             else:
#                 return False
#
#         return True
#     def minWindow(self, s: str, t: str) -> str:
#         if len(s) < len(t):
#             return ''
#         if s == t:
#             return t
#         if not self.check(s,t):
#             return ''
#         left = 0
#         right = 0
#         window_len = float('inf') # t를 포함하는 윈도우의 길이
#         ans = ''
#         while left <= right < len(s):
#             window_s = s[left:right + 1] # 윈도우로 문자열을 확인
#             if self.check(window_s,t): # 윈도우 문자열이 t를 포함하면
#                 left += 1 # 윈도우를 늘려본다
#                 if window_len > len(window_s):
#                     ans = window_s
#                     window_len = len(window_s)
#             else:
#                 right += 1 # 포함 안하면 윈도우를 키워본다.
#         #print(ans)
#         return ans

# Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
Solution().minWindow(s="bbaa", t="aba")
