class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt = int(area ** 0.5)
        factor = []
        for i in range(1, sqrt+1):
            if (area % i == 0):
                factor.append([(area // i),  i])

        return (factor[-1])