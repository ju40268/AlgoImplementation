# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        final = []
        return self.traverse(root, final)
        
    def traverse(self, root, final):
        if root == None: return 
        final.append(root.val)
        self.traverse(root.left, final)
        self.traverse(root.right, final)
        return final

# iterative ==> use stack, LIFO to achieve the order
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final, stack = [], []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                final.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return final