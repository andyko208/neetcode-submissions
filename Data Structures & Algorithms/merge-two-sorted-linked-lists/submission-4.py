# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        head = node = ListNode(0)
        # iterate through while pointers are valid
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                node.next = list2
                list2 = list2.next
            node = node.next
            # print(node.val)
        # make sure that all nodes are used
        if not list1:
            node.next = list2
        if not list2:
            node.next = list1
        
        return head.next