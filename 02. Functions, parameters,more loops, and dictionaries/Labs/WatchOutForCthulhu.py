from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    try: # the try except clause for user input seem to need the input before the try then assigned another var tp the orginal input variable.
        how_much = int(input("> ")) # seems that if a try is i a function the above comment can be ignored
        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            dead("You greedy bastard! Bear smells your greedy and eats you for dinner.")
    except ValueError:
            print("Man we can can only use number...Never count before? Try again.\n")
            gold_room()

def bear_room():
    print('''\tThere is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    ''')
    bear_moved = False

    while True:
        choice = input("""\t\t>take honey? 
        >taunt bear?
        >open door?
        >""")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("""The bear has moved from the door.
            You head through it""")
            bear_moved = True
            gold_room()
        # elif choice == "open door" and bear_moved:
        #     gold_room()
        elif choice == "open door" and not bear_moved:
            dead("Bear sees you being sneaky and eats your face off. Esta deliciouso.")
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("""\tHere you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?""")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print(why, "Game over")
    exit(0)

def start():
    print("""\tYou are in a dark room.
    There is a door to your right and left.
    Which one do you take?""")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
