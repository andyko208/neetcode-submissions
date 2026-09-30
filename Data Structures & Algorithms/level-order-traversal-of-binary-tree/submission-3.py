# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = {}
        # DFS
        def dfs(node, depth):
            # keep a depth to append to
            # base case to return if not node
            if not node:
                return
            # if not res[depth], res[depth] = []
            if depth not in nodes:
                nodes[depth] = [node.val]
            # else, res[depth].append node.val 
            else:
                nodes[depth].append(node.val)
            # recurse on dfs(node.left, depth+1)
            dfs(node.left, depth+1)
            # recurse on dfs(node.right, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return [nodes[i] for i in range(len(nodes.keys()))]

            