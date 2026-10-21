# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative DFS
        stack = [(p, q)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            stack.append([left.left, right.left])
            stack.append([left.right, right.right])
        return True
            
            
        