# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # push all node to a list
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nodeLen = len(nodes)
        print(nodes)
        # remove element at len(list) - n
        remove = nodeLen - n
        # # check if both
        # if 0 <= l and r < Len:
        #     lList[l].next = lList[r]
        # # check if we have element only to the left
        # elif 0 <= l and r >= Len:
        #     lList[l].next = None
        # # check if we have element only to the right
        # elif l < 0 and r < n:
        #     return lList[r]
        # else:
        #     return None
        if remove <= 0:
            return head.next
        nodes[remove-1].next = nodes[remove].next
        return head
        