"""This is a function to function that
 allows you to add things to that list"""

myUniqueList = []
myLeftovers = []
def addToList(fig):
    if fig not in myUniqueList:
        myUniqueList.append(fig)
        return True
    else:
        myLeftovers.append(fig)
        return False


addToList(1)
addToList("Yes")
addToList("Yes")
addToList("Yes")
addToList(1)
print(myUniqueList)
print(myLeftovers)

