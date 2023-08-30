def getinput():
    inputlist=[]
    t=int(input("Enter the number of test cases:"))
    for i in range(t):
        n=int(input("Enter the Number:"))
        inputlist.append(n)
    return inputlist

def calculatesum(inputlist):
    sumlist=[]
    for i in inputlist:
        sum=0
        for j in range(1,i):
            if j%3==0 or j%5==0:
                sum=sum+j
        sumlist.append(sum)
    return sumlist
        
def printoutput(sumlist):
    for sum in sumlist:
        print("Sum:",sum)

inputlist=getinput()
sumlist=calculatesum(inputlist)
printoutput(sumlist)
