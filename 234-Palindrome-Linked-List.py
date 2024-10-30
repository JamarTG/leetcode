# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(-1,head)
        slow = fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   

        curr = slow.next
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        right = prev
        left = head
     
        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True