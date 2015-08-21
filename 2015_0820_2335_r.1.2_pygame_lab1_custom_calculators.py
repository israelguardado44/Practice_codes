def get_celcius():
    fh_temp = float(input("Enter temperature in Fahrenheit: "))
    celcius = (fh_temp - 32) * (5/9)
    return celcius
#print (get_celcius())

def area_of_trapezoid():
    height = float(input("Enter the height of the trapezoid: "))
    bottom_length = float(input("Enter the bottom length of the trapezoid: "))
    top_length = float(input("Enter the top length of the trapezoid: "))
    area = ((bottom_length + top_length)/2) * height
    print ("The area is:", area)
#print (area_of_trapezoid())

def find_area_of_circle():
    pi = 3.14
    radius = float(input("Enter radius of the circle: "))
    area = pi * (radius**2)
    print ("The area is: ", area)
print (find_area_of_circle())
