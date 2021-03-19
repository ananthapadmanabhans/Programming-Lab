def sumOfSeries(num): 
    res = 0
    m = 1
      
    for i in range(1, num+1,2): 
       m=m*i
       res = res + (i/ m) 
          
    return res 
      
  
n=int(input("Enter Range"))
print("Sum: ", sumOfSeries(n)) 
