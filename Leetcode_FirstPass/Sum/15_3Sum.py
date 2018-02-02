class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
# #         res = []
# #         nums.sort()
        
# #         for i in range(len(nums)-2):
# #             if i > 0 and nums[i] == nums[i-1]: continue
# #             l, h, target = i+1, len(nums)-1, 0 - nums[i]
# #             while l < h:
# #                 if target + nums[l] + nums[h] == 0:
# #                     res.append([nums[l], nums[h], nums[i]])
# #                     while l < h and nums[l] == nums[l + 1]: l += 1
# #                     while l < h and nums[h] == nums[h - 1]: h -= 1
# #                     l += 1; h -= 1
# #                 elif target + nums[l] + nums[h] < 0:
# #                     l += 1
# #                 else:
# #                     h -= 1
# #         return res


        # O(n^2), O(n)
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