# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        def dfs(node, p, q):
            # if p and q are both on the left, recurse on root.left
            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)
            # if p and q are both on the right, recurse on root.right
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
            # else return root
            else:
                return node
        return dfs(root, p, q)