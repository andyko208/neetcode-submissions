# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Floyd's algorithm to find the middle
        # keep slow and fast pointer to move slow to middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # partition into two linkedlists
        # reverse the second linkedlist
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # merge the first and second into one by alternating
        first, second = head, prev
        while second:
            # keep the next elements of first and second
            tmp1, tmp2 = first.next, second.next
            # first.next = second
            first.next = second
            # second.next = first.next
            second.next = tmp1
            # first, second = first.next, second.next
            first, second = tmp1, tmp2
        # return head