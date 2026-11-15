# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # keep two pointers, one to store the right and one for left to switch direction
        # handle edge case
        if not head:
            return None
        prev, cur = head, head.next
        # update the new tail
        prev.next = None
        # itereate through the linked list
        while cur:
            # preserve the next pointer
            next = cur.next
            # switch the direction
            cur.next = prev
            # update the pointers
            prev = cur
            cur = next
        return prev

