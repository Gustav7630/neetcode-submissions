class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        lowerb = 1
        upperb = max(piles)
        k = int((upperb + lowerb) / 2)
       
        x = 0
        flag = False
        
        while upperb > lowerb:
            flag = False
            k = ((upperb + lowerb) // 2)
            #print(((upperb + lowerb) / 2))
            #print(upperb)
            #print(lowerb)
            time = 0
            #x+=1
            #if x > 50:
                #break
            for i in piles:
                time += -(i//-k)
           
            print(f" Time = {time}, k = {k}")
            print(f" Bounds = {lowerb}, k = {upperb}")
            

            if time > h:
                lowerb = k + 1
                print("BIGGER")
                flag = True
               
            else:
                upperb =k
                print("SMALLER")
        print("FINAL")
        #print(f" Time = {time}, k = {k}")
        print(f" Bounds = {lowerb},{upperb}")
        k = ((upperb + lowerb) // 2)
        return k