# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)
    
    def dfs(self, root):
        if root == None: return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        
        return max(l,r)+1