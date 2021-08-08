class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == " ":
            return 0

        s_list = s.split()

        if s_list:
            return len(s_list[-1])
        else:
            return 0

#Solution().lengthOfLastWord("a")