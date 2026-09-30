# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # BFS
        res = []
        # keep a q
        q = deque([root])
        while q:
            curs = []
            # iterate i from 0 to n of q
            for i in range(len(q)):
                # popleft
                cur = q.popleft()
                if cur:
                    # append to currs
                    curs.append(cur.val)
                    # check if node.left and node.right to append to q
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            # append curs to res
            res.append(curs)
        # return res
        return res