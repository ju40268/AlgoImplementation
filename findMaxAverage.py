class Solution:
	# https://leetcode.com/problems/maximum-average-subarray-i/solution/
	# better algo? better space complexity?
	# time complexity: O(n), space: accumlative sum O(1), sliding window: O(n)
	# http://www.csie.ntnu.edu.tw/~u91029/MaximumSubarray.html#5
	# for the Algo explained above.
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = [0] + list(itertools.accumulate(nums))
        return max(map(operator.sub, sums[k:], sums)) / k