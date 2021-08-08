from typing import List
# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#



class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        # left, right = 0, len(nums) - 1
        # # 최솟값 찾기
        # while left < right:
        #     mid = (left + right)//2
        #
        #     if nums[mid] > nums[right]:
        #         # mid 값이 맨 끝 값보다 크면 회전된 곳에 포함됬다는 뜻
        #         # left를 mid + 1로 하고 다시 검색 시작
        #         left = mid + 1
        #     else:# 아니면 아직 회전되지 않은곳이므로 right를 mid로 하고 다시 검색시작
        #         right = mid

        n = nums[0]
        pivot = 0
        for i in range(1,len(nums)):
            if nums[i] >= n:
                n = nums[i]
            else:
                pivot = i
                break

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            mid_pivot = (mid + pivot) % len(nums) # 미드 인덱스에 피벗 인덱스를 더해준후
            # 모듈러 연산을 통해 인덱스를 회전시켜준다

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return True

        return False

print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2))