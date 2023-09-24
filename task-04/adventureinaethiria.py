def getinput():
    num=int(input())
    inputlist=input().split()
    for i in range(len(inputlist)):
        inputlist[i]=int(inputlist[i])
    return inputlist

def calculatemincount(inputlist):
    if inputlist.count(min(inputlist))>1:
        return 1
    else:
        return 0

inputlist=getinput()
minimum=calculatemincount(inputlist)
if minimum==0:
    print(inputlist.index(min(inputlist))+1)
else:
    print("Still Aetheria")

