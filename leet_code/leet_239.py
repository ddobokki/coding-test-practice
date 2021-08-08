from typing import List

import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max_sliding_window = []
        #
        # sl = collections.deque()
        #
        # for i in range(k):
        #     sl.append(nums[i])
        #
        # cur_max = max(sl)
        # max_sliding_window.append(cur_max)
        # cur_max_cnt = sl.count(cur_max)
        #
        # for num in (nums[k:]):
        #     sl.append(num)
        #
        #     if num == cur_max: # 최댓값과 같은 숫자가 들어옴
        #         cur_max_cnt += 1
        #         pop = sl.popleft() # 팝
        #
        #         if pop == cur_max:
        #             cur_max_cnt -= 1
        #
        #     elif num > cur_max: # 최댓값보다 큰 수가 들어옴
        #         cur_max = num # 최댓값 갱신
        #         cur_max_cnt = 1 # 최댓값 카운트
        #         pop = sl.popleft() # 팝
        #
        #     else: # 최댓값보다 작은수가 들어옴
        #         pop = sl.popleft() # 팝
        #
        #         if (pop == cur_max) and (cur_max_cnt == 1): #나가는게 최댓값이고, 그 수가 1이면
        #             cur_max = max(sl) # 최댓값 갱신
        #             cur_max_cnt = sl.count(cur_max) # 갱신된 최댓값의 수
        #         elif (pop == cur_max) and (cur_max_cnt != 1):
        #             cur_max_cnt -= 1
        #
        #     max_sliding_window.append(cur_max)
        # print(max_sliding_window)

        max_sliding_window = []
        window = collections.deque()
        cur_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if cur_max == float('-inf'):
                cur_max = max(window)
            elif v > cur_max:
                cur_max = v

            max_sliding_window.append(cur_max)

            if cur_max == window.popleft():
                cur_max = float('-inf')



        return max_sliding_window


'''
주석코드는 첫 시도

아랫 코드는 파이썬 알고리즘 인터뷰에서 나온 코드

윗 코드가 통과는 더 많이 했다

아랫 코드 역시 통과 실패

무엇이 문제...?!

'''

Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)

