def getinput():
    inputlist=[]
    t=int(input("Enter the number of test cases:"))
    for i in range(t):
        n=int(input("Enter the Number:"))
        inputlist.append(n)
    return inputlist

def findmaxprimefactor(x):
    maxprimefactor=0
    for i in range(2,x+1):
        n=0
        if x%i==0:
            for a in range(1,i):
                if i%a== 0:
                    n=n+1
            if n==1:
                maxprimefactor=i
    return maxprimefactor

def calculate(inputlist):
    maxprimefactorslist=[]
    for i in inputlist:
        maxprimefactorslist.append(findmaxprimefactor(i))
    return maxprimefactorslist
   
def printoutput(maxprimefactorslist):
    for factor in maxprimefactorslist:
        print("Highest Prime Factor:",factor)

inputlist=getinput()
maxprimefactorslist=calculate(inputlist)
printoutput(maxprimefactorslist)

