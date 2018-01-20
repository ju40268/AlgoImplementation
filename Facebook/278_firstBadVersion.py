# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n-1
        while l <= r:
            mid = (r-l)/2 + l
            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l