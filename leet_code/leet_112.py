class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def helper(root,target,val):
    if root is None:
        return False
    print(root.val)
    if not root.left and not root.right:
        print('return')
        return val+root.val==target
    return helper(root.left,target,val+root.val) or helper(root.right,target,val+root.val)

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return helper(root,targetSum,0)

a = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(Solution().hasPathSum(a,13))