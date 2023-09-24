def getinput():
    t=int(input())
    inputlist=[]
    for i in range(t):
        row=input().split()
        inputlist.append(row)
    for row in inputlist:
        for i in range(len(row)):
            row[i]=int(row[i])
    return inputlist

def processcolumn(inputlist):            
    flag=False
    sumcolumnlist=[0,0,0]
    for row in inputlist:
        sumcolumnlist[0]=sumcolumnlist[0] + row[0]
        sumcolumnlist[1]=sumcolumnlist[1] + row[1]
        sumcolumnlist[2]=sumcolumnlist[2] + row[2]
    if sumcolumnlist[0]==0 and sumcolumnlist[1]==0 and sumcolumnlist[2]==0:
        flag=True
            
    if flag==False:
        print("NO")
    else:
        print("YES")        
    
inputlist=getinput()
processcolumn(inputlist)
