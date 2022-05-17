from datetime import date
import random

room1 = [(date(2022,random.randrange(1,6,1),random.randrange(1,29,1)),date(2022,random.randrange(1,6,1),random.randrange(1,29,1)))]
print(room1)
Hotel = {"single": [(1,room1),(2,room2)],
    "double": [(11,room11),(12,room12)],
    "triple": [(21,room21),(22,room22)]}