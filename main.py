#importing modules
import time
import random
import colorama
from colorama import Fore, Style

print(Fore.GREEN + "Yo it's ya boy Noah here the DJ!" + Style.RESET_ALL)

start_game = input("Type BAM to start the game: ")

while start_game != "BAM":
    print("You need to type 'BAM' to start the game.")
    start_game = input("Type 'BAM' to begin the game")

print("test line one")
time.sleep(3)
print("test line two")
