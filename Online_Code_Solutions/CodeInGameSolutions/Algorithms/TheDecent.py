import sys

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
#   shuttle height
    shuttleHeight = 0
#   set our index to shoot
    indexToShoot = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
#         conditions if shuttle height is less than mountain heigh
        if shuttleHeight < mountain_h:
#             set shuttele height to moutain height
            shuttleHeight = mountain_h
#            set index to shoot
            indexToShoot = i
#   shoot the mountain needed
    print(indexToShoot)
