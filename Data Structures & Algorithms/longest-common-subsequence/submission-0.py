class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        #consider scenarios

        # case 1 - match, consume char
        # case 2 - no match, discard text1 char, run an alternative search but discarding text 2 char instead
        #   repeat untill one string is empty



                    #text2 inner, text1 outer
        dp = [[0] * len(text2) for i in range(len(text1))]
        print(dp)
        print(len(text1))
        print(len(text2))
        step = 1
        for i in range(len(text1)):
            for j in range(len(text2)):
                if i ==0 and j ==0:
                    if text1[i] == text2[j]:
                        dp[i][j] = 1

                elif i ==0:
                    dp[i][j] = dp[i][j-1]
                    if text1[i] == text2[j]:
                        dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                    if text1[i] == text2[j]:
                        dp[i][j] = 1
                
                else:
                    
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        for r in dp:
            print (r)
        return dp[-1][-1]