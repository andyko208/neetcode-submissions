# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # let one pointer move as twice as fast as the other and check if they meet
        # keep a slow and fast
        fast, slow = head, head
        # while fast and fast.next, slow = fast and fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False