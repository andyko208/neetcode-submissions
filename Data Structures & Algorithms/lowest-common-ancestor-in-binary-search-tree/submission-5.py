# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # while loop to traverse down the node 
        while root:
            # move pointer to left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # move pointer to right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # return the root
            else:
                return root

        