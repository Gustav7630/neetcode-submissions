# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
       #BFS
        if(root == None):
            return root
        queue = [root]

        while len(queue) > 0:
            current = queue[0]
            queue.pop(0)
            temp = current.left
            if(current.left):
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)
            current.left = current.right
            current.right = temp
        return root
        