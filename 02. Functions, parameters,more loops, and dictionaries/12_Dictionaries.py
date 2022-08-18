# create a mapping of state to abbreviations
states={
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}


# create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# add some more cities
cities["NY"] = 'New York'
cities["OR"] = "Portland"

# print out cities
print("-" * 10)
print("NY state has: ", cities["NY"])
print("OR state has: ", cities["OR"])

# print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

# do it by using the state then cities dict
print("-" * 10)
print("Michigan has, ", cities[states['Michigan']]) #gets MI fron state so cities["MI"]
print("Florida has, ", cities[states["Florida"]])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}") # the cites part is says look in this dict while using the for loops abbre in sstate dict.

print("-" * 10)
#safely get an abbreviation by state that might not be there
state = states.get("Texas")
if not state:
    print("meh")

# get a city with a default value
city = cities.get("TX", "Does not exist in dict")
print(f"The city for the state 'TX' is: {city}")
