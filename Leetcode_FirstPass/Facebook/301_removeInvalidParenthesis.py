class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.remove(res, s, 0, 0, ['(', ')'])
        return res
        
    def remove(self, res, s, last_i, last_j, pair):
        count = 0
        # print par, s, last_i, last_j
        for i in range(last_i, len(s)):
            # deal with the prefix s[:i], and we already know that s[:last_i] is good 
            if s[i] == pair[0]:count += 1
            if s[i] == pair[1]:count -= 1
            if count >= 0: continue    
            for j in range(last_j, i+1): # need remove
                if s[j] == pair[1] and (j == last_j or s[j-1] != pair[1]):
                    # remove s[j] = ')', pass in the res substring into the recursion call again
                    self.remove(res, s[:j]+s[j+1:], i, j, pair)
            return # this is not a valid string

        # This is a valid string
        reverse = s[::-1]
        if pair[0] == '(': # The valid string is from left to right
            self.remove(res, reverse, 0, 0, [')', '('])
        else: # The valid string is from right to left, two directions are complete
            res.append(reverse)