class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
#  prefix sum + double for loop --> TLE
#         prefix = [0] * (len(nums)+1)
#         for i in range(1,len(nums)+1):
#             prefix[i] = nums[i-1] + prefix[i-1]
        
#         count = 0
#         for i in range(len(prefix)):
#             for j in range(i+1, len(prefix)):
#                 if prefix[j] - prefix[i] == k: count += 1
#         return count
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res