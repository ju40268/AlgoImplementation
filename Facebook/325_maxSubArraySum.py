class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        
        dic = {0:-1}
        res = 0
        
        # prefix sum            
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        for i in range(len(nums)):
            if (nums[i] - k) in dic:
                res = max(res, i - dic[nums[i] - k])
            if nums[i] not in dic:
                dic[nums[i]] = i
        
        return res