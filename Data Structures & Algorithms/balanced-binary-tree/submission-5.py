# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_subtree_height(root):
            if not root:
                return 0
            left = get_subtree_height(root.left)
            right = get_subtree_height(root.right)
            if left == float('inf'):
                return float('inf')
            if right == float('inf'):
                return float('inf')
            if abs(left-right) > 1:
                return float('inf')
            return max(left, right) + 1
        return get_subtree_height(root) != float('inf')