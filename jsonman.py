# JsonMan - Written by Patrik Nagy (https://www.lopastudio.sk)
# On 2.11.2023

import json

data_store = {}

def add(key, value):
    data_store[key] = value
    print(f"Added data: {key}: {value}")

def remove(key, value):
    whatorem = input("What to remove? Key or Value from a key (k/v): ")
    if whatorem == "k":
        if key in data_store:
            #Ask for confirmation from the user.
            are_you_sure = input(f"Are you sure you want to remove {key}? (y/n): ")
            if are_you_sure.lower() == "y":
                del data_store[key]
                print(f"Removed {key} from the data store.")
            else:
                return 0
        else:
            print(f"Data not found: {key}")
    
    if whatorem == "v":
        key = input("Enter the key you want to remove: ")
        if key in data_store:
            # Ask for confirmation from the user.
            are_you_sure = input(f"Are you sure you want to remove the value for key '{key}'? (y/n): ")
            if are_you_sure.lower() == "y":
                del data_store[key]
                print(f"Removed value for key '{key}' from the data store.")
            else:
                return 0
        else:
            print(f"Key not found: {key}")


def view(key):
    if key in data_store:
        print(f"Data for {key}: {data_store[key]}")
    else:
        print(f"Data not found: {key}")

def edit(key, new_value):
    if key in data_store:
        data_store[key] = new_value
        print(f"Edited data for {key} to: {new_value}")
    else:
        print(f"Data not found: {key}")

def save(filename):
    try:
        with open(filename, "w") as file:
            json.dump(data_store, file)
            print("Data saved successfully")
    except Exception as e:
        print("Error: " + str(e))

def load(filename):
    try:
        with open(filename, "r") as file:
            global data_store
            data_store = json.load(file)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Error: File not found. Please check if the file exists or if you entered the correct name.")
    except Exception as e:
        print("Error: " + str(e))