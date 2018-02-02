# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum_num = 0
        if root == None: return 0
        if root.left and root.left.left == None and root.left.right == None:
            sum_num += root.left.val
        return sum_num + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)