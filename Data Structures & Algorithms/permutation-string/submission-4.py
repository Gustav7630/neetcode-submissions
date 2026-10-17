class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #take advantage of how order doesn't matter
        #Both strings only contain lowercase letters.
        if len(s1)>len(s2):
            return False
        s1_chars = [0]* 26

        window_chars = [0]* 26
        for i in range(len(s1)):
            s1_chars[ord(s1[i]) - ord('a')] += 1
            window_chars[ord(s2[i]) - ord('a')] += 1
            #print(window_chars)
        #window_chars = [0]* 26
        prev_point = 0
        prev = ord(s2[0]) - ord('a')
        #print(s1_chars)
        #print(window_chars)
        #print("GOAL")
        for i in range(len(s1),len(s2)):
            #print(window_chars)
            if window_chars == s1_chars:
                return True
            window_chars[prev] -=1
            window_chars[ord(s2[i]) - ord('a')] += 1
            prev_point +=1
            prev = ord(s2[prev_point]) - ord('a')
        if window_chars == s1_chars:
                return True
        
        return False
        
        