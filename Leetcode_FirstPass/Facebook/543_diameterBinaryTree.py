# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if not root: return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.res = max(self.res, l+r)
        return max(l, r) + 1