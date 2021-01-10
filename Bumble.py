# if error from beautifultable type in console: pip install beautifultable
from math import *
from beautifultable import BeautifulTable


class Model:

    def __init__(self,starting=20,max_grass=1000):
        self.bumbles = starting
        self.meadow_max = max_grass
        self.meadow = max_grass/2
        self.meadow_growth_rate = .25
        self.month = 0
        self.table = BeautifulTable()
        

        self.table.columns.header = ["Month","Starting Pop", "Eating Capactiy", "Grass Eaten", "Grass Required", "Grass Deficit", "Bumble Starved", "Pop After Starve", "Bumble Births"]
    
    def run_month(self):
        self.month += 1
        self.meadow += self.meadow_growth_rate*(self.meadow_max-self.meadow)
        old_pop = self.bumbles
        if self.meadow > self.bumbles*3:
            birthed = ceil(self.bumbles/2)
            self.bumbles += ceil(self.bumbles/2)
            starved = 0
        elif self.meadow >self.bumbles*2:
            birthed = ceil(self.bumbles/2)
            self.bumbles += ceil(self.bumbles/2)
            starved = 0
        else:
            starved = ceil((self.bumbles*2-self.meadow)/2)
            self.bumbles -= ceil((self.bumbles*2-self.meadow)/2)
            birthed = ceil(self.bumbles/2)
            self.bumbles += ceil(self.bumbles/2)
            

        self.table.rows.append([self.month, 
        int(old_pop), 
        old_pop*3, 
        min(old_pop*3, 1000), 
        old_pop*2, 
        max(0, old_pop*2-1000), 
        starved,
        old_pop-starved,
        birthed
        ])

    def run(self,months):
        for r in range(months):
            self.run_month()
        

model = Model()

model.run(30)
print(model.table)