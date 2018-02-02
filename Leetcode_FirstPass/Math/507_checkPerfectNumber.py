class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # TLE approach 
        # factor = []
        # for i in range(1,num):
        #     if(num % i == 0): factor.append(i)
        # return (sum(factor) == num)
        if num <= 0 or num == 1: return False
        sqrt = int(num ** 0.5)
        double = 2 * num
        for i in range(1, sqrt + 1):
            if (num % i == 0):
                double = double - i - (num//i)
        return (double == 0)