#Attributes about a song
MusicDic = {"Song":"Lonely","Album":"Trouble","Artist":"Akon","Genre":"Hip Hop",
"Producer":"Disco D","Year":"2004","Released":"February 21, 2005",
"Source":"Youtube","DurationInSeconds":"238","Filesize":"3.72mb","Bitrate":"128"}

for i in MusicDic:
	print(i,":",MusicDic[i])
	
#Guess the value
def fun_guess(i,j):
	if i in MusicDic:
		if MusicDic[i] == j:
			return True
		else:
			return False
		
choice = True

while(choice):
    print()
    print("Guess an attribute and value of my song!")
    print("Type stop to end guess")
    print()
    key = input("Input a song attribute: ")
    if key == "stop":
        choice = False
        print("Continue = ", key)
        print("Program Ended!")      
    else:
        value = input("Input an attribute value: ")
        h = fun_guess(key, value)
        if h == True:
            print("Wow correct! Nice guess!")
        else:
            print("Sorry, Not correct guess ")