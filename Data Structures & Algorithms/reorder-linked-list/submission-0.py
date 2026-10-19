# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        init_h = head
        temp = head
        while head:
            count += 1
            head = head.next
        count = count // 2
        _t = 1

        while _t <= count:
            temp = temp.next
            _t += 1
        half = temp.next
        prev = None
        next_n = half
        while half:
            next_n = half.next
            half.next = prev
            prev = half
            half = next_n
        half = prev
        temp.next = None
        while init_h and half:
            temp_h = init_h.next
            init_h.next = half
            temp = half.next
            half.next = temp_h
            init_h = temp_h
            half = temp
            