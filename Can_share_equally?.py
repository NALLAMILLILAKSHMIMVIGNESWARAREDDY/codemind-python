x,y=[int(x) for x in input().split()]
if(x==0 and y%2==0):
 print("YES")
elif (x==0 and y%2!=0):
 print("NO")
elif ((x+2*y)%2==0):
 print("YES")
else:
 print("NO")  