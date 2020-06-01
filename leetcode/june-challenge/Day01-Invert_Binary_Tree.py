# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        if root.left:
            root.left = self.invertTree(root.left)
        if root.right:
            root.right = self.invertTree(root.right)
        return root


# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#         return root