# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack traces
        # reverseList(3) newHead = node 3
        # reverseList(2) 
        # 2.next.next = 2 -> 3.next = 2
        # 2.next = None
        # reverseList(1)
        # 1.next.next = 1 -> 2.next = 1
        # 1.next = None
        # reverseList(0)
        # 0.next.next = 0 -> 1.next = 0
        # 0.next = None
        # newHead = node(5)
        if not head or not head.next:
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail