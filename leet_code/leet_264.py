import heapq
class Solution:


    def nthUglyNumber(self, n: int) -> int:

        result = [1]

        idx2,idx3,idx5 = 0,0,0

        while len(result) != n:
            ugly2 = result[idx2] * 2
            ugly3 = result[idx3] * 3
            ugly5 = result[idx5] * 5

            ugly_nums = [ugly2,ugly3,ugly5]
            ugly_nums.sort()

            for ugly_num in ugly_nums:
                if not ugly_num in result:
                    result.append(ugly_num)
                    break
            if result[-1] == ugly2:
                idx2 += 1
            if result[-1] == ugly3:
                idx3 += 1
            if result[-1] == ugly5:
                idx5 += 1

        return result[-1]

'''
class Solution(object):
def nthUglyNumber(self, n):

    dp = [0] * n
    
    dp[0] = 1
    
    t2 = t3 = t5 = 0
    
    for i in range(1, n):
        dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
                                               
        if dp[i] == dp[t2] * 2:
            t2 += 1
            
        if dp[i] == dp[t3] * 3:
            t3 += 1
            
        if dp[i] == dp[t5] * 5:
            t5 += 1
            
    return dp[-1]
    
이게 좀더 나은것 같다.

'''

print(Solution().nthUglyNumber(30))

#[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80]