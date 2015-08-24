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
#print (find_area_of_circle())

def quiz_time():
    correct = 0
    print ("It is Quiz time!")
    print ("\n")

    print ("1. What is 45 + 87?")
    ans1 = int(input(":"))
    if ans1 == 132:
        print ("Correct!")
        correct += 1
    else:
        print ("Wrong, you dummy.")
    
    print ("\n")
    print ("2. What is President Obama's first name?")
    ans2 = input(":")
    ans2 = ans2.lower()
    if ans2 == "barack":
        print ("Correct!")
        correct += 1
    else:
        print ("Wrong, way to go genius.")

    print ("\n")
    print ("3. What is the best fast food available?")
    print ("A) McDonalds \nB) In-n-out \nC) Arby's")
    ans3 = input()
    ans3 = ans3.lower()
    if ans3 == "b":
        print ("Correct")
        correct += 1
    elif ans3 == "c":
        print ("You are an idiot, you are wasting oxygen, a weight on society, and you should be ashamed of yourself...how dare you...")
    else:
        print ("No.")

    print ("\n")
    print ("Great! You finished the quiz")
    print ("\n")
    if correct >= 2:
        print ("Congratulations you passed the quiz")
    else:
        print ("You did not pass the quiz...\nYou just wasted everyones time....")
    
print (quiz_time())






