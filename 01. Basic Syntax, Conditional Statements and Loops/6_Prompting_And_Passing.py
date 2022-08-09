from sys import argv

script, userName = argv
prompt = "> "

print(f"Hi {userName}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {userName}?")
likes = input(prompt)

print(f"Where so you live {userName}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live ub {lives}. Not sure where that is.
And yo have a {computer} computer. Nice!
""")

