#Random meal generator

import random

meat = [
    "steak" ,
    "chicken" ,
    "ham" , 
    "ground beef"
]


vegetables = [
    "green beans" ,
    "corn" ,
    "broccoli" ,
    "asparagus"
]


sides = [
    "mashed potatoes" ,
    "salad" ,
    "garlic bread" ,
    "au gratin" ,
]

x = random.choice(meat)
y = random.choice(vegetables)
z = random.choice(sides)

print(x , y , z)