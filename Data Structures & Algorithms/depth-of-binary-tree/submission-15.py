# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        # keep a stack with (root, 1)
        stack = [(root, 1)]
        # keep a maxDepth variable
        maxDepth = 0
        # while stack is not empty
        while stack:
            # pop a node from the stack
            node, depth = stack.pop()
            # if node is valid
            if node:
                # update maxDepth to be the max between itself and depth
                maxDepth = max(maxDepth, depth)
                # push node.left, depth + 1
                stack.append((node.left, depth + 1))
                # push node.right, depth + 1
                stack.append((node.right, depth + 1))
        # return maxDepth
        return maxDepth