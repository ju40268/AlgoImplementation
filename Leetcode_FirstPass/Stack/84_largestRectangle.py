class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        stack, res = [], 0
        for i in range(len(heights)+1):
            h = 0 if i == len(heights) else heights[i]
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                start = -1 if not stack else stack[-1]
                area = height * (i - start - 1)
                res = max(res, area)
            stack.append(i)
        return res