# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        \\\
        :type head: ListNode
        :rtype: ListNode
        \\\

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if fast == slow:
                break
        
        if not fast or not fast.next:
            return None

        slow = head

        while fast:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        return fast
