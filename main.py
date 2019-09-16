import argparse
import imported

#nombre = input("Nombre a saludar? \n")

#imported.salute(nombre)
#print("Concate %s" % "Nando")

parser = argparse.ArgumentParser(description='Brakes your pc')
parser.add_argument('String', metavar='N', type=str, nargs='+',
                    help='a name for this mofo')

args = parser.parse_args()

cohete = args.String[0] #"Saturno"

print(cohete.upper())

print("Hola mi amigo {0} talves esto no {1}".format("Saturno","funcione"))
#print("\n" *5)
print(f"hola {cohete}")