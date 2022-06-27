import random as rnd
import sys

print("wohnung_tasks.py wurde geladen.")

loeseung_wohnung = ["a", "r", "t", "e", "p"]
loesung_wohnung_gefunden = [None, None, None, None, None]

def task_1(): # Um die Aufgage zu starten muss man den PC im Arbeitszimmer einschalten
    """ player must find a specific word with 5 letters
    """    
    word_list = ["angel", "katze", "mauer", "lauer", "linux", "paul", "charlot", "catharina", "petra", "heiner"]
    word = rnd.choice(word_list)
        
    print("\nDer geht nach einigem flackern an. Nach dreimal 'Piep' erscheint folgende Anzeige:\n")
    print("\nUm das erste Zeichen vom Code zu erhalten, musst Du ein Wort erraten.")
    print(f"Du hast 5 Versuche. Das Wort hat {len(word)} Buchstaben.") 
    print("Nach jedem Versuch bekommst Du für jeden eingegebenen Buchstaben mitgeteilt,")
    print("ob er im Wort vorkommt und bereits an der richtigen Stelle ist.\n")
    
    
    for t in range(1,6):
        attemp = "" 
        while len(attemp) != len(word):
            attemp = input(f"\nGib ein Wort mit {len(word)} Buchstaben ein: ").strip().lower()
            if attemp == "q":
                sys.exit()
                    
        if attemp == word:
            print("Du hast das Wort gefunden!")
            print (f" Das erste Zeichen: {loeseung_wohnung[0]}")
            loesung_wohnung_gefunden[0] = loeseung_wohnung[0]
            return True
        else:
            for i in range(len(word)):
                if word[i] == attemp[i]:
                    print(f"{attemp[i]} steht schon an der richtigen Stelle.")
                elif attemp[i] in word:
                    print(f"{attemp[i]} ist im Wort vorhanden")
                else:
                    print(f"{attemp[i]} ist nicht im Wort vorhanden")         
            print(f"\nDu hast noch {5-t} Versuche.\n")    
    print("\nDu hast das Wort nicht gefunden.\n")
    return False

