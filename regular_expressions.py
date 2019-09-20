import re
import os

text = """
this is    my text wow.
But this wow, has some problems.
Python 101
A problem of problems
"""

expresion_regular = '\\W+'
#print(text.split())

#palabras = re.split(expresion_regular, text)
palabras = re.findall(r'[a-z|A-Z]+', text)
print(palabras)

numeros = re.findall(r'\d+', text)
print(numeros)

ipconfig = os.popen('ipconfig').read()

splited = re.findall(r'\d+\.\d+\.\d+\.\d+', ipconfig, flags=re.IGNORECASE+re.MULTILINE)
print("1- " + str(splited[0]))


#\d+\.\d+\.\d+\.\d+
#[0-225]+\.[0-225]+\.[0-225]+\.[0-225]+

splited = re.findall(r'(\d+\.\d+\.\d+\.\d+){1}', ipconfig)
print("2- " + str(splited))