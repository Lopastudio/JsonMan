import jsonman as e # Importing Json Manager to our project as e
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
    if itr == "rem":
        key = input("Artist: ") # Getting the key from the user
        value = input("Album: ") # Getting the value from the user
        e.remove(key, value) # Calling the json manager's "remove" function
    if itr == "rem":
        key = input("Artist: ") # Getting the key from the user
        value = input("Album: ") # Getting the value from the user
        e.remove(key, value) # Calling the json manager's "remove" function
    if itr == "rem":
        key = input("Artist: ") # Getting the key from the user
        value = input("Album: ") # Getting the value from the user
        e.remove(key, value) # Calling the json manager's "remove" function