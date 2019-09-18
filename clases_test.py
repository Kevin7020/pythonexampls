import math
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, otro_punto):
        delta_x = self.x - otro_punto.x
        delta_y = self.y - otro_punto.y
        return math.sqrt(delta_x**2 + delta_y**2)


p1 = point(22, 30)
p2 = point(25, 35)

isinstance(p1, point) # verifies if the instance comes from the given class
p1.__dict__
p1.__dict__["x"]
p1.__dict__["x"] = "50"
print(p1 - p2)


# import math
# class point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __sub__(self, otro_punto):
#         return (self.x - otro_punto.x, self.y - otro_punto.y)

#     def pitagoras(self, lista):
#         return math.sqrt(lista[0]**2 + lista[1]**2)


# p1 = point(22, 30)
# p2 = point(25, 35)

# lista = p1 - p2
# print(p1.pitagoras(lista))



#Paralel asigment
# import math
# class point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __sub__(self, otro_punto):
#         delta_x, delta_y = (self.x - otro_punto.x, self.y - otro_punto.y)
#         return math.sqrt(delta_x**2 + delta_y**2)


# p1 = point(22, 30)
# p2 = point(25, 35)

# print(p1 - p2)
