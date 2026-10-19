# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.null = "null"
        if not root:
            return self.null
        pre_order = []
        def get_preorder(root):
            if not root:
                pre_order.append(self.null)
                return 
            if root:
                pre_order.append(root.val)
                get_preorder(root.left)
                get_preorder(root.right)
        get_preorder(root)
        return "|".join(map(str,pre_order)) 
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_values = []
        data_values = data.split("|")
        if data == "null":
            return None
        def get_tree():
            if not data_values:
                return None
            val = data_values.pop(0)
            if val == "null":
                return 
            root = TreeNode(int(val))
            root.left = get_tree()
            root.right = get_tree()
            return root
        
        return get_tree()
