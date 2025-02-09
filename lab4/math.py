import math

#1
def degrees(degrees1):
    return math.radians(degrees1)
degrees1 = float(input("Input degree:"))
radians = degrees(degrees1)
print(f"Output radian:{radians}")

#2

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: " ))
S = (a + b)/2 * h
print(f"Expected Output:{S}")

#3

n = int(input("Input number of sides: "))
x = float(input("Input the length of a side: "))
print("The area of the polygon is:", (x ** 2 * n) / (4 * math.tan(math.pi / n)))

#4

a = float(input("Length of base: "))
b = float(input("Height of parallelogram: "))
print("Expected Output: ", a * b)