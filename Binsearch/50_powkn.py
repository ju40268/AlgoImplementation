class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
#         if n == 0: return 1
#         if n < 0: return 1/self.myPow(x, -n)
#         # return x * self.myPow(x, n-1)
#         pow_result = self.myPow(x, n/2)
        
#         if n % 2 == 0:
#             return pow_result ** 2
#         else:
#             return x * pow_result ** 2
        if n == 0: return 1
        if n < 0:
            n = -n
            x = (1/x)
        return self.myPow(x**2, n/2) if n % 2 == 0 else x*self.myPow(x**2, n/2)