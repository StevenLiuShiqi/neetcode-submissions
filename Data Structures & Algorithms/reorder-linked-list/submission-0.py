# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def copiedNode(self, head):
        return ListNode(head.val, head.next)

    def reverselist(self, head: Optional[ListNode]):
        curr = head
        prev = None
        length = 0
        while curr:
            curr = ListNode(curr.val, curr.next)
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            length += 1
        
        return prev, length

    def reorderList(self, head: Optional[ListNode]) -> None:
        reversedL, length = self.reverselist(head)
        odd = length % 2
        res = ListNode()
        res_start = res
        for i in range(length // 2):
            res.next = head
            res = res.next
            head = head.next
            res.next = reversedL
            res = res.next
            reversedL = reversedL.next
        res.next = None

        if odd:
            head.next = None
            res.next = head
        
        head = res_start.next
