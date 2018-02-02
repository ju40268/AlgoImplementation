class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0: return ""
        s = '1'
        self.res = ""
        
        for i in range(1, n):
            count, prev, current = 0, '.', ""
            for j in range(len(s)):
                if s[j] == prev or prev == '.':
                    count += 1
                else:
                    current += str(count) + prev
                    count = 1
                prev = s[j]
            
            current += str(count) + prev
            s = current
        
        return s