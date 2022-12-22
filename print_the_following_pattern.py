n=int(input())
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="")
    for l in range(i+1):
        print(l,end="")
    print()