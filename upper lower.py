def test(s):
   d=0
   e=0
   for i in s:
    if i.isupper():
           d=d+1
    elif i.islower():
           e=e+1
   print(s)
   print("No:of Upper:",d)
   print("No:of Lower:",e)
   
n=input("Enter your string")
test(n)
