# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = {}
        def level_order(level, root):
            if not root:
                return []
            result.setdefault(level, [])
            result[level].append(root.val)
            level_order(level+1, root.left)
            level_order(level+1, root.right)
            return result
        res = level_order(0, root)
        return [v for i,v in res.items()]
