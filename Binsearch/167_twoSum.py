class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # TLE approach        
        # l = len(numbers)
        # for i in range(l):
        #     for j in range(i+1, l):
        #         if target == numbers[i] + numbers[j]: return [i+1, j+1]
        if numbers == None: return []
        
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            while l <= r:
                mid = l + (r - l)/2
                if numbers[mid] == (target - numbers[i]):
                    return [i+1, mid+1]
                elif numbers[mid] < (target - numbers[i]):
                    l = mid + 1
                else:
                    r = mid - 1
        return []