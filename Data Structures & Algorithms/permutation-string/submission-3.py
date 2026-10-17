class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = ""
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            window += s2[i]
        s1 = ''.join(sorted(s1))
        
        for i in range(len(s1),len(s2)):
            print(window)
            if ''.join(sorted(window)) == s1:
                return True
            
            window = window[1:]
            window += s2[i]
        if ''.join(sorted(window)) == s1:
                return True
        return False