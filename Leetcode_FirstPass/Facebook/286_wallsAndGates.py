class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        # careful for the corner case input: []         
        if m > 0: n = len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, m, n, 0)
    
    def dfs(self, rooms, i, j, m, n, dis):
        if i < 0 or i >= m or j < 0 or j >= n or rooms[i][j] < dis: return
        rooms[i][j] = dis
        self.dfs(rooms, i+1, j, m, n, dis+1)
        self.dfs(rooms, i-1, j, m, n, dis+1)
        self.dfs(rooms, i, j-1, m, n, dis+1)
        self.dfs(rooms, i, j+1, m, n, dis+1)