# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # move a pointer to the mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the linked list
        prev, curr = None, slow.next
        # must set none to slow.next
        slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # keep one pointer from the back and the other on head to merge one after another
        front, back = head, prev
        while back:
            tmp1, tmp2 = front.next, back.next
            back.next = tmp1
            front.next = back
            front, back = tmp1, tmp2
