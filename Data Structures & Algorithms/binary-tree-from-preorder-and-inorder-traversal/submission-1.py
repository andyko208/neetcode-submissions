# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        # Brute force: Time: O(n^2), Space: O(n)
        # Hashmap: Tine(O(n)), Space: O(n)
        # build a hashmap to reduce lookup of mid index to O(1)
        orderMap = {val: i for i, val in enumerate(inorder)}
        
        # if not preorder or not inorder:
        #     return None
        # separate variable to track preorder ind
        self.preInd = 0
        # create a separate recursive function to take range than slicing
        def dfs(l, r):
            # base case to return 0
            if l > r:
                return None
            rootVal = preorder[self.preInd]
            self.preInd += 1
            root = TreeNode(val=rootVal)
            mid = orderMap[rootVal]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(orderMap)-1)
        # # create the root
        # root = TreeNode(val=preorder[0])
        # # get the mid
        # mid = inorder.index(preorder[0])
        # # set the left child
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # # set the right child
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # return root