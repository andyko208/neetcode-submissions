# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        pp = deque([p])
        qq = deque([q])
        while pp and qq:
            curP = pp.popleft()
            curQ = qq.popleft()
            
            if not curP and not curQ:
                continue
            elif not curP or not curQ:
                return False
            elif curP.val != curQ.val:
                return False
            pp.append(curP.left)
            pp.append(curP.right)
            qq.append(curQ.left)
            qq.append(curQ.right)
        return True