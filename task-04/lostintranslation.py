def getinput():
    inputstring=input()
    return inputstring

def checkhello(inputstring):
    var="hello"
    count=0
    if len(inputstring)<5:
        print("NO")
    else:
        for i in var:
            if i in inputstring:
                inputstring=inputstring[inputstring.index(i)+1::]
                count=count+1
        if count==len(var):
            print("YES")
        else:
            print("NO")

inputstring=getinput()
checkhello(inputstring)
