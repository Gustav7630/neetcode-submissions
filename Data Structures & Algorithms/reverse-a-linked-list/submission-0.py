# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
             return None
        step = ListNode(head.val,None)
        while head.next != None:
            head = head.next
            step = ListNode(head.val,step)
        
        return step
            
        