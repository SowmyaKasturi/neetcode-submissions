# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def get_number(head):
            exp = 0
            number = 0
            while head:
                number += (head.val * pow(10, exp))
                exp += 1
                head = head.next
            return number
        str_sum = str(get_number(l1) + get_number(l2))[::-1]
        res = ListNode(0)
        dummy = res
        for i in str_sum:
            res.next = ListNode(int(i))
            res = res.next
        return dummy.next
        

