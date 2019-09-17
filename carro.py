import math
# class carro():
#     def __init__(self, motor):
#         self.motor = motor

#     def acelerar(self, tiempo, intensidad):
#         self.motor.acelerar(tiempo, intensidad)

# class motor:
#     def __init__(self,tipo):
#         self.tipo = tipo

#     def acelerar(self, tiempo, intensidad):
#         print("estoy acelerando por " + str(tiempo) + " segundos a una intensidad " + intensidad)


# v10 = motor("deisel")

# jeep = carro(v10)

# jeep.acelerar(10, "alta")


class carro():
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad


class punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, otro_punto):
        delta_x = self.x - otro_punto.x
        delta_y = self.y - otro_punto.y
        return math.sqrt(delta_x**2 + delta_y**2)

marca = input("Ingrese la marca del vehiculo: \n")
velocidad = input("Ingrese la velocidad del vehiculo: \n")
pichirulo = carro(marca, velocidad)

inpt = []
x = None
y = None
while x != 0 and y != 0:
    if x is not None and y is not None:
        pnt = punto(x, y) 
        inpt.append(pnt)
    x = int(input("Ingrese la coordenada x: \n"))
    y = int(input("Ingrese la coordenada y: \n"))

print(inpt)





import math

class Punto:


    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self, otro_punto):
        return (self.x - otro_punto.x, self.y - otro_punto.y)

class carro():

    def __init__(self,p1,p2,velocidad):
        self.tiempo = 0
        self.velocidad = velocidad
        (self.delta_x, self.delta_y) = p1 - p2




    def pitagoras(self):
        return (math.sqrt(self.delta_x ** 2 + self.delta_y ** 2))


    def calcularTiempo(self):
        distancia = self.pitagoras()
        self.tiempo = float(distancia / self.velocidad)
        return(self.tiempo)

class interfaz():
    @classmethod
    def pedirListPuntos(cls):
        lista =[]
        while True:
            punto = input("Escriba su punto").split()

            if punto == ['0','0']:
                break
            else:
                punto1 = Punto(int(punto[0]),int(punto[1]))
                lista.append(punto1)
        return lista

    @classmethod
    def iterar(cls):
        velocidad = int(input("Cual es la velocidad"))
        tiempoTotal = 0
        lista = cls.pedirListPuntos()
        index = 1
        puntoant = None
        punto = None
        while index < len(lista):
            puntoant = lista[index-1]
            punto = lista[index]
            tiempoTotal += carro(puntoant,punto,velocidad).calcularTiempo()
            index += 1
        print("El tiempo total fue {0}".format(tiempoTotal))


interfaz.iterar()