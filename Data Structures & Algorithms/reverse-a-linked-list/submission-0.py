# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        if curr:
            next = curr.next
        else:
            return head
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            if next:
                next = next.next
        return prev