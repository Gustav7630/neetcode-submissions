class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        front = 0
        back = 0
        current = []
        while front < len(s):
            while s[front] in current:
                current.pop(0)
            current.append(s[front])
            if len(current) > max:
                max = len(current)
            front += 1
        
        return max