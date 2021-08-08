from typing import List


class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:

        def compute(left, right, op):
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result

        if expression.isdigit():
            return [int(expression)]

        results = []

        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                results.extend(compute(left,right,value))
        #print(results)
        return results

Solution().diffWaysToCompute("2*3-4*5")