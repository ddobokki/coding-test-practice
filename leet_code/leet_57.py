from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals:

            if result[-1][1] >= interval[0]:
                result[-1] =[min(interval[0],result[-1][0]) ,max(interval[1], result[-1][1])]
            else:
                result.append(interval)
        return result
print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))