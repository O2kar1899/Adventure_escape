import random as rnd
import sys

loeseung_wohnung = [False, False, False, False, False]

def wordle(): # Um die Aufgage zu starten muss man den PC im Arbeitszimmer einschalten
    """ player must find a specific word with 5 letters
    """    
    word_list = ["angel", "katze", "mauer", "lauer", "linux", "paul", "charlot", "catharina", "petra", "heiner"]
    word = rnd.choice(word_list)
        
    print("\nDu hast 5 Versuche um das Wort zu finden.\n")
    
    for t in range(1,6):
        attemp = "" 
        while len(attemp) != len(word):
            attemp = input(f"\nGib ein Wort mit {len(word)} Buchstaben ein: ").strip().lower()
            if attemp == "q":
                sys.exit()
                    
        if attemp == word:
            print("Du hast das Wort gefunden!")
            loeseung_wohnung[0] = "a"
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

wordle()