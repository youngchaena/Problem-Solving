# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Stack을 활용한 방법 -> O(N) / O(N)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stk = []
        node = head
        
        while node:
            stk.append(node.val)
            node = node.next
        
        head = node = ListNode(stk.pop()) if len(stk) != 0 else None
        
        while len(stk) != 0:
            node.next = ListNode(stk.pop())
            node = node.next
            
        return head

# 순회해서 푸는 방법
# 재귀함수로 푸는 방법