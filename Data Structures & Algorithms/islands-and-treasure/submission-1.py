class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        #for loop on all zeroes
        #bfs surroundings till reach end, updating cells with lesser distance

        # stop on edges

        from collections import deque
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append(([i,j,0]))
        
        while q:
            cur = q.popleft()
            if cur[0] < 0:
                continue
            if cur[1] < 0:
                continue
            if cur[0] == len(grid):
                continue
            if cur[1] == len(grid[0]):
                continue
            
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            x = cur[0]
            y = cur[1]
            if(grid[x][y] > cur[2]):
                grid[x][y] = cur[2]
            for d in directions:
                if x+d[0] < 0:
                    continue
                if y + d[1] < 0:
                    continue
                if x + d[0] == len(grid):
                    continue
                if y +d[1] == len(grid[0]):
                    continue

                if grid[x+d[0]][y+d[1]] > cur[2]+1:
                    grid[x+d[0]][y+d[1]] = cur[2]+1
                    q.append([x+d[0],y+d[1],cur[2]+1])
        
        for l in grid:
            print(l)


        