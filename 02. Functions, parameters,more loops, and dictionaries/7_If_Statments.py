print('''You enter a dark room with two doors.
do you go through door # 1 or door #2?''')

door = input('> ')

if door == "1":
    print("There is a giant bear here eating a cheese cake")
    print('''What do you do?
    1. Take the cake.
    2. Scream at the bear.''')

    bear = input("> ")

    if bear == "1":
        print("The bear wats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your face off. Good Job!")
    else:
        print(f"Well doing {bear} is probably better")
        print("Bear runs away.")

elif door == '2':
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("""
    1. Blueberries
    2. Yellow jacket clothespins
    3. Understanding revolvers yelling melodies.""")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good Job!")
    else:
        print("""This is insanity""")
else:
    print("You stumble around and fall into a pit and can't get out. Good Job!")