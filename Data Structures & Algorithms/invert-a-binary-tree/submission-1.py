# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # base case
        # if not root:
        #     return None
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        # return root

        # BFS
        # create a dequeue of root
        if not root:
            return root
        q = deque([root])
        while q:
            node = q.popleft()
            # perform the operation
            node.left, node.right = node.right, node.left
            # push to dequeue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root