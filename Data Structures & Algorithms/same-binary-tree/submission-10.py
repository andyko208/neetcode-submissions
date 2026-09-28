# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # create two dequeus for p and q to return its equivalency
        # pq, qq = deque([p]), deque([q])
        # while pq and qq:
        #     curP = pq.popleft()
        #     curQ = qq.popleft()
        #     # when root have different values
        #     if not curP and not curQ:
        #         continue
        #     if not curP or not curQ or curP.val != curQ.val:
        #         return False
        #     pq.append(curP.left)
        #     pq.append(curP.right)
        #     qq.append(curQ.left)
        #     qq.append(curQ.right)
        # return True

        # DFS
        def dfs(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False
        return dfs(p, q)


