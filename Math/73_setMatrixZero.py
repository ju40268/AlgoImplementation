class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
# Almost TLE
#         m, n = len(matrix), len(matrix[0])
#         queue = []
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     queue.append([i,j])

#         while queue:
#             x,y = queue.pop()
#             for i in range(m):
#                 for j in range(n):
#                     matrix[x][j] = 0
#                 matrix[i][y] = 0

        m = len(matrix)
        n = len(matrix[0])
        row_set = set()
        col_set = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for row in row_set:
            for j in range(n):
                matrix[row][j] = 0

        for col in col_set:
            for i in range(m):
                matrix[i][col] = 0