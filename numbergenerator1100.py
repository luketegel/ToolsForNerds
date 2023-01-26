import random


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
##END OF SCRIPT##
