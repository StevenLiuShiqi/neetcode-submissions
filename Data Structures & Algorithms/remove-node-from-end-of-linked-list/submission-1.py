# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        for i in range(n):
            f = f.next

        s = head
        prev = None
        while f:
            f = f.next
            prev = s
            s = s.next
        if prev:
            prev.next = s.next
        else:
            return head.next

        return head
        
        