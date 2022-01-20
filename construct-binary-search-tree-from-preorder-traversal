# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        count = 1
        while count < len(preorder) and preorder[count] < root.val:
            count += 1
        root.left = self.bstFromPreorder(preorder[1:count])
        root.right = self.bstFromPreorder(preorder[count:])
        print(f'root = {root} ')

        return root
                      
class Solution:
    def bstFromPreorder(self, pre_order: List[int]) -> TreeNode:
        iterator = iter(pre_order)
        root = current = TreeNode(next(iterator))
        for val in iterator:
            node = TreeNode(val)
            if node.val < current.val:
                node.right = current
                current.left = current = node
            else:
                while current.right is not None and node.val > current.right.val:
                    current.right, current = None, current.right

                node.right = current.right
                current.right = current = node

        while current.right is not None:
            current.right, current = None, current.right

        return root           
