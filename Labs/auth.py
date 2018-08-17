name = input ("Enter your name: ")
pin = int(input("Enter pin: "))
i = 2
    
while (i>0):
    if pin == 1234:
        print ("Welcome to python 101")
        break
    else:
        print ("Wrong pin." + str(i) + " attempt(s) remaining")
        name = input ("Enter your name: ")
        pin = int(input("Enter pin: "))
    i -= 1

exit()

