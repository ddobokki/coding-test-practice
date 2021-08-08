class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = ''
        total = []
        for char in s:
            if not char in ans:
                ans += char
            else:
                total.append(ans)
                ans = ans.replace(char,'') + char
        total.append(ans)
        print(total)



Solution().removeDuplicateLetters("bcabc")
Solution().removeDuplicateLetters("cbacdcbc")



'''

        lookUp = {}

        for indx, c in enumerate(s):
            lookUp[c] = indx
        print(lookUp)
        stack = []  # to compare index of previous chars
        seen = set()  # to keep track of current char

        for indx, c in enumerate(s):

            if c in seen:
                continue
            while stack and stack[-1] > c and lookUp[stack[-1]] > indx:
                seen.remove(stack[-1])
                stack.pop()

            stack.append(c)
            seen.add(c)

        return "".join(stack)

'''









# a = 'abc'
#
# b = a.replace('a','') + 'a'
# print(a,b)
# print(a>b)