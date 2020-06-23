# Day 23 - Count Complete Tree Nodess

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        right_depth = self.getDepth(root.right)
        left_depth = self.getDepth(root.left)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)
        
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)