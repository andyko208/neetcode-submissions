# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS with hashmap
        levelMap = defaultdict(list)
        def dfs(node, depth):
            if not node:
                return
            levelMap[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)
        return [levelMap[i+1] for i in range(len(levelMap))]
# levelMap = {1: [1], 2: [2, 3], 3: [4, 5, 6, 7]}