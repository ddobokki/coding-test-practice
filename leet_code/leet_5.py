# import collections
# class Solution:
#
#     def longestPalindrome(self, s: str) -> str:
#
#         def check(ss):
#             return ss[:] == ss[::-1]
#
#
#         pali_dict = collections.defaultdict(str)
#         for i in range(len(s)):
#             for j in range(i + 1,len(s)):
#                 if s[i] == s[j]:
#                     if check(s[i:j + 1]):
#                         pali_dict[len(s[i:j + 1])] = s[i: j + 1]
#
#         if not pali_dict.keys():
#             return s[0]
#
#         return pali_dict[max(pali_dict.keys())]


class Solution:

    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) -> str:
            while(left >=0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i,i+1),expand(i,i+2),key=len)
        return result




print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("ac"))