import sys
from this import d
from wohnung_instances import player,schlafzimmer, coin # im Schlafzimmer startet die Welt "wohnung"
from wohnung_funktionen import  change_room, help_command, info_command, room_acivity, hase
import time

print("main.py wurde geladen.")

def wohnung_befehl_auswerten(input:str, player:str)->None:
    """" This function is used to evaluate the input of the user. """    
        
    if input == "hilfe" or input == "help":
        help_command()
    if input == "info":
        info_command(player.location)        
    if input == "quit" or input == "q":
        sys.exit()  
    else:
        change_room(player=player, input=input)
        room_acivity(player=player, input=input)



def wohnung():
    """
    This function is the main function of the world "wohnung".
    """
    time.sleep(1)
    print("\nDu wachst in einer fremden Wohnung auf. Du hast keine Ahnung wie Du hierher gekommen bist.")
    print("Das ist Dir jetzt auch erstmal völlig egal.") 
    print("Du willst jetzt einfach möglichst schnell nachhause und in ruhe duschen.")
    time.sleep(1)

    print(f"Du hörst die freundliche Stimme einer Sprachbox neben dem Bett: Guten morgen {player.name}.")
    print("Zurzeit sind es 19 Grad Celsius und Sonnenschein.\n") 
    help_command()
    
    while True:
        time.sleep(0.5)
        player_input = input("\n--> ").lower().strip()
        time.sleep(0.5)   
        act_location = player.location
        
        wohnung_befehl_auswerten(input=player_input, player=player)
        
        hase()
        if act_location != player.location: # wenn bei der Auswertung der Raum gewechselt wurde
            print(f"\n{player.location.name}\n{player.location.description}")
            #print(f"\nAusgänge: {player.location.exits}")
            act_location = player.location      
                        
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 # ***************************    Das Spiel beginnt     *********************************
 # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("Das Spiel beginnt!\n")
hase()
time.sleep(1)

player.name = input("Gib bitte Deinen Spielernamen ein: ")
player.welt = "wohnung" # Das Spiel startet in der Welt "wohnung"
player.location = schlafzimmer # Das Spiel startet im Schlafzimmer

if player.welt == "wohnung":
    wohnung()