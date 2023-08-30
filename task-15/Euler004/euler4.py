palindromelist=[]
for i in range(100, 1000):
    for j in range(100, 1000):
        num=i*j
        if str(num)==str(num)[::-1] and num not in palindromelist:
            palindromelist.append(num)
palindromelist.sort()
length=len(palindromelist)


def getinput():
    inputlist=[]
    t=int(input("Enter the number of test cases:"))
    for i in range(t):
        n=int(input("Enter the Number:"))
        inputlist.append(n)
    return inputlist

def calculate(inputlist):
    plist=[]
    for i in inputlist:    
        for j in range(length-1,-1,-1):
            if palindromelist[j]<i:
                plist.append(palindromelist[j])
                break
    return plist

def printoutput(plist):
    for p in plist:
        print("Highest Palindrome:",p)
        

inputlist=getinput()
plist=calculate(inputlist)
printoutput(plist)
