print("Welcome to the tip calculator.")

Bill = float(input("What was the total bill?: $"))
tipAmount = int(input("What percentage(%) tip would you like to give? 10, 12, 15, enter other number amount "))
totalPeople = int(input("How many people to split the bill? "))

# # break down
# tipAsPercent = tipAmount / 100
# totalTipAmount = Bill * tipAsPercent
# totalBill = Bill + totalTipAmount
# billPerPerson = totalBill / totalPeople
# finalBill = round(billPerPerson, 2)

# all the above in one line
totalBill = round((Bill * (tipAmount/100) + Bill) / totalPeople,2)

# needed to us :.2f to be sure to always get 2 decimal places not just one. 
print("Each person should pay: ${:.2f}".format(totalBill))
