# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def dfs(node, p, q):
        #     # if p and q are both on the left, recurse on root.left
        #     if p.val < node.val and q.val < node.val:
        #         return dfs(node.left, p, q)
        #     # if p and q are both on the right, recurse on root.right
        #     elif p.val > node.val and q.val > node.val:
        #         return dfs(node.right, p, q)
        #     # else return root
        #     else:
        #         return node
        # return dfs(root, p, q)

        # BFS
        if not root or not p or not q:
            return None
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if p.val < cur.val and q.val < cur.val:
                queue.append(cur.left)
            elif p.val > cur.val and q.val > cur.val:
                queue.append(cur.right)
            else:
                return cur
        return root





