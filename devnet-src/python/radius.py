#! /usr/bin/python3

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        pi = 3.14159 # (Will hardcode pi in this example)
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()
        print (f"Circumference of a circle with a radius of {self.radius}\
                 is {myCircumference:.2f}")

radius = [Circle(2), Circle(5), Circle(7)]
# In the below line of code, the value of radius1 (2)
# is the argument to the printCircumference function
for r in radius:
    r.printCircumference()
