# import math
# from turtle import *

# def coeur_a(k):
#     return 15 * math.sin(k)**3
# def coeur_b(k):
#     return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)
# speed(0)
# bgcolor("black")
# for i in range(10000):
#     goto(coeur_a(i) * 20, coeur_b(i) * 20)
#     for j in range(5):
#         color("#f73487")
#         goto(0,0)
#     done()

import math
from turtle import *

def coeur_a(k):
    return 15 * math.sin(k)**3

def coeur_b(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")
color("#f73487")
penup()
goto(0, 0)
pendown()

# Boucle pour tracer le coeur
for i in range(10000):
    k = i * 0.01  # Conversion en angle pour un tracé fluide
    x = coeur_a(k) * 20
    y = coeur_b(k) * 20
    goto(x, y)

done()
