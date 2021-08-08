class Solution:
    arr = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if not self.arr.get(n-1):
            self.arr[n-1] = self.climbStairs(n-1)
        if not self.arr.get(n-2):
            self.arr[n-2] = self.climbStairs(n-2)
        return self.arr[n-1] + self.arr[n-2]

print(Solution().climbStairs(3))