class Persona():
    def __init__(self, nombre, edad, peso, color_pelo, asegurado=True):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color_pelo = color_pelo
        self.asegurado = asegurado

    def __str__(self):
        return "Esta Persona se llama " + self.nombre
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor:
            self.nombre = valor
        else:
            raise(Exception("Valor invalido"))

class Trabajador(Persona):
    def __init__(self, horas, nombre, edad, peso, color_pelo, asegurado=True):
        self.horas = horas
        Persona.__init__(self, nombre, edad, peso, color_pelo, asegurado)

carlos = Persona("Carlos", 25, 75, "Negro")

print(carlos)

Trabajador1 = Trabajador(40, "marcos", 28, 80, "blanco")
print(Trabajador1)

trabajador2 = Trabajador(horas=40, nombre="Martha", edad=21, peso=50, color_pelo="rubio", asegurado=False)
print(trabajador2)
print(trabajador2.asegurado)