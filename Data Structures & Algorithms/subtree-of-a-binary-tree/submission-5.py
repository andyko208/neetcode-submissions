# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # create sameTree function 
        def sameTree(p, q):
            # base case
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            return False

        # traversal of root tree 
        def dfs(node):
            if not node:
                return False
            elif node.val == subRoot.val and sameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        
        return dfs(root)