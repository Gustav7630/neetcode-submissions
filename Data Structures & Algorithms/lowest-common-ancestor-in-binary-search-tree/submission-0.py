# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #two dfs, then reverse to find common

        pres = ""
        qres = ""
        def dfs(node,path,target):
            

            if node.val == target:
                path.append(node)
                return path
            
            if target > node.val:
                path = dfs(node.right,path,target)
                path.append(node)
                return path
            else:
                path = dfs(node.left,path,target)
                path.append(node)
                
                return path
        ppath = dfs(root,[],p.val)
        qpath = dfs(root,[],q.val)
        pmap = {ppath[i]:i for i in range(len(ppath))}
        
        
        for i in ppath:
            pres += str(i.val) + ","
        for i in qpath:
            qres += str(i.val) + ","
        print(pres)
        print(qres)
        for i in qpath:
            if i in ppath:
                return i


            

        