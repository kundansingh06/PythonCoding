count=1

def printName(name):
    global count
    if count<=10:
        print(count,"-",name)
        count=count+1
        printName(name)


printName("kundan Singh")





