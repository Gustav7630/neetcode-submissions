class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        resLen = 1
        curLen = 0
        cur = ""
        #oddlength
        
        for i in range(1,len(s)-1):
            flag = False
            l = i-1
            r = i+1
            
            
            
            while  l >-1 and r < len(s) and s[l] ==s[r]:
                
                flag = True
                l -=1
                r +=1
            #curLen = r-l -1
            if(flag):
                
                #cur = s[l+1:r]
                curLen = r-l - 1
                
                
                if(curLen > resLen):
                    
                    resLen = curLen
                    res = s[l+1:r] #stop point exclusive start inclusive
                                    #undo the change that broke
        print(res)
        for i in range(len(s)-1):
            flag = False
            l = i
            r = i+1
            
            
            
            while  l >-1 and r < len(s) and s[l] ==s[r]:
                
                flag = True
                l -=1
                r +=1
            #curLen = r-l -1
            if(flag):
                
                #cur = s[l+1:r]
                curLen = r-l -1 # right pointer - left pointer, acounting for themselves with -1
                #print(curLen)
                
                if(curLen > resLen):
                    
                    resLen = curLen
                    res = s[l+1:r] #stop point exclusive start inclusive
                                    #undo the change that broke
        
        return res


            