# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # recursive fn
        def rec(root, cur):
            # base case
            if not cur:
                return root
            
            # recursive call to move cur to right end
            root = rec(root, cur.next)
            if not root:
                return None

            # unwinding
            tmp = None
            # break if crosses at the middle
            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                # connect back with cur: 2->3
                root.next = cur
                # connect cur with back: 1->2
                cur.next = tmp
            
            return tmp
        head = rec(head, head.next)


