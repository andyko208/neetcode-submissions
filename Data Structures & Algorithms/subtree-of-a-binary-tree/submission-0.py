# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # return true if no subtree to comapre root with
        if not subRoot:
            return True
        # return false if no root to comapre subtree with
        if not root:
            return False
        # check if the root has the same subtree
        if self.sameTree(root, subRoot):
            return True
        # check whether left or right child has the subtree
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))
        
    def sameTree(self, root, subRoot):
        # return true if both null
        if not root and not subRoot:
            return True
        # if both are non null and val are the same, recurse on left and right
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False


