# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_sorted(head1, head2):
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
        
        # Instead of an extra dummy node, initialize result properly
        result = None
        for i in lists:
            result = merge_sorted(result, i)  # Merge each list into result
        
        return result
