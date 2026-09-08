class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])
        y = 0
        while y + 1 < len(matrix) and target >= matrix[y+1][0]:
            y= y + 1
        
        left = 0
        right = len(matrix[0])

      #  if(len(matrix[y]) == 1):
       #     return matrix[y][0] == target
        
        while left < right:
            pivot = (left + right) // 2
            if matrix[y][pivot] == target:
                return True
            if matrix[y][pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        print(y)
        print(left)
        if left == right and left < len (matrix[y]):
            return matrix[y][left] == target
        else:
            return False
        

