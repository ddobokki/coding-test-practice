from typing import List

# import itertools
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]
#         idx_list = list(range(0,len(nums)))
#         for i in range(1,len(nums)+1):
#             #print(i)
#             idxs = list(itertools.combinations(idx_list,i))
#             #print(idxs)
#             for idx in idxs:
#                 temp = []
#                 for j in idx:
#                     #print(nums[j])
#                     temp.append(nums[j])
#                 result.append(temp)
#
#         #print(result)
#         return result


'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:

            output += [curr + [num] for curr in output]

        return output
#모범답
'''




Solution().subsets([1,2,3])


