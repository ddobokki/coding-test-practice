from typing import List


class Solution:
    def find_check_point(self,nums):
        right = len(nums) - 2 # 마지막 인덱스의 전 인덱스부터 0까지 검사
        check_point = len(nums)

        while right >= 0:
            if right + nums[right] >= len(nums) - 1: # 점프로 마지막점 이상까지 도달 할 수 있으면 체크포인트로 선택
                check_point = min(check_point, right) # 같이 도달하더라도 인덱스 값이 작은 것을 선택
            right -= 1

        return check_point

    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        left = 0
        check_point = -1
        cnt = 0
        while left != check_point:
            check_point = self.find_check_point(nums) # 마지막 인덱스에 도착할수 있는 점프지점을 찾는다.
            nums = nums[0 : check_point+1] # 체크 포인트를 마지막 지점으로 해서 다시 루프를 돈다.
            cnt += 1


        return cnt


