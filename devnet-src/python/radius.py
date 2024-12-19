def circumference(radius):
    pi = 3.14159 # (Will hardcode pi in this example)
    circumferenceValue = pi * radius * 2
    return circumferenceValue

def printCircumference(radius):
    myCircumference = circumference(radius)
    print (f"Circumference of a circle with a radius of {radius} is {myCircumference}")

radius1 = 2
radius2 = 5
radius3 = 7
# In the below line of code, the value of radius1 (2)
# is the argument to the printCircumference function
printCircumference(radius1)
printCircumference(radius2)
printCircumference(radius3)
