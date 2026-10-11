class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_sym = 1
        centres = []

        for i in range(1,len(s)-1):
            if s[i-1] == s[i+1]:
                centres.append(i)
        
        index = 0
        
        if(centres):
            res1 = s[centres[0] - max_sym:centres[0]+max_sym+1]
        else:
            res1 = s[0]
        print(centres)
        # odd palindrome
        flag = True # need loop to fully expend 1 centre
        while len(centres) > 0 :
            
            if index >= len(centres):
                
                #res1 = s[centres[0] - max_sym:centres[0]+max_sym+1]
                #print(res1)
                max_sym +=1
                
                index = 0
                

            if centres[index] - max_sym < 0 or centres[index] + max_sym >= len(s):
                centres.pop(index) #out of bounds elminate
                
            
            elif s[centres[index] + max_sym] !=s[centres[index] - max_sym]:
                centres.pop(index)
            else:
                flag = True #valid pair but we havent updated max sym yet
                res1 = s[centres[0] - max_sym:centres[0]+max_sym+1]
                #print("PASSED " + res1)
                #print(centres[index] + max_sym)
                #print()
                index +=1
        #print("FINAL 1 " + res1)
        
       # if(flag):
        #    print("AGGG")
       #     max_sym +=1
        #    res1 = s[centres[0] - max_sym + 1 :centres[0]+max_sym+1]
       #     print(res1)

        #even palindromes

        max_sym = 1
        centres = []

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                centres.append(i)
        
        index = 0
        if(centres):
            res2 = s[centres[0]:centres[0] +2]
        else:
            res2 = ""
        print(centres)
        #print(res1 + "AG")
        flag = False
        while len(centres) > 0:
            #print("WORK")
            if index >= len(centres):
                #print("POLISHING")
                max_sym +=1
                res2 = s[centres[0] - max_sym + 1 :centres[0]+max_sym+1]
                #print(res2)
                #print(centres[0])
                
                flag = False
                index = 0
                
            #print(f"{centres[index]} - {max_sym}")
            if centres[index] - max_sym < 0:
                
               
                print(centres[index] - max_sym < 0)
                centres.pop(index) 
            elif centres[index] + max_sym + 1  >= len(s):
                centres.pop(index)
                
                
            
            elif s[centres[index] + max_sym + 1] !=s[centres[index] - max_sym]: #even, skip centres match so +1 on add
                centres.pop(index)
                #print("NOT PAL")
            else:
                #print("VALID")
                flag = True
                res2 = s[centres[0] - max_sym + 1 :centres[0]+max_sym+1]
                index +=1
        
        if len(res2) > len(res1):
            return res2
        else:
            return res1
            