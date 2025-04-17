#Here are the atributes

import random
class pet :
    def __init__(self):
        self.name = "Pluto"
    
    def show_hunger(self) :
        self.hunger = random.randint(0,10)
        print(f"{self.name} has a hunger level:{self.hunger}")

    def show_energy(self):
        self.energy = random.randint(0,10)
        print(f"{self.name} has a energy level:{self.energy}")

    def show_happiness(self):
        self.happiness = random.randint(0,10)
        print(f"{self.name} has a happiness level:{self.happiness}")

        #Here are the Methods below
    
    def aftermeal(self):
        self.aftermeal = (self.hunger-3);(self.happiness +1)
        #print(f"{self.name} after a meal has a hunger level of:{self.hunger}")

    def sleep_level(self):
        self.sleep = (self.energy +5)
        if self.aftermeal >= 10:
            self.aftermeal = 10
        #print(f"{self.name} after a sleep has an energy level of:{self.energy}")

    def playfulness(self):
        self.play = (self.energy-2);(self.happiness+2);(self.hunger+1)
        #print(f"{self.name} has a playfulness level of:{self.aftermeal}")

    #Here is the status 
    
    def show_status(self):
        self.status = (self.energy);(self.hunger);(self.happiness)
        print(f"{self.name} has a {self.hunger} level of hunger, {self.energy} level of energy and a {self.happiness} level of happiness")

    #Bonus trick
        

my_pet = pet()
my_pet.show_hunger()
my_pet.show_energy()
my_pet.show_happiness()
my_pet.show_status()


    