# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for i in range(k-1):
            curr = curr.next
        

        left = head
        right = curr

        while right.next:
            left = left.next
            right = right.next

        curr.val,left.val = left.val, curr.val

        return head