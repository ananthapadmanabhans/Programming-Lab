def common(a,b): 
    c = [value for value in a if value in b] 
    return c
s
x=input("Enter 1st list")
y=input("Enter 2nd list")
d=common(x,y)
print(d)
