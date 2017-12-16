class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        overlap = []
        for i in nums1:
            dic[i] = dic.get(i)
        for i in nums2:
            if i in dic: overlap.append(i)
        return list(set(overlap))