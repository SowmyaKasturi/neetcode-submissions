# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head, stop):
            prev = None
            curr=head
            while curr:
                if curr == stop:
                    return prev,head
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            return prev, head

        result = None
        while head:
            not_enough = 0
            temp_head = head
            for i in range(k):
                if not head:
                    not_enough = 1
                    break
                val = head.val
                head = head.next
            if not result:
                result, tail = reverse(temp_head, head)
            elif not_enough != 1:
                tail.next, tail = reverse(temp_head, head)
            else:
                tail.next, tail = temp_head, None
        return result

