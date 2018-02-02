class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        # need to sort the citations list first and do the binary search
        citations.sort()
        # if(len(citations) == 2 and citations[0] == 0 and citations[1] ==1): return 1
        n = len(citations)
        l, r = 0, n - 1
        
        while l <= r:
            mid = l + (r-l)/2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return (n-l)