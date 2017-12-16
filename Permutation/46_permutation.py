class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return list(itertools.permutations(nums))
        
        if not nums: return []
        length = len(nums)
        if length == 1: return [nums]
        result = []
        # for pair in self.permute(nums[1:]):
        #     for i in range(len(pair) + 1):
        #         newPair = pair[:i] + [nums[0]] + pair[i:]
        #         result.append(newPair)
        for i in range(len(nums)):
            center = nums[i]
            other = nums[:i] + nums[i+1:]
            for p in self.permute(other): result.append([center]+p)
        return result