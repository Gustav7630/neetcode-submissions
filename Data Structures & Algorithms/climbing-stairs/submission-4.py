class Solution:
    def climbStairs(self, n: int) -> int:
        
        stored = [0] * (n +1)
        if len(stored) <3:
            stored = [0] * 3
        stored[1] = 1
        stored[2] = 2
        def count(n):
            if(n < 3):
                return n
            
            if stored[n-2] > 0:
                two = stored[n-2]
            else:
                two = count(n-2)
        
            if stored[n-1] > 0:
                one = stored[n-1]
            else:
                one = count(n-1)

            stored[n] = one + two
            
            return one + two
        
        return count(n)
            
            



        
        