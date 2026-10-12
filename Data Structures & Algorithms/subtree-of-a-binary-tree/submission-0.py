# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def isLeftIdentical(root,subRoot):
            if root and subRoot:
                if root.val != subRoot.val:
                    #print("1")
                    return False

            if not root and not subRoot:
                #print("2")
                return True
            if not root and subRoot or root and not subRoot: 
                #print("3")
                return False
           # print("4")
            return isLeftIdentical(root.left,subRoot.left) and isLeftIdentical(root.right,subRoot.right)
        nodes = []
        def dfs(root):
            if root:
                nodes.append(root)
                if root.left:
                    
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
        dfs(root)
        for n in nodes:
            #print(n.val)
            if isLeftIdentical(n,subRoot):
                return True  
        return False
            


        