from classes import Location, Object, Device, Character

player = Character(inventory={"coin": 0})

# **************************  objects Wohnung **************************
blumentopf_1 = Object(
    name="Blumentopf",
    description="Ein mittelgroßer Blumentopf, etwas schmutzig aber mit einer wunderschönen gelben Blume.",
    portable=True,
    weight=500,
    inventory={"coin": 1}
    )

coin = Object(
    name="Münze",
    description="Eine goldene Münze.",
    portable=True,
    weight=10
    )

nachttisch = Object(
    name="Nachttisch",
    description="Ein kleiner Nachttisch aus hellem Holz.",
    portable=False,
    weight=1000,
    inventory={"coin": 1}
    )

schuhschrank = Object(
    name="Schuhschrank",
    description="Ein gewöhnlicher weißer Schuhschrank.",
    inventory={"coin":1}
    )


schrank_arbeitszimmer = Object( # --> Arbeitzimmer
    name="Schrank im Arbeitszimmer", 
    description="Ein weißer Schrank aus einem schwedischen Möbelhaus.",
    inventory=None,
    portable=False,
    weight=None
    )

schreibtisch_schublade = Object( # --> Schreibtisch --> Arbeitszimmer --> Wohnung
    name="Schreibtisch-Schublade",
    description="Eine Schublade aus einem schwarzen Schreibtisch.",
    inventory={"coin":1}, # task_2
    portable=False,
    weight=None
    )

schreibtisch_arbeitszimmer = Object( # Arbeitszimmer --> Wohnung
    name="Schreibtisch", 
    description="Ein schwarzer Schreibtisch, mit einer einzelnen Schublade.",
    inventory={"Schublade":schreibtisch_schublade},
    portable=False,
    weight=None    
    )

piggy_bank = Object( # --> Wohnzimmer (task_2)
    description="Auf den ersten Blick, ein ganz normales Sparschwein.\nAuf der Seite steh in sehr kleiner Schrift: Soll ich Dein Helfer sein, wirf Münzen rein.",
    inventory={"coin":0},
    portable=True,
    weight=500
    )


# **************************  devices **************************
computer_arbeitszimmer = Device(
    name="Computer im Arbeitszimmer",
    description= "Ein Computer mit einer grauen Tastatur und einem schwarzen Bildschirm.", 
    portable=False,      
    power = False,
    power_string="ausgeschaltet"
    )

bildschirm_schwarz = Device(
    name="Schwarzer Bildschirm", 
    description="Ein schwarzer Bildschirm.", 
    portable=False, 
    power=False,
    power_string="ausgeschaltet"
    )

schreibtischlampe = Device(
    name="Schreibtischlampe",
    description="Ein ganz normale klein Schreibtischlampe.",
    portable=True, 
    power=False,
    power_string="ausgeschaltet"       
    )

kuehlschrank = Device(
    name="Kühlschrank",
    description="Ein kleiner Kühlschrank der schon bessere Tage gesehen hat.",
    portable=False,
    power=True,
    power_string="eingeschaltet",
    inventory={"coin":1}, # task_2
    eigenschaft={"sauber":False}  
    )

# **************************  locations **************************
arbeitszimmer = Location(      
    name="Arbeitszimmer", 
    description=f"Auf dem Schreibtisch stehen zwei Bildschirme und davor eine Tastatur. Der PC ist {computer_arbeitszimmer.power_string}.\
        \nVorne am PC ist ein großer Knopf mit der Beschriftung POWER.",        
    exits=["Osten", "Süden", "Westen"],
    objects={"Schreibtisch":schreibtisch_arbeitszimmer, "Computer":computer_arbeitszimmer} 
    )
    
abstellkammer = Location(
    name="Abstellkammer",
    description="Ein kleiner Raum in dem man Dinge unterbringen kann, die man zurzeit nicht braucht. \
            Im Osten liegt das Arbeitszimmer, nach Süden kommst Du in den Flur",
    exits=["Osten","Süden"],
    objects=None
    )

bad = Location(
    name = "Bad", 
    description="Ein schönes Bad mit einem WC, einer Dusche und einer kleinen Badewanne. Nach Westen kommst Du auf den Balkon ", 
    exits=["Westen","Süden" ],
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
    objects={"Liegestuhl":None, "Blumentopf":blumentopf_1, "Kerzenständer":None}
    )

flur = Location(
    name="Flur",
    description="Im Osten liegt das Wohnzimmer. Nach Süden kommst Du in die Küche.\nNach Norden kommst Du in die Abstellkammer Im Westen ist der Ausgan der Wohnungn",
    exits=["norden", "osten", "sueden", "westen"],    
    objects={"Garderobe":None, "Schuhschrank":schuhschrank}
    )

kueche = Location(
    name="Küche", 
    description="Im Norden lieg der Flur. Nach Osten kommst Du auf einen Balkon",
    exits=["osten", "norden"],
    objects={"Herd":None, "Kühlschrank":kuehlschrank, "Schrank":None}
    )   

schlafzimmer = Location(
    name="Schlafzimmer", 
    description="Du bis im Schlafzimmer. Es lieg im Osten der Wohnung. Im Norden ist ein kleines Bad.  \
        \nIm Süden kommst Du auf einen kleinen Balkon und nach Westen ins Woznzimmer",
    exits=["norden", "sueden", "westen"],
    objects={"Bett":None, "Schrank":None, "Nachttisch":None},
    )  

wohnzimmer = Location(
    name="Wohnzimmer", 
    description="Das Wohnzimmer liegt im Mittelpunkt der Wohnung.\nIm Norden ist befindet sich das Arbeitszimmer. \
        \nIm Süden ist ein großer Balkon. Nach Westen kommst Du in den Flur. Im Osten liegt das Schlafzimmer",
    exits=["norden", "osten", "sueden", "westen"], 
    objects={"Sofa":None,"Schrank":None,"Fernseher":None,"Tisch":None,"Sparschwein": piggy_bank}
    )

