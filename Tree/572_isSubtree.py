# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check(s, t):
                # helper function that does the actual subtree check
                if (s is None) and (t is None):
                    return True
                if (s is None) or (t is None):
                    return False
                return (s.val == t.val and check(s.left, t.left) and check(s.right, t.right))

        # need to do a pre-order traversal and do a check
        # for every node we visit for the subtree
        if not s:
            # return False since None cannot contain a subtree 
            return
        if check(s, t):
            # we found a match
            return True
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            # a match was found
            return True
        return False
