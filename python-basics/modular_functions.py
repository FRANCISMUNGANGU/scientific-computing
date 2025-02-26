from math import pi

def calculate_area(shape, dimension1, dimension2=0):
    if shape == 'circle':
        area = pi * dimension1**2
    elif shape == 'rectangle':
        area = dimension1 * dimension2
    elif shape == 'triangle':
        area = 0.5 * dimension1 * dimension2
    else:
        area = "Unsupported shape"
    return area


print(f"Area of the circle is: {calculate_area('circle', 7)}")
print(f"Area of the rectangle is: {calculate_area('rectangle', 5, 10)}")
print(f"Area of the triange is: {calculate_area('triangle', 3, 4)}")