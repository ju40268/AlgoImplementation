class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic_pattern, dic_string = {}, {}
        
        for i,p in enumerate(pattern):
            dic_pattern[p] = dic_pattern.get(p, [])+[i]
        
        for i, p in enumerate(str.split()):
            dic_string[p] = dic_string.get(p, []) + [i]
            
        return (sorted(dic_pattern.values()) == sorted(dic_string.values()))