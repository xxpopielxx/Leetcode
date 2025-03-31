# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insert(newnode, sorted_head):
            if sorted_head is None or sorted_head.val >= newnode.val:
                newnode.next = sorted_head
                return newnode
            else:
                current = sorted_head

                while current.next and current.next.val < newnode.val:
                    current = current.next
                newnode.next = current.next
                current.next = newnode
                return sorted_head
                
        sorted_head = None
        current = head
        while current:
            next_node = current.next

            sorted_head = insert(current, sorted_head)

            current = next_node
        return sorted_head



        