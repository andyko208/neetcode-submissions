# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # keep a slow and fast pointer to iterate through to return True if meet
        # Time: O(n)
        # Space: O(n)
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            # if there is a cycle, two pointers will eventually meet
            if fast == slow:
                return True
            # update the pointers
            fast = fast.next.next
            slow = slow.next
        return False
            