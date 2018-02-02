class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         not pass: 'aab' vs 'baa'
#         if not s or not t: return True
#         if len(s) != len(t): return False
        
#         dic_s = {}
#         dic_t = {}        
#         for i in s:
#             dic_s[i] = dic_s.get(0,1)+1
#         for i in t:
#             dic_t[i] = dic_t.get(0,1)+1

#         return (dic_s.values() == dic_t.values())
        # record the char and the position in the dictionary
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        # s = 'add', t = 'egg'
        # {'a': [0], 'd': [1, 2]}
        # {'e': [0], 'g': [1, 2]}
        return sorted(d1.values()) == sorted(d2.values())