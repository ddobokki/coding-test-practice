class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        left = 0
        temp = []
        for char in s:
            for i in range(left,len(t)):
                if char == t[i]:
                    left = i + 1
                    temp.append(char)
                    break
            else:
                left = len(t) - 1

        if s == ''.join(temp):
            return True
        else:
            return False

Solution().isSubsequence(s = "abc", t = "ahbgdc")
Solution().isSubsequence(s = "axc", t = "ahbgdc")

