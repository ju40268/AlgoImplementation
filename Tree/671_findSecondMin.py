# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        final = []
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                final.append(node.val)
                if(node.left): queue.append(node.left)
                if(node.right): queue.append(node.right)
        final.sort()
        return self.getSecondMin(final) 
         
    
    def getSecondMin(self, nums):
        for i in range(len(nums)-1):
            if (nums[i] != nums[i+1]): return nums[i+1]
        return -1