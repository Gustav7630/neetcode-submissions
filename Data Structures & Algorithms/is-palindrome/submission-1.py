class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valids = "abcdefghijklmnopqrstuvwxyz0123456789"
        new = ""
        for i in s:
            if i in valids:
                new += i

        for i in range(len(new)):
            if(new[i] != new[-i - 1]):
                return False
            
            if( i >= len(new) /2):
                return True
        return True
            


        