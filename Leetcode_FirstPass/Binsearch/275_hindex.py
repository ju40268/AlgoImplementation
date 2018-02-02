class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # l ==> the first that dose not match the index
        if not citations: return 0
        
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

        # if not citations: return 0
        # l = len(citations)
        # for i in range(l):
        #     if(citations[i] >= l - i): return (l-i)
        # return 0