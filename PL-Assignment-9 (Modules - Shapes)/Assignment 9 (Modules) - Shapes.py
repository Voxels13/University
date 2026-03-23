#Modules (Shapes)

import shapes_PLPRAC as sp

print("----------------------------------------------------------")
print("Which Area do you want to calculate?")
print("1.Circle\n2.Rectangle\n3.Triangle")
option = int(input(":"))
print("----------------------------------------------------------")

match option:
    case 1:
        radius = float(input("Enter radius of the circle: "))
        sp.Ar_circle(radius)

    case 2:
        length = float(input("Enter length of the Rectangle: "))
        breadth = float(input("Enter breadth of the Rectangle: "))
        sp.Ar_Rectangle(length,breadth)

    case 3:
        height = float(input("Enter height of the Triangle: "))
        base = float(input("Enter base of the Triangle: "))
        sp.Ar_Triangle(height,base)

    case _:
        raise ValueError("Invalid Input")

