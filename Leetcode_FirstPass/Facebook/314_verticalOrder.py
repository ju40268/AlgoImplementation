import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        depth_dict = collections.defaultdict(list)
        
        def BFS(root):
            stack = collections.deque()
            stack.append((root,0))
            while stack:
                node,depth = stack.popleft()
                depth_dict[depth].append(node.val)                
                if node.left:
                    stack.append((node.left, depth-1))
                if node.right:
                    stack.append((node.right, depth+1))
                        
                    
        BFS(root)
        return [ values for keys, values in sorted(depth_dict.items(), key = lambda x: x[0])]
