asd=open("fle.txt","r")
d=dict()
for i in asd:
    i=i.strip()
    i=i.lower()
    w=i.split(" ")
for wd in w:
    if wd in d:
        d[wd]=d[wd]+1
    else:
        d[wd]=1
for h in list(d.keys()):
    print(h,":",d[h])
    
