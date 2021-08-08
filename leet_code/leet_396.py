from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
               :type A: List[int]
               :rtype: int
               """

        '''
        Example:
        n = 5 
        A = [a, b, c, d, e]

        k = 0:
        B = [a, b, c, d, e]
        F_0 =  0*a + 1*b + 2*c + 3*d + 4*e

        k = 1: 
        B = [e, a, b, c, d]
        F_1 =  1*a + 2*b + 3*c + 4*d + 0*e
     ______________________________________________________  
        F_1 - F_0 =  1*a + 1*b + 1*c + 1*d - 4*e = sum - 4*e
        F_1 = F_0 + sum - n*A[-1]
     ______________________________________________________  

        k = 2: 
        B = [d, e, a, b, c]
        F_2 =  2*a + 3*b + 4*c + 0*d + 1*e
     ______________________________________________________  
        F_2 - F_1 =  1*a + 1*b + 1*c + 1*e - 4*d = sum - 4*d
        F_2 = F_1 + sum - n*A[-2]
     ______________________________________________________  

        k = 3: 
        B = [c, d, e, a, b]
        F_3 =  3*a + 4*b + 0*c + 1*d + 2*e
     ______________________________________________________  
        F_3 - F_2 =  1*a + 1*b + 1*d + 1*e - 4*c = sum - 4*c
        F_3 = F_2 + sum - n*A[-3]
     ______________________________________________________  

        General Rule:
                F(i+1) = F(i) + sum - n * A[-1 * (i+1)]
        '''

        sum_A = sum(nums)
        n = len(nums)

        # cur_sum is F_0
        cur_sum = sum(i * n for i, n in enumerate(nums))
        max_sum = cur_sum

        for i in range(1, n):
            cur_sum = cur_sum + sum_A - n * nums[-i]
            max_sum = max(cur_sum,max_sum)

        return max_sum



Solution().maxRotateFunction([4,3,2,6])