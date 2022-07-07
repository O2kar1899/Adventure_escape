from wohnung_instances import player, abstellkammer, arbeitszimmer, bad, balkon_schlafzimmer, \
    balkon_wohnzimmer, balkon_schlafzimmer, flur, kueche, schlafzimmer, wohnzimmer,\
        computer_arbeitszimmer, schreibtisch_arbeitszimmer, schreibtisch_schublade, kuehlschrank, \
            blumentopf_1, schuhschrank, nachttisch 

from classes import *
from wohnung_tasks import loesung,loesung_wohnung_gefunden, task_1_wordle, task_2_coins
import sys

print("wohnung_funktionen.py wurde geladen.")



def info_command(location):
    print("INFO:")
    print(f"Aktueller Ort: {location.name}")
    if location.objects != None:
        print(f"Im Raum befinden sich folgende Gegenstände:")
        for a in location.objects.keys():
            print(a)
   
def help_command():
    """_summary_
    Prints a help text.
    """
    print("Hilfe:")
    print("Du kannst folgende Befehle eingeben:")      
    print("Raum wechseln: ost, süd, west oder nord")
    print("Informationen über einen Gegenstand: Namen des Gegenstands")
    print("Informationen zum aktuellen Raum: info")
    print("Spiel beenden: q oder quit")
    print("Um wieder hierher zu kommen: hilfe oder help")

    print(f"Aktueller Ort: {player.location.name}")
    if player.location.objects != ["???", "???", "???", "???", "???"]:
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

def input_answer(question:str="--> ") -> str:
        answer = input(question).lower().strip()
        return answer


def room_acivity(player:str, input:str):
     
    if player.location == arbeitszimmer:       
        if input == "computer"  or input == "pc": #  ++++++++++++++++++++++ Computer
            print("Willst Du den Computer anschauen oder einschalten?")
            if input_answer("--> ") == "einschalten":
                task_1_wordle()
            elif input_answer("--> ") == "anschauen":
                print(computer_arbeitszimmer.description)
            else:
                print("\nDu kannst den Computer nur einschalten oder anschauen. Zu mehr ist er nicht zu gebrauchen.")
        
        if input == "schreibtisch":# ++++++++++++++++++++++ Schreibtisch
            print(player.location.objects["Schreibtisch"].description)

        if input == "schublade": # ++++++++++++++++++++++ Schublade
            print("Du öffnest die Schublade.")
            if schreibtisch_schublade.inventory != None:
                if schreibtisch_arbeitszimmer.inventory["coin"]>0:
                    print(f"In der Schublade befindet sich {schreibtisch_schublade.inventory['coin']} Münze")
                    answer = input("\nMöchtest Du die Münze einsammeln? (ja/nein) --> ").lower().strip()
                    if answer == "ja":
                        player.inventory["coin"] += schreibtisch_schublade.inventory["coin"]
                        schreibtisch_schublade.inventory["coin"] = 0
                        print(f"Du hast {player.inventory['coin']} Münze(n) in Deinem Inventar")
                else:
                    print("In der Schublade befindet sich keine Münze.")
            else:
                print("Die Schublade ist leer.")
    
    if player.location == balkon_wohnzimmer:
        if input == "blumentopf":
            print(blumentopf_1.description)
            print("Möchtest Du den Blumentopf hocheben oder das dreckige Ding lieger stehen lassen?")
            answer = input_answer("hochheben/stehen lassen --> ")
            if "stehen" in answer:
                print("Gute Entscheidung. Deine Hände bleiben sauber und die Blume wurde nicht gefährdet.")
            elif "heben" in answer:
                if blumentopf_1.inventory["coin"]>0: 
                    print("Der Blumentopf ist schwerer als gedacht. An der Stelle, an welcher der Blumentopf stand, \
                    liegt eine goldene Münze")
                    answer = input_answer("\nMöchtest Du die Münze einsammeln? (ja/nein) --> ")
                    print(answer)
                    if answer == "ja":
                        player.inventory["coin"] += 1
                        blumentopf_1.inventory["coin"] = 0
                        print("\nDu steckst die Münze in Deine Tasche und stellst den Blumentopf zurück an seinen Platz.")
                        print(f"Du hast {player.inventory['coin']} Münze(n) in Deiner Tasche")
                    elif answer == "nein":
                        print("\nDu steckst den Blumentopf zurück an seinen Platz.")
                    else: print("\nDu kannst nur ja oder nein antworten.")
                else:
                    print("\nDer Blumentopf ist schwerer als gedacht. An der Stelle, an welcher der Blumentopf stand, \
                        ist etwas Schmutz zu sehen.")

    if player.location == flur:
        if input == "schuhschrank":
            print("Willst Du den Schuhschrank öffnen oder hochheben?")
            answer = input_answer(" hochheben/öffnen --> ")
            if "heben" in answer:
                print("Der Schrank ist leider etwas schwer für Dich.")
            if "öffnen" in answer:
                print(f"Im Schuhrank befinden sich: schwarze Schuhe, braune Schuhe und gelbe Schuhe")                
                while True:
                    auswahl = input_answer("\n --> ")
                    if "schuh" in auswahl:
                        print("Ein schönes Paar Schuhe, mit dem Du leider nichts anfangen kannst")
                        if "schwarze" in auswahl and schuhschrank.inventory["coin"] > 0:
                            print("An der Stelle an der die Schuhe standen, endeckst Du eine goldene Münze")
                            answer = input_answer("\nMöchtest Du die Münze einsammeln? (ja/nein) --> ")
                            if answer == "ja":
                                player.inventory["coin"] += 1
                                schuhschrank.inventory["coin"] = 0
                                print("Du steckst Die Münze in Deine Tasche")
                                print(f"Du hast {player.inventory['coin']} Münze(n) in Deiner Tasche")
                        else: print("\nDu schließt den Schuhschrank wieder")
                        break
                    else: print("Ich kann Dich leider nicht verstehen.\n")          
           
    if player.location == kueche:
        if input == "kühlschrank":
            print(kuehlschrank.description)
            #answer_1 = input("Was willst Du tun? (öffnen/putzen) --> ").lower().strip()
            answer_1 = input_answer("Was willst Du tun? (öffnen/putzen) --> ")
            if answer_1 == "öffnen":
                if kuehlschrank.inventory != None:
                    if kuehlschrank.inventory["coin"]>0: # task_2
                        print(f"Der Kühlschrank ist leer. Nur unten im Gemüsefach\n findest Du {schreibtisch_schublade.inventory['coin']} Münze")
                        answer_2 = input_answer("\nMöchtest Du die Münze einsammeln? (ja/nein) --> ")
                        if answer_2 == "ja":
                            player.inventory["coin"] += kuehlschrank.inventory["coin"]
                            kuehlschrank.inventory["coin"] = 0
                            print(f"Du hast {player.inventory['coin']} Münze(n) in Deinem Inventar")
                    else:
                        print("In der Schublade befindet sich keine Münze.")
                else:
                    print("Der Kühlschrank ist leer.")
            
            elif answer_1 == "putzen":
                durchgang = 1
                if kuehlschrank.eigenschaft["sauber"] == False:
                    print("Harte Arbeit, aber nach ca 20 Minuten hast Du es geschaft. Der Kühlschrank ist sauber")
                    kuehlschrank.eigenschaft["sauber"] = True
                elif kuehlschrank.eigenschaft["sauber"] == True:
                    print("Der Kühlschrank ist bereits sauber. Nochmal putzen wäre nicht schlau.")
                    durchgang +=1
                    if durchgang >= 3: kuehlschrank.eigenschaft["sauber"] = False
       
if player.location == schlafzimmer:
    if input == "Nachttsich":
        print(nachttisch.description)
        if nachttisch.inventory["coin"] > 0:   
            print("Oben auf dem Nachttisch liegt eine goldene Münze")
            answer = input_answer("\nMöchtest Du die Münze einsammeln? (ja/nein) --> ")
            if answer == "ja":
                player.inventory["coin"] += 1
                nachttisch.inventory["coin"] = 0
                print("Du steckst die Münze ein. Mehr hat der Nachttisch offenbar nicht zu bieten")
                print(f"Du hast {player.inventory['coin']} Münze(n) in Deiner Tasche")


    if player.location == wohnzimmer:
        if input == "sparschwein":
            task_2_coins(player=player)

def change_room(player:str, input:str)->None:
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
                    
    
    elif player.location == abstellkammer:                                       # Abstellkammer
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
          