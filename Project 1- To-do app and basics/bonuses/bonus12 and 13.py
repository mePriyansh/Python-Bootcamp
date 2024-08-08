from paser14 import parse
from convert14 import convert

feet_inches= input("Enter the height in feet and inches: ")

parsed = parse(feet_inches)
result= convert(parsed['feet'],parsed['inches'])

print(f"{parsed['feet']} feet {parsed['inches']} inches is equal to {result} meters")

if result < 1.0:
    print("Not Possible")
else:
    print("Possible")