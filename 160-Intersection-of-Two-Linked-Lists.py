# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p2 != p1:
            p2 = p2.next
            p1 = p1.next

            
            if not p1 and p2 :
                p1 = headB
            if not p2 and p1:
                p2 = headA

        return p1
        