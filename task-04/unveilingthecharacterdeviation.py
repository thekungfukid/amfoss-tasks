refstring="amfoss"
stringlist=[]
refstringlength=len(refstring)
for i in range(refstringlength):
    stringlist.append(refstring[i])

def getinput():
    t=int(input())
    inputlist=[]
    for i in range(t):
        string=input()
        inputlist.append(string)
    return inputlist


def countdev(inputstring):
    inputlist=[]
    for letter in inputstring:
        inputlist.append(letter)
        
    count=0
    for i in range(refstringlength):
        if stringlist[i]!=inputlist[i]:
            count=count+1
            
    return count
    
def calculate(inputlist):
    countlist=[]
    count=0
    
    for inputstring in inputlist:
        count=countdev(inputstring)
        countlist.append(count)
        
    return countlist


def printcount(countlist):
    for i in countlist:
        print(i)
                
inputlist=getinput()
countlist=calculate(inputlist)
printcount(countlist)













