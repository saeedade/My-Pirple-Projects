# ASSIGNMENT 5: BASIC LOOPS

for num in range(1,101):
    if num % 3 == 0:      #Code for multiples of 3
        print("Fizz")
    if num % 5 == 0:      #Code for multiples of 5
        print("Buzz")
    if num % 3 == 0 and num % 5 == 0:   #Code for both multiples of 3 and 5
        print("FizzBuzz")
    
    #Code for Prime Numbers
    if num > 1:            
        for i in range(2,num):
           if (num % i) == 0:
               break
        else:
           print("prime")