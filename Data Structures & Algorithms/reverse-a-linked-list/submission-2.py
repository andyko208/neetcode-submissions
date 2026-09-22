# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head:
            return None
        newHead = head
        # check if next is valid
        if head.next:
            # recursive call to move head to the last
            newHead = self.reverseList(head.next)
            # reverse the direction
            head.next.next = head
        # set head's next to None
        head.next = None
        # return newHead
        return newHead