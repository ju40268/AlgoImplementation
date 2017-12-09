# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if root == None: return []
        # index = -1
        # final = []
        # queue = [root]
        # while queue:
        #     level = []
        #     for i in range(len(queue)): 
        #         print(i, len(queue))
        #         node = queue.pop(0)
        #         level.append(node.val)
        #         if index % 2 == 0:
        #             if(node.left): queue.append(node.left)
        #             if(node.right): queue.append(node.right)
        #         else:
        #             if(node.right): queue.append(node.right)
        #             if(node.left): queue.append(node.left)
        #     index = index + 1
        #     print(index)
        #     print(level)
        #     final.append(level)
        # return final
        
        if root == None: return []
        index = 0
        final = []
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)): 
                node = queue.pop(0)
                level.append(node.val)
                if(node.left): queue.append(node.left)
                if(node.right): queue.append(node.right)            
            if(index%2 == 0):
                final.append(level)
            else:
                final.append(level[::-1])
            index = index + 1
        return final