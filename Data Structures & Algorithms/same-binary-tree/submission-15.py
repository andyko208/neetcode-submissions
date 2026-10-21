# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        def dfs(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            elif l.val == r.val:
                return dfs(l.left, r.left) and dfs(l.right, r.right)
            return False
        return dfs(p, q)