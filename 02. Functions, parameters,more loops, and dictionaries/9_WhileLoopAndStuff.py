# numbers = []
# i = 0

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom  i is {i}")
#
#
# print('The numbers: ')
#
# for num in numbers:
#     print(num)


# for function practice
def randomNum(user):
    numbers = []
    i = 0
    while i < user:
        print("\n>>>>>>Top<<<<<<<Number: \n", numbers)
        numbers.append(i)

        i += 1
        print(">>>>>>>Bottom<<<<<<<<Number: \n", numbers)

    print("The List of Numbers are: ")

    for num in range(user):
        print(num)


userInput= randomNum(int(input("Enter a number: ")))