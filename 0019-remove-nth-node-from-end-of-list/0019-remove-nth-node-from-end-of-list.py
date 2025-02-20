# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        if length == 1 and n == 1:
            return None
        
        cnt = length - n
        if cnt == 0:
            return head.next
        
        prev, current = None, head
        for i in range(cnt):
            prev, current = current, current.next
        
        prev.next = current.next
        
        return head
