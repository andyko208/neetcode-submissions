# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.val = None
        def dfs(node):
            if not node:
                return False
            if dfs(node.left):
                return True
            if self.i == k-1:
                self.val = node.val
                return True
            else:
                self.i += 1
            if dfs(node.right):
                return True
        dfs(root)
        return self.val