class Solution:


    def decodeString(self, s: str) -> str:
        idx = 0
        ans = ''
        while idx < len(s):
            if s[idx].isalpha():
                ans += s[idx]

            if s[idx].isdigit():
                num = ''
                while s[idx].isdigit():
                    num += s[idx]
                    idx += 1
                num = int(num)

                p_idx = idx
                cnt = 0
                while p_idx < len(s):
                    #print(s[p_idx])
                    if s[p_idx] == ']':
                        if cnt == 1:
                            break
                        else:
                            cnt -= 1
                    if s[p_idx] == "[":
                        cnt += 1
                    p_idx += 1
                if p_idx == len(s):
                    p_idx -= 1
                #print(s[idx + 1:p_idx])
                ans += num * s[idx + 1:p_idx]
                idx = p_idx
            idx += 1
        #print(ans)
        if not "[" in ans:
            return ans
        else:
            return self.decodeString(ans)
#print(Solution().decodeString(s = "3[a]2[bc]"))
print(Solution().decodeString(s = "3[a2[c]]"))
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
#print(Solution().decodeString("zzz2[y]pq4[2[jk]e1[f]]]ef2[y]pq4[2[jk]e1[f]]]ef"))
