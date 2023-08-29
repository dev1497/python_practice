import math
from datetime import date
def area(radius):
    """ calculates area of circle from radius
        args(radius):int or float
        returns calculated area  O(1) time, O(1) space"""
    return math.pi*(radius**2)
print("Area is:",area(10))
def genListTuple(numbers):
    """ converts comma-separated numbers into list,tuple
        args(numbers):comma-separated string values
        returns generated list and tuple
        O(n) time,O(n) space
     """
    listNum = numbers.split(",")
    tupleNum = tuple(listNum)
    return listNum,tupleNum
num = input("Enter numbers:")
list,tuple = genListTuple(num)
print("List:",list)
print("Tuple:",tuple)
def countDays(d1,d2):
    """ counts date difference in days between 2 days
        args(d1,d2):date type objects
        returns absolute difference of dates
        O(1) time,O(1) space
    """
    return abs(d1-d2)

d2 = date(2023,5,4)
d1 = date(2023,6,2)
print("Days are",countDays(d1,d2))




