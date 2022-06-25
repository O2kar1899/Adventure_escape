
import sys
from classes import Character, schlafzimmer 
from funktionen_wohnung import  change_room, help_command
import time


def befehl_auswerten(input:str, player:str, befehle: list=None)->None:
    change_room(player=player, input=input)
        
    if input == "hilfe" or input == "help":
        help_command()        
    if input == "quit" or input == "q":
        sys.exit()

def wohnung():
    while True:
        time.sleep(0.5)
        player_input = input("\n\n--> ").lower().strip()
        time.sleep(0.5)   
        akt_ort = player.location
        befehl_auswerten(input=player_input, player=player)
        if akt_ort != player.location:
            print(f"\n{player.location.name}\n{player.location.description}")
            print("\nAusgänge:")
            for i in range(len(player.location.exits)):
                print(f"{player.location.exits[i]}")
                #print(f"{i.name} - {i.description}")
            
            akt_ort = player.location    
        else:
            print(f"[Aktueller Ort: {player.location.name}]")      
       
    
    
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 # ***************************    Das Spiel beginnt     *********************************
 # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("Das Spiel beginnt!\n")
time.sleep(1)

player_name = input("\nGib bitte Deinen Spielernamen ein? ")

time.sleep(1)
print("Du wachst in einer fremden Wohnung auf. Du hast keine Ahnung wie Du hierher gekommen bist.")
print("Das ist Dir jetzt auch erstmal völlig egal. Du willst jetzt einfach möglichst schnell nachhause und in ruhe duschen.\n")
time.sleep(1)


player = Character(player_name, health=100, damage=0, location= schlafzimmer, welt="wohnung")
print(f"\nDu hörst die freundliche Stimme einer Sprachbox neben dem Bett: Guten morgen {player.name},\n" \
     f"Zurzeit sind es 19 Grad Celsius und Sonnenschein.\n") 
print(f"\n[{player.location.description}.]")

if player.welt == "wohnung":
    wohnung()