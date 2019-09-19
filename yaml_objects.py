import yaml

listt = [1, 2, 3, 4, "texto"]
sett = {7, 8, 0}
dic = {1:'Juan',2:'Carlos',3:'Frank'}

print(yaml.dump(dic))
print(yaml.dump(sett))
print(yaml.dump(listt))

#Save our dictionary to a yml file
with open('my_obj.yml', 'w') as yml_file:
    yml_file.write(yaml.dump(dic))

#Open the saved file
with open('my_obj.yml', 'r') as yml_file:
    new_obj_readed = yaml.load(yml_file, Loader=yaml.SafeLoader)  #SafeLoader is only going to load python proprietary classes

print(new_obj_readed)


"""
import yaml
import persona

carlos = persona.Persona('Carlos', 25, 70, 'negro')
lista = [1, 3, 6, 7, 7]
conjunto = {7, 8, 0}
dictionario = {1:'Juan', 2:'Carlos', 3:'Frank'}

texto = yaml.dump(carlos)

print(texto)

with open('mi_objecto.yml', 'w') as yml_file:
    yml_file.write(yaml.dump(carlos))

with open('mi_objecto.yml', 'r') as yml_file:
    nuevo_obj = yaml.load(yml_file, Loader=yaml.SafeLoader)

print(nuevo_obj)
"""
import yaml

kevin = Persona("kevin","11/11/2001",101)
caleb = Persona("caleb","11/11/5000",103)
personas = {101:kevin, 103:caleb}

with open('mi_objecto.yml', 'w') as yml_file:
    yml_file.write(yaml.dump(personas))

with open('mi_objecto.yml', 'r') as yml_file:
    nuevo_obj = yaml.load(yml_file, Loader=yaml.Loader)

for persn in nuevo_obj:
    print(persn)
print(nuevo_obj)



#if __name__ == '__main__': #if this is the main file that is being run then __name__ is going to be __main__
#    Code to run...         #Else if this is just being imported __name__ is going to be the name of the "module" or the file