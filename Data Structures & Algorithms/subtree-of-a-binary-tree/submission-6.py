# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            return False
        
        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            if dfs(node.left) or dfs(node.right):
                return True
            return False
        return dfs(root)