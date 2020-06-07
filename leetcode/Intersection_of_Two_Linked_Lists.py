# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 공통값이 아니라 Node 주소를 기반으로 한 Intersection을 찾는다
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        len_a, len_b = 0, 0
        
        while pa:
            len_a += 1
            pa = pa.next
        while pb:
            len_b += 1
            pb = pb.next
        pa, pb = headA, headB
        
        if len_a > len_b:
            for i in range(abs(len_a - len_b)):
                pa = pa.next
        else:
            for i in range(abs(len_a - len_b)):
                pb = pb.next
        
        while pa is not pb:
            pa = pa.next
            if pa is pb: break
            pb = pb.next
        
        return pa

# 다른 사람 숏코딩 예제
class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa, pb = headA, headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa