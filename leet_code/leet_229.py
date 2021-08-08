from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return_list = [] # 반환할 리스트

        nums.sort() # 정렬
        pointer = 0 # 인덱스 포인터

        while pointer < len(nums):
            num = nums[pointer] # 첫 숫자
            cnt = 0
            while num == nums[pointer]: # 다른숫자가 나올때까지 카운트
                pointer += 1
                cnt += 1 # 카운트
                if pointer == len(nums): # 포인터가 증가하다가 마지막 인덱스 + 1 즉, 셀수 없으면
                    break # 종료

            if cnt > len(nums) / 3: # 조건에 맞으면 리스트에 리턴
                return_list.append(num)

        #print(return_list)
        return return_list

Solution().majorityElement([1,2])




