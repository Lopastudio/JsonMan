#Band Jsoner - Simple example script for JsonManager - Written by Patrik Nagy (https://www.lopastudio.sk)

"""
This script demonstrated, how you can use JsonMan in a real project.
It contains every function that JsonMan can provide.

Happy Coding
-- Patrik
"""


import jsonman as e # Importing JsonMan to our project as e
import titler as titler # Importing the titlecard


titler.titlecard() # Calling the titlecard

def clear(): # simple screen clear function
    for x in range(50): # You can adjust this if you would like to
        print("\n")

clear()
titler.titlecard() # Displaying the title card
while True:
    itr = input("@/ ") # Getting input from the user
    if itr == "add": 
        key = input("Artist: ") # Getting the key from the user
        value = input("Album: ") # Getting the value from the user
        e.add(key, value) # Calling the json manager's "add" function
    if itr == "rem":
        key = input("Artist: ") # Getting the key from the user
        value = input("Album: ") # Getting the value from the user
        e.remove(key, value) # Calling the json manager's "remove" function
    if itr == "view":
        key = input("Artist: ") # Getting the key from the user
        e.view(key) # Calling the json manager's "view" function
    if itr == "edit":
        key = input("Artist: ") # Getting the key from the user
        new_value = input("New album: ") # Getting the value from the user
        e.edit(key, new_value) # Calling the json manager's "edit" function
    if itr == "save":
        filename = input("Filename (without .json or others): ") # Getting the key from the user
        e.save(filename + ".json") # Calling the json manager's "save" function
    if itr == "load":
        filename = input("Filename: ") # Getting the key from the user
        e.load(filename) # Calling the json manager's "load" function
    if itr == "exit":
        print("Thanks for using Band Jsoner.")
        quit() # Stopping the application in a peacefull way.