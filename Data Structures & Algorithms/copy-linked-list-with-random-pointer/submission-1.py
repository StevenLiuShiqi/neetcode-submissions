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
        if head == None:
            return None
        copiednodes = []
        headnodes = {}
        hStart = head
        i = 0
        while head:
            hc = Node(head.val)
            copiednodes.append(hc)                
            headnodes[head] = i
            head = head.next
            hc = hc.next
            i += 1

        hc = copiednodes[0]
        copiednodes.append(None)
        
        for j in range(len(copiednodes) - 1):
            hc.next = copiednodes[j + 1]
            if hStart.random != None:
                position = headnodes[hStart.random]
                hc.random = copiednodes[position]
            hStart = hStart.next
            hc = hc.next

        return copiednodes[0]

        



