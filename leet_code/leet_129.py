class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nums = []

        def dfs(root,s):
            s += str(root.val)
            if not root.right and not root.left:
                nums.append(int(s))
                return

            if root.left:
                dfs(root.left,s[:])
            if root.right:
                dfs(root.right,s[:])

        dfs(root,'')

        return sum(nums)
