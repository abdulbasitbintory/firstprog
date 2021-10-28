                  # CODE WITH HARRY
while(1):
    i = int(input("Please enter a number\n")) # use \n for new line.
    if (i < 100):
        print("TRY AGAIN!!!")
        continue
    else:
        print("Congratulations! you have entered a number greater than 100")
        break
                 # MINE
while(True):
    inpnum = int(input("ENter a number\n"))   #prob
    if (inpnum<=100):
        print("please try again\n")
        continue
    elif inpnum>100:
        print ("congraguations u have done it")
        break

    # the problem was that i was writing print in line # 2
    # u have to \n