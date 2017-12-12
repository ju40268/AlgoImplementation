# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return []
        current = head
        # need to keep an extra copy of head ndoe, cannot reivse it directly. will lost reference on it.
        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next    
        return head