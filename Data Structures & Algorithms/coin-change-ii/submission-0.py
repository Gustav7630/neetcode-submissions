class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        #outer loop, different coins
        #inner loop, amounts
        
        #different ways to make each amount
        dp = [0 for num in range(amount+1)]
        dp[0] = 1
        #print (dp)

        sum = 0
        for i in range(len(coins)):
            
            for j in range(1,amount+1):
               # print(j - coins[i])
                if j - coins[i] >= 0:
                    dp[j] += dp[j-coins[i]]
                
        return dp[-1]