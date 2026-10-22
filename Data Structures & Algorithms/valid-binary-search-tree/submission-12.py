# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float('-inf'), float('inf'))])
        while q:
            cur, minVal, maxVal = q.popleft()
            if not cur:
                continue
            if not (minVal < cur.val < maxVal):
                return False
            if cur.left:
                q.append((cur.left, minVal, cur.val))
            if cur.right:
                q.append((cur.right, cur.val, maxVal))
        return True