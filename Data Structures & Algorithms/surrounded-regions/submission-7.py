class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        from collections import deque


        q = deque()
        frontier = []
        explored = {-1,-2} #dummy values to initalise as set


        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j] == 'O' and (i,j) not in explored:
                    q = deque()
                    q.append((i,j))
                    explored.add((i,j))
                    frontier = []
                    flag = True
                    while len(q) > 0:
                        cur = q.popleft()
                        if board[cur[0]][cur[1]] =="X":
                            continue
                        frontier.append((cur[0],cur[1]))
                        if(cur[0] == 0 or cur[0] == len(board)-1 or cur[1] == 0 or cur[1] == len(board[0])-1):
                            flag = False
                            #break
                            continue
                        
                        if (cur[0] +1,cur[1]) not in explored:
                            explored.add((cur[0] +1,cur[1]))
                            q.append((cur[0] +1,cur[1]))
                        if (cur[0] -1,cur[1]) not in explored:
                            explored.add((cur[0] -1,cur[1]))
                            q.append((cur[0] -1,cur[1]))
                        if (cur[0] ,cur[1]+1) not in explored:
                            explored.add((cur[0] ,cur[1]+1))
                            q.append((cur[0] ,cur[1]+1))
                        if (cur[0],cur[1]-1) not in explored:
                            explored.add((cur[0],cur[1]-1))
                            q.append((cur[0],cur[1]-1))
                    if flag:
                        #print(frontier)
                        for c in frontier:
                            board[c[0]][c[1]] = "X"
        #for l in board:
            #print(l)
                        
        


        
        
            