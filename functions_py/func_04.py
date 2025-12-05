import math

def circle(rad):
    area = math.pi * rad * rad
    circum = math.pi * 2 * rad
    return area, circum

num_1, num_2 = circle(int(input()))
print(f"Area is {num_1} and Circumference {num_2}")