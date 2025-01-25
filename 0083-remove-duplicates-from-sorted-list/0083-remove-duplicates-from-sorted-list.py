# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        dictionary = {}
        while current:
            dictionary[current.val] = dictionary.get(current.val, 0) + 1
            current = current.next

        Dummy = ListNode(0, head)
        prev, current = Dummy, head
        while current:
            if dictionary[current.val] > 1:
                dictionary[current.val] = dictionary.get(current.val) - 1
                prev.next = current.next
                
            else:
                prev = prev.next
            current = current.next
        
        return Dummy.next


        