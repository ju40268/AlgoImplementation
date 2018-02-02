# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        return self.compare(root.left, root.right)
        
        
    def compare(self, left, right):
        if left == None and right == None: return True
        if left and right and left.val == right.val:
            return self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else: return False