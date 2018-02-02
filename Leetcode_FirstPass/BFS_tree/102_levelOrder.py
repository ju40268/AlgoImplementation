# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        final = []
        queue = [root]
#         while queue is not empty
        while queue:
            level = []
            for i in range(len(queue)):           
                node = queue.pop(0)
                level.append(node.val)
                # print 'node val', node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            final.append(level)
        return final