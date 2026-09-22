# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # push all node to a list
        lList = []
        curr = head
        while curr:
            lList.append(curr)
            curr = curr.next
        Len = len(lList)
        print(lList)
        # remove element at len(list) - n
        l, r = Len - n - 1, Len - n + 1
        # check if both
        if 0 <= l and r < Len:
            lList[l].next = lList[r]
        # check if we have element only to the left
        elif 0 <= l and r >= Len:
            lList[l].next = None
        # check if we have element only to the right
        elif l < 0 and r < n:
            return lList[r]
        else:
            return None
        return head
        