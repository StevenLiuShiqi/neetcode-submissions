# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def twoadd(self, n1, n2, n3):
        res = n1 + n2 + n3
        r0 = res % 10
        r1 = res // 10
        return r0, r1

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1s, l2s = l1, l2
        lres = ListNode()
        prev = ListNode()
        start = prev
        cout = 0
        while l1 and l2:
            sum0, temp = self.twoadd(l1.val, l2.val, cout)
            lres = ListNode(sum0)
            cout = temp
            l1, l2, prev.next = l1.next, l2.next, lres
            prev = prev.next

        while l1:
            sum0, temp = self.twoadd(l1.val, 0, cout)
            lres = ListNode(sum0)
            cout = temp
            l1, prev.next = l1.next, lres
            prev = prev.next
        
        while l2:
            sum0, temp = self.twoadd(l2.val, 0, cout)
            lres = ListNode(sum0)
            cout = temp
            l2, prev.next = l2.next, lres
            prev = prev.next
        
        if cout != 0:
            prev.next = ListNode(cout)

        return start.next
