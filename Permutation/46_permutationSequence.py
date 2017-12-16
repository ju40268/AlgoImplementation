class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # approach TLE
        if n == 1: return "1"
        nums = [i for i in range(1,n+1)]
        result = self.permute(nums, k)
        return ''.join(map(str, result[k-1]))
        # # return ''.join(map(str, result))
        # return ''.join(result[])
        
    def permute(self, nums, k):
        result = []
        if len(nums) == 1: return [nums]
        for i in range(len(nums)):
            center = nums[i]
            other = nums[:i] + nums[i+1:]
            for p in self.permute(other, k): result.append([center]+p)
        return result