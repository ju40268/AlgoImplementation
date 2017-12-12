# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return []
        final = []
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):           
                node = queue.pop(0)
                level.append(node.val)
                # print 'node val', node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            final.append(level)
        # after level order traversal, return the last element of list(should be the last level), and return the first element   
        return final[-1][0]