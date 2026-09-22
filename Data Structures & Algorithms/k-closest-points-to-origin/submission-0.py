class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        


        def distance(point1 ,point2 = [0,0]):
            
            difX = (point1[0] - point2[0])**2
            difY = (point1[1] - point2[1])**2
            

            return (difX + difY) ** 0.5
        
        res =[]

        for p in points:
            dist = distance(p)
            if(len(res) < k):
                heapq.heappush(res,[-dist,p])
            
            else:
                heapq.heappush(res,[-dist,p])
                heapq.heappop(res) #max heap, size limit k, remove largest aka furthest
            

        ans = []
        for i in res:
            ans.append(i[1])

        return ans 




