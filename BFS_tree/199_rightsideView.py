# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        queue = [root]
        bfs_result = []
        final = []
        while(queue):
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if(node.right): queue.append(node.right)
                if(node.left): queue.append(node.left)         
            bfs_result.append(level)
        for i in bfs_result:
            final.append(i[0])       
        return final