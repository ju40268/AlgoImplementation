class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d, result = {}, []
        for i in range(len(s) - 9):
            slice_s = s[i:i+10]
            d[slice_s] = d.get(slice_s, 0) + 1
        for k, v in d.items():
            if v >= 2: result.append(k)
        return result