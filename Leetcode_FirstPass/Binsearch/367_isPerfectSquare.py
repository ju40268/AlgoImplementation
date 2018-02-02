class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left,right = 0,num
        mid_square = left
        while left <= right:
            mid = (left+right)/2
            mid_square = mid*mid
            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid+1
            else:
                right = mid-1
        if left-1 ** 2 == num: return True
        else: return False