class Solution:
    def countSubstrings(self,s: str) -> int:
        res = 0


        for i in range(len(s)):
            res +=1
            left = i-1
            right = i+1
            #Odd length palindromes
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res +=1
                left-=1
                right +=1

            left = i-1		
            right = i
            #even
            while left >= 0 and right < len(s) and s[left] == s[right]:

                res +=1
                left-=1
                right +=1
        return res

        