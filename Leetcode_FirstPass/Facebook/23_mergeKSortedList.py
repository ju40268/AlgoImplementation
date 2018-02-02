# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return []
        # divide and conquer 
        return self.sort(lists, 0, len(lists)-1)
    
    def sort(self, lists, l, h):
    	# base case
        if l >= h: return lists[l]
        mid = (h-l)/2 + l
        # split into smaller block
        l1 = self.sort(lists, l, mid)
        l2 = self.sort(lists, mid+1, h)
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
    	# merge 2 lists
        current = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        
        return dummy.next