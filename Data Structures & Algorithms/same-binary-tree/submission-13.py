# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # need a base case
        def dfs(p, q):
            # return true if not p and not q
            if not p and not q:
                return True
            # return dfs(p.left, dfs.q.left) and dfs(p.right, q.right) if p and q and p.val==q.val
            elif p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            # return False otherwise
            return False
        return dfs(p, q)