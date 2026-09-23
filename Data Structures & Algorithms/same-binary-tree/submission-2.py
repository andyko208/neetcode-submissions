# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS without additional list
        if not q and not p:
            return True
        elif not q:
            return False
        elif not p:
            return False
        qp = deque([q])
        pp = deque([p])
        while qp and pp:
            for _ in range(len(pp)):
                nodeQ = qp.popleft()
                nodeP = pp.popleft()
                if nodeP is None and nodeQ is None:
                    continue
                elif nodeP is None and nodeQ is not None:
                    return False
                elif nodeP is not None and nodeQ is None:
                    return False
                elif nodeP.val != nodeQ.val:
                    return False
                qp.append(nodeQ.left)
                qp.append(nodeQ.right)
                pp.append(nodeP.left)
                pp.append(nodeP.right)
        return True

