# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        l, r = head, head.next
        count = 2
        while r:
            if r == l:
                return True
            if count == 0:
                l = l.next
                count = 2
            r = r.next
            count -= 1
        return False