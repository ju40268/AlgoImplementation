class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        l, r, current = 0, int(c ** 0.5)+1, 0
        while l <= r:
            current = l ** 2 + r ** 2
            if current < c:
                l += 1
            elif current > c:
                r -= 1
            else:
                return True
        return False
            