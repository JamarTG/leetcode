# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(-1,head)
        fast = slow = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        right = slow.next
        slow.next = None
        left = None
        curr = head

        while curr:
            nexx = curr.next
            curr.next = left
            left = curr
            curr = nexx
    
        result = 0

        while left:
            result = max(result,left.val + right.val)
            left = left.next
            right = right.next
        return result