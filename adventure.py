# Text based adventure game

number = 2 #keeps track of the player's location
letter = "B"

#dictionary of descriptions of the rooms
description = {
    "1B":"The room is covered in smooth, mirror-like ice from floor to ceiling. It's really cold...",
    "2B":"You lift your gaze and see luscious grassland. The wind gently breezes by, and the sea of green before you rustles with it. Where did all the birds and rivers come from?",
    "3B":"You step into the room and almost get hit by a stream of boiling lava. The entire room is like a cave lit by the orange-red glow of fire.",
    "2A":"There's a lagoon! It's filled with clear, turquoise water. There's shadows of fish swimming underneath, and it looks pretty bottomless... You're suddenly filled with the urge to go in for a swim.",
    "2C":"Suddenly you're not on land anymore. You're riding on a cloud in the vast skies; there's birds flying beside you. You idly wonder how you're being supported by a cloud...",
    }
print ("Welcome to the Text-Based Adventure Game!")
print ("You may move right (r), left (l), up (u), or down (d), into different rooms.")
print ('''This is the basic layout of the mysterious building:
             ____
            | 2A |
        ____|____|____
       | 1B | 2B | 3B |
       |____|____|____|
            | 2C |
            |____|
''')

#Starting description
print ("You are currently in room 2B.")
print (description.get(str(number)+letter))

again="Y"
#loop until the player is done exploring
while (again=="y" or again == "Y"):
    valid=False
    while (valid == False):
        direction = input("How would you like to move?: ")

        if (direction.lower() == "r" or direction.lower() == "right"):
            if (number<3):
                if (letter=="B"):
                    #move to the right
                    number+=1
                    valid=True
            else:
                print ("You cannot move further in this direction!")
        elif (direction.lower() == "l" or direction.lower() == "left"):
            if (number>1):
                if (letter=="B"):
                    #move to the left
                    number-=1
                    valid=True
            else:
                print ("You cannot move further in this direction!")
        elif (direction.lower() == "u" or direction.lower() == "up"):
            if (letter>"A"):
                if (number==2):
                    #move up
                    letter = chr(ord(letter)-1) #ord() transforms the string of length one into the ASCII value, #chr() transforms the value of the ASCII code into its respective string
                    valid=True
            else:
                print ("You cannot move further in this direction!")
        elif (direction.lower()=="d" or direction.lower () == "down"):
            if (letter<"C"):
                if (number==2):
                #move down
                    letter = chr(ord(letter)+1)
                    valid=True
            else:
                print ("You cannot move further in this direction!")
        else:
            print ("This is an invalid answer.")
            
    print ("\nYou are now in room " + str(number) + letter)
    print (description.get(str(number)+letter))
    
    again = input ("Would you like to keep exploring? (Y to continue): ")
print ("Thank you for playing!")
