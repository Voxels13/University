import math

def Ar_circle(r):
    areaC = math.pi * (r*r)
    print(f"{areaC:.2f}")

def Ar_Rectangle(l,w):
    areaR = l*w
    print(f"{areaR:.2f}")

def Ar_Triangle(l,b):
    areaT = (1/2)*l*b
    print(f"{areaT:.2f}")
