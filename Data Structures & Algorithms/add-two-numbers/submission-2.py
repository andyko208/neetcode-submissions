# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # iterate through l1 and l2 and append each val to a list
        # l1Str, l2Str = "", ""
        # while l1:
        #     # sum them up element wise
        #     l1Str += str(l1.val)
        #     l1 = l1.next
        # while l2:
        #     l2Str += str(l2.val)
        #     l2 = l2.next
        # # reverse of the sum
        # total = str(int(l1Str[::-1]) + int(l2Str[::-1]))[::-1]
        # # create a new node and set its val to the sum of digits one by one
        # head = node = ListNode(val=int(total[0]))
        # # set corresponding next node
        # for i in range(1, len(total)):
        #     node.next = ListNode(val=int(total[i]))
        #     node = node.next
        # node.next = None
        # return head

        # now do this recursively
        # one recursive function to get the reverse sum
        # base case to return
        def addl1l2(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, val = divmod(val1 + val2 + carry, 10)
            next_node = addl1l2(
                l1.next if l1 else None,
                l2.next if l2 else None,
                carry
            )
            return ListNode(val=val, next=next_node)
        return addl1l2(l1, l2, 0)


