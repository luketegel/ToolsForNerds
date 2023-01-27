import random
import os
import time

value1 = 1
value2 = 100

print("Welcome to the number generator")
print("Input first number")

#allow user to input a value for value1
value1 = int(input())


print("Input second number")

#allow user to input a value for value2
value2 = int(input())

print("Returning final value...")
def number_generator():
    return random.randint(value1, value2)

if __name__ == "__main__":
    print(number_generator())



print("script ran successfully!")

print("Type 1 to exit the program")
print("Type 2 to run the program again")



while True:
    user_input = input("Enter input here: ")
    if user_input == "1":
        print("Exiting program...")
        break
    elif user_input == "2":
        print("Running program again...")
        os.system("python numbergenerator1100.py")

    else:
        print("Invalid input, please try again")



