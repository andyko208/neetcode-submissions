# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Intuition: recurse to move to the tail and perform addition w/ carry
        
        # Step 1. Create a recursive function with (l1, l2, carry) as args
        def addTwo(l1, l2, carry):
            # Step 2: base case
            if not l1 and not l2 and carry == 0:
                return None
            # Step 3: get l1 and l2 values if they exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Step 4: compute the sum of vals and divmod it to get the val and carry
            carry, val = divmod(val1 + val2 + carry, 10)
            
            # Step 5: recurse on the next node with l1.next and l2.next if valid
            next_node = addTwo(l1.next if l1 else None, l2.next if l2 else None, carry)
            return ListNode(val, next_node)
            

        # Step 6: return the recursive function with carry as 0 initially
        return addTwo(l1, l2, 0)
