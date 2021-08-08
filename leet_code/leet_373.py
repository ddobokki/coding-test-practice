from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        total = []

        for i in range(len(nums1)):

            for j in range(len(nums2)):
                total.append([nums1[i],nums2[j]])

        total.sort(key=lambda x:x[0]+x[1])


        return total[:k]

print(Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))

'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        M, N = len(nums1), len(nums2)
        h, visited, ans = [(nums1[0] + nums2[0], 0, 0)], set((0, 0)), []
        while h and k:
            _, i, j = heapq.heappop(h)
            ans.append((nums1[i], nums2[j]))
            if (i + 1) < M and (i+1, j) not in visited:
                heapq.heappush(h, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            if (j + 1) < N and (i, j+1) not in visited:
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
            k -= 1
        return ans

모범답안

'''