# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS
        # keep a tuple of left, root, and right in queue
        q = deque([(float('-inf'), root, float('inf'))])
        # while q
        while q:
            left, node, right = q.popleft()
            # return false if not left < root.val < right
            if not node or not (left < node.val < right):
                return False
            # if left, append (left, node.left, node.val)
            if node.left:
                q.append([left, node.left, node.val])
            # if right, append (node.val, node.right, right)
            if node.right:
                q.append([node.val, node.right, right])
        # return True
        return True