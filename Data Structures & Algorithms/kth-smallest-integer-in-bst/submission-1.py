# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # get all nodes and append to res
        # return the k-1 element
        tree = []
        # perform preorder traversal: left -> root -> right
        def dfs(node):
            # base case to return when node isn't valid
            if not node:
                return
            # left first
            dfs(node.left)
            # then the node
            tree.append(node.val)
            # then the right
            dfs(node.right)
        dfs(root)
        return tree[k-1]
