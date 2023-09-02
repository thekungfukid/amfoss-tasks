def getinput():
    inputlist=[]
    t=int(input())
    for i in range(t):
        testcase=input().split()
        inputlist.append(testcase)
    return inputlist


def calculatesum(num1,num2):
    remainder1=0
    remainder2=0
    remainderdiff=0
    sum=0
    while True:
        if num1==0:
            remainder1=0
        else:
            remainder1=num1%10
            num1=num1//10
        if num2==0:
            remainder2=0
        else:
            remainder2=num2%10
            num2=num2//10
            
        remainderdiff=abs(remainder1-remainder2)
        sum=sum+remainderdiff
        
        if num1==0 and num2==0:
            break
    
    return sum


def alchemy(num1string,num2string):
    num1list=list(num1string)
    num1length=len(num1list)
    
    num2list=list(num2string)
    num2length=len(num2list)
    
    breakflag=False
    breakindex=0
    if num1length!=num2length:
        for i in range(num1length):
            if i==0:
                num1list[i]='9'
            else:
                num1list[i]='0'
                
        for i in range(num2length-num1length,num2length):
            if i==num2length-num1length:
                num2list[i]='0'
            else:
                num2list[i]='9'
                
    else:
        for i in range(num1length):
            if num1list[i]==num2list[i]:
                continue
            else:
                breakflag=True
                breakindex=i
                break

        if breakflag==True :
            for i in range(breakindex+1,num1length):
                if i==breakindex+1:
                    num1list[i]='9'
                    num2list[i]='0'               
                else:
                    num1list[i]='0'
                    num2list[i]='9'                
    
    updatednum1string="".join(num1list)
    updatednum2string="".join(num2list)
    updatednum1=int(updatednum1string)
    updatednum2=int(updatednum2string)
    sum=calculatesum(updatednum1,updatednum2)
    
    return sum


def processinputlist(inputlist):
    sumlist=[]
    for i in inputlist:
        sumlist.append(alchemy(i[0],i[1]))
    return sumlist
            

def printoutput(maxsumlist):
    for maxsum in maxsumlist:
        print(maxsum)


inputlist=getinput()
sumlist=processinputlist(inputlist)
printoutput(sumlist)
