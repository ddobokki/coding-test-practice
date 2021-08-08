class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/')
        path = path.split('/')
        s_l = []
        for i in range(len(path) - 1, -1, -1):
            if path[i] == '':
                continue
            if path[i] == '.' or path[i] == '..':
                if len(s_l) == 0:
                    continue
                break
            s_l.append(path[i])
        ans = ''
        #print(s_l)
        for s in s_l[::-1]:
            ans += '/' + s
        if len(ans) == 0:
            ans = '/'
        #print(ans)
        return ans
#Solution().simplifyPath("/home//foo/")
#Solution().simplifyPath("/a/./b/../../c/")
#Solution().simplifyPath("/a/../../b/../c//.//")