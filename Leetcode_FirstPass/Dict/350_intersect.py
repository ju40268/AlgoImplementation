class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic_l = {}
        dic_s = {}
        overlap = []
        # for i in nums1:
        #     dic[i] = dic.get(i)
        # for i in nums2:
        #     if i in dic: overlap.append(i)
        # return overlap
        dic_l = {}
        dic_s = {}
        overlap = []
        longer, shorter = (nums1, nums2) if (len(nums1) > len(nums2)) else (nums2, nums1)
        for i in longer:
            dic_l[i] = dic_l.get(i, 0) + 1
        for i in shorter:
            dic_s[i] = dic_s.get(i, 0) + 1
        for k, v in dic_s.items():
            if k in dic_l:
                if dic_l[k] < v: overlap += [k]*dic_l[k]
                else: overlap += [k]*v
        return overlap