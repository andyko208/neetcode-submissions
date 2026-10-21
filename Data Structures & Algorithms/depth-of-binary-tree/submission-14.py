# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS - Time: O(n), Space: O(n)
        if not root:
            return 0
        # queue with root
        q = deque([root])
        # lv at 0
        lv = 0
        # while q is not empty
        while q:
            # iterate through for loop for the length of the elements in q
            for i in range(len(q)):
                # pop a node from the left
                node = q.popleft()
                # if node.left, push node.left to queue
                if node.left:
                    q.append(node.left)
                # if node.right, push node.right to queue
                if node.right:
                    q.append(node.right)
            # increment lv by 1
            lv += 1
        # return lv
        return lv