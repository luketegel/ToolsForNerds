import random
import os


print("Welcome to the coin flipper")

# Ask the user how many times they want to flip the coin
print("How many times would you like to flip the coin?")
user_input = int(input())

# Create a variable to store the number of heads
heads = 0

# Create a variable to store the number of tails
tails = 0


# Create a loop that will flip the coin the number of times the user inputted
for i in range(user_input):
    # Generate a random number between 1 and 2
    flip = random.randint(1, 2)

    # If the number is 1, add 1 to the heads variable
    if flip == 1:
        heads += 1

    # If the number is 2, add 1 to the tails variable
    if flip == 2:
        tails += 1


# Print the number of heads and tails
print("Heads: " + str(heads))
print("Tails: " + str(tails))

# Print the percentage of heads and tails
print("Heads: " + str(heads / user_input * 100) + "%")
print("Tails: " + str(tails / user_input * 100) + "%")

#ask the user if they want to run the program again
print("Type 1 to exit the program")
print("Type 2 to run the program again")

while True:
    user_input = input("Enter input here: ")
    if user_input == "1":
        print("Exiting program...")
        break
    elif user_input == "2":
        print("Running program again...")
        os.system("python headsortails.py")

    else:
        print("Invalid input, please try again")
