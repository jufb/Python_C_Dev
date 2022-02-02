# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# define a list of days in English and French
from ast import Pass
import enum
from logging import exception
from queue import Empty
from tracemalloc import start


days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
daysdict = {"Sun": "Dim", "Mon": "Lun", "Tue": "Mar",
            "Wed": "Mer", "Thu": "Jeu", "Fri": "Ven", "Sat": "Sam"}

# TODO: iterate over a list
print("using iter:")
i = iter(days)

try:
    print(next(i))
    print(next(i))
    print(next(i))
except ValueError as e:
    print("Could not read the next item of the list. Item might be inexistent.", e)
    pass
print("\n---------\n")

# TODO: iterate over a dictionary
try:
    print("dictionary iteration:")
    for i in daysdict:
        print(i, "is", daysdict[i])
except ValueError as e:
    print("Could not read the next item of the list. Item might be inexistent.", e)
    pass

print("\n---------\n")

for i, x in daysdict.items():
    print(i, "is", x)

print("\n---------\n")

# TODO: use the enumerate function
print("using enumerate:")
try:
    for i,x in enumerate(days, start=1):
        print(i,x)
except ValueError as e:
    print("Could not read the next item of the list. Item might be inexistent.", e)
    pass

print("\n---------\n")

# TODO: use the zip function
print("using zip:")
try:
    for i in zip(days, daysFr):
        print(i)
except ValueError as e:
    print("Could not read the next item of the list. Item might be inexistent.", e)
    pass

print("\n---------\n")

# TODO: combine enumerate and zip
print("using enumerate with zip:")
try:
    daysEnglish = ""
    daysFrench = ""
    for i,x in enumerate(zip(days, daysFr), start=1):
        print(i,x)
        print(f"Day {i}, {x[0]} is {x[1]} in French")
        daysEnglish += x[0] + ", "
        daysFrench += x[1] + ", "

    print(f"The days {daysEnglish[:-2]} are in English and {daysFrench[:-2]} are in French")

except ValueError as e:
    print("Could not read the next item of the list. Item might be inexistent.", e)
    pass