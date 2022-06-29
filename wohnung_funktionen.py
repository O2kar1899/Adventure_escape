from wohnung_instances import player, abstellkammer, arbeitszimmer, bad, balkon_schlafzimmer, \
    balkon_wohnzimmer, balkon_schlafzimmer, flur, kueche, schlafzimmer, wohnzimmer,\
        computer_arbeitszimmer 
from wohnung_tasks import loesung, loesung_wohnung_gefunden, task_1 
import sys

print("wohnung_funktionen.py wurde geladen.")

def info_command(player):
    inventar = []
    for i in player.location.objects:
        print(i)
   
    print(f"Du schaust dich im Raum um und siehst folgendes: {inventar}")


def help_command():
    """_summary_
    Prints a help text.
    """
    print("Hilfe:")
    print("Du kannst folgende Befehle eingeben:")      
    print("Um den Raum/Ort zu wechseln, gib einfach die Himmelsrichtung (ost, süd, west, nord) \nein in die Du gehen möchtest.")
    print("Wenn Du etwas mit einem Gegenstand tun möchtest, gib den Namen des Gegenstandes ein.")
    print("Um zu sehen, was in diesem Raum ist, gib einfach 'info' ein.")
    print("Um wieder hierher zu kommen gib hilfe oder help ein.")
    print(f"Aktueller Ort: {player.location.name}")
    print(f"Das Lösungswort: {loesung_wohnung_gefunden}")

def wohnung_ausgangstuer():
        code_input = input("\nDie Ausgangstür ist verschlossen. Um sie zu öffnen, musst Du den Code eingeben:\n --> ")
        if code_input == loesung: 
            print("\nDu hast den Code erfolgreich eingegeben.\nDie Tür ist jetzt offen.")
            print("\nDu hast gewonnen! Das Spiel ist vorbei.\n")
            sys.exit()
            #player.location = outside
        else:
            print("Der Code ist falsch.\nDie Tür bleibt verschlossen.")

def input_answer(question:str="--> "):
        answer = input(question).lower().strip()
        return answer

def room_acivity(player, input):
    if player.location == arbeitszimmer:
        if input == "computer"  or input == "pc":
            print("Willst Du den Computer anschauen oder einschalten?")
            if input_answer("--> ") == "einschalten":
                task_1()
            elif input_answer("--> ") == "anschauen":
                print(computer_arbeitszimmer.description)
            else:
                print("\nDu kannst den Computer nur einschalten oder anschauen. Zu mehr ist er nicht zu gebrauchen.")


def change_room(player, input):
    """
    This function changes the location of the character.
    """      
    if player.location == arbeitszimmer:                                    # Arbeitszimmer
        if input == "s" or "süd" in input:
            player.location = wohnzimmer
        elif input == "o" or "ost" in input:
            player.location = bad
        elif input == "w" or "west" in input:
            player.location = abstellkammer 
        elif input == "n" or "nord" in input:
            print("Du kannst nicht nach Norden gehen.")        
                    
    
    if player.location == abstellkammer:                                       # Abstellkammer
        if input == "s" or "süd" in input:
            player.location = flur
        elif input == "o" or "ost" in input:
            player.location = arbeitszimmer
        else: help_command()

    
    elif player.location == bad:                                             # Bad
        if input == "s" or "süd" in input:
            player.location = schlafzimmer
        elif input == "w" or "west" in input:
            player.location = arbeitszimmer
        elif input == "n" or "nord" in input:
            print("Du kannst nicht nach Norden gehen.")
        elif input == "o" or "ost" in input:
            print("Du kannst nicht nach Osten gehen.")
    
    elif player.location == balkon_schlafzimmer:                             # Balkon_Schlafzimmer
        if input == "n" or "nord" in input:
            player.location = schlafzimmer
        elif input == "w" or "west" in input:
            player.location = balkon_wohnzimmer
        elif input == "s" or "süd" in input:
            print("Du kannst nicht nach Süden gehen.")
        elif input == "o" or "ost" in input:
            print("Du kannst nicht nach Osten gehen.")
    
    elif player.location == balkon_wohnzimmer:                               # Balkon_wohnzimmer
        if input == "n" or "nord" in input:
            player.location = wohnzimmer
        elif input == "w" or "west" in input:
            player.location = kueche
        elif input == "o" or "ost" in input:
            player.location = balkon_schlafzimmer
        elif input == "s" or "süd" in input:
            print("Du kannst nicht nach Süden gehen.")
    
    elif player.location == flur:                                               # Flur (AUSGANG)
        if input == "n" or "nord" in input:
            player.location = abstellkammer
        elif input == "o" or "ost" in input:
            player.location = wohnzimmer
        elif input == "s" or "süd" in input:
            player.location = kueche
        elif input == "w" or "west" in input:
            wohnung_ausgangstuer(player)
            

    elif player.location == kueche:                                            # Kueche
        if input == "n" or "nord" in input:
            player.location = flur
        elif input == "o" or "ost" in input:
            player.location = balkon_wohnzimmer
        elif input == "s" or "süd" in input:
            print("Du kannst nicht nach Süden gehen.")
        elif input == "w" or "west" in input:
            print("Du kannst nicht nach Westen gehen.")
    
    elif player.location == schlafzimmer:                                     # Schlafzimmer
        if input == "n" or "nor" in input:
            player.location = bad
        elif input == "s" or "süd" in input:
            player.location = balkon_schlafzimmer
        elif input == "w" or "west" in input:
            player.location = wohnzimmer
        elif input == "o" or "ost" in input:
            print("Du kannst nicht nach Osten gehen.")    
    
    elif player.location == wohnzimmer:                                     # Wohnzimmer
        if input == "n" or "nord" in input:
            player.location = arbeitszimmer
        elif input == "o" or "ost" in input:
            player.location = schlafzimmer
        elif input == "s" or "süd" in input:
            player.location = balkon_wohnzimmer
        elif input == "w" or "west" in input:
            player.location = flur   
          