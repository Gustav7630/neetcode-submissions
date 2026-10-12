class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check horizontal
        


        for i in range(9):
            row = set()
            val_count = 0
            for j in range (9):
                if board[i][j] != ".":
                    row.add(board[i][j])
                    
                    val_count +=1
            #print(row)
            if len(row) != val_count:
                #print(row)
                return False
        
        #check vertical

        for i in range(9):
            col = set()
            val_count = 0
            for j in range (9):
                if board[j][i] != ".":
                    col.add(board[j][i])
                    val_count +=1
            #print(col)
            if len(col) != val_count:
                #print(f"BREAKER IS {col}")
                #print(f"valcount is {val_count}")
                return False

        
        #check 3x3 (when incomplete boards)
       
        x = 0
        y = 0
        for i in range(9):
            sect = set()
            val_count = 0
            for j in range(3):
                for k in range(3):
                    if board[j+ x][k+y] != ".":
                        sect.add(board[j+ x][k+y])
                        val_count +=1
            if(len(sect) != val_count):
                return False
            
            x+=3

            if(x>6):
                x =0
                y+=3
                

        return True