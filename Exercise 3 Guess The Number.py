n=18 #what is the work of this line
number_of_guesses=1 #what is the work of this line
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):  #greater than mark
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you entered SMALLer number please input greater number.\n")
    elif guess_number>18:
        print("you entered greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1 #what is the work of this line

if(number_of_guesses>9):
    print("Game Over")

      # AND WHY IS IS REPEATING CUZ THIS DONT EVEN HAVE COTINUE COMMAND