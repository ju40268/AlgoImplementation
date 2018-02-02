# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # Solution 1, iterative: O(n), O(1)
        if not root: return 
        res = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        return res
        
        # Solution 2, recursion: O(n), O(n)         
        if not root: return
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            success = self.inorderSuccessor(root.left, p)
            return success if success else root