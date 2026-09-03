class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        front = 0
        changes = 0
        current = []
        def mostFreq(s):
            result = 0
            count = 0
            char = ""
            for i in range(len(s)):
                count = 0
                for j in range(i,len(s)):
                    if s[i] == s[j]:
                        count +=1
                if count > result:
                    result = count
                    char = s[i]
            return result

        while front < len(s):
            
            
            current.append(s[front])
            changes = len(current) - mostFreq(current)

               
            while  changes > k:
                current.pop(0)
                changes = len(current) - mostFreq(current)
                    
            
            if len(current) > result:
                result = len(current)
            front += 1
        
        return result