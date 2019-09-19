#delete or copy only file menu

import os
import shutil
import Logs

miLog = Logs.lg.getLogger()

#Return the list of files only! 
def get_files(locat="."):
    os.chdir(locat)
    return [obj for obj in os.listdir(locat) if os.path.isfile(obj)]

#Check whats on the given folder '.' means working directory
os.chdir("./list_dirExpl")
contents_folder = os.listdir()
miLog.debug("Contents read from the yml file:\n" + str(contents_folder))

#check for subDirectories on the folder scanned by listdir
def listt():
    counter = 0
    for item in contents_folder:
        counter += 1
        print(f"{str(counter)} : {item}")

Contn = "y"
while Contn.lower() != "n":
    listt()

    file_index = int(input("Ingrese el numero del archivo a modficar: \n"))
    action = input("Ingrese la operacion a realizar: delete | copy \n")
    miLog.debug(f"Index selected {file_index} Operation {action}")

    if action.lower() == 'copy' or action.lower() == 'c':
        new_file = input("Ingrese el nombre del nuevo archivo \n")
        #Copy a given file
        miLog.debug(f"Working directory {os.getcwd()}")
        
        shutil.copy(contents_folder[file_index -1], new_file)
    elif action.lower() == 'delete' or action.lower() == 'd':
        conf = input(f"Esta seguro que desea eliminar {contents_folder[file_index -1]}\n")
        if conf.lower() == 'y' or conf == 'yes':
            os.remove(contents_folder[file_index -1])
        else:
            print(f"{contents_folder[file_index -1]} no se ha modificado\n")
    
    Contn = input("Desea realizar otra operacion? N/n: \n")