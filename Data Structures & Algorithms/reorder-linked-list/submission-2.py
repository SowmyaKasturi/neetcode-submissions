# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        slow, fast = head, head
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
    
        first, second  = head, prev
        
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second  = temp1, temp2
            