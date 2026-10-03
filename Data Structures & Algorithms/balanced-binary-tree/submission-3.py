# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get the left and right and keep track whenever their diff is > 1
        def dfs(node):
            # base case
            if not node:
                return [True, 0]
            # get the left and right height
            l = dfs(node.left)
            r = dfs(node.right)
            # determine the balance
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1
            # return it to the root with the height
            return [balanced, max(l[1], r[1]) + 1]
        return dfs(root)[0]
        # self.balanced = True
        # def dfs(node):
        #     if not node:
        #         return 0
        #     l = dfs(node.left)
        #     r = dfs(node.right)
        #     if l + r > 1:
        #         self.balanced = False
        #     return max(l, r) + 1
        # dfs(root)
        # return self.balanced