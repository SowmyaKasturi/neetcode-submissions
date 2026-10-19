# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next
        c = 0
        t = head
        if count == n:
            return head.next
        while c < (count-n-1):
            t = t.next
            c += 1
        if t.next:
            t.next = t.next.next
        return head
            
        