class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # use 2 pointer + hashmap solution
        # need is a hashmap to show all the characters needed, it can be negative, if negative => implies that the needed char is too much
        # missing is how many character is missing
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        # enumerate(s, 1) -> index start from 1 instead of 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0  # if needed, missing - 1
            need[c] -= 1            # need - 1
            #  if missing == 0 --> meet the requirement, all character appear
            if not missing:
                while i < j and need[s[i]] < 0:     
                    # left pointer increase if need < 0(if needed < 0, means too much char meets)
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    # if smaller len is found, updated it.     
                    I, J = i, j
        #if not found return s[0:0] == ''
        return s[I:J]