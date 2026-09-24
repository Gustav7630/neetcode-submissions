class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "g"
        for s in strs:
            res += str(len(s)) + "#" + s
        res = res[1:]
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        index = 0
        while index < len(s):
            msg = ""
            num = ""
            while s[index] != "#":
                num += s[index]
                index +=1
            num = int(num)
            for i in range(num):
                msg += s[index + i +1]#skip num
            index += num +1 #get to num
            
            res.append(msg)
        
        return res
