class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        




        dp = [[0] * m for n in range(n)]

        for i in range(n):
            for j in range(m):
                if i ==0:
                    dp[i][j] = 1
                elif j ==0:
                    dp[i][j] =1
                
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        #for r in dp:
        #    print(r)
        return dp[n-1][m-1]
