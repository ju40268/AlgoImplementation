class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation
#         if n == 1: return 1
#         nums = [i for i in range(1, n+1)]
#         section_width = self.factorial(n - 1)
#         qoi = k // section_width
#         result = []
#         all_perm = self.permute(nums, qoi, result)
#         return all_perm[k % section_width]
        
     
#     def permute(self, nums, qoi, result):
#         center = nums[qoi]
#         other = nums[:qoi] + nums[qoi+1:]
#         for p in self.permute(other, qoi, result): result.append([center]+p)
#         return result
    
#     def factorial(self, n):
#         if n == 1: return 1
#         return n * self.factorial(n-1)