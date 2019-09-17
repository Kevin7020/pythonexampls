#large_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

#splitedd = large_string.split()

#print(len(splitedd))

#####import decimal

#monto = 1000.98

#plata = decimal.Decimal(monto)

#print(type(plata))
#print(plata)

lista = [12, 5, "hola"]
lista.append("el fin")
lista += ["otro fin"]
lista.remove("hola")

print(lista)
print(lista[0:3])

if "hola" in lista:
    print("Hay un saludo")
else:
    print("No hay saludos")


#for item in lista:
#    print(item, end=" ")

rango = range(0, 10, 2)
print(list(rango))

import math

def hipotenusa(p1, p2):
    deltx = p1[0] - p2[0]
    delty = p1[1] - p2[1]

    pitag1 = pow(deltx, 2)
    pitag2 = pow(delty, 2)

    resultado = math.sqrt(pitag1 + pitag2)
    print(resultado)


#hipotenusa((30, 30), (50, 60))

def listcleaner(listToClean):
    listToClean = set(listToClean)
    list(listToClean)
    return listToClean

somelist = [1, 1, 2, 3]
print(listcleaner(somelist))