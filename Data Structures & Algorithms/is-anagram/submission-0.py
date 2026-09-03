class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sortString(str):
            return ''.join(sorted(str))


        s1 = sortString(s)
        s2 = sortString(t)
        return s1 == s2