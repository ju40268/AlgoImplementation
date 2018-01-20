class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Solution #1
        if not nums: return 
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        while start < len(nums):
            nums[start] = 0
            start += 1
        
        # Solution #2 
        if not nums: return 
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1