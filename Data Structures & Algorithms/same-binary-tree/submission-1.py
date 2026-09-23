# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # keep two lists for each p and q
        listP, listQ = [], []
        # append elements to p_list and q_list each
        def bfs(root):
            if not root:
                return None
            deq = deque([root])
            nodes = [root.val]
            level = 0
            while deq:
                for i in range(len(deq)):
                    node = deq.popleft()
                    if node.left:
                        deq.append(node.left)
                        nodes.append(node.left.val)
                    else:
                        nodes.append(None)
                    if node.right:
                        deq.append(node.right)
                        nodes.append(node.right.val)
            return nodes

        # return p_list == q_list
        print(bfs(p), bfs(q))
        return bfs(p) == bfs(q)