class Solution:
    def myAtoi(self, s: str) -> int:
        temp_s = ""
        for i in range(len(s)):
            #print(s[i])
            if s[i] == " " and len(temp_s) == 0:
                continue
            elif s[i] == " " and len(temp_s)>0:
                break
            if s[i] == "+" or s[i] == "-":
                if len(temp_s) == 0:
                    temp_s += s[i]
                    continue
                elif s[i-1].isdigit():
                    break
                # elif temp_s[i-1] != s[i]:
                #     temp_s = temp_s.replace(temp_s[i-1],s[i])
                #     continue
                else:
                    temp_s = ""
                    break
            if not s[i].isdigit():
                break
            elif s[i].isdigit():
                temp_s += s[i]
        if temp_s == "":
            s = "0"
        elif temp_s == "+" or temp_s =="-":
            s = "0"
        else:
            s = temp_s

        s = int(s)

        min_num = -2**31
        max_num = 2**31 - 1
        if min_num <= s <= max_num:
            return s
        elif s < min_num:
            return min_num
        else:
            return max_num