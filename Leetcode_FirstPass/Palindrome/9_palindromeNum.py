class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        s_int = str(x)
        
        l, r = 0, len(s_int)-1
        while l < r:
            if s_int[l] != s_int[r]: return False
            l += 1 
            r -= 1
        return True