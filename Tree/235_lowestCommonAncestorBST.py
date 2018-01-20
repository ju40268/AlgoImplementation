# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if the root, or either node is null, return None
        if not root or not p or not q: return None
        # if both node are smaller than the root, then the answer should be on the left side tree
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        # if both node are greater than the root, then the answer should be on the right side tree
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
        # else p, q should be on different side of the tree, their common ancestor should be root
            return root