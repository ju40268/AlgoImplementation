class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        count = 0
        odd = []
        for k, v in dic.items():
            if v % 2 == 0: count += v
            else: odd.append(v)
        
                
        return count + (sum(odd) - len(odd) + bool(odd))