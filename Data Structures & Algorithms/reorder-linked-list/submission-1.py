# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head ==None:
            return None

        chain1 = head
        fast = head
        slow = head
        
        count = 0
        #find middle
        while fast:
            count +=1
            slow = slow.next
            fast = fast.next
            if(fast):
                fast = fast.next
        
        back1 = head
        for i in range(count - 1):
            back1 = back1.next
        back1.next = None
        #detatch middle from chain 1
        #reverse and re insert 2

        def reverseL(head):
            newHead = head
            if(head == None):
                return None
            
            if(head.next):
                newHead = reverseL(head.next)
                head.next.next = head
            head.next = None
            return newHead
        
        middle = slow
        
        
        chain2 = reverseL(slow)
        

        while chain1!= middle and chain2:
            temp = chain1.next
            chain1.next = chain2
            
            chain1 = temp
            temp = chain2.next
            chain2.next = chain1
            chain2 = temp
        

            
            




        
        
        
                
        



            