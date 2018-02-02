class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        queue = [(sr, sc)]
        originalColor = image[sr][sc]
        visit = [[0 for i in range(n)] for j in range(m)]
        
        while queue:
            x, y = queue.pop()
            image[x][y] = newColor
            if (x - 1 >= 0) and image[x-1][y] == originalColor and not visit[x-1][y]:
                visit[x-1][y] = 1
                image[x-1][y] = newColor
                queue.append((x-1, y))           
            if (x + 1 < m) and image[x+1][y] == originalColor and not visit[x+1][y]:
                visit[x+1][y] = 1
                image[x+1][y] = newColor
                queue.append((x+1, y))
            if (y + 1 < n) and image[x][y+1] == originalColor and not visit[x][y+1]:
                visit[x][y+1] = 1
                image[x][y+1] = newColor
                queue.append((x, y+1))
            if (y - 1 >= 0) and image[x][y-1] == originalColor and not visit[x][y-1]:
                visit[x][y-1] = 1
                image[x][y-1] = newColor
                queue.append((x, y-1))
            
        return image