# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.helper(root, float('inf'), float('-inf'))
    
    def helper(self, root, max_val, min_val):
        if not root: return True
        if root.val >= max_val or root.val <= min_val: return False
        return self.helper(root.left, root.val, min_val) and self.helper(root.right, max_val, root.val)