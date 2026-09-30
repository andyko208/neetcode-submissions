# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS
        def dfs(left, node, right):
            # base case to return True if not node
            if not node:
                return True
            # return false if not left < node.val < right
            elif not (left < node.val < right):
                return False
            # recurse on left, node.left, node.val
            return dfs(left, node.left, node.val) and dfs(node.val, node.right, right)
            # recurse on node.val, node.right, right
        return dfs(float('-inf'), root, float('inf'))
            