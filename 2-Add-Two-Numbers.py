# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        val = 0
        start = ListNode(-1,None)
        curr = start


        while l1 or l2:
            l1_val = 0
            l2_val = 0

            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val
            
            summ = l2_val + l1_val + carry
            carry = 1 if summ > 9 else 0
            place = summ % 10
            
            new_node = ListNode(place,None)
            curr.next = new_node
            curr = new_node
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        

        if carry:
            curr.next = ListNode(carry,None)
        
        return start.next

        
        