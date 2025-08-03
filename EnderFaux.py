# Importing the required module
import random

# Creating data for lists
subjects = [
    "Priyanka Chopra",
    "Virat Kohli",
    "Narendra Modi",
    "Nitin Gadkare",
    "Nirmala Sitaraman",
    "A group of bikers",
    "Students of IIT Bombay",
    "People of Maharashtra",
    "A big horned Cow",
    "A woman in scooty",
    "Famous Youtuber"
]
Actions = [
    "launches",
    "cancels",
    "orders",
    "declares",
    "dances with",
    "eating",
    "riding",
    "fell in manhole"
]
Objects = [
    "at Red Fort",
    "in local train",
    "inside parliament",
    "in Wankhede Cricket Stadium",
    "during IPL match",
    "in Indian Military",
    "at India Gate",
    "a plate of samosa",
    "near Ganga River",
    "across the Zebra crossing"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(Actions)
    object = random.choice(Objects)
    
    headline = f"BREAKING NEWS: {subject} {action} {object} "
    print("\n" + headline)
    
    userInput = input("Do you create a new headline?(y/n)").strip().lower()
    if(userInput == "n"):
        break


print("Thanks for using EnderFaux, Goodbye!!")