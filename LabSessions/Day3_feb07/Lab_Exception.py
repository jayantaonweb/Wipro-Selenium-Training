#1.Handle FileNotFoundError Exception When Opening a File
import json
try:


    with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//employ.json", 'r') as file:
        data = json.load(file)


    # read the json file load method
    print(data)
    print(data["name"])
except FileNotFoundError:
    print("enter valid path")


#2.write a program to handle invalid user input

try:
    a= int(input("Enter Digit"))
except Exception as e:
    print(e,"\nEnter valid input")

#3.Write a Python program that generates random alphabetical
# characters, alphabetical strings, and alphabetical strings
# of a fixed length. Use random.choice()


import random



