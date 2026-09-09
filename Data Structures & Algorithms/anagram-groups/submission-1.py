class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        def hshr(word):
            key = [0 for num in range(26)]
            for c in word:
                key[ord(c)-97] +=1
            return key
        
        for s in strs:
            hsh = tuple(hshr(s))
            if words.get(hsh):
                words[hsh].append(s)
            else:
                words.update({hsh:[s]})
        result = []
        for value in words.values():
            result.append(value)
        return result
        
        
