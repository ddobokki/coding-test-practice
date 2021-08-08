from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]


        for interval in intervals:
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(interval[1],result[-1][1])
            else:
                result.append(interval)
        return result


Solution().merge([[1,3],[2,6],[8,10],[15,18]])
Solution().merge( [[1,4],[4,5]])

