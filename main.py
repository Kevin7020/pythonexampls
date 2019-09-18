import argparse
import imported

#nombre = input("Nombre a saludar? \n")

#imported.salute(nombre)
#print("Concate %s" % "Nando")

parser = argparse.ArgumentParser(description='Brakes your pc')
parser.add_argument('-n', '--name', type=str, help='a name for this mofo')

args = parser.parse_args()

cohete = args.name #"Saturno"

print(cohete.upper())

print("Hola mi amigo {0} talves esto no {1}".format("Saturno","funcione"))
#print("\n" *5)
print(f"hola {cohete}")

#slicing
#li = [1, 2, 3]
#li[:2]
#li[:]