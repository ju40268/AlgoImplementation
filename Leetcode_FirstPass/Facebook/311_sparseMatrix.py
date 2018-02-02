class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(m * n * nB), O(nB * m)
        m, n = len(A), len(A[0])
        nB = len(B[0])
        # Careful the init here
        res = [[0] * nB for j in range(m)]
        
        for i in range(m):
            for k in range(n):
                if A[i][k] != 0:
                    for j in range(nB):
                        if B[k][j] != 0: res[i][j] += A[i][k] * B[k][j]
        return res