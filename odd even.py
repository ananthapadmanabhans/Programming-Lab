x=0
y=0
m=int(input("enter from"))
n=int(input("enter to"))
for i in range(m,n):
    if i%2==0 :
        x=x+1
    if i%2!=0 :
        y=y+1
print("No of odd is",y)
print("No of even is",x)