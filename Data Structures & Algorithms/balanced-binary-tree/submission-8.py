# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Intuition: get the diff between the height of left and right <= 1
        
        # define balanced
        self.balanced = True
        # define a recursive function to trace through the nodes
        def dfs(node):
            # base case
            if not node:
                return 0
            # get the left and right height
            l = dfs(node.left)
            r = dfs(node.right)
            # check if condition for binary tree is met
            if abs(l - r) > 1:
                self.balanced = False
            # return the height of current node
            return max(l, r) + 1
        # call dfs on the root
        dfs(root)
        # return balanced result
        return self.balanced