class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])      
        def sum_adjacent(i, j):
            # surrounding
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
            res = 0
            for x, y in adjacent:
                # if encounter the broader, or its surrounding is 0, sum up the result
                if x < 0 or y < 0 or x == m or y == n or grid[x][y] == 0:
                    res += 1
            return res

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # if encounter 1 in the spot
                    count += sum_adjacent(i, j)
        return count