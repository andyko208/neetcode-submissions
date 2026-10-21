# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative DFS - Time: O(N), Space: O(N)
        if not root:
            return 0
        
        maxHeight = 1
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                maxHeight = max(maxHeight, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return maxHeight
            
