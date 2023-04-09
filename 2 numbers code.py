import random
try:
    x = int(input("The lowest number: "))
    y = int(input("The highest number: "))
    Finish = False
    def t(x,y):
            global number_input
            global answer
            global Finish
            answer = random.randint(x,y)
            number_input = 0
            times_to_guess = 3
            Finish = False
            while answer != number_input:
                if times_to_guess == 0:
                    break
                number_input = int(input(f"Guess a number between {x} and {y}: "))
                if number_input > y:
                    Finish = True
                    break
                elif number_input < x:
                    Finish = True
                    break
                if number_input > answer and Finish == False:
                    print(f"{number_input} is bigger than the answer")
                elif number_input < answer and Finish == False:
                    print(f"{number_input} is lower than the answer")
                times_to_guess -= 1


    t(x,y)
    if answer == number_input and Finish == False:
        print(f"You're right it was {answer}")
    elif Finish == True:
        print("You have not been playing by rules, you've lost.")
    elif answer != number_input and Finish == False:
        print(f"You've lost the game, the answer was {answer}")

except:
    print("Invalid value")



