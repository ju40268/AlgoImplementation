class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # for sanity check: if the size dose not match
        if r * c != len(nums) * len(nums[0]):
            return nums
        # else to the reshape
        flat_num = list(itertools.chain.from_iterable(nums))
        # solution stackoverflow: https://stackoverflow.com/questions/10124751/convert-a-flat-list-to-list-of-list-in-python
        return zip(*[iter(flat_num)]*c)
            
        