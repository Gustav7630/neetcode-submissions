# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #greedy

        stack1 = [p]
        stack2 = [q]

        if p and not q:
            return False
        if q and not p:
            return False
        
        if not p and not q:
            return True

        while stack1:

            t1 = stack1.pop()
            t2 = stack2.pop()

            #print(t1.val)
            #print(t1.left)
            #print(t2.left)
            #if(t1.left):
                #print("P")
           # if(t2.left):
                #print("Q")
            if t1.left and t2.left:
                stack1.append(t1.left)
                stack2.append(t2.left)
                #print("LEFT")
            
            if t2.right and t1.right:
                stack1.append(t1.right)
                stack2.append(t2.right)
                #print("RIGHT")

            if(t1.left and not t2.left) or (t2.right and not t1.right) or t2.left and not t1.left or (t2.right and not t1.right):
                return False
            
            if(t1.val != t2.val):
                return False
        
        return True