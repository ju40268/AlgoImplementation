# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        final = []
        result = self.traverse(root, final)
        return result[k-1]
        
    def traverse(self, root, final):
        if root == None: return
        self.traverse(root.left, final)
        final.append(root.val)
        self.traverse(root.right, final)
        return final

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        left_count = self.count(root.left)
        if left_count + 1 == k:
            return root.val
        elif left_count + 1 < k:
            return self.kthSmallest(root.right, k-(left_count + 1))
        else:
            return self.kthSmallest(root.left, k)
        
    def count(self, root):
        if root == None: return 0
        return self.count(root.left) + self.count(root.right) + 1

# 