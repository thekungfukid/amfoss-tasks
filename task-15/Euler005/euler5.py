def getinput():
    inputlist=[]
    t=int(input("Enter the number of test cases:"))
    for i in range(t):
        n=int(input("Enter the Number:"))
        inputlist.append(n)
    return inputlist

def calculate(inputlist):
    outputlist=[]
    for i in inputlist:
        loopnumber=1
        N=i
        while True:
            count=0
            for j in range(1,N+1):
                if loopnumber%j==0:
                    count=count+1
            if count==N:
                outputlist.append(loopnumber)
                break
            loopnumber=loopnumber+1
    return outputlist

   
def printoutput(outputlist):
    for i in outputlist:
        print(i)

inputlist=getinput()
outputlist=calculate(inputlist)
printoutput(outputlist)
    
