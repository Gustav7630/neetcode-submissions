class MinStack:

    
    def __init__(self):
        self.body = []
        self.minbody = []

    def push(self, val: int) -> None:
        self.body.append(val)
        if(len(self.minbody) > 0):

            self.minbody.append(min(val,self.minbody[-1]))
        else:
            self.minbody.append(val)

    def pop(self) -> None:
        self.body.pop()
        self.minbody.pop()

    def top(self) -> int:
        return self.body[-1]

    def getMin(self) -> int:
        return self.minbody[-1]
