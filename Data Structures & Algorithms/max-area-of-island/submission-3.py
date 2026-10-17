class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0
        cur_size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                   
                    stack = [(i,j)]
                    grid[i][j] = 2
                    cur_size = 0
                    while stack:
                        
                        
                        cur = stack[-1]
                        x = cur[0]
                        y = cur[1]
                        
                        stack.pop()
                        cur_size +=1
                        if x >0:
                            if grid[x-1][y] ==1:
                                stack.append((x-1,y))
                                grid[x-1][y]= 2
                        if x <len(grid)-1:
                            if grid[x+1][y] ==1:
                                stack.append((x+1,y))
                                grid[x+1][y]= 2
                        
                        if y >0:
                            if grid[x][y-1] ==1:
                                stack.append((x,y-1))
                                grid[x][y-1]= 2
                        if y <len(grid[0])-1:
                            if grid[x][y+1] ==1:
                                stack.append((x,y+1))
                                grid[x][y+1]= 2
                    
                    res = max(res,cur_size)
        #print(grid)
        return res
                            

                

