#! /usr/bin/python3

def circumference(radius):
    pi = 3.14159 # (Will hardcode pi in this example)
    circumferenceValue = pi * radius * 2
    return circumferenceValue

def printCircumference(radius):
    myCircumference = circumference(radius)
    print (f"Circumference of a circle with a radius of {radius} is {myCircumference:.2f}")

radius = [2, 5, 7]
# In the below line of code, the value of radius1 (2)
# is the argument to the printCircumference function
for r in radius:
    printCircumference(r)
