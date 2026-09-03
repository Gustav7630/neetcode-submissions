class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortString(s):
            return ''.join(sorted(s))
        result = []
        for i in strs:
            flag = True
            x = sortString(i)
            for j in range(len(result)):
                if(sortString(result[j][0]) == x):
                    result[j].append(i) 
                    flag = False
            if(flag):
                result.append([i])       
        return result