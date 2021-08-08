class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip().rstrip()
        s_list = s.split()

        left = 0
        right = len(s_list) - 1

        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        reverse_s = ''
        for i,word in enumerate(s_list):
            reverse_s+=word
            if i != len(s_list) - 1:
                reverse_s += ' '

        return reverse_s


print(Solution().reverseWords("  hello world  "))
