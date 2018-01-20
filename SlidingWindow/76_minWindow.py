class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        if len(t) > len(s):
            return ""
        
        m = len(s)
        n = len(t)
        
        result = ""
        
        hashmap = {}
        
        for char in t:
            if char in hashmap: 
                hashmap[char] += 1
            else: 
                hashmap[char] = 1
        
        left, minDis, count = 0, m + 1, 0
        
        for right in xrange(m):
            
            if s[right] in hashmap:
                
                hashmap[s[right]] -= 1
                
                if hashmap[s[right]] >= 0: count += 1
                    
                while count == n:
                    
                    if right - left + 1 < minDis:
                        
                        minDis = right - left + 1
                        result = s[left:left+minDis]
                    
                    if s[left] in hashmap:
                        
                        hashmap[s[left]] += 1
                        if hashmap[s[left]] > 0 :
                            count -= 1
                    
                    left += 1
                    
        return result