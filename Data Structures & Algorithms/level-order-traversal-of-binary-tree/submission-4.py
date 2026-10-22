# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # creating a deque with the root node
        # res = []
        res = []
        q = deque([root])
        # while q
        # q = []
        # lvList = [4, 5, 6, 7]
        # res = [[1], [2, 3], [4, 5, 6, 7]]
        if not root:
            return res
        while q:
            # lvList = []
            lvList = []
            # for loop iterate through len(q)
            for i in range(len(q)):
                # curr node = q.popleft()
                cur = q.popleft()
                # append left and right to the queue
                if cur.left:
                    q.append(cur.left)
                # lvList.append(curr node)
                if cur.right:
                    q.append(cur.right)
                lvList.append(cur.val)
            # res.append(lvList)
            res.append(lvList)
        # return res
        return res
        