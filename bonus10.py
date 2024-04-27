try:
    length=float((input("Enter the length of the rectangle: ")))
    width=float((input("Enter the width of the rectangle: ")))

    if length==width:
        exit("This is a square!!")

    area = length * width
    print(f"The area of the rectangle is {area}")
except ValueError:
    print("Please enter a valid number!!")