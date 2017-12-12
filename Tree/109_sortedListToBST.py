# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        value = []
        while head:
            value.append(head.val)
            head = head.next
        return self.convertBST(value)
    
    def convertBST(self, nums):
        if not nums: return 
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.convertBST(nums[:mid])
        root.right = self.convertBST(nums[mid+1:])
        return root