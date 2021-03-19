for i in range(1,500):  
   sum = 0  
   temp = i  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if i == sum:  
            print(i)  
