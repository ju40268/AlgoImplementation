class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None: return 0
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        
        count = 0
        
        for y in xrange(m):
            for x in xrange(n):
                if grid[y][x] == '1':
                    count += 1
                    self.dfs(grid,x,y,m,n)
        return count
    
    def dfs(self, grid, x, y, m, n):
        if(x < 0 or y < 0 or x >= n or y >= m or grid[y][x] == '0'): return
        grid[y][x] = '0'
        self.dfs(grid, x - 1, y, m, n)
        self.dfs(grid, x + 1, y, m, n)
        self.dfs(grid, x, y + 1, m, n)
        self.dfs(grid, x, y - 1, m, n)