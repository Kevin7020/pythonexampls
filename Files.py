# try :
#     names = open()
#     #
#     #TODO

# except Exception in ex :
#     print(ex)

# finally:
#     names.close()


# with open('names.txt', 'w') as names: # "With" handles the exeptions automatically
#     try: #Optional, but it can be done

import csv

class Persona():
    def __init__(self, nombre, fecha_nacimineto, ID):
        self._nombre = nombre
        self._fecha_nacimineto = fecha_nacimineto
        self._id = ID
    @property
    def ID(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def fecha_nacimento(self):
        return self._fecha_nacimento


class Trabajador(Persona):
    def __init__(self, nombre, fecha_nacimineto, ID, tarifa):
        self.tarifa = tarifa
        Persona.__init__(self, nombre, fecha_nacimineto, ID)


planilla = {}
hours_worked = {}

with open("planilla.csv", newline='') as csvfile:
    planillaReader = csv.reader(csvfile, delimiter=",", quotechar="\"")
    for row in planillaReader:
        print(row)
        #['kevin,18/12/1900,1006,3,240']
        trab = Trabajador(row[0], row[1], row[2], int(row[3]))
        planilla[row[2]] = trab
        hours_worked[row[2]] = int(row[4])

print(planilla)
print(hours_worked)

""" Contn = "y"
 while Contn.lower() != "n":
     name = input("Ingrese el nombre del trabajador: \n")
     dte = input("Ingrese la fecha de nacimiento del trabajador: \n")
     work_id = int(input("Ingrese el id del trabajador: \n"))
     work_fare = int(input("Ingrese la tarifa del trabajador: \n"))
     work_hours = int(input("Ingrese las horas laboradas del trabajador: \n"))
     trab = Trabajador(name, dte, work_id, work_fare)

     planilla[work_id] = trab
     hours_worked[work_id] = work_hours
     Contn = input("Desea ingresar otro trabajador? N/n: \n")
"""

total = 0
for item in planilla:
    total += planilla[item].tarifa * hours_worked[item]
    print("Nombre: {0} id: {1} ₡: {2}\n".format(planilla[item].nombre, str(planilla[item].ID), planilla[item].tarifa * hours_worked[item]))
print("Total apagar {0}\n".format(total))

 

 #######################
#  class Empleado():
#     def __init__(self, nombre, id):
#         self.nombre, self.id = nombre, id

# with open("empleados.txt", "r") as archivo_empleados:
#     empleados_string = archivo_empleados.read()

# lista_empleados_string = empleados_string.split()
# print(lista_empleados_string)

# empleados = {}
# for empleado in lista_empleados_string:
#     empleado_temp = empleado.split(",")
#     empleados[empleado_temp[1]] = empleado_temp[0]

# print(empleados)