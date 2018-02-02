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
        if root == None: return True
        final = []
        result = self.inorderTraversal(root, final)
        return self.checkAscending(result)
    
    def checkAscending(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i+1]: return False
        return True
        
        
    def inorderTraversal(self, root, final):
        if root == None: return
        self.inorderTraversal(root.left, final)
        final.append(root.val)
        self.inorderTraversal(root.right, final)
        return final