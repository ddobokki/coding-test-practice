from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        hashMap = []
        for ind, num in enumerate(nums):
            hashMap.append([num,ind])
        hashMap = sorted(hashMap,key=lambda x: x[0])
        for i in range(len(hashMap)):
            for j in range(i+1,len(hashMap)):
                if abs(hashMap[i][0] - hashMap[j][0]) > t:
                    break
                elif abs(hashMap[i][1]-hashMap[j][1]) <= k:
                    return True
        return False



print(Solution().containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))
print(Solution().containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))
print(Solution().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))