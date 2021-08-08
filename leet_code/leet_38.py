import collections
class Solution:
    def countAndSay(self, n: int) -> str:
        k = n - 1
        cur_say = "1"
        while k > 0:
            new_say = ""
            new_say_li = []


            cur_n = cur_say[0]
            cur_st = cur_say[0]

            for i in range(1, len(cur_say)):
                if cur_n != cur_say[i]:
                    new_say_li.append(cur_st)
                    cur_st = cur_say[i]
                else:
                    cur_st += cur_say[i]
                cur_n = cur_say[i]

            new_say_li.append(cur_st)
            for s in new_say_li:
                new_say += str(s.count(s[0])) + s[0]
            #print(new_say_li)
            cur_say = new_say
            k -= 1

        return cur_say

print(Solution().countAndSay(4))

s = "112211"

# li = []
# cur_n = s[0]
# cur_st = s[0]
# for i in range(1,len(s)):
#     if cur_n != s[i]:
#         li.append(cur_st)
#         cur_st = s[i]
#     else:
#         cur_st += s[i]
#     cur_n = s[i]
#
# li.append(cur_st)

