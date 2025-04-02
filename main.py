#importing modules
import time
import random
from colorama import Fore, Style

#adding set delay times for ease of adjustment later on
short_delay = 1
regular_delay = 2.25
long_delay = 3

#random number for the bank vault part
door_code = random.randint(1,100)

#game start
start_game = input("Type 'start' to begin the game\n")

while start_game.strip().lower() != "start":
    print("You need to type 'start' to start the game.")
    start_game = input("Type 'start' to begin (please)\n")

#introduction
print('"Hello agent. Before we begin this mission, we\'ll go over what you need to do one last time."')
time.sleep(regular_delay)
print('"The yacht you are looking at right now is owned by the world\'s biggest supervillain, Mr.Lamb."')
time.sleep(regular_delay)
print('"We have actionable intel that he is up to something... something very devious."')
time.sleep(regular_delay)
print("You need to sneak on, find out what that is, and report back to us.")
time.sleep(regular_delay)
print("Good luck!")
time.sleep(long_delay)
print("You are looking at the boat, HMS Computer Science. How will you get on?")

#First choice
time.sleep(short_delay)
print("1. Swim up and sneak onto the boat")
print("2. Disguise yourself as a guard and walk onto the boat")

choice = input("Please enter '1' or '2'.\n")
if choice.strip().lower() == "1":

    #Swimming route
    print("You delve into the biting cold of the ocean water, accompanied only by the hiss of your oxygen mask.")
    time.sleep(short_delay)
    print("You approach the boat undetected.")
    time.sleep(short_delay)
    print("You take 2 plungers from your bag, and plunge your way up the side of the boat.")
    time.sleep(regular_delay)
    print("You're aboard the boat. You see a nearby stairwell. Which way do you go?")
    time.sleep(regular_delay)

    #Second choice
    print("1. Go upstairs")
    time.sleep(short_delay)
    print("2. Go downstairs")
    choice = input("Please enter '1' or '2'.\n")
    if choice.strip().lower() == "1":

        #Upstairs route
        print("You climb the stairs and reach what appears to be a break room.")
        time.sleep(regular_delay)
        print("There is a balcony with an open door, and a man looking out towards the ocean.")
        time.sleep(regular_delay)
        print("The man is extremely well dressed, with a cigar in his right hand.")
        time.sleep(regular_delay)
        print("The man begins to speak, without turning around.")
        time.sleep(regular_delay)
        print('"Well well well, if it ain\'t the feds"')
        time.sleep(regular_delay)
        print('"Let me make it clear, I am the developer of this game, Noah."')
        time.sleep(regular_delay)
        print("You feel a deep sense of disappointment because of this shameless self-insert.")
        time.sleep(regular_delay)
        print('"Mr.Lamb and his plans are elsewhere, but let me ask you one thing."')
        time.sleep(regular_delay)
        choice = input('"Do you like my game?" y/n\n')
        if choice.strip().lower() == "yes" or "y":

            #I love this amazing game route
            print('"Good choice"')
            time.sleep(long_delay)
            print('"Also, this cigar is fake."')
            time.sleep(regular_delay)
            print("The man jumps off the balcony, into the ocean, never to be seen again.")
            time.sleep(regular_delay)
            print("You return to the stairwell and continue your climb. Eventually, you see something worth investigating.")
            time.sleep(regular_delay)
            print("It's a large metal door, like the ones in those cartoon banks.")
            time.sleep(regular_delay)
            print("This must be where the plans are. You approach the door, and have a closer look at the locking mechanism.")
            time.sleep(regular_delay)
            print("The code appears to be a random number in between one and one hundred!")
            time.sleep(regular_delay)
            print("You decide the only reasonable course of action is to keep trying numbers until you unlock it.")

            #Bank door unlock simulator (extremely fun game mechanic)
            while choice.strip() != door_code:
                choice = int(input("What number do you input?\n"))
                if choice.strip() == door_code:
                    break
                elif choice.strip() == 69:
                    break
                else:
                    print("Looks like that didn't work.")
            print("Success! The door opens with a loud creak, revealing a small podium with a single USB stick on it.")
            time.sleep(regular_delay)
            print("You take the USB, but an alarm sounds! Looks like it's time to leave.")
            time.sleep(regular_delay)
            print("You secure the USB in a waterproof pouch, put on your oxygen mask, and swan dive into the ocean, cinematically.")
            time.sleep(long_delay)
            print("3 guards hold up signs with '10' on them. Perfect score!")
            time.sleep(regular_delay)
            print("Congratulations! You have successfully retrieved the devious plans of Mr.Lamb successfully,\nthe contents of which will be revealed in the sequel.\n(sold separately)")
            time.sleep(long_delay)
            time.sleep(long_delay)
            print(Fore.LIGHTBLUE_EX + "Good ending!" + Style.RESET_ALL)
        elif choice.strip().lower() == "no" or "n":

            #I wouldn't know art if it slapped me in the face route
            print('"Oh... alright then."')
            time.sleep(long_delay)
            print("You die of a heart attack.")
            time.sleep(long_delay)
            print(Fore.LIGHTBLUE_EX + "Bad ending :(" + Style.RESET_ALL)
    elif choice.strip().lower() == "2":

        #Downstairs route
        print("You descend the stairs, reaching a room filled with servers and computers and blinking lights (for cinematic effect)")
        time.sleep(long_delay)
        print("Ask you walk further into the room, you can no longer hear the boat engines or the sound of the waves.")
        time.sleep(long_delay)
        print("There is only the hum of servers in the room.")
        time.sleep(long_delay)
        print("You hear another sound coming from the other end of the room.... typing?")
        time.sleep(regular_delay)
        print("It's a rapidfire, furious typing, like someone is programming, or in an argument on twitter.")
        time.sleep(long_delay)
        print("You get closer to the source of the sound. A mysterious man is sitting in front of a group of monitors.")
        time.sleep(long_delay)
        print("The man is dressed in a hiking outfit, with short hair, glasses and a mask.")
        time.sleep(regular_delay)
        print("This must be the devilish Mr.Lamb.")
        time.sleep(long_delay)
        print("You have 2 options:")
        time.sleep(regular_delay)
        print("1. Confront him")
        print("2. Run away (he is extremely menacing)")
        time.sleep(long_delay)
        choice = input("What do you do?\n")
        if choice.strip().lower() == "1":

            #Confrontation route
            print("You come out of the shadows, ready to strike.")
            time.sleep(regular_delay)
            print('"Who dares disturb my stardew valley gameplay?" He begins to monologue without turning around.')
            time.sleep(regular_delay)
            print('"You know, I-"')
            time.sleep(short_delay)
            #Note: The developer also did not want to figure out an entire Mr.Lamb monologue
            print("You knock him out because you don't have time for this monologue")
            time.sleep(regular_delay)
            print("A small, blinking red light draws your attention. Mr.Lamb pressed a silent alarm button!")
            time.sleep(regular_delay)
            print("There's not much time. You can't take Mr.Lamb with you, but you can take the next best thing, his files.")
            time.sleep(regular_delay)
            print("You steal as many files as you can from his computer, making an extremely close escape.")
            time.sleep(regular_delay)
            print("You get back to your base of operations successfully. Sifting through many pirated games, you find Mr.Lamb's evil plans,\n the contents of which will be revealed in the sequel\n(sold separately)")
            time.sleep(long_delay)
            time.sleep(long_delay)
            print(Fore.LIGHTBLUE_EX + "Good ending!" + Style.RESET_ALL)
        elif choice.strip().lower() == "2":

            #Run away route
            print("You find yourself shaking in your boots because of his menacing aura.")
            time.sleep(regular_delay)
            print("You NEED to get out of this place NOW!")
            time.sleep(regular_delay)
            print("You run as fast as you can, shoving guards out of the way, even though you never saw one on the way here.")
            time.sleep(long_delay)
            print("You jump overboard, returning home in shame. Mr.Lamb was too powerful for your mere mortal mind to handle.")
            time.sleep(long_delay)
            print(Fore.LIGHTBLUE_EX + "Bad ending :(" + Style.RESET_ALL)

elif choice.strip().lower() == "2":

    #guard disguise route
    print("You find a lone guard at the docks and knock them out, stealing their uniform.")
    time.sleep(regular_delay)
    print("It's about 6 sizes too small, but nobody will notice")
    time.sleep(regular_delay)
    print("You make your way onto the boat, acting natural.")
    time.sleep(regular_delay)
    print("A guard notices that your uniform is 6 sizes too small!")
    time.sleep(regular_delay)
    print('"Hey! What\'s wrong with your uniform?"')
    time.sleep(regular_delay)
    print("1. Flirt")
    print("2. Lie")
    time.sleep(short_delay)
    choice = input("What do you do?\n")
    if choice.strip().lower() == "1":

        #flirt route
        print("You remember Mr.Nagra's masterclass on flirting, and conjure up a line sure to seduce this guard.")
        time.sleep(regular_delay)
        print('"Hey, are you a toilet? Because you\'re so skibidi"')
        time.sleep(long_delay)
        print("...")
        time.sleep(long_delay)
        print("...")
        time.sleep(long_delay)
        print("...")
        time.sleep(long_delay)
        print(Fore.RED + "you are shot and killed." + Style.RESET_ALL)
        time.sleep(long_delay)
        print(Fore.LIGHTBLUE_EX + "Yikes man I don't even know what ending this is" + Style.RESET_ALL)

    elif choice.strip().lower() == "2":

        #lie route
        print('"My uniform got shrunk in the laundry" you say')
        time.sleep(regular_delay)
        print('"Alright. Pay more attention next time"')
        time.sleep(regular_delay)
        print("The guard walks away, then slips on a banana peel, then gets up and continues walking away.")
        time.sleep(regular_delay)
        print("You continue to wander through the boat, until eventually you find yourself in the bowels of the ship.")
        time.sleep(regular_delay)
        print('Eventually, you reach a door labeled "DO NOT ENTER"')
        time.sleep(regular_delay)
        print("1. Go through the door")
        print("2. Look elsewhere")
        choice = input("What do you do?\n")
        if choice.strip().lower() == "1":

            #enter the door route
            print("You open the door and go through, realizing there is nothing beneath your feet.")
            time.sleep(regular_delay)
            print('"That door just goes out the side of the boat!" You realize, as you plummet into the ocean')
            time.sleep(regular_delay)
            print("Due to a very deceptive door, you return home empty handed. Who does something like that anyway???")
            time.sleep(long_delay)
            print(Fore.LIGHTBLUE_EX + '"Bruh" ending' + Style.RESET_ALL)
        elif choice.strip().lower() == "2":

            #go somewhere else route
            print("You decide it's better to heed the door's warning and look elsewhere.")
            time.sleep(regular_delay)
            print("As you continue to traverse the ship, you see a sign in the corridor.")
            time.sleep(regular_delay)
            print('"NO UNAUTHORIZED ACCESS", this is a good sign. You continue in that direction.')
            time.sleep(regular_delay)
            print("Suddenly, you hear an approaching conversation. People are heading in your direction!")
            time.sleep(regular_delay)
            print("1. Try to hide")
            print("2. Appear like you're supposed to be there")
            choice = input("What do you do?\n")
            if choice.strip().lower() == "1":

                #hide attempt route
                print("You look around frantically, searching for a spot to hide, but there's no good spots!")
                time.sleep(regular_delay)
                print("The guards catch you in an unauthorized area. You try to fight back, but the guards have plot armor.")
                time.sleep(regular_delay)
                print("They overpower you, and bring you to the monstrous Mr.Lamb himself.")
                time.sleep(regular_delay)
                print('"I\'ve been expecting you" he says, as he turns around in his revolving chair.')
                time.sleep(regular_delay)
                print('"You were so close, and yet, so far."')
                time.sleep(regular_delay)
                print('"This is where it ends. No more games, no more choices."')
                time.sleep(regular_delay)
                print("A guard walks up to Mr.Lamb, and whispers something. Mr.Lamb's face twists into an expression of surprise.")
                time.sleep(regular_delay)
                print('"I\'ll deal with you later. Right now, I have more pressing concerns." Mr.Lamb gets up, and walks out of the room.')
                time.sleep(regular_delay)
                print("You have fallen into the hands of the villainous villain, Mr.Lamb, but his attention was drawn away by something else. What could've happened?")
                time.sleep(long_delay)
                print(Fore.LIGHTBLUE_EX + "Bad ending :(" + Style.RESET_ALL)
            elif choice.lower().strip() == "2":

                #nonchalant dreadhead route
                print("You walk as if you're supposed to be there, ignoring the guards and continuing on your way.")
                time.sleep(regular_delay)
                print("One of them reaches out to block your path.")
                time.sleep(regular_delay)
                print('Hey, can\'t you read? Nobody is allowed here without permission!')
                time.sleep(regular_delay)
                print("At the risk of your pants spontaneously combusting, you lie again.")
                time.sleep(regular_delay)
                print('"I have permission to be here, directly from Mr.Lamb himself!" you reply sternly.')
                time.sleep(regular_delay)
                print("The man begins to shake at the mere mention of Mr.Lamb's name. He backs off.")
                time.sleep(regular_delay)
                print('"A- Alright. Sorry sir."')
                time.sleep(regular_delay)
                print("The guards slink out of sight, leaving you free to continue on your way.")
                time.sleep(regular_delay)
                print("You reach what appears to be a laboratory of some sort, a room made for designing nefarious devices.")
                time.sleep(regular_delay)
                print("The room is filled with a strange assortment of items. Saws and centrifuges, 3D printers, even random pieces of metal scrap.")
                time.sleep(long_delay)
                print("In the middle of the room, there is a small workbench with a stereotypical manila folder on it, labeled 'PLANS' in red ink.")
                time.sleep(regular_delay)
                print("Something valuable definitely has to be in here!")
                time.sleep(regular_delay)
                print("You open the folder, only to find that it is completely empty, save for a small sheet of paper.")
                time.sleep(regular_delay)
                print(Fore.GREEN + "Clara was here" + Style.RESET_ALL)
                time.sleep(long_delay)
                print("It appears the plans you were looking for were taken, but by whom?")
                time.sleep(long_delay)
                print("You have no choice but to return home, although, not empty handed.")
                time.sleep(long_delay)

                #Had to make her a plot point for the memes
                print("This mysterious new adversary, " + Fore.GREEN + "Clara " + Style.RESET_ALL + "will not be disappearing any time soon.")
                time.sleep(long_delay)
                print(Fore.LIGHTBLUE_EX + "To be continued?" + Style.RESET_ALL)
else:
    print("Error, please try again.")
    choice = input("Please enter '1' or '2'.\n")
