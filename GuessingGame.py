
import random

number = random.randint(1, 9)

chances = 0

while(chances < 5):
    try:
        answer = int(input("Guess A Number From 1 to 9 : "))
        if(answer > 9 or answer < 1):
            print("Guess a number between 1 to 9")
    except:
        print("Guess a number between 1 to 9")

    if(answer == number):
        print("Congratulations!! Your Guess Is Correct.You are Genius")
        chances = 6
    elif (answer > number):
        print("Your Guess is Greater than the Number")
    elif (answer < number):
        print("Your Guess is Smaller than the Number")

    chances = chances + 1

if(chances == 5):
    print("Your Chances Are Completed")
    print('The Number Is {number} ')