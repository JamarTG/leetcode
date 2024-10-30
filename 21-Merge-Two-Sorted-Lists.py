# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
         
        dummy = ListNode(-1, None) 
        newLL = dummy

        while list1 and list2:
            if list1.val < list2.val:
                newLL.next = list1
                list1 = list1.next
            else:
                newLL.next = list2
                list2 = list2.next

            newLL = newLL.next
        
        if list1:
            newLL.next = list1
        else:
            newLL.next = list2
        
        return dummy.next
