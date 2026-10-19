# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # ✅ Base case should return True, not 0

        left = self.height(root.left)  # ✅ Use a helper function to get height
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False  # ✅ Correctly checks if the tree is unbalanced

        return self.isBalanced(root.left) and self.isBalanced(root.right)  # ✅ Recurse on both subtrees

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # ✅ Base case: Empty tree has height 0
        return max(self.height(root.left), self.height(root.right)) + 1 