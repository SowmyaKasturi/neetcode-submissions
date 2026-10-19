"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # prev = None
        # temp = Node(0)
        # dummy = temp
        # h = head
        # random = dict()
        # while head:
        #     new = Node(head.val)
        #     temp.next = new
        #     temp = temp.next
        #     head = head.next
        # new_t = dummy.next
        # while h:
        #     if not h.random:
        #         new_t.random = None
        #     else:
        #         _n = dummy.next
        #         while h.random.val != _n.val:
        #             _n = _n.next
        #         new_t.random = _n
        #     h = h.next
        #     new_t = new_t.next

        # return dummy.next
        #interleave nodes
        curr = head
        while curr:
            new_node = Node(curr.val,curr.next,None)
            curr.next = new_node
            curr = curr.next.next
        #assign random pointers

        curr=head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        old_head = head
        new_head = head.next
        res = new_head
        while old_head:
            old_head.next = old_head.next.next
            new_head.next = new_head.next.next if new_head.next else None
            old_head = old_head.next
            new_head = new_head.next

        return res