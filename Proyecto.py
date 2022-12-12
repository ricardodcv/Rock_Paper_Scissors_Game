"""
Piedra, Papel o Tijera
"""
import random
Options = ["Rock","Scissors","Paper"]
print("Hi! Do you want to play 'Rock, Paper or Scissors' with me?.")
while True:
    Computer_Choice = random.choice(Options) #Choose an element of the list of options
    a = input()
    if a.capitalize() == "Yes": #I used capitalize to avoid problems with upper and lower case
        print("Fine!. Rock, Paper or Scissors... ")
        Choice = input("Now tell me what did you choose ").capitalize()
        if Choice not in Options:
            print("HAH. I chose Lizard, it wins vs random stuff.")
            print("Want to play again?")
            continue                    #If you say other option
        else: #The game itself. Rock wins Scissors, Scissors wins Paper, Paper wins Rock.
            if  Computer_Choice == Choice:
                print("I also chose "+ Choice + " . That's a tie")
            elif Computer_Choice == "Rock":
                if Choice == "Paper":
                    print("Yikes. I chose " + Computer_Choice + ". You win")
                if Choice == "Scissors":
                    print("Yeeaaaah. I chose " + Computer_Choice + ". I win")
            elif Computer_Choice == "Paper":
                if Choice == "Scissors":
                    print("Yikes. I chose " + Computer_Choice + ". You win")
                if Choice == "Rock":
                    print("Yeeaaaah. I chose " + Computer_Choice + ". I win")            
            elif Computer_Choice == "Scissors":
                if Choice == "Rock":
                    print("Yikes. I chose " + Computer_Choice + ". You win")
                if Choice == "Paper":
                    print("Yeeaaaah. I chose " + Computer_Choice + ". I win")
            print("Want to play again?")
            continue                    #The while goes until you say no


    elif a.capitalize() == "No":
        print("All right. See you later.")
        break
    else:
        print("Say yes or no, pal.") #For other answers to a "yes or no" question
