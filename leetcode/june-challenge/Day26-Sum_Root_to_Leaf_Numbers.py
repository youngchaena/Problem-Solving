# Day 26 - Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0
        self.dfs(root, 0)
        return self.total
        
    def dfs(self, root, num):
        if root:
            if not root.left and not root.right:
                self.total += 10 * num + root.val
            self.dfs(root.left, 10 * num + root.val)
            self.dfs(root.right, 10 * num + root.val)

