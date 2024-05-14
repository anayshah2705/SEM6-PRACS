class accounting:
    def __init__(self):
        self.stack = []
        self.totalOperations = 0
        self.cost = 0
        self.amortizedCost = 0
        self.creditBank = 0

    def push(self,element):
        self.stack.append(element)
        self.cost+=1
        self.amortizedCost+=2
        self.totalOperations+=1
        self.creditBank+=1
        print(f"Push: {element}")
        print("Actual Cost: 1")
        print("Amortized Cost: 2")
    
        self.displayStack()
        
    def pop(self):
        if len(self.stack)==0:
            print("Stack Underflow")
        popped = self.stack.pop()
        self.cost+=1
        self.amortizedCost+=0
        self.totalOperations+=1
        self.creditBank-=1
        print(f"Pop: {popped}")
        print("Actual Cost: 1")
        print("Amortized Cost: 0")
        self.displayStack()
        
    
    def multipop(self,k):
        print(f"Multipop start:")
        while self.stack and k>0:
            k-=1
            self.pop()
        print(f"multipop over.")
        # self.displayStack()
    
    def displayStack(self):
        print("Stack: ",self.stack)
        print(f"Credit Bank: {self.creditBank}\n")

stack = accounting()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.multipop(2)
print("Actual Cost: ", stack.cost)
print("Total Operations: ", stack.totalOperations)
print("Amortized Cost: ", stack.amortizedCost)