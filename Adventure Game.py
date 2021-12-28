import time
import random

def main():
   
    print("You are trying to find your way to the centre of a maze where there is a pot of gold!")
    time.sleep(2)
    print("What you don't know is that this is a dangerous maze with traps and hazards.")
    time.sleep(2)
    start = input ("Do you want to enter the maze? (y/n)")
    if start == "y" or start == "Y" or start == "Yes" or start == "yes":
        print ("Welcome to the maze.")
        print("You enter the maze...")
        time.sleep(2)
       
        print("You reach a opening in the wall and go through it...")
        time.sleep(2)
       
        print("You can go left (L) or right (R)")
        answer = input("Make your choice ... ")
        print("You chose",answer,"... what will happen? ")
        time.sleep(2)
       
        print("You turn a corner...")
        time.sleep(2)
       
        print("You take a few steps forward...")
        time.sleep(2)
       
        if answer == "R" or answer == "r" or answer == "right" or answer == "Right":
           print("...and fall down a trapdoor!")
           time.sleep(1)
           print ("After falling down for few seconds, you arrived in a damp room with no light.")
           A = input ("Do you want to explore the room? (Y/N)")
           if A == "Y" or A == "y" or A == "Yes" or A == "yes":
               print ("Exploring. . .")  
               time.sleep(2)
               print ("You found a torch and two stones!")
               AN = input ("Ignite the torch? (Y/N)")
               if AN == "Y":
                   print ("Igniting the torch...")
                   
                   time.sleep(2)
                   
                   items = ["You failed to ignite the torch. After a few hours in the dark, you died due to hypothermia. No one could find your dead body.",
                            "You succeeded! With the torch, you found many pots of gold... But where is the way to escape?"]
                   ri = random.choice (items)
                   print (ri)
                   
               else:
                   time.sleep(2)
                   print ("After a few hours in dark, you died due to hypothermia. No one could find your dead body.")
           else:
               time.sleep(2)
               print ("You were too afraid to move an inch in the dark, so you stayed... and never saw the sun again.")
        else:
            print('''...and see a beautiful grassy patch lined with trees!
There is a pot of gold at the end!''')
            time.sleep(2)
            print("You run towards the pot of gold, shining under the bright sunshine...")
            time.sleep(2)
            print(". . .and find out that the pot of gold was an illusion.")
            time.sleep(2)
            print("The beautiful grassy patch was just a grey path covered with mold, and the trees were just tall torches!")
            time.sleep(3)
            print("And the bright sunshine was...")
            time.sleep(2)
            print("An enormous burning stone falling directly towards you! \n")
            time.sleep(2)
            print("Farewell, explorer. You encountered death!")
           
    elif start == "n":
        print ("Well, well, you coward! Come back whenever you feel brave enough to start!")

main()
