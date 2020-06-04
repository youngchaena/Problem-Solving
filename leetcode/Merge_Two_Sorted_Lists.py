# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sorted_list = ListNode()
        node = sorted_list
        
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                node = node.next
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                node = node.next
                l2 = l2.next
        
        while not l1 and l2:
            node.next = ListNode(l2.val)
            node = node.next
            l2 = l2.next
        
        while l1 and not l2:
            node.next = ListNode(l1.val)
            node = node.next
            l1 = l1.next
        
        return sorted_list.next