# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #dfs

        
        def dfs(root):

            if root == None:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return max(left,right) + 1

        dfs(root)    

        return self.balanced
        
        
        


