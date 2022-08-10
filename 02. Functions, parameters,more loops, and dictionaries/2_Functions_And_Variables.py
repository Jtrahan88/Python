# Lesson: Variables in function are not tied into script

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"""
         You have {cheese_count} cheeses!
         You have {boxes_of_crackers} box of crackers!
         Man that's enough for the party!
         Get a blanket\n""")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 20
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We an even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000

                    )