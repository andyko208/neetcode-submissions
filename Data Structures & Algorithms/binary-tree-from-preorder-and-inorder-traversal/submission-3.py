# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # set up variables for tracking preorder list
        self.preInd = 0
        # map the values of inorder to indices
        inMap = {val: i for i, val in enumerate(inorder)}

        # define a recursive function that builds the tree
        def dfs(l, r):
            # base case to create empty node
            if l > r:
                return None
            # get the root val
            root_val = preorder[self.preInd]
            # increment preInd by 1
            self.preInd += 1
            # create the root node
            root = TreeNode(root_val)
            # lookup the root node from inMap
            mid = inMap[root_val]
            # recurse on the index of root exclusive
            root.left = dfs(l, mid-1)
            # recurse on the index of root exclusive
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(preorder)-1)
        {9: 0, 3:1, 15: 2, 20: 3, 7: 4}
        # preorder = 3 9 20 15 7
        # inorder = 9, 3, 15, 20, 7

        # root_val = 3, self.preInd -> create root node 3
        #     dfs(0, 0) -> self.preInd = 1 -> create left node of 9
        #         dfs(0, -1) -> empty left child of 9
        #     dfs(1, 4) -> self.preInd = 2 -> create right node of 20
        #         dfs(1, 2) -> self.preInd = 3 -> create left node of 15
        #             dfs(1, 1) -> self.preInd = 4 -> create left node of 7
                    





        