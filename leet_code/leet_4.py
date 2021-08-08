from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        ans = []
        m, n = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        cnt = 0
        fin = median = (m + n) // 2
        while True:
            if idx1 == m:
                ans += nums2[idx2:]
                break
            if idx2 == n:
                ans += nums1[idx1:]
                break

            num1, num2 = nums1[idx1], nums2[idx2]

            if num1 > num2:
                ans.append(num2)
                idx2 += 1
            else:
                ans.append(num1)
                idx1 += 1


        median = (m + n) // 2
        if (m+n) % 2 == 0:

            average = (ans[median - 1] + ans[median]) / 2
        else:
            average = ans[median] / 1
        #print(ans)
        return average

a = Solution()
print(a.findMedianSortedArrays([1,2],[3,4]))
