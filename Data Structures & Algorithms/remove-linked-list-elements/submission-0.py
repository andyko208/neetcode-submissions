# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # base case to return itself 
        if not head:
            return head
        # if node.val == val, set node.next = recurse(node.next, val) and return node.next
        elif head.val == val:
            head.next = self.removeElements(head.next, val)
            return head.next
        # else, set node.next = recurse(node.next, val) adn return node
        else:
            head.next = self.removeElements(head.next, val)
            return head