class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(index,choices,total = 0):

            if index == len(candidates) or total >= target:
                
                if total == target:
                    print(choices)
                    print(total)
                    res.append(choices.copy())
                return
            
            val =candidates[index]
            choices.append(val)
            total += val
            backtrack(index +1,choices,total)
            total -= val
            choices.pop()
            
            clear_dupes = 0
            
            while index + 1 + clear_dupes < len(candidates) and val == candidates[index+1 + clear_dupes] :
                #if equal, we skip untill next new value, to avoid repeated combinations from not using the current value
                clear_dupes +=1
            backtrack(index +1 + clear_dupes,choices,total)
        
        backtrack(0,[],0)
        return res


                
        