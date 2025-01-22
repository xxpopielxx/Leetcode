# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        prev, current = sentinel, head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = prev.next   
            current = current.next
        return sentinel.next

        