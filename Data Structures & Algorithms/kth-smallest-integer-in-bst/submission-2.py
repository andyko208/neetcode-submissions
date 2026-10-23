# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.res = None
        def dfs(node):
            if not node:
                return False
            if dfs(node.left):
                return True
            if self.i != k-1:
                self.i += 1
            else:
                self.res = node.val
                return True
            if dfs(node.right):
                return True
            return False
        dfs(root)
        return self.res
        
