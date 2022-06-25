from classes import *
import sys


def help_command():
    print("\nHilfe:")
    print("\nDu kannst folgende Befehle eingeben:")      
    print("\nUm den Raum/Ort zu wechseln, gib einfach die Himmelsrichtung (ost, süd, west, nord) \nein in die Du gehen möchtest.")
    print("\nWährend Deines Abenteuers werden Dir weitere Befehle angeboten.\n Um einen Befel einzugeben, gib einfach den Befehl ein.")
    print("\nUm zu sehen, was in diesem Raum ist, gib einfach 'info' ein.")
    print("\nUm wieder hierher zu kommen gib hilfe oder help ein.")


def wohnung_ausgangstuer(player, code:str = "artep"):
        door_open = False
        code_input = input("\nDie Ausgang ist verschlossen.\n Um sie zu öffnen, musst Du den Code eingeben:\n -->")
        if code_input == code: 
            door_open = True
            print("\nDu hast den Code erfolgreich eingegeben.\nDie Tür ist jetzt offen.")
            print("\nDu hast gewonnen! Das Spiel ist vorbei.\n")
            sys.exit()
            #player.location = outside
        else:
            print("\nDer Code ist falsch.\nDie Tür bleibt verschlossen.")

def change_room(player, input):
    """
    This function changes the location of the character.
    Locations:
    arbeitszimmer, bad, balkon, flur, kueche, wohnzimmer, schlafzimmer, abstellkammer
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
    
    elif player.location == flur:                                               # Flur
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
                    
    
    
    
       

  