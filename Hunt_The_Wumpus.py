#Hunt The Wumpus v1.04
#goal is to find and shoot the wumpus without going in same room as it.
#This release is a testing release for an idea to display maps during the game.

import random
import time
import os

def rules():
    #Prompt player if they would like to view rules
    rules = input("Welcome to Hunt The Wumpus! Would you like to view the rules? Y/N: ")
    #view rules
    if rules == "Y" or rules == "y":
        print("You are a spelaeologist who has found the cave said to contain an ancient beast called a Wumpus. You job is to catch and shoot it in order to analyze it.\nYou can move within the cave, which is a 4 by 4 grid of identical rooms, with the command 'm' or 'move', and shoot with 's' or 'shoot'.\nYou must shoot into the next room if you think the wumpus is there. But beware, if you shoot and miss the wumpus may come out and eat you! You will be told when you smell a wumpus in a nearby room. If you enter the room with the wumpus, it will eat you and kill you.\nTwo rooms in the cave have bottomless pits. You will be told if you feel a draft coming from a pit.\nTwo rooms in the cave contain bats that teleport you to a random room. They may teleport you into a bottomless pit, or even in with the Wumpus. You will be told when you hear bats nearby.\nThere may be cases where more than one of these hazards can occur in the same room. \nGood luck and have fun!")
        time.sleep(1)
    #prompt again if input is not Y or N
    elif rules != "N" and rules != "n":
        print("Invalid input.")
        time.sleep(0.5)
        main()
    #skip rules if player wishes
    else:
        print("OK. Have fun!")
        time.sleep(1)
        
def playagain():
    #Prompt user if they want to replay game
    replay = input("Would you like to play again? Y/N: ")
    #Go to main if user replies yes
    if replay == "Y" or replay == "y":
        print("OK. Replaying... ")
        time.sleep(1)
        main()
    #close game if input is N
    elif replay == "N" or replay == "n":
        print("OK. Exiting now.")
        time.sleep(1)
    else: 
        print("Invalid input.")
        playagain()
        
def main():
    #Prompt for rules
    rules()
    #Set locations for wumpus, pits and player
    wumpusRoom = str(random.randint(1,16))
    playerLocation = str(random.randint(1,16))
    pit1 = str(random.randint(1,16))
    pit2 = str(random.randint(1,16))
    bat1 = str(random.randint(1,16))
    bat2 = str(random.randint(1,16))
    if pit1 == wumpusRoom:
        pit1 = str(random.randint(1,16))
    if pit2 == wumpusRoom:
        pit2 = str(random.randint(1,16))
    if pit1 == pit2:
        pit2 = str(random.randint(1,16))
    if bat1 == pit1 or bat1 == pit2 or bat1 == wumpusRoom:
        bat1 = str(random.randint(1,16))
    if bat2 == pit1 or bat2 == pit2 or bat2 == wumpusRoom:
        bat2 = str(random.randint(1,16))
    if bat2 == bat1:
        bat2 = str(random.randint(1,16))
    if bat2 == pit1 or bat2 == pit2 or bat2 == wumpusRoom:
        bat2 = str(random.randint(1,16))
    #Reset player location so they have only a (1/16^2) *3 (about 1 in 133) chance to spawn in the same room as the wumpus or a pit. This chance can be changed by the bats. 
    #The cave also has about a 1 in 400 chance to generate with only one pit or one bat.
    if playerLocation == wumpusRoom or playerLocation == pit1 or playerLocation == pit2:
        playerLocation = str(random.randint(1,16))
    crash = False
    #return wumpusRoom,playerLocation,pit1,pit2,crash
    #go to wumpus function to play
    wumpus(wumpusRoom,playerLocation,pit1,pit2,bat1,bat2,crash)
    
def wumpus(wumpusRoom,playerLocation,pit1,pit2,bat1,bat2,crash):
    crash = False
    while crash == False:
        #tp player somewhere. There is a likely but not guaranteed chance that if they begin by teleporting into a pit or wumpus, they die. This becomes guaranteed after turn 1.
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))
            if playerLocation == wumpusRoom:
                playerLocation = str(random.randint(1,16))
            elif playerLocation == pit1 or playerLocation == pit2:
                playerLocation = str(random.randint(1,16))
        #On the off-chance the player still spawns with the wumpus, they die
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            break
        #Check if player spawns in pit on rare chance
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            break
        #Set possibilities for each room the player can be in.
        #For sake of simplicity, only room 1 has comments that apply to all the rooms.
        if playerLocation == "1":
            #tell user what room they're in
            print("You are in room 1. You can move to room 2 or 5.")
            #Tell user if wumpus is in room within shooting range, if bats are around, and if pit is in neighbouring cave.
            if pit1 == "2" or pit2 == "2" or pit1 == "5" or pit2 == "5":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")
            if wumpusRoom == "2" or wumpusRoom == "5":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "2" or bat2 == "2" or bat1 == "5" or bat2 == "5":
                time.sleep(0.5)
                print("You hear bats nearby.")
            #Prompt user to move or shoot
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                #prompt user what room to go to
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                #pass if player inputs anything that isn't an integer 0-16
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)
                    time.sleep(0.5)
                    if dest == 2:
                        #change playerLocation to chosen room
                        print("You move to room 2.")
                        playerLocation = "2"
                        time.sleep(0.5)
                    elif dest == 5:
                        print("You move to room 5.")
                        playerLocation = "5"
                        time.sleep(0.5)
                    elif dest != 2 and dest != 5:
                        print("You can't go there.")
                        #reset dest value
                        dest = 0
                        time.sleep(0.5)
                        pass
            elif ms == "s" or ms == "shoot": 
                #prompt user for what room they will shoot to
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 2:
                        print("You shot toward room 2.")
                    elif shot == 5:
                        print("You shot toward room 5.")
                    else:
                        print("You can't shoot there.")
                        #Reset shot value
                        shot = 0
                        pass
                    #if shot is accurate, tell player they win and ask them to replay
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass
                    #if shot misses, wumpus has 1 in 2 chance to eat player. If this happens, the player loses.
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            #prompt player to play again if shot misses
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            #set player location to out of world so program stops properly
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass 
            
        #Check if player entered a room with bats. Done after end of each room. Before Wumpus and pit as those can kill the player if they are teleported there.
        #If the bats spawn in the same room as a wumpus or pit, that hazard can no longer kill the player.
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))        
        
        #check if player is now in same room as wumpus before advancing. This is done after end of each room.
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            #set player location to out of world so program stops properly
            playerLocation = "0"
            break
        #Also check if player walked into a pit at end of each room
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True 
            playerLocation = "0"
            break
       
            
        if playerLocation == "2":
            print("You are in room 2. You can move to room 1, 3, or 6.")
            if pit1 == "1" or pit2 == "1" or pit1 == "3" or pit2 == "3" or pit1 == "6" or pit2 == "6":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")            
            if wumpusRoom == "1" or wumpusRoom == "3" or wumpusRoom == "6":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "1" or bat2 == "1" or bat1 == "3" or bat2 == "3" or bat1 == "6" or bat2 == "6":
                time.sleep(0.5)
                print("You hear bats nearby.")                
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 1:
                        print("You move to room 1.")
                        playerLocation = "1"
                        time.sleep(0.5)
                    elif dest == 3:
                        print("You move to room 3.")
                        playerLocation = "3"
                        time.sleep(0.5)
                    elif dest == 6:
                        print("You move to room 6")
                        playerLocation = "6"
                        time.sleep(0.5)
                    else:
                        print("You can't go there.")
                        dest = 0
                        time.sleep(0.5)
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 1:
                        print("You shot toward room 1.")
                    elif shot == 3:
                        print("You shot toward room 3.")
                    elif shot == 6:
                        print("You shot toward room 6")
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass  
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break 
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True 
            playerLocation = "0"
            break
        

            
        if playerLocation == "3":
            print("You are in room 3. You can move to room 2, 4, or 7.")
            if pit1 == "2" or pit2 == "2" or pit1 == "4" or pit2 == "4" or pit1 == "7" or pit2 == "7":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "2" or wumpusRoom == "4" or wumpusRoom == "7":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "2" or bat2 == "2" or bat1 == "4" or bat2 == "4" or bat1 == "7" or bat2 == "7":
                time.sleep(0.5)
                print("You hear bats nearby.")                      
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)
                    time.sleep(0.5)
                    if dest == 2:
                        print("You move to room 2.")
                        playerLocation = "2"
                        time.sleep(0.5)
                    elif dest == 4:
                        print("You move to room 4.")
                        playerLocation = "4"
                        time.sleep(0.5)
                    elif dest == 7:
                        print("You move to room 7")
                        playerLocation = "7"
                        time.sleep(0.5)
                    else:
                        print("You can't go there.")
                        dest = 0
                        time.sleep(0.5)
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 2:
                        print("You shot toward room 2.")
                    elif shot == 4:
                        print("You shot toward room 4.")
                    elif shot == 7:
                        print("You shot toward room 7")
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass  
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = "0"
            break 
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True   
            playerLocation = "0"
            break

            
        if playerLocation == "4":
            print("You are in room 4. You can move to room 3 or 8.")
            if pit1 == "8" or pit2 == "8" or pit1 == "3" or pit2 == "3":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "3" or wumpusRoom == "8":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "3" or bat2 == "3" or bat1 == "8" or bat2 == "8":
                time.sleep(0.5)
                print("You hear bats nearby.")                      
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 3:
                        print("You move to room 3.")
                        playerLocation = "3"
                        time.sleep(0.5)
                    elif dest == 8:
                        print("You move to room 8.")
                        playerLocation = "8"
                        time.sleep(0.5)
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 3:
                        print("You shot toward room 3.")
                    elif shot == 8:
                        print("You shot toward room 8")
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = "0"
            break 
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True    
            playerLocation = "0"
            break
                    
            
        if playerLocation == "5":
            print("You are in room 5. You can move to room 1 or 6.")
            if pit1 == "1" or pit2 == "1" or pit1 == "6" or pit2 == "6":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "1" or wumpusRoom == "6":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "1" or bat2 == "1" or bat1 == "6" or bat2 == "6":
                time.sleep(0.5)
                print("You hear bats nearby.")                      
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)
                    time.sleep(0.5)
                    if dest == 1:
                        print("You move to room 1.")
                        playerLocation = "1"
                        time.sleep(0.5)
                    elif dest == 6:
                        print("You move to room 6")
                        playerLocation = "6"
                        time.sleep(0.5)
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 1:
                        print("You shot toward room 1.")
                    elif shot == 6:
                        print("You shot toward room 6")
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = "0"
            break   
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break
                
            
    
        if playerLocation == "6":
            print("You are in room 6. You can move to room 2, 5, 7, or 10.")
            if pit1 == "2" or pit2 == "2" or pit1 == "5" or pit2 == "5" or pit1 == "7" or pit2 == "7" or pit1 == "10" or pit2 == "10":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "2" or wumpusRoom == "5" or wumpusRoom == "7" or wumpusRoom == "10":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "2" or bat2 == "2" or bat1 == "5" or bat2 == "5" or bat1 == "7" or bat2 == "7" or bat1 == "10" or bat2 == "10":
                time.sleep(0.5)
                print("You hear bats nearby.")                      
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)
                    time.sleep(0.5)
                    if dest == 2:
                        print("You move to room 2.")
                        playerLocation = "2"
                        time.sleep(0.5)
                    elif dest == 5:
                        print("You move to room 5.")
                        playerLocation = "5"
                        time.sleep(0.5)
                    elif dest == 7:
                        print("You move to room 7.")
                        playerLocation = "7"
                        time.sleep(0.5) 
                    elif dest == 10:
                        print("You move to room 10.")
                        playerLocation = "10"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 2:
                        print("You shot toward room 2.")
                    elif shot == 5:
                        print("You shot toward room 5")
                    elif shot == 7:
                        print("You shot toward room 7")    
                    elif shot == 10:
                        print("You shot toward room 10")            
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = "0"
            break 
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break
                   
    
        if playerLocation == "7":
            print("You are in room 7. You can move to room 3, 6, 8, or 11.")
            if pit1 == "3" or pit2 == "3" or pit1 == "6" or pit2 == "6" or pit1 == "8" or pit2 == "8" or pit1 == "11" or pit2 == "11":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom =="3" or wumpusRoom == "6" or wumpusRoom == "8" or wumpusRoom == "11":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "3" or bat2 == "3" or bat1 == "6" or bat2 == "6" or bat1 == "8" or bat2 == "8" or bat1 == "11" or bat2 == "11":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)
                    time.sleep(0.5)
                    if dest == 3:
                        print("You move to room 3.")
                        playerLocation = "3"
                        time.sleep(0.5)
                    elif dest == 6:
                        print("You move to room 6.")
                        playerLocation = "6"
                        time.sleep(0.5)
                    elif dest == 8:
                        print("You move to room 8.")
                        playerLocation = "8"
                        time.sleep(0.5) 
                    elif dest == 11:
                        print("You move to room 11.")
                        playerLocation = "11"
                        time.sleep(0.5)            
                    else:
                        print("Invalid input.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 3:
                        print("You shot toward room 3.")
                    elif shot == 6:
                        print("You shot toward room 6")
                    elif shot == 8:
                        print("You shot toward room 8")    
                    elif shot == 11:
                        print("You shot toward room 11")            
                    else:
                        print("You can't go there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = "0"
            break  
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True   
            playerLocation = "0"
            break
                      
            
        if playerLocation == "8":
            print("You are in room 8. You can move to room 4, 7, or 12.")
            if pit1 == "4" or pit2 == "4" or pit1 == "12" or pit2 == "12" or pit1 == "7" or pit2 == "7":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "4" or wumpusRoom == "7" or wumpusRoom == "12":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "4" or bat2 == "4" or bat1 == "7" or bat2 == "7" or bat1 == "12" or bat2 == "12":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)
                    time.sleep(0.5)
                    if dest == 4:
                        print("You move to room 4.")
                        playerLocation = "4"
                        time.sleep(0.5)
                    elif dest == 7:
                        print("You move to room 7.")
                        playerLocation = "7"
                        time.sleep(0.5) 
                    elif dest == 12:
                        print("You move to room 12.")
                        playerLocation = "12"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 4:
                        print("You shot toward room 4.")
                    elif shot == 7:
                        print("You shot toward room 7")    
                    elif shot == 12:
                        print("You shot toward room 12")            
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = "0"
            break        
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True   
            playerLocation = "0"
            break
                    
        
        if playerLocation == "9":
            print("You are in room 9. You can move to room 5, 10, or 13.")
            if pit1 == "5" or pit2 == "5" or pit1 == "10" or pit2 == "10" or pit1 == "13" or pit2 == "13":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "5"  or wumpusRoom == "10" or wumpusRoom == "13":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "5" or bat2 == "5" or bat1 == "13" or bat2 == "13" or bat1 == "10" or bat2 == "10":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)
                    time.sleep(0.5)
                    if dest == 5:
                        print("You move to room 5.")
                        playerLocation = "5"
                        time.sleep(0.5)
                    elif dest == 10:
                        print("You move to room 10.")
                        playerLocation = "10"
                        time.sleep(0.5) 
                    elif dest == 13:
                        print("You move to room 13.")
                        playerLocation = "13"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 5:
                        print("You shot toward room 5")
                    elif shot == 10:
                        print("You shot toward room 10")    
                    elif shot == 13:
                        print("You shot toward room 13")            
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = "0"
            break   
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True  
            playerLocation = "0"
            break
           
            
        if playerLocation == "10":
            print("You are in room 10. You can move to room 6, 9, 11, or 14.")
            if pit1 == "6" or pit2 == "6" or pit1 == "9" or pit2 == "9" or pit1 == "11" or pit2 == "11" or pit1 == "14" or pit2 == "14":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "2" or wumpusRoom == "5" or wumpusRoom == "7" or wumpusRoom == "10":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "6" or bat2 == "6" or bat1 == "9" or bat2 == "9" or bat1 == "11" or bat2 == "11" or bat1 == "14" or bat2 == "14":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 6:
                        print("You move to room 6.")
                        playerLocation = "6"
                        time.sleep(0.5)
                    elif dest == 9:
                        print("You move to room 9.")
                        playerLocation = "9"
                        time.sleep(0.5)
                    elif dest == 11:
                        print("You move to room 11.")
                        playerLocation = "11"
                        time.sleep(0.5) 
                    elif dest == 14:
                        print("You move to room 14.")
                        playerLocation = "14"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 6:
                        print("You shot toward room 6.")
                    elif shot == 9:
                        print("You shot toward room 9")
                    elif shot == 11:
                        print("You shot toward room 11")    
                    elif shot == 14:
                        print("You shot toward room 14")            
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = "0"
            break  
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break
           
    
        if playerLocation == "11":
            print("You are in room 11. You can move to room 7, 10, 12, or 15.")
            if pit1 == "7" or pit2 == "7" or pit1 == "10" or pit2 == "10" or pit1 == "12" or pit2 == "12" or pit1 == "15" or pit2 == "15":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "7" or wumpusRoom == "10" or wumpusRoom == "12" or wumpusRoom == "15":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "12" or bat2 == "12" or bat1 == "15" or bat2 == "15" or bat1 == "7" or bat2 == "7" or bat1 == "10" or bat2 == "10":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 7:
                        print("You move to room 7.")
                        playerLocation = "7"
                        time.sleep(0.5)
                    elif dest == 10:
                        print("You move to room 10.")
                        playerLocation = "10"
                        time.sleep(0.5)
                    elif dest == 12:
                        print("You move to room 12.")
                        playerLocation = "12"
                        time.sleep(0.5) 
                    elif dest == 15:
                        print("You move to room 15.")
                        playerLocation = "15"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 7:
                        print("You shot toward room 7.")
                    elif shot == 10:
                        print("You shot toward room 10")
                    elif shot == 12:
                        print("You shot toward room 12")    
                    elif shot == 15:
                        print("You shot toward room 15")            
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = "0"
            break 
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True   
            playerLocation = "0"
            break
                      
            
        if playerLocation == "12":
            print("You are in room 12. You can move to room 8, 11, or 16.")
            if pit1 == "8" or pit2 == "8" or pit1 == "11" or pit2 == "11" or pit1 == "16" or pit2 == "16":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "8" or wumpusRoom == "11" or wumpusRoom == "16":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "8" or bat2 == "8" or bat1 == "11" or bat2 == "11" or bat1 == "16" or bat2 == "16":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 8:
                        print("You move to room 8.")
                        playerLocation = "8"
                        time.sleep(0.5)
                    elif dest == 11:
                        print("You move to room 11.")
                        playerLocation = "11"
                        time.sleep(0.5) 
                    elif dest == 16:
                        print("You move to room 16.")
                        playerLocation = "16"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 8:
                        print("You shot toward room 8.")
                    elif shot == 11:
                        print("You shot toward room 11")
                    elif shot == 16:
                        print("You shot toward room 16")
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = "0"
            break  
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True  
            playerLocation = "0"
            break
            
            
        if playerLocation == "13":
            print("You are in room 13. You can move to room 9 or 14.")
            if pit1 == "9" or pit2 == "9" or pit1 == "14" or pit2 == "14":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "9" or wumpusRoom == "14":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "9" or bat2 == "9" or bat1 == "14" or bat2 == "14":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 9:
                        print("You move to room 9.")
                        playerLocation = "9"
                        time.sleep(0.5)
                    elif dest == 14:
                        print("You move to room 14.")
                        playerLocation = "14"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 9:
                        print("You shot toward room 9.")
                    elif shot == 14:
                        print("You shot toward room 14")           
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass 
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break 
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True  
            playerLocation = "0"
            break
     
        if playerLocation == "14":
            print("You are in room 14. You can move to room 10, 13, or 15.")
            if pit1 == "15" or pit2 == "15" or pit1 == "13" or pit2 == "13" or pit1 == "10" or pit2 == "10":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "10" or wumpusRoom == "13" or wumpusRoom == "15":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "13" or bat2 == "13" or bat1 == "15" or bat2 == "15" or bat1 == "10" or bat2 == "10":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 10:
                        print("You move to room 10.")
                        playerLocation = "10"
                        time.sleep(0.5)
                    elif dest == 13:
                        print("You move to room 13.")
                        playerLocation = "13"
                        time.sleep(0.5)
                    elif dest == 15:
                        print("You move to room 15.")
                        playerLocation = "15"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 10:
                        print("You shot toward room 10.")
                    elif shot == 13:
                        print("You shot toward room 13")
                    elif shot == 15:
                        print("You shot toward room 15")          
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass 
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = "0"
            break 
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break
                    
            
        if playerLocation == "15":
            print("You are in room 15. You can move to room 11, 14, or 16.")
            if pit1 == "11" or pit2 == "11" or pit1 == "14" or pit2 == "14" or pit1 == "16" or pit2 == "16":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "11" or wumpusRoom == "14" or wumpusRoom == "16":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "11" or bat2 == "11" or bat1 == "14" or bat2 == "14" or bat1 == "16" or bat2 == "16":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                
                    time.sleep(0.5)
                    if dest == 11:
                        print("You move to room 11.")
                        playerLocation = "11"
                        time.sleep(0.5)
                    elif dest == 14:
                        print("You move to room 14.")
                        playerLocation = "14"
                        time.sleep(0.5)
                    elif dest == 16:
                        print("You move to room 16.")
                        playerLocation = "16"
                        time.sleep(0.5)            
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 11:
                        print("You shot toward room 11.")
                    elif shot == 14:
                        print("You shot toward room 14")
                    elif shot == 16:
                        print("You shot toward room 16")               
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass                    
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break  
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True 
            playerLocation = "0"
            break
                      
        
        if playerLocation == "16":
            print("You are in room 16. You can move to room 12 or 15.")
            if pit1 == "12" or pit2 == "12" or pit1 == "15" or pit2 == "15":
                time.sleep(0.5)
                print("You feel a draft coming from a nearby room.")             
            if wumpusRoom == "12" or wumpusRoom == "15":
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            if bat1 == "12" or bat2 == "12" or bat1 == "15" or bat2 == "15":
                time.sleep(0.5)
                print("You hear bats nearby.")                 
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                strdest = input("What room will you move to? ")
                time.sleep(0.5)
                if strdest != "0" and strdest != "1" and strdest != "2" and strdest != "3" and strdest != "4" and strdest != "5" and strdest != "6" and strdest != "7" and strdest != "8" and strdest != "9" and strdest != "10" and strdest != "11" and strdest != "12" and strdest != "13" and strdest != "14" and strdest != "15" and strdest != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    dest = int(strdest)                    
                    time.sleep(0.5)
                    if dest == 12:
                        print("You move to room 12.")
                        playerLocation = "12"
                        time.sleep(0.5)
                    elif dest == 15:
                        print("You move to room 15.")
                        playerLocation = "15"
                        time.sleep(0.5)          
                    else:
                        print("You can't go there.")
                        time.sleep(0.5)
                        dest = 0
                        pass
            elif ms == "s" or ms == "shoot": 
                strshot = input("Which room will you shoot towards? ")
                if strshot != "0" and strshot != "1" and strshot != "2" and strshot != "3" and strshot != "4" and strshot != "5" and strshot != "6" and strshot != "7" and strshot != "8" and strshot != "9" and strshot != "10" and strshot != "11" and strshot != "12" and strshot != "13" and strshot != "14" and strshot != "15" and strshot != "16":
                    time.sleep(0.5)
                    print("Invalid input.")
                    pass
                else:
                    shot = int(strshot)
                    if shot == 12:
                        print("You shot toward room 12.")
                    elif shot == 15:
                        print("You shot toward room 15")           
                    else:
                        print("You can't shoot there.")
                        shot = 0
                        pass
                    if shot == int(wumpusRoom):
                        time.sleep(0.5)
                        print("You shot the wumpus! You win!")
                        time.sleep(0.5)
                        playagain()
                        crash = True
                        playerLocation = "0"
                        pass                        
                    elif shot != 0:
                        time.sleep(0.5)
                        print("You missed.")
                        eat = random.randint(0,1)
                        if eat == 1:
                            print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                            playagain()
                            crash = True
                            playerLocation = "0"
                            pass
            else:
                print("Invalid input.")
                pass
            
        while playerLocation == bat1 or playerLocation == bat2:
            print("The bats took you to another room.")
            playerLocation = str(random.randint(1,16))            
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break  
        if playerLocation == pit1 or playerLocation == pit2:
            print("You fell in a pit to your death. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = "0"
            break
                   

main()
