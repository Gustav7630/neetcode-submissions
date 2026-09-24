class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if(len(strs)==0):
            return "¬¬¬"
        for s in strs:
            res += s + "¬"
        
        return res[:-1]

    def decode(self, s: str) -> List[str]:
        if s == "¬¬¬":
            return []
        return(s.split("¬"))
