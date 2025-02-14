# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None  

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return self.merge(left_sorted, right_sorted)

    def find_middle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        if b:
            tail.next = b

        return dummy.next
