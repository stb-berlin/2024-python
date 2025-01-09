#! /usr/bin/python3

import pytest
import unittest

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

circles = [Circle(2), Circle(5), Circle(7)]
# In the below line of code, the value of radius1 (2)
# is the argument to the printCircumference function
for circle in circles:
    circle.printCircumference()


# Unit test with pytest
def test_circumference():
    # Erstelle eine Instanz von Circle mit radius 1
    circle = Circle(1)
    # Berechne den Umfang
    result = circle.circumference()
    # Überprüfe, ob das Ergebnis 6.28 ist (ungefähr)
    assert result == 6.28318  # Verwende den exakten Wert von pi * 2
    assert result > 6
    assert result < 7

    circle = Circle(2.5)
    result = circle.circumference()
    assert result == 15.70795


# Unit test with pytest
@pytest.mark.parametrize(
    "radius, expected",
    [
        (1, 6.28318),           # Ganze Zahlen
        (2.5, 15.70795),        # Fliesskommazahlen
        (0, 0),                 # Nullwert
    ]
)

def test_param(radius, expected):
    result = Circle(radius).circumference()
    assert result == expected

####
'''
class TestCircle(unittest.TestCase):
    def test_add(self):
        result = Circle(1).circumference()
        self.assertEqual(result, 6.28318)  # Erwartetes Ergebnis
if __name__ == '__main__':
    unittest.main()
'''
