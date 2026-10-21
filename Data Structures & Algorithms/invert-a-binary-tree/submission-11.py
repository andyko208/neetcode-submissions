# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS - Time: O(N), Space: O(N)
        # define a dfs
        def dfs(node):
            # base case to return if not node
            if not node:
                return
            # recurse on the left node
            dfs(node.left)
            # recurse on the right node
            dfs(node.right)
            # swap the left and right child
            node.left, node.right = node.right, node.left
        # return the root
        dfs(root)
        return root