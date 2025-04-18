#Here are the atributes
import random
class pet :
    
    def __init__(self):
        self.name = "Pluto"
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = ["Roll","Jump","Spin","Bow","Shake Paws","Bark","Stand"]
    
    def show_hunger(self) :
        print(f"{self.name} has a hunger level:{self.hunger}")

    def show_energy(self):
        print(f"{self.name} has a energy level:{self.energy}")

    def show_happiness(self):
        print(f"{self.name} has a happiness level:{self.happiness}")

        #Here are the Methods below
    
    def aftermeal(self):
        self.hunger = min(0,self.hunger-3)
        self.happiness = (self.happiness +1)
        #print(f"{self.name} after a meal has a hunger level of:{self.hunger}")

    def sleep_level(self):
        self.energy = max(10,self.energy +5)
        #print(f"{self.name} after a sleep has an energy level of:{self.energy}")

    def playfulness(self):
        self.energy = (self.energy-2)
        self.happiness = (self.happiness+2)
        self.hunger = (self.hunger+1)
        #print(f"{self.name} has a playfulness level of:{self.aftermeal}")

    #Here is the status 
    
    def show_status(self):
        self.status = (self.energy);(self.hunger);(self.happiness)
        print(f"{self.name} has a {self.hunger} level of hunger, {self.energy} level of energy and a {self.happiness} level of happiness")


    def show_tricks(self):
        print(f"{self.name} performs a {random.choice(self.tricks)}")

    #Bonus trick       

my_pet = pet()
my_pet.show_status()
my_pet.aftermeal()
my_pet.sleep_level()
my_pet.playfulness()
my_pet.show_tricks()
my_pet.show_status()