# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # ✅ Handle negative values
        
        def helper(node):
            if not node:
                return 0
            
            # ✅ Compute max path sum including left & right children (ignore negative sums)
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            
            # ✅ Update global max sum considering the current node as a peak
            self.max_sum = max(self.max_sum, left + right + node.val)
            
            # ✅ Return max path sum extendable to parent (either left or right)
            return node.val + max(left, right)
        
        helper(root)
        return self.max_sum  # ✅ Return global max sum

