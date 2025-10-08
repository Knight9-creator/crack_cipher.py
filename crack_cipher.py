#import necessary libraries
import random
import time

#initialize
ans = random.randint(1, 50)

playing = "yes"
tries = 0
lives = 10

#While loop to play
while playing == "yes":
    u_input = 0
    print(f"You have {lives} lives left!")
    
    #Get input from user
    while True:
        temp = 0
        u_input = input("Enter 'HINT', 'EXIT', or a number between 1-50: ")
        if u_input.upper() == "HINT":
            if ans > 25:
                print("The number is greater than 25!")
            else:
                print("The number is less than 26!")
        elif u_input.upper() == "EXIT":
            temp = 1
            break
        else:
            try:
                u_input = int(u_input)
                if u_input > 1 and u_input < 50:
                    break
                else:
                    print("Please enter a number within that range!")
            except ValueError:
                print("Enter a valid input please: ")
                continue
    

    if temp == 1:
        break

    tries = tries + 1
#Check for user being right/wrong.
    if u_input < ans:
        if u_input % 3 == 0:
            continue
        else:
            print("The number is larger!")
        lives = lives - 1

        if lives == 0:
            print(f"The number was {ans}")
            print(f"You ran out of lives!")
            playing = "N/A"

            while not playing == "yes" and not playing == "no":
                playing = input("Would you like to play again? (yes/no): ").strip(" ").lower()

            ans = random.randint(1, 50)
            lives = 10
            tries = 0

            if playing == "no":
                break

    elif u_input > ans:
        if u_input % 3 == 0:
            continue
        else:
            print("The number is smaller!")
        lives = lives - 1

        if lives == 0:
            print(f"The number was {ans}")
            print(f"You ran out of lives!")
            playing = "N/A"

            while not playing == "yes" or not playing == "no":
                playing = input("Would you like to play again? (yes/no): ").strip(" ").lower()

            ans = random.randint(1, 50)
            lives = 10
            tries = 0
            
            if playing == "no":
                break
#check for user getting it right and result screen.
    else:
        for x in range(3):
            print(f"{3 - x}")
            time.sleep(1)
        time.sleep(1)
        print(f"The number was {ans}")
        print(f"You got the number in {tries} tries with {lives} life/lives left!")
        if tries <= 3:
            print(f"Congrats on finishing it in under than 4 tries! ({tries} tries!)")
        playing = "N/A"
        while not playing == "yes" or not playing == "no":
            playing = input("Would you like to play again? (yes/no): ").strip(" ").lower()
        ans = random.randint(1, 50)
        lives = 10
        tries = 0



#README PARAGRAPH
#This is a short program a lot like Guess the Number!
#The computer has a number between 1-50, and the user must guess a valid number
#The computer gives a hint if the number isn't a multiple of 3.
