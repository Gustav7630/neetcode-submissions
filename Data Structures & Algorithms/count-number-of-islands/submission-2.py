class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def search(x,y):
           # print("MAX Y IS")
           # print(len(grid[0]))
            if x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1:
                return # out of bounds
            #print(f" x = {x} y = {y}")
            if grid[x][y] =='1':
                grid[x][y] ='2'
                if x >=0:
                    search(x-1,y)
                    #print("BOOM")
                if x < len(grid):
                    search(x+1,y)
                    #print("XOOM")
                if y >=0:
                    search(x,y-1)
                    #print("LEFT")
                if y < len(grid[0]):
                    search(x,y+1)
                    #print("RIGHT")
                return True
            return False
        res = 0
        # modify grid to mark found
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =='1':
                    res +=1
                    search(i,j)
               
        #print(grid)
        return res

                
