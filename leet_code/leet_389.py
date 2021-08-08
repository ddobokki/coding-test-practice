class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = sorted(s)
        t_list = sorted(t)

        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return t_list[i]

        return t_list[-1]