num=int(input("Enter a number:"))
t=num
r=0
while(num>0):
    d=num%10
    r=r*10+d
    num=num//10
if(t==r):
    print("palindrome")
else:
    print("Not a palindrome")