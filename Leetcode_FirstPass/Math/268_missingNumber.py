class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case         
        # if nums == [0]: return 1
        # if nums == [1]: return 0
        # if nums == [0,1] or nums == [1,0]: return 2
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i]+1 != nums[i+1]: return nums[i] + 1
        
        # solve it by math!
        l = len(nums)
        return l*(l+1)/2 - sum(nums)