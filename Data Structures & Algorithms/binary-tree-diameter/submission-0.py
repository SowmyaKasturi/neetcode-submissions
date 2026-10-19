# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def get_diameter(root):
            if not root:
                return 0
            left = get_diameter(root.left)
            right = get_diameter(root.right)
            self.diameter = max(left+right, self.diameter) 
            return max(left, right) + 1
        get_diameter(root)
        return self.diameter
