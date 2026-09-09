# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast:
            for i in range (5):

                fast = fast.next
                if(fast == None):
                    return False
            slow = slow.next
            if fast == slow:
                return True
        return False
        