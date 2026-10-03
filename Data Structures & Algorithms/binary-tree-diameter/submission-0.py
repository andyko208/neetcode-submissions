# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        # get the height of left and right node and get their sum 
        # maximize the sum of left at right throughout the traversal
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diam = max(self.diam, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.diam
            
