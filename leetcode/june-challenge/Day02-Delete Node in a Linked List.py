# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next

# class Solution:
#     def deleteNode(self, node):
#         node_not_used = node.next
#         node.val, node.next = node.next.val, node.next.next
#         del node_not_used