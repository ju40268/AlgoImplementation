class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # l = len(p)
        # dic = {}
        # sorted_p = ''.join(sorted(p))
        # for i in range(len(s) - l + 1):
        #     sorted_s = ''.join(sorted(s[i:i+l]))
        #     # if (sorted_s == sorted_p): subs_index.append(i)
        #     dic[sorted_s] = dic.get(sorted_s, []) + [i]
        # return (dic[sorted_p]
        
        # dict = {}
        # l = len(p)
        # subs_index = []
        # p_counter = collections.Counter(p) 
        # for i in range(len(s) - l + 1):
        #     s_counter = collections.Counter(s[i:i+l])
        #     if s_counter == p_counter: subs_index.append(i)
        # return subs_index
            
        res = []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res