"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # get a copy of all the nodes with val
        nodeMap = {}
        node = head
        while node:
            nodeMap[node] = Node(node.val)
            node = node.next
        curr = head
        while curr:
            nodeMap[curr].next = nodeMap.get(curr.next)
            nodeMap[curr].random = nodeMap.get(curr.random)
            curr = curr.next
        return nodeMap[head]