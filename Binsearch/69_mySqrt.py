class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left,right = 0, x
        mid_square = left
        while left <= right:
            mid = (left+right)/2
            mid_square = mid*mid
            if mid_square == x:
                return mid
            elif mid_square < x:
                left = mid+1
            else:
                right = mid-1
        return (left - 1)