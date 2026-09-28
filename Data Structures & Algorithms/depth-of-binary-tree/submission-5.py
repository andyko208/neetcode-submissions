# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS
        # def dfs(node):
        #     if not node:
        #         return 0
        #     left, right = 0, 0
        #     if node.left:
        #         left = dfs(node.left)
        #     if node.right:
        #         right = dfs(node.right)
        #     return max(left, right) + 1
                
        # return dfs(root)
        # BFS
        if not root:
            return 0
        q = deque([root])
        lv = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if not cur:
                    continue
                if cur.left:
                    q.append(cur.left)        
                if cur.right:
                    q.append(cur.right)
            lv += 1
        return lv
            



