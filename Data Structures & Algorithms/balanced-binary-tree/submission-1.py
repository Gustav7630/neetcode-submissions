# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        #balanced = True


        def getHeight(root):
            if root == None:
                return -1
            
            return 1 + max(getHeight(root.left),getHeight(root.right))
        
        def balanceCheck(root):
            if root == None:
                return True

            balanceCheck(root.left)
            balanceCheck(root.right)

            if abs( getHeight(root.right) - getHeight(root.left)) < 2:
                #print("AHHHHHHHH")
                pass
            else:
                #print("bankai")
                self.balanced = False
            
        balanceCheck(root)
        return self.balanced
        
        
        


