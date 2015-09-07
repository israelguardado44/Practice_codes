import random
print ("Welcome to Camel!")
print ("You have stolen a camel to make your way across the great Mobi desert.")
print ("The natives want their camel back and are chasing you down!")
print ("Survive your desert trek and out run the native.")
done = False
miles_traveled = 0
thirst = 0
energy = 0
natives_distance =  -20
water_in_canteen = 3
oasis = 1
while done == False:
    print ("\n")
    print ("A. Drink from your canteen")
    print ("B. Ahead moderate speed.")
    print ("C. Ahead full speed.")
    print ("D. Stop for the night.")
    print ("E. Status check.")
    print ("Q. Quit.")
    user_input = input("What is your choice? : ")
    print ("\n")
    user_input = user_input.upper()
    if user_input == "Q":
        done = True
    elif user_input == "E":
        print ("Miles traveled: " + str(miles_traveled))
        print ("Drinks in canteen: " + str(water_in_canteen))
        print ("The natives are %d miles behind you" % natives_distance)
        print ("Your camel has used %s energy." % energy)
    elif user_input == "D":
        energy = 0
        print ("The camel is happy")
        rand = random.randrange(7, 15)
        natives_distance += rand
    elif user_input == "C":
        rand = random.randrange(10, 21)
        miles_traveled += rand
        thirst += 1
        rand = random.randrange(1, 4)
        energy += rand
        rand = random.randrange(7, 15)
        natives_distance += rand
        print ("You have travled %d miles" % miles_traveled)
    elif user_input == "B":
        rand = random.randrange(5, 13)
        miles_traveled += rand
        thirst += 1
        energy += 1
        rand = random.randrange(7, 15)
        natives_distance += rand
        print ("You have travled %d miles" % miles_traveled)
    elif user_input == "A":
        if water_in_canteen > 0:
            water_in_canteen -= 1
            thirst = 0
            print ("You feel refreshed")
        else:
            print ("Error: You have no water left")
    if thirst > 6:
        print ("You died of thirst!")
        print ("GAME OVER")
        done == True
    elif thirst > 4:
        print ("You are thristy.")
    if done == True:
        pass
    elif energy > 8:
        print ("Your camel is dead.")
        print ("GAME OVER")
        done = True
    elif energy > 5:
        print ("Your camel is getting tired.")
    if done == True:
        pass
    elif miles_traveled <= natives_distance:
        print ("The natives have caught you!")
        print ("GAME OVER")
        done = True
    elif miles_traveled - natives_distance < 15:
        print ("the natives are getting close!")
    elif miles_traveled >= 200:
        print ("Congratulations you have won the game!")
        done = True
    if done == False:
        desert_oasis = random.randrange(20)
        if desert_oasis == oasis:
            print ("Congratulations, you found an oasis!")
            water_in_canteen = 3
            thirst = 0
            energy = 0


