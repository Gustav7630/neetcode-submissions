class KthLargest:

    myHeap = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        import heapq
        if nums!= None:
            
            
            self.myHeap = list(map(lambda x: x*-1,nums))
            heapq.heapify(self.myHeap)
        else:
            self.myHeap = []
        self.k=k
        print(self.myHeap)

    def add(self, val: int) -> int:
        print(self.myHeap)
        heapq.heappush(self.myHeap,val * -1) #min heap behave as max heap

        temp = []
        for i in range(self.k-1):
            if(len(self.myHeap) ==1):
                break #break early when not enough elements
            temp.append(heapq.heappop(self.myHeap))
        
        res = heapq.heappop(self.myHeap)

        heapq.heappush(self.myHeap,res)
        for i in temp:
            heapq.heappush(self.myHeap,i)
        
        return res * -1

