# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        slow, fast = head, head
        init_h = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        prev, half = None, slow.next
        slow.next = None
        next_n = None
        while half:
            next_n = half.next
            half.next = prev
            prev = half
            half = next_n
    
        half = prev
        
        while init_h and half:
            temp_h = init_h.next
            init_h.next = half
            temp = half.next
            half.next = temp_h
            init_h = temp_h
            half = temp
            