# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse the second half of the linkedlist
        # move a pointer to the second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # make sure the first half doesn't contain a cycle
        curr = slow.next
        prev = slow.next = None
        # reverse the pointer of the second half
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # start from head to set next to by taking turns
        while prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2
        # return head


