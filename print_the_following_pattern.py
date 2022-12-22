N=int(input())
for i in range(1,N+1):
    for j in range(i,N):
        print(end=" ")
    for k in range(1,N+1):
        if(i==1 or i==N or k==1 or k==N):
            print("*",end="")
        else:
            print(end=" ")
    print()