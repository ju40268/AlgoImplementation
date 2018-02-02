# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # DFS solution
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: return False


# Generating Error ==> Some not pass

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # DFS solution
        if p == None and q == None:
            return True
        stack = [(p,q)]
        
        while stack:
            l,r = stack.pop()
            if l == None and r == None:
                continue
            elif l and r and l.val and r.val:
                stack.append((l.left, r.left))
                stack.append((l.right, r.right))
            else: 
                return False
        
        return True