class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace('/','//')
        return int(eval(s))

print(eval("14//3"))