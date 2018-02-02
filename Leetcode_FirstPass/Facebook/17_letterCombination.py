class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.mapping = ["*","*","abc","def","ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits: return []
        res = []
        self.helper(digits, 0, "",res)
        return res
    
    def helper(self, digits, index, current, res):
        # or
        # if index == len(digits):
        #   res.append(current)
        #   return
        # 
        if len(digits) == len(current):
            res.append(current)
            return 
        for i in self.mapping[int(digits[index])]:
            self.helper(digits, index + 1, current + i, res)