import sys
from classes import Character
from wohnung_instances import schlafzimmer
from wohnung_funktionen import  change_room, help_command, info_command
from wohnung_tasks import task_1, loeseung_wohnung
import time

print("main.py wurde geladen.")

def befehl_auswerten(input:str, player:str, befehle: list=None)->None:
    """" This function is used to evaluate the input of the user. """    
        
    if input == "hilfe" or input == "help":
        help_command()
    if input == "info":
        info_command(player)        
    if input == "quit" or input == "q":
        sys.exit()
    aufgabe = change_room(player=player, input=input)
    if aufgabe == "aufgabe[0]":                                      # player turns pc im arbeitszimmer on
        task_1()            
    if aufgabe == "aufgabe[1]":
        pass
    if aufgabe == "aufgabe[2]":
        pass
    if aufgabe == "aufgabe[3]":
        pass
    if aufgabe == "aufgabe[4]":
        pass
    if aufgabe == "aufgabe[5]":
        pass


def wohnung():
    """
    This function is the main function of the world "wohnung".
    """
    while True:
        time.sleep(0.5)
        player_input = input("\n--> ").lower().strip()
        time.sleep(0.5)   
        act_location = player.location
        befehl_auswerten(input=player_input, player=player)
        if act_location != player.location:
            print(f"\n{player.location.name}\n{player.location.description}")
            print(f"\nAusgänge: {player.location.exits}")
            act_location = player.location    
        else:
            print(f"[Aktueller Ort: {player.location.name}]")      
       
    
   
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 # ***************************    Das Spiel beginnt     *********************************
 # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
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