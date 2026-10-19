class Solution:
    def countSubstrings(self,s: str) -> int:
        res = 0


        for i in range(len(s)):
            res +=1
            left = i-1
            right = i
            canOdd = True
            canEven = True
            while left >= 0 and right < len(s) and (canOdd or canEven):

                if (canOdd):
                    if s[left] == s[right]:
                        res +=1
                    else:
                        canOdd = False
                if (canEven):
                    if right < len(s)-1 and s[left] == s[right+1]:
                        res +=1
                    else:
                        canEven = False
                left -=1
                right +=1
                    
            
        return res

        