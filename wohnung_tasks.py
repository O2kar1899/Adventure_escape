import random as rnd
from re import L
import sys

loesung_wohung_list = ["artep", "rakso", "reuam", "easy!"] # 5 Zeichen!
loesung = rnd.choice(loesung_wohung_list)
loesung_wohnung = []

for i in range(len(loesung)):
    loesung_wohnung.append(loesung[i])

loesung_wohnung_gefunden = ["???", "???", "???", "???", "???"]


def task_1(): # Um die Aufgage zu starten muss man den PC im Arbeitszimmer einschalten
    """ wordle player must find a specific word with 5 letters
    """   
    if loesung_wohnung[0] == loesung_wohnung_gefunden[0]:
        print("nach kurzem flackern erscheint auf dem Bildschirm:")
        print(f"Das erste Zeichen des Codes lautet: {loesung_wohnung[0]}")
        
    else:
        word_list = ["angel", "katze", "mauer", "lauer", "linux", "paul", "charlot", "catharina", "petra", "heiner"]
        word = rnd.choice(word_list) 
            
        print("Der geht nach einigem flackern an. Nach dreimal 'Piep' erscheint folgende Anzeige:\n")
        print("Um das erste Zeichen vom Code zu erhalten, musst Du ein Wort erraten.")
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
                print (f" Das erste Zeichen des Codes: {loesung_wohnung[0]}")
                loesung_wohnung_gefunden[0] = loesung_wohnung[0]
                return True
            else:
                for i in range(len(word)):
                    if word[i] == attemp[i]:
                        print(f"{attemp[i]} steht schon an der richtigen Stelle.")
                    elif attemp[i] in word:
                        print(f"{attemp[i]} ist im Wort vorhanden")
                    else:
                        print(f"{attemp[i]} ist nicht im Wort vorhanden")         
                print(f"Du hast noch {5-t} Versuche.")    
        print("\nDu hast das Wort nicht gefunden.\n")
        

def task_2():
    pass

def task_3():
    pass

def task_4():
    pass

def task_5():
    pass