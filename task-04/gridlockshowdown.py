def findvictor(testcase):
    for i in range(3):
        if testcase[i][0] == testcase[i][1] == testcase[i][2] and testcase[i][0] != '.':
            return testcase[i][0]
        
        if testcase[0][i] == testcase[1][i] == testcase[2][i] and testcase[0][i] != '.':
            return testcase[0][i]
        
    if testcase[0][0] == testcase[1][1] == testcase[2][2] and testcase[0][0] != '.':
        return testcase[0][0]
    if testcase[0][2] == testcase[1][1] == testcase[2][0] and testcase[0][2] != '.':
        return testcase[0][2]

    return "DRAW"


def processtestcase():
    testcase = [list(input()) for i in range(3)]
    return findvictor(testcase)


t = int(input())
outputlist=[]
for i in range(t):
    outputlist.append(processtestcase())
for output in outputlist:
    print(output)    
