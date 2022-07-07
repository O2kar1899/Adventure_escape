
# ++++++++++++++++++++++++++++++ class Object ++++++++++++++++++++++++++++++



class Object:
    def __init__(self, name:str="", description:str="", inventory=None, portable: bool =True, weight: int =0, eigenschaft: dict=None):
        self.name = name
        self.description = description
        self.portable = portable
        self.inventory = inventory
        self.weight = weight
        self.eigenschaft = eigenschaft
    
    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPortable: {self.portable}"

# ++++++++++++++++++++++++++++++ class Device ++++++++++++++++++++++++++++++
class Device(Object):
    def __init__(        
        self, 
        name:str, 
        description:str, 
        inventory: list =None, 
        portable: bool =True, 
        weight: int =0,
        power: bool =False,
        power_string: str ="aus",
        eigenschaft: dict=None
        ):
        super().__init__(name, description, inventory, portable, weight, eigenschaft)
        self.power = power
        self.power_string = power_string
        
        
    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPortable: {self.portable}\nPower: {self.power}"
       
# ++++++++++++++++++++++++++++++ class Location ++++++++++++++++++++++++++++++
class Location:
    def __init__(self, name: str, description: str, exits=None, objects: dict=None, inventory: dict=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.objects = objects
        self.inventory = inventory         
      
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nDescription:{self.description}\nobjects: {self.objects}, inventory: {self.inventory}"

# ++++++++++++++++++++++++++++++ class Character ++++++++++++++++++++++++++++++
class Character:
    def __init__(self, name: str="", health:int=100, damage: int=0, location: Location=None, welt: str=None, inventory: dict=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.location = location
        self.welt = welt
        self.inventory = inventory
       
    def set_location(self, location):
        self.location = location

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def __str__(self):
        return f"{self.name} hat {self.health} Lebenspunkte und {self.damage} Schadenspunkte"

    def __repr__(self):
        return f"{self.name} has {self.health} health and {self.damage} damage"