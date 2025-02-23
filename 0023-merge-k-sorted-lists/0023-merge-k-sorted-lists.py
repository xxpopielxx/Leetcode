# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(a, b):
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
            tail.next = a or b
            return dummy.next

        def merge_sort(head):
            if not head or not head.next:
                return head

            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None  
            left = merge_sort(head)
            right = merge_sort(mid)
            return merge(left, right)

        merged_list = None
        for lst in lists:
            merged_list = merge(merged_list, lst)

        return merge_sort(merged_list)

        