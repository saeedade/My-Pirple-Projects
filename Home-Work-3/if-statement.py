#ASSIGNENT IF STATEMENTS
#funtion to check equality between 3 numbers

def equalityTest(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    if (a==b or a==c or b==c) :
        check=True
    else:
        check= False
    print(check)
equalityTest("1",2,2)

