# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://stackoverflow.com/questions/13707457/python-value-that-occurs-the-most-in-a-list
# >>> freq_list = count.values()
# >>> freq_list
# [2, 2, 1, 1]
# >>> max_cnt = max(freq_list)
# >>> total = freq_list.count(max_cnt)

# >>> most_common = count.most_common(total)
# [('a', 2), ('c', 2)]

# >>> [elem[0] for elem in most_common]
# ['a', 'c']

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        final = []
        # find the biggest element in the collection/dictionary
        c = collections.Counter(self.traverse(root, final))
        max_ct = max(c.itervalues())
        return [k for k, v in c.iteritems() if v == max_ct]
        
    
    def traverse(self, root, final):
        if root == None: return
        self.traverse(root.left, final)
        final.append(root.val)
        self.traverse(root.right, final)
        return final