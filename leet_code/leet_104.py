class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    return_d = 0
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(r, depth):
            depth += 1
            if not r.left and not r.right:
                self.return_d = max(self.return_d,depth)
                return
            elif not r.left and r.right:
                dfs(r.right, depth)
            elif not r.right and r.left:
                dfs(r.left, depth)
            else:
                dfs(r.left, depth)
                dfs(r.right, depth)
        dfs(root,0)

        return self.return_d

a = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))


'''
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
    
모범답안.....

'''

print(Solution().maxDepth(a))