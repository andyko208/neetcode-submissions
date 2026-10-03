# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def dfs(node):
            # base case 
            if not node:
                return 0
            # get the height of left and right
            l = dfs(node.left)
            r = dfs(node.right)
            # maximize the diameter by getting the sum of l and r
            self.diam = max(self.diam, l + r)
            # return the height as the original
            return max(l, r) + 1
        dfs(root)
        return self.diam