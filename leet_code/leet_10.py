import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not re.match(p, s):
            return False
        else:
            return len(s) == re.match(p,s).span()[1]

s = "aa"
#print(re.match("c*a*b","aab"))
print(re.match(".*c","ab"))

if not re.match(".*c","ab"):
    print('a')

print(re.match("mis*is*p*.","mississippi"))