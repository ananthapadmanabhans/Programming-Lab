class Rect:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b        
    def __areao__(self):
        return self.length*self.breadth
    def __lt__(self,o):
        if(self.length*self.breadth<o.length*o.breadth):
            return True
        else:
            return False
        
re1=Rect(2,3)
re2=Rect(5,6)
print(re1)
print(re2)
if(re1<re2):
    print("re1 is less")
else:
    print("re2 is less")
print(re1)
print(re2)


