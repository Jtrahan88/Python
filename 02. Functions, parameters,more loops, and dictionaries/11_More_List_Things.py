ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ') # makes strings into a list
more_stuff = ["Day", "Night", "Song", "Fisbee", "Corn", "Banana", "Girl", "Boy"]

for item in more_stuff:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go : ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) #what cool!
print(' # '.join(stuff[3:5])) #super stellar!

