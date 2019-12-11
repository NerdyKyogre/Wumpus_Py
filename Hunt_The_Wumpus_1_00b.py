#Hunt The Wumpus v1.00 beta
#goal is to find and shoot the wumpus without going in same room as it.

import random
import time

def rules():
    #Prompt player if they would like to view rules
    rules = input("Welcome to Hunt The Wumpus! Would you like to view the rules? Y/N: ")
    #view rules
    if rules == "Y" or rules == "y":
        print("You are a spelaeologist who has found the cave said to contain an ancient beast called a Wumpus. You job is to catch and shoot it in order to analyze it.\nYou can move within the cave, which is a 4 by 4 grid of identical rooms, with the command 'm' or 'move', and shoot with 's' or 'shoot'.\nYou must shoot into the next room if you think the wumpus is there. But beware, if you shoot and miss the wumpus may come out and eat you! You will be told when you smell a wumpus in a nearby room. If you enter the room with the wumpus, it will eat you and kill you.\nGood luck and have fun!")
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
        #tell quit function to pass and end program
        stop = 1
        quit(stop)
    else: 
        print("Invalid input.")
        playagain()
        
def main():
    #Prompt for rules
    rules()
    #Set locations for wumpus and player
    wumpusRoom = random.randint(1,16)
    playerLocation = random.randint(1,16)
    #Reset player location so they have only a 1/16^2 (about 1 in 400) chance to spawn in the same room as the wumpus.
    if playerLocation == wumpusRoom:
        playerLocation = random.randint(1,16)
    #go to wumpus function to play
    wumpus(wumpusRoom,playerLocation)
    
def wumpus(wumpusRoom,playerLocation):
    crash = False
    while crash == False:
        #On the off-chance the player still spawns with the wumpus, they die
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
        #Set possibilities for each room the player can be in.
        #For sake of simplicity, only room 1 has comments that apply to all the rooms.
        if playerLocation == 1:
            #tell user what room they're in
            print("You are in room 1. You can move to room 2 or 5.")
            #Tell user if wumpus is in room within shooting range.
            if wumpusRoom == 2 or wumpusRoom == 5:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            #Prompt user to move or shoot
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                #prompt user what room to go to
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 2:
                    #change playerLocation to chosen room
                    print("You move to room 2.")
                    playerLocation = 2
                    time.sleep(0.5)
                elif dest == 5:
                    print("You move to room 5.")
                    playerLocation = 5
                    time.sleep(0.5)
                else:
                    print("Invalid input.")
                    #reset dest value
                    dest = 0
                    time.sleep(0.5)
                    pass
            elif ms == "s" or ms == "shoot": 
                #prompt user for what room they will shoot to
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
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
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass 
        
        #check if player is now in same room as wumpus before advancing. This is done after end of each room.
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            #set player location to out of world so program stops properly
            playerLocation = 0
            pass        
            
        if playerLocation == 2:
            print("You are in room 2. You can move to room 1, 3, or 6.")
            if wumpusRoom == 1 or wumpusRoom == 3 or wumpusRoom == 6:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 1:
                    print("You move to room 1.")
                    playerLocation = 1
                    time.sleep(0.5)
                elif dest == 3:
                    print("You move to room 3.")
                    playerLocation = 3
                    time.sleep(0.5)
                elif dest == 6:
                    print("You move to room 6")
                    playerLocation = 6
                    time.sleep(0.5)
                else:
                    print("Invalid input.")
                    dest = 0
                    time.sleep(0.5)
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass  
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 3:
            print("You are in room 3. You can move to room 2, 4, or 7.")
            if wumpusRoom == 2 or wumpusRoom == 4 or wumpusRoom == 7:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 2:
                    print("You move to room 2.")
                    playerLocation = 2
                    time.sleep(0.5)
                elif dest == 4:
                    print("You move to room 4.")
                    playerLocation = 4
                    time.sleep(0.5)
                elif dest == 7:
                    print("You move to room 7")
                    playerLocation = 7
                    time.sleep(0.5)
                else:
                    print("Invalid input.")
                    dest = 0
                    time.sleep(0.5)
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass  
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 4:
            print("You are in room 4. You can move to room 3 or 8.")
            if wumpusRoom == 3 or wumpusRoom == 8:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 3:
                    print("You move to room 3.")
                    playerLocation = 3
                    time.sleep(0.5)
                elif dest == 8:
                    print("You move to room 8.")
                    playerLocation = 8
                    time.sleep(0.5)
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
                if shot == 3:
                    print("You shot toward room 3.")
                elif shot == 8:
                    print("You shot toward room 8")
                else:
                    print("You can't shoot there.")
                    shot = 0
                    pass
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 5:
            print("You are in room 5. You can move to room 1 or 6.")
            if wumpusRoom == 1 or wumpusRoom == 6:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 1:
                    print("You move to room 1.")
                    playerLocation = 1
                    time.sleep(0.5)
                elif dest == 6:
                    print("You move to room 6")
                    playerLocation = 6
                    time.sleep(0.5)
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
                if shot == 1:
                    print("You shot toward room 1.")
                elif shot == 6:
                    print("You shot toward room 6")
                else:
                    print("You can't shoot there.")
                    shot = 0
                    pass
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = 0
            pass        
            
    
        if playerLocation == 6:
            print("You are in room 6. You can move to room 2, 5, 7, or 10.")
            if wumpusRoom == 2 or wumpusRoom == 5 or wumpusRoom == 7 or wumpusRoom == 10:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 2:
                    print("You move to room 2.")
                    playerLocation = 2
                    time.sleep(0.5)
                elif dest == 5:
                    print("You move to room 5.")
                    playerLocation = 5
                    time.sleep(0.5)
                elif dest == 7:
                    print("You move to room 7.")
                    playerLocation = 7
                    time.sleep(0.5) 
                elif dest == 10:
                    print("You move to room 10.")
                    playerLocation = 10
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = 0
            pass        
    
        if playerLocation == 7:
            print("You are in room 7. You can move to room 3, 6, 8, or 11.")
            if wumpusRoom == 3 or wumpusRoom == 6 or wumpusRoom == 8 or wumpusRoom == 11:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 3:
                    print("You move to room 3.")
                    playerLocation = 3
                    time.sleep(0.5)
                elif dest == 6:
                    print("You move to room 6.")
                    playerLocation = 6
                    time.sleep(0.5)
                elif dest == 8:
                    print("You move to room 8.")
                    playerLocation = 8
                    time.sleep(0.5) 
                elif dest == 11:
                    print("You move to room 11.")
                    playerLocation = 11
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
                if shot == 3:
                    print("You shot toward room 3.")
                elif shot == 6:
                    print("You shot toward room 6")
                elif shot == 8:
                    print("You shot toward room 8")    
                elif shot == 11:
                    print("You shot toward room 11")            
                else:
                    print("You can't shoot there.")
                    shot = 0
                    pass
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 8:
            print("You are in room 8. You can move to room 4, 7, or 12.")
            if wumpusRoom == 4 or wumpusRoom == 7 or wumpusRoom == 12:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 4:
                    print("You move to room 4.")
                    playerLocation = 4
                    time.sleep(0.5)
                elif dest == 7:
                    print("You move to room 7.")
                    playerLocation = 7
                    time.sleep(0.5) 
                elif dest == 12:
                    print("You move to room 12.")
                    playerLocation = 12
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 9:
            print("You are in room 9. You can move to room 5, 10, or 13.")
            if wumpusRoom == 5  or wumpusRoom == 10 or wumpusRoom == 13:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 5:
                    print("You move to room 5.")
                    playerLocation = 5
                    time.sleep(0.5)
                elif dest == 10:
                    print("You move to room 10.")
                    playerLocation = 10
                    time.sleep(0.5) 
                elif dest == 13:
                    print("You move to room 13.")
                    playerLocation = 13
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards?" ))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 10:
            print("You are in room 10. You can move to room 6, 9, 11, or 14.")
            if wumpusRoom == 2 or wumpusRoom == 5 or wumpusRoom == 7 or wumpusRoom == 10:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 6:
                    print("You move to room 6.")
                    playerLocation = 6
                    time.sleep(0.5)
                elif dest == 9:
                    print("You move to room 9.")
                    playerLocation = 9
                    time.sleep(0.5)
                elif dest == 11:
                    print("You move to room 11.")
                    playerLocation = 11
                    time.sleep(0.5) 
                elif dest == 14:
                    print("You move to room 14.")
                    playerLocation = 14
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = 0
            pass        
    
        if playerLocation == 11:
            print("You are in room 11. You can move to room 7, 10, 12, or 15.")
            if wumpusRoom == 7 or wumpusRoom == 10 or wumpusRoom == 12 or wumpusRoom == 15:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 7:
                    print("You move to room 7.")
                    playerLocation = 7
                    time.sleep(0.5)
                elif dest == 10:
                    print("You move to room 10.")
                    playerLocation = 10
                    time.sleep(0.5)
                elif dest == 12:
                    print("You move to room 12.")
                    playerLocation = 12
                    time.sleep(0.5) 
                elif dest == 15:
                    print("You move to room 15.")
                    playerLocation = 15
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()  
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 12:
            print("You are in room 12. You can move to room 8, 11, or 16.")
            if wumpusRoom == 8 or wumpusRoom == 11 or wumpusRoom == 16:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 8:
                    print("You move to room 8.")
                    playerLocation = 8
                    time.sleep(0.5)
                elif dest == 11:
                    print("You move to room 11.")
                    playerLocation = 11
                    time.sleep(0.5) 
                elif dest == 16:
                    print("You move to room 16.")
                    playerLocation = 16
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 13:
            print("You are in room 13. You can move to room 9 or 14.")
            if wumpusRoom == 9 or wumpusRoom == 14:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 9:
                    print("You move to room 9.")
                    playerLocation = 9
                    time.sleep(0.5)
                elif dest == 14:
                    print("You move to room 14.")
                    playerLocation = 14
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
                if shot == 9:
                    print("You shot toward room 9.")
                elif shot == 14:
                    print("You shot toward room 14")           
                else:
                    print("You can't shoot there.")
                    shot = 0
                    pass
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass 
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 14:
            print("You are in room 14. You can move to room 10, 13, or 15.")
            if wumpusRoom == 10 or wumpusRoom == 13 or wumpusRoom == 15:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 10:
                    print("You move to room 10.")
                    playerLocation = 10
                    time.sleep(0.5)
                elif dest == 13:
                    print("You move to room 13.")
                    playerLocation = 13
                    time.sleep(0.5)
                elif dest == 15:
                    print("You move to room 15.")
                    playerLocation = 15
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass 
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain() 
            crash = True
            playerLocation = 0
            pass        
            
        if playerLocation == 15:
            print("You are in room 15. You can move to room 11, 14, or 16.")
            if wumpusRoom == 11 or wumpusRoom == 14 or wumpusRoom == 16:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 11:
                    print("You move to room 11.")
                    playerLocation = 11
                    time.sleep(0.5)
                elif dest == 14:
                    print("You move to room 14.")
                    playerLocation = 14
                    time.sleep(0.5)
                elif dest == 16:
                    print("You move to room 16.")
                    playerLocation = 16
                    time.sleep(0.5)            
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
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
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass                    
            else:
                print("Invalid input.")
                pass
        
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = 0
            pass        
        
        if playerLocation == 16:
            print("You are in room 16. You can move to room 12 or 15.")
            if wumpusRoom == 12 or wumpusRoom == 15:
                time.sleep(0.5)
                print("You smell the intense odor of a wumpus.")
            time.sleep(0.5)
            ms = input("Will you move or shoot? ")
            time.sleep(0.5)
            if ms == "m" or ms == "move": 
                dest = int(input("What room will you move to? "))
                time.sleep(0.5)
                if dest == 12:
                    print("You move to room 12.")
                    playerLocation = 12
                    time.sleep(0.5)
                elif dest == 15:
                    print("You move to room 15.")
                    playerLocation = 15
                    time.sleep(0.5)          
                else:
                    print("Invalid input.")
                    time.sleep(0.5)
                    dest = 0
                    pass
            elif ms == "s" or ms == "shoot": 
                shot = int(input("Which room will you shoot towards? "))
                if shot == 12:
                    print("You shot toward room 12.")
                elif shot == 15:
                    print("You shot toward room 15")           
                else:
                    print("You can't shoot there.")
                    shot = 0
                    pass
                if shot == wumpusRoom:
                    time.sleep(0.5)
                    print("You shot the wumpus! You win!")
                    time.sleep(0.5)
                    playagain()
                elif shot != 0:
                    time.sleep(0.5)
                    print("You missed.")
                    eat = random.randint(0,1)
                    if eat == 1:
                        print("The wumpus was alerted by your shot and came out and ate you! You lose.")
                        playagain()
                        crash = True
                        playerLocation = 0
                        pass
            else:
                print("Invalid input.")
                pass   
            
        if playerLocation == wumpusRoom:
            print("You entered the room the wumpus was in. It got mad and ate you. You lose.")
            time.sleep(0.5)
            playagain()
            crash = True
            playerLocation = 0
            pass       
        
    
def quit(stop):
    if stop == 1:
        pass

main()