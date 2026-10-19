# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1
        
        dummy = ListNode()
        temp = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        if head1:
            temp.next = head1
        
        elif head2:
            temp.next = head2
        return dummy.next