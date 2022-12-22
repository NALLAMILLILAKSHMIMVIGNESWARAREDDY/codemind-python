n=int(input())
arr=list(map(int,input().split()))
zeros=[]
ones=[]
for i in range(n):
    if arr[i]==0:
        zeros.append(arr[i])
    else:
        ones.append(arr[i])
sortedd=zeros+ones
for i in range(n):
    arr[i]=sortedd[i]
print(*arr)