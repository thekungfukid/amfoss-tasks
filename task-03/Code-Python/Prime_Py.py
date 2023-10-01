def primenumbers(n):
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
n=int(input("Enter the No upto which to print Prime Number:"))
primenumbers(n)
