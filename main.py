#importing modules
import time
import random
from colorama import Fore, Style

#adding set delay times for ease of adjustment later on
short_delay = 1
regular_delay = 2
long_delay = 3

#game start
start_game = input("Type 'start' to begin the game\n")

while start_game != "start":
    print("You need to type 'start' to start the game.")
    start_game = input("Type 'start' to begin (please)\n")

#introduction
print('"Hello agent. Before we begin this mission, we\'ll go over what you need to do one last time."')
time.sleep(regular_delay)
print('"The yacht you are looking at right now is owned by the world\'s biggest supervillain, Mr.Lamb."')
time.sleep(regular_delay)
print('"We have actionable intel that he is up to something... something very devious."')
time.sleep(short_delay)
print("You need to sneak on, find out what that is, and report back to us.")
time.sleep(short_delay)
print("Good luck!")
time.sleep(long_delay)
print("You are looking at the boat, HMS Computer Science. How will you get on?")

#First choice
time.sleep(short_delay)
print("1. Swim up and sneak onto the boat")
print("2. Disguise yourself as a guard and walk onto the boat")

choice = input("Please enter '1' or '2'.\n")
if choice == "1":
    print("They chose option 1")
elif choice == "2":
    print("They chose option 2")
