from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)

        small = temp[:len(nums)//2]
        big = temp[len(nums)//2:]

        if len(small) < len(big):
            small.append(big.pop(0))


        total_idx = min(len(small),len(big))

        s = 0
        b = 0
        for i in range(len(big) + len(small)):
            if i % 2 == 0:
                nums[i] = small[s]
                s += 1
            else:
                nums[i] = big[b]
                b += 1

        print(nums)

Solution().wiggleSort([1,5,1,1,6,4,7])