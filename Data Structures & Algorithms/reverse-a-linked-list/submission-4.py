# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 0 -> None
        # base case 
        if not head or not head.next:
            return head
        # get the tail to return at the end
        tail = self.reverseList(head.next)
        # reverse the direction of the nodes
        head.next.next = head
        head.next = None

        return tail