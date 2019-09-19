import os
if os.path.isdir('my_dir'):
    print("my_dir exists")
else:
    print("my_dir doesnt exists")

#Check whats on the given folder '.' means working directory
contents_folder = os.listdir(".")
print(contents_folder)

#check for subDirectories on the folder scanned by listdir
for item in contents_folder:
    if os.path.isdir(item):
        print(f"El item {item} es un directorio")

#Rename works like mv on linux
os.rename("old_dir", "renamed_dir")

#Delete files
os.remove("old_file_to Remove")

#Delete EMPTY folders
os.rmdir("old_dir_to_Remove")

#Create a folder
os.mkdir("new_folder")

#Delete a folder along with its contents
import shutil
shutil.rmtree("Old_dir_to_Remove")

#Copy a given file
shutil.copyfile("original_file", "new_file")

#copy a folder with its contents
shutil.copytree("original_dir", "new_dir")

#Search for files using wildcards
import glob
list_py = glob.glob(".*/*.py")

#Change the working directory
os.chdir("new_path")

#Print the working directory
print(os.getcwd())