# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Intuition: get the diff between the height of left and right <= 1
        self.balanced = True
        def dfs(node):
            # base case
            if not node:
                return 0
            # get the left and right height
            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l - r) > 1:
                self.balanced = False
            return max(l, r) + 1

        dfs(root)
        return self.balanced