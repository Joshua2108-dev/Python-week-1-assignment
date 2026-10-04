import my_module
import math
import random
from datetime import datetime

# Customs modules
print(my_module.add(99, 33))
print(my_module.square(99))

# Buildind a module
print(math.sqrt(625))

candidates = ["Sifuna", "Kalonzo", "Ruto", "Matiangi", "Maraga", "Boniface", "Wajakoya"]
winner = random.choice(candidates)
print(winner)

# date time library
today = datetime.today()
print(today)

