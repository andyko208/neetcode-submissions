# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS
        # # base case
        # if not root:
        #     return 0
        # # DFS on left and right
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # BFS
        q = deque()
        if root:
            q.append(root)
        maxDepth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxDepth += 1
        return maxDepth