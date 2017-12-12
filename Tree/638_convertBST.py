# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return []
        self.accumulate = 0
        return self.add(root)
    
    def add(self, root):
        if root == None: return
        self.add(root.right)
        root.val = root.val + self.accumulate
        self.accumulate = root.val
        self.add(root.left)
        return root