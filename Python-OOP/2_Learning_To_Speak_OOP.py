# """
# class - Tell python to make a new type of thing
#
# object - Two meanings: the most basic type of thing, and any instance of the same thing.
#
# instance - What you get when you tell Python to create a class.
#
# def - How you define a function inside a class.
#
# self - inside the functions in a class, self is a variable for the instane/object being accessed.
#
# inheritance - The concept that one class can inherit traits from another class, much like you and your parents.
#
# composition - The concept that a class an be composed of other classes as parts, much like how a car has wheels.
#
# attribute - A property classes have that are from composition and are usually variables.
#
# is-a - A phrase to say that something inherits from another, as in a "salmon" is-a "fish"
#
# has-a - A phrase to say that something is composed of other things or has a trait, as in " a salmon has-a month"
#
# """
#
#
#
# """
# Phrase Drills
#
# class X(Y) - "Makes a class named X that is-a Y"
#
# class X(object): def __init__(self, J) - "Class X has-a __init__ that takes self and J parameters."
#
# class X(object): def M(self,J) - "Class X has a function named M that takes self and J parameters."
#
# foo - X() - "Sets foo to an instance of class X."
#
# foo.M(J) - "From foo, get the M Function, and call it with parameters self, J"
#
# foo.K - Q "From foo, get the K attribute, and set it to Q"
#
# """


import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object): \n\tdef ***(self,@@@)":
        "class %%% has-a function *** that take self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From the *** variable get the *** attribute and set it to '***'."
}

# do they want to drill phrase first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going intil theu hit CTRL-C
try:
    while True:
        snippnets = list(PHRASES.keys())
        random.shuffle(snippnets)

        for snippnet in snippnets:
            phrase = PHRASES[snippnet]
            question, answer = convert(snippnet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER:   {answer}\n\n")
except EOFError:
    print("\nBye")







