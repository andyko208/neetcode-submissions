# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtree_ids = {}
        root_ids = set()

        def get_id(node, collect=False):
            if node is None:
                return 0

            left_id = get_id(node.left, collect)
            right_id = get_id(node.right, collect)

            key = (node.val, left_id, right_id)

            if key not in subtree_ids:
                subtree_ids[key] = len(subtree_ids) + 1

            current_id = subtree_ids[key]

            if collect:
                root_ids.add(current_id)

            return current_id

        get_id(root, True)
        target_id = get_id(subRoot)

        return target_id in root_ids
