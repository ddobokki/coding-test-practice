class Solution:
    def isHappy(self, n: int) -> bool:
        n_list = list(str(n))
        chache = []
        while True:
            #print(chache)
            num = sum(list(map(lambda x:int(x)**2,n_list)))
            if num == 1:
                return True
            if not num in chache:
                chache.append(num)
                n_list = list(str(num))
            else:
                return False

print(Solution().isHappy(2))