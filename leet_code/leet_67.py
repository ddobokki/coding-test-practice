class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a,2) + int(b,2),'b')



a = format(11,'b')
print(a)

