# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev_list(head):
            prev, current = None, head
            while current:
                temp = current.next
                current.next = prev
                prev, current = current, temp
            return prev

        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        if not head or k == 1:
            return head
        n = get_length(head)

        if n < k:
            return head

        dummy = ListNode(0) 
        dummy.next = head
        prev_end = dummy 
        current = head

        for _ in range(n // k):
            start = current 
            end = current

            for _ in range(k - 1):
                end = end.next

            next_start = end.next
            end.next = None

            reversed_start = rev_list(start)
            prev_end.next = reversed_start

            prev_end = start
            current = next_start

        
        prev_end.next = current

        return dummy.next

                


        
        