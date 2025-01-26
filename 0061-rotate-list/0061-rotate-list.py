# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1    
        
        k %= length
        if k == 0:
            return head

        def rotate_1(head):
            current = head
            while current.next.next:
                current = current.next
            next_node = current.next
            current.next = None
            current = next_node
            current.next = head
            return current
        temp = head
        for i in range(k):
            temp = rotate_1(temp)
        return temp
        

