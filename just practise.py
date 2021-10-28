n=18
number_of_guesses=1
print("u have limited 9 number of guesses: ")
while (number_of_guesses<=9) :
    guess_number =int(input("guess the number:\n"))
    if guess_number>18:
        print("please enter another number ur guess is too low \n")
    elif guess_number<18:
        print("your guess is too high please try another number \n")
    else:
        print("you won this guess game! \n")
        print(number_of_guesses, "number of guesses u took to finish this game\n")
        break
    print(9-number_of_guesses, "number of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses>9):
    print("GAME OVER U DONT HAVE MOVES LEFT")