
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root.right and root.left:
            return True
        if not root.right or root.left:
            return False
        if root.right.val != root.left.val:
            return False
        return self.isSymmetric(root.right) and self.isSymmetric(root.left)