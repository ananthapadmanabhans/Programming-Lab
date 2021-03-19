qwe=open("lop.txt","r")
strg=qwe.read()
print(strg)
qwe.seek(0)
s=qwe.readlines()
print("No.of lines :",len(s))

c=0
for i in s:
    c=c+1
print("No.of lines :",c)
    

