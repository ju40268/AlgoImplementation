class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return nums
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            low, high = i+1, len(nums)-1
            while low < high:
                if nums[low] + nums[high] + nums[i] > 0: high -= 1                       
                elif nums[low] + nums[high] + nums[i] < 0: low += 1
                else: 
                    res.append([nums[low], nums[high], nums[i]])
                    while low < high and nums[low] == nums[low+1]: low += 1
                    while low < high and nums[high] == nums[high-1]: high -= 1
                    low += 1
                    high -= 1
        return res