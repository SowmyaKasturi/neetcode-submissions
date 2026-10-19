# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        def get_count(root, prev):
            if not root: 
                return 0
            good = 1 if root.val >= prev else 0 
            prev = max(root.val, prev)
            return good+get_count(root.left, prev) + get_count(root.right, prev)
        return get_count(root, root.val)