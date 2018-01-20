class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.helper(nums, i+1, path+[nums[i]], res)