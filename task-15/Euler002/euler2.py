def getinput():
    inputlist=[]
    t=int(input("Enter the number of test cases:"))
    for i in range(t):
        n=int(input("Enter the Number:"))
        inputlist.append(n)
    return inputlist

def fibonacciseries(N):
    num1=1
    num2=2
    l=[]
    while num1<N:   
        l.append(num1)
        t=num1+num2
        num1=num2
        num2=t
    return l

def calculatesum(inputlist):
    sumevenlist=[]
    for i in inputlist:
        serieslist=fibonacciseries(i)
        sumeven=0
        for j in serieslist:
            if j%2==0:
                sumeven=sumeven+j
        sumevenlist.append(sumeven)
    return sumevenlist
        
def printoutput(sumlist):
    for sum in sumlist:
        print("Even Sum:",sum)

inputlist=getinput()
sumevenlist=calculatesum(inputlist)
printoutput(sumevenlist)

