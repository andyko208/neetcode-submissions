# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check for the same binary tree
        def dfs(node):
            if not node:
                return False
            elif node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            return False
        
        if not root:
            return False
        elif not subRoot:
            return True
        return dfs(root)