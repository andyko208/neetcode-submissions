# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # move one pointer to the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half and partition into two list
        curr = slow.next
        slow.next = None  # cuts off the first list
        prev = None # cuts off the second list as we set curr.next = prev(None)
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # merge first and second
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2





