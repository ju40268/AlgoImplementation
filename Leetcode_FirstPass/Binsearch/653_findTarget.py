# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        final = []
        self.inorderTraversal(root, final)
        return self.binsearch(final, k)
        
    def inorderTraversal(self, root, final):
        if root == None: return
        self.inorderTraversal(root.left, final)
        final.append(root.val)
        self.inorderTraversal(root.right, final)
        return final
    
    def binsearch(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            while l <= r:
                mid = l + (r - l)/2
                if numbers[mid] == (target - numbers[i]):
                    return True
                elif numbers[mid] < (target - numbers[i]):
                    l = mid + 1
                else:
                    r = mid - 1
        return False