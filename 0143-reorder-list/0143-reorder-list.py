# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        def find_middle(head):
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = find_middle(head)
        second_half = mid.next
        mid.next = None

        def rev_list(head):
            prev, current = None, head
            while current:
                next_node = current.next
                current.next = prev
                prev, current = current, next_node
            return prev
        
        second_half = rev_list(second_half)
        first_half = head
        while first_half and second_half:
            first_next = first_half.next
            second_next = second_half.next
            
            first_half.next = second_half
            second_half.next = first_next
            
            first_half = first_next
            second_half = second_next

            





        """
        Do not return anything, modify head in-place instead.
        """
        