class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # final = []
        # for i in range(1, len(nums) - 1):
        #     if nums[i-1] < nums[i] and nums[i] > nums[i+1]: final.append([i, nums[i]])
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l)/2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid -1]:
                r = mid - 1
            else:
                l = mid + 1
        return -1