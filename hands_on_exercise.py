"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(f"pi is a {type(pi)} and the value is{pi}")


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print(i)
if(i>50):
    print("i is greater than 50")
elif(i==50):
    print("i is equal to 50")
elif(i<50):
    print("i is less than 50")
else:
    print("i is something else")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print(picked_fruit)
if(picked_fruit=='orange'):
    print("color of orange")
elif(picked_fruit=='strawberry'):
    print("color is strawberry")
elif(picked_fruit=='banana'):
    print("color is banana")
else:
    print("color is something else")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multi(x,y):
    result=x*y
    return result

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multi(12,96))

print("48 x 17 =",multi(48,17))

print("196523 x 87323 =",multi(196523,87323))
