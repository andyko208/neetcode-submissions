# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers for each l1 and l2
        l1, l2 = list1, list2
        merged = None
        # return the other node if one is none
        if not l1:
            return l2
        elif not l2:
            return l1
        # set the head to the smaller
        if l1.val <= l2.val:
            merged = l1
            l1 = l1.next
        else:
            merged = l2
            l2 = l2.next
        # keep a head to return
        head = merged
        # keep a merged node to set merged.next to based on compariosn with l1 and l2
        while l1:
            if not l2:
                merged.next = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        while l2:
            merged.next = l2
            l2 = l2.next
            merged = merged.next
        
        return head