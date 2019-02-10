#ASSIGNMENT ON INPUT/OUTPUT

import os        #os module-operating system dependent functionality
filename = input("Input file name: ")      #receive keyboard input for file name
print(filename)

if os.path.isfile(filename):       #testing for file existence
   option=input("A) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\n")
   if option=="A":
     holder=open(filename,"r")
     print(holder.read())
     holder.close()
   elif option=="B":
     holder=open(filename,"w")
     text=input("write in a file : \n")
     holder.write(text)
     holder.close()
   elif option=="C":
     holder=open(filename,"a")
     text=input("Append a file : \n")
     holder.write(text)
     holder.close()
   else :
     print("wrong input..")
   
  
else:    #code to run if file does not exist
 holder=open(filename,"w")
 text=input("write in a file : \n")
 holder.write(text)
 holder=open(filename,"r")
 print (holder.read())
 holder.close() 