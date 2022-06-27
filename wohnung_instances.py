from classes import Location, Object, Device
# **************************  objects Wohnung **************************
blumentopf_1 = Object(name="Blumentopf", 
description="Ein mittelgroßer Blumentopf, mit einer gelben Blume.")

schrank_arbeitszimmer = Object( # --> Arbeitzimmer
    name="Schrank im Arbeitszimmer", 
    description="Ein weißer Schrank aus einem schwedischen Möbelhaus.")

schreibtisch_schublade = Object( # --> Schreibtisch --> Arbeitszimmer --> Wohnung
    name="Schreibtisch-Schublade",
    description="Eine Schublade aus einem schwedischen Schreibtisch.",
    portable=False
    )

schreibtisch_arbeitszimmer = Object( # Arbeitszimmer --> Wohnung
    name="Schreibtisch im Arbeitszimmer", 
    description="Ein schwarzer Schreibtisch.",
    portable=False,
    inventory=[schreibtisch_schublade],
    )


# **************************  devices **************************
computer_arbeitszimmer = Device(name="Computer im Arbeitszimmer",
    description= "Ein Computer mit einer grauen Tastatur und einem schwarzen Bildschirm.", 
    portable=False,    
    power = False,
    power_string="ausgeschaltet"
    )

bildschirm_schwarz = Device(
    name="Schwarzer Bildschirm", 
    description="Ein schwarzer Bildschirm.", 
    portable="True", 
    power="aus")

schreibtischlampe = Device(
    name="Schreibtischlampe",
    description="Ein ganz normale klein Schreibtischlampe.",
    portable=True, 
    power=False)

# **************************  locations **************************
arbeitszimmer = Location(      
    name="Arbeitszimmer", 
    description=f"Auf dem Schreibtisch stehen zwei Bildschirme und davor eine Tastatur. \
        Der PC ist {computer_arbeitszimmer.power_string}. Vorne am PC ist ein großer Knopf mit der Beschriftung POWER \
        Hinter dem Schreibtisch steht ein Bücherregal. \
        Auf dem Bücherregal stehen einige Bücher. Gegenüber steht ein Schrank. \
        Im Süden liegt das Wohnzimmer. Im Osten das Bad und im Westen eine kleine Abstellkammer.",
    exits=["Osten", "Süden", "Westen"],
    objects=[schreibtisch_arbeitszimmer, schrank_arbeitszimmer, computer_arbeitszimmer, bildschirm_schwarz, schreibtischlampe], 
    )
     
abstellkammer = Location(
    name="Abstellkammer",
    description="Ein kleiner Raum in dem man Dinge unterbringen kann, die man zurzeit nicht braucht. \
            Im Osten liegt das Arbeitszimmer, nach Süden kommst Du in den Flur",
    exits=["Osten","Süden"],
    objects=["Gegenstände"]
    )

bad = Location(
    name = "Bad", 
    description="Ein schönes Bad mit einem WC, einer Dusche und einer kleinen Badewanne. Nach Westen kommst Du auf den Balkon ", 
    objects=None
    )

balkon_schlafzimmer = Location(
    name="Schlafzimmer-Balkon",
    description="Ein schöner Balkon mit einem Stuhl und einem kleinem Tisch. Nach Westen kommst Du auf einen weiteren Balkon", 
    objects=None
    )

balkon_wohnzimmer = Location(
    name="Wohnzimmer-Balkon",
    description="Im Nordn liegt das Wohnzimmer. Nach Osten kommst Du auf einen anderen Balkon. Nach Westen kommst Du in die Küche ",
    objects=["Liegestuhl", blumentopf_1, "Kerzenständer"]
    )

flur = Location(
    name="Flur",
    description="Im Osten liegt das Wohnzimmer. Nach Süden kommst Du in die Küche.\nNach Norden kommst Du in die Abstellkammer Im Westen ist der Ausgan der Wohnungn",
    exits=["norden", "osten", "sueden", "westen"],    
    objects=["Garderobe", "Schuhschrank"]
    )

kueche = Location(
    name="Küche", 
    description="Im Norden lieg der Flur. Nach Osten kommst Du auf einen Balkon",
    exits=["osten", "norden"],
    objects=["Herd", "Kühlschrank", "Schrank"]
    )   

no_exit = Location(
    name="No_Exit",
    description="Hier geht es nicht weiter",
    objects=None  
    )

schlafzimmer = Location(
    name="Schlafzimmer", 
    description="Du bis im Schlafzimmer. Es lieg im Osten der Wohnung. Im Norden ist ein kleines Bad.  \
        \nIm Süden kommst Du auf einen kleinen Balkon und nach Westen ins Woznzimmer",
    exits=["norden", "sueden", "westen"],
    objects=["Bett","Schrank","Wäschekorb"]    
    )  

wohnzimmer = Location(
    name="Wohnzimmer", 
    description="Das Wohnzimmer liegt im Mittelpunkt der Wohnung.\nIm Norden ist befindet sich das Arbeitszimmer. \
        \nIm Süden ist ein großer Balkon mit vielen Blumen. \
        \nNach Westen kommst Du in den Flur. Im Osten liegt das Schlafzimmer",
    exits=["norden", "osten", "sueden", "westen"], 
    objects=["Sofa","Schrank","Ferseher","Tisch"]
    )

no_exit = Location(
    name="Kein Ausgang",
    description="Hier geht es nicht weiter",
    objects=None
    )