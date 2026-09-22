# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # two pointers for each l1 and l2
        # l1, l2 = list1, list2
        # merged = None
        # # return the other node if one is none
        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1
        # # set the head to the smaller
        # if l1.val <= l2.val:
        #     merged = l1
        #     l1 = l1.next
        # else:
        #     merged = l2
        #     l2 = l2.next
        # # keep a head to return
        # head = merged
        # # keep a merged node to set merged.next to based on compariosn with l1 and l2
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         merged.next = l1
        #         l1 = l1.next
        #     else:
        #         merged.next = l2
        #         l2 = l2.next
        #     merged = merged.next
        # merged.next = l2 if l2 else l1
        
        # return head
        
        # base case for list1 and list2
        if not list1:
            return list2
        elif not list2:
            return list1
        # if list1.val <= list2.val, recurse on list1.next and list2 for list.next then return list1 or list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        # else, recurse on list2.next and list1 for list2.next
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2




