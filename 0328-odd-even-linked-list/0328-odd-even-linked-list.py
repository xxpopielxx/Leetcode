# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head_even = tail_even = ListNode(0)
        head_odd = tail_odd = ListNode(0)

        current = head
        is_even = False  

        while current:
            next_node = current.next
            current.next = None
            if is_even:
                tail_even.next = current
                tail_even = tail_even.next
            else:
                tail_odd.next = current
                tail_odd = tail_odd.next
            is_even = not is_even 
            current = next_node

       
        tail_odd.next = head_even.next

        return head_odd.next

        