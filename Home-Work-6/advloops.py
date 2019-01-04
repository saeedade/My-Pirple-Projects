#ASSIGNMENT 6: ADVANCED LOOP
# function takes in 2 parameters and draws a play board according to no of rows and column

def fun(row,column):
    if row <=100 and column<=100:
         for r in range(row):
            if r%2 == 0:
                for c in range(column):
                    if c%2 == 0:
                        print(" ",end="")
                    else:
                         print("|",end="")
                print(" ")
            else:
                print("-"*column)
                
         print(True) 
    else:
         print(False)    
              
fun(10,10)