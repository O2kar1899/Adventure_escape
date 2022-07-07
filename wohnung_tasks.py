import random as rnd
from wohnung_instances import coin, piggy_bank
import sys

loesung_wohung_list = ["artep", "rakso", "reuam", "easy!"] # 5 Zeichen!
loesung = rnd.choice(loesung_wohung_list)
loesung_wohnung = []
for i in range(len(loesung)):
    loesung_wohnung.append(loesung[i])
loesung_wohnung_gefunden = ["???", "???", "???", "???", "???"]

def input_answer(question:str="--> ") -> str:
        answer = input(question).lower().strip()
        return answer

def task_1_wordle(): # Um die Aufgage zu starten muss man den PC im Arbeitszimmer einschalten
    """ wordle player must find a specific word with 5 letters
    """   
    if loesung_wohnung[2] == loesung_wohnung_gefunden[2]:
        print("nach kurzem flackern erscheint auf dem Bildschirm:")
        print(f"Das dritte Zeichen des Codes lautet: {loesung_wohnung[2]}")
        
    else:
        word_list = ["angel", "katze", "mauer", "lauer", "linux", "paul", "charlot", "catharina", "petra", "heiner"]
        word = rnd.choice(word_list)             
        print("Der Computer geht nach einigem flackern an. Nach drei mürrischen piepsern erscheint folgende Anzeige:\n")
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
                print("Der Computer schaltet sich mit einem leisen räuspern wieder aus")
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
        print("...versuch es später nochmal!")
       
def task_2_coins(player):
    """Orte der Münzen:
        - Arbeitszimmer - Schreibtisch - Schublade
        - Küche - Kühlschrank
        - Balkon_wohnzimmer - blumentopf_1
        - Flur - Schuhschrank - schwarze Schuhe
        - Schlafzimmer - Nachttisch
    """
    print(piggy_bank.description)
    print(f"Anzahl der Münzen im Sparschwein: {piggy_bank.inventory['coin']}")
    
    coins_player = player.inventory["coin"]
    
    if coins_player > 0:
        print(f"Du hast {coins_player} Münzen in deinem Inventar\n")
        while True:
            answer = input("Möchtest Du die Münze(n) in das Sparschwein legen Ja/Nein? ").lower().strip()
            if answer == "ja":
                print("Du wirfst eine Münze in das Sparschwein und stelltst es wieder an seinen Platz.")
                piggy_bank.inventory["coin"] += coins_player
                player.inventory["coin"] = 0
                print(f"Anzahl der Münzen im Sparschwein: {piggy_bank.inventory['coin']}")
                break
            elif answer == "nein":
                print("Du stellst das Sparschwein wieder auf seinen Platz")                
                break
            else: print ("Das ist keine gültige Eingabe!")
    
    if piggy_bank.inventory["coin"] >= 5:
        print("Aus dem Sparschwein ertönt eine blecherne Stimme:")
        print(f"Das zweite Zeichen des Codes lautet: {loesung_wohnung[1]}")
        loesung_wohnung_gefunden[1] = loesung_wohnung[1]

def task_3_Fibonacci(player):
    print("Ein einfaches Rätsel zum Start:")
    while True:
        print("Welche Zahl folgt nach |0|1|1|2|3|5|8| ?")
        if input(" --> ") == "13":
            print(f"Super! Das erste Zeichen des Codes hast Du gefunden: {loesung_wohnung[0]}")
            loesung_wohnung_gefunden[0] = loesung_wohnung[0]
            return True
        else: 
            print("Leider falsch. Willst Du gleich noch einmal versuchen? oder erste einen Tipp")
            answer = input_answer("versuchen/Tipp/Abbrechen? ")
            if answer == "tipp":
                print("Fibonacci würde die Antwort kennen")
            elif answer == "versuchen":
                pass
            else:
                print("Vielleicht kommst Du später nochmal vorbei - Du stehst weiterhin im Flur")
                return False

def task_4():
    pass

def task_5():
    pass