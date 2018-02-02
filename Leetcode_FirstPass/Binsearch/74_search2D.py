class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        
        return self.binsearch(matrix, target, m, n)
        
#         vertical = []
#         for i in range(m):
#             vertical.append(matrix[i][0])
#         index = self.findVertical(vertical, target)
#         # print(matrix[index])
#         return self.binsearch(matrix[index], target)
    
    
#     def findVertical(self, vertical, target):      
#         if not self.binsearch(vertical, target):
#             for i in range(len(vertical)):
#                 if vertical[i] > target: return (i-1)
#         else: return True
            
    def binsearch(self, nums, target, m, n):
            l, r = 0, m*n - 1
            while l <= r:
                mid = l + (r - l)/2
                row = mid / n
                col = mid % n
                if target == nums[row][col]:
                    return True
                elif target < nums[row][col]:
                    r = mid - 1
                else:
                    l = mid + 1
            return False