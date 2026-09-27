# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        q = deque([root])
        while q:
            cur = q.popleft()
            if not cur:
                return root
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            cur.left, cur.right = cur.right, cur.left
        return root