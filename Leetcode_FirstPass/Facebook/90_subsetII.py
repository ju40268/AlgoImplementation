class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ##### different from 78, need to sort the nums first ######
        nums.sort()
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            ##### different from 78, need to avoid duplicated value ######
            if i != index and nums[i] == nums[i-1]: continue
            self.helper(nums, i+1, path+[nums[i]], res)