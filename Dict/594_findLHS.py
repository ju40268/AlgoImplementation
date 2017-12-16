class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d, final = {}, []
        for i, n in enumerate(nums):
            d[n] = d.get(n, 0) + 1
        
        sort_key = sorted(d.keys())
        
        lhs = 0
        for i in range(len(sort_key)-1):
            if sort_key[i+1] - sort_key[i] == 1:
                lhs = max(d[sort_key[i+1]] + d[sort_key[i]], lhs)
        return lhs