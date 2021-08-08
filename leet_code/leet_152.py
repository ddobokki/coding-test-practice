from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def sub_product(li):
            left = 0
            right = 0
            while right < len(nums):
                if li[right] != 0:
                    if left == right:
                        li[right] = li[right]
                    else:
                        li[right] = li[right] * li[right - 1]
                    right += 1
                else:
                    li[right] = 0
                    right += 1
                    left = right

            return max(li)
        reverse = list(reversed(nums))
        #print(reverse)
        return max(sub_product(nums),sub_product(reverse))

Solution().maxProduct([0,2])
Solution().maxProduct([2,3,-2,-4])
Solution().maxProduct([-2,2,2,2,-1])