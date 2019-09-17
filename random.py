import random

#dado con 6 caras con 100 ejecuciones

#random_range = random.randrange(1, 7) #range between 1 and 6
#print(random_range)

side1 = 0
side2 = 0
side3 = 0
side4 = 0
side5 = 0
side6 = 0

def dado():
    return random.randrange(1, 7)

for roll in range(1000):
    sideResult = dado()

    if sideResult == 1:
        side1 += 1
    if sideResult == 2:
        side2 += 1
    if sideResult == 3:
        side3 += 1
    if sideResult == 4:
        side4 += 1
    if sideResult == 5:
        side5 += 1
    if sideResult == 6:
        side6 += 1

print("El numero 1 salio {0} veces".format(side1))
print("El numero 2 salio {0} veces".format(side2))
print("El numero 3 salio {0} veces".format(side3))
print("El numero 4 salio {0} veces".format(side4))
print("El numero 5 salio {0} veces".format(side5))
print("El numero 6 salio {0} veces".format(side6))
print(side1 + side2 + side3 + side4 + side5 + side6)
