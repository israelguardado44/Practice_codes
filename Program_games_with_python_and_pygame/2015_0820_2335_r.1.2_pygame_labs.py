import pygame
import random

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
    
#print (quiz_time())

def print_asterisk():
    i = 16
    t = ' '
    j = 9
    g = 1
    for row in range(1, 10):
        print (' ' * i, end= '')
        i -= 2
        for n in range(1, row):
            print (n, end= ' ')
        for x in range(row, 0, -1):
            if x > 9:
                pass
            else:
                print (x , end= ' ')
        print ()   
    for row in range(1,9):
        print ((t * g), end= ' ')
        for row in range(1,j):
            print (row, end= ' ')
        for row in range(j-2,0, -1):
            print (row, end= ' ')
        j -= 1
        g += 2
        print ()
##print (print_asterisk())

def lab_ch_6_1():
    x = 10
    y = 11
    a = 1
    for row in range(1,10):
        for n in range(x, y):
            print (n, end= ' ')
        x += row
        y += row + 1
        print ()
##print (lab_ch_6_1())


def make_grid():
    green = (0, 255, 0)
    black = (0,0,0)
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("The Grid")

    done = False

    clock = pygame.time.Clock()

    while not done:
        x = 0
        y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(black)
        for row in range (0, 500, 8):
            for col in range(0, 700, 8):
                pygame.draw.rect(screen, green, [col,row,4,4])

        pygame.display.flip()

        clock. tick(60)


##print (make_grid())

def the_dungen():
    room_list = []
    room = ['Dinning room', 3, 1, None, 4]
    room_list.append(room)
    room = ['Kitchen', 2, None, None, 0]
    room_list.append(room)
    room = ['Living Room', None, None, 1, 3]
    room_list.append(room)
    room = ['Bedroom', None, 2, 0, None]
    room_list.append(room)
    room = ['Bathroom', None, 0, None, None]
    room_list.append(room)
    current_room = 0
    done = False
    while not done:
        print ("You are in the {0}. There is a passage to the North and to the East.".format(room_list[current_room][0]))
        direction = input("What direction do you want to go? > ")
        direction = direction.lower()


        if direction == 'quit':
            done = True
        elif direction == 'north':
            next_room = room_list[current_room][1]
        elif direction == 'east':
            next_room = room_list[current_room][2]
        elif direction == 'south':
            next_room = room_list[current_room][3]
        elif direction == 'west':
            next_room = room_list[current_room][4]
        if done == True:
            pass
        elif next_room == None:
            print ("You can't go that way.")
        else:
            current_room = next_room

##print (the_dungen())

def min(a,b,c):
    x = a - b
    if x >= 0:
        if b < c:
            return b
        else:
            return c
    elif a < c:
        return a
    else:
        return c
##print (min(-4,-1007,-3))

def box(h, w):
    for i in range(h):
        for n in range(w):
            print ('*', end='')
        print ()
##print(box(3,2))

def find(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            print (i)
super_lst = [36,31,79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
##print (find(lst, 12))

def create_list(x):
    lst = []
    for i in range(x):
        y = random.randrange(1,x + 1)
        lst.append(y)
    return lst
##print (create_list(5))

def count_list(lst, n):
    count = 0
    for item in lst:
        if item == n:
            count += 1
    return count
##print (count_list(super_lst, 17))

def average_list(lst):
    count = 0
    total = 0
    for item in lst:
        count += 1
        total += item
    average = total / item
    return average
##print (average_list(super_lst))





