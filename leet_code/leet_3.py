
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         max_length = -1
#         for i in range(len(s)):
#             length = 1
#             for j in range(i + 1, len(s)):
#                 if s[j] not in s[i:j]:
#                     #word.append(s[j])
#                     length += 1
#                 else:
#                     break
#             if length > max_length:
#                 max_length = length
#         return max_length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        #and start <= used[char]
        for index, char in enumerate(s):
            print(used)
            if char in used:
                print(start, '->', used[char] + 1, s[start:index+1] , char, start)
                start = used[char] + 1
            else:
                max_length = max(max_length,index - start + 1)
            used[char] = index
        return max_length

a = Solution()
# print(a.lengthOfLongestSubstring("abcabcabc"))
# print(a.lengthOfLongestSubstring("pwwkew"))
# print(a.lengthOfLongestSubstring("aaaaabb"))
print(a.lengthOfLongestSubstring("tmmzuxt"))
'''
{}
{'t': 0}
{'t': 0, 'm': 1}
0 -> 2 tmm
{'t': 0, 'm': 2}
{'t': 0, 'm': 2, 'z': 3}
{'t': 0, 'm': 2, 'z': 3, 'u': 4}
{'t': 0, 'm': 2, 'z': 3, 'u': 4, 'x': 5}

{}
{'t': 0}
{'t': 0, 'm': 1}
0 -> 2 tmm
{'t': 0, 'm': 2}
{'t': 0, 'm': 2, 'z': 3}
{'t': 0, 'm': 2, 'z': 3, 'u': 4}
{'t': 0, 'm': 2, 'z': 3, 'u': 4, 'x': 5}
2 -> 1 mzuxt


'''