# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current  = current.next
        if length == 1:
            return None
        def which(length):
            return length // 2
        cnt = which(length)

        prev, current = None, head
        for i in range(cnt):
            prev, current = current, current.next
        
        prev.next = current.next

        return head
