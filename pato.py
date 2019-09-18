#Functions are objects as well.....

def quack(volumen): # the parameters need to be standard !!
    print("quack " + volumen)

def quack2(volume): # the parameters need to be standard !!
    print("quack2 " + volume)

class Pato():
    def __init__(self, quack_method):
        self.quack_method = quack_method

    def hacer_quack(self, volumen="default"):
        self.quack_method(volumen) #The method passed as parameter is executed here!

patito = Pato(quack) #The method "quack" is passed as parameter to "Pato" for it to be executed
patito.hacer_quack()

patito.quack_method = quack2 #Changes the given method to be called
patito.hacer_quack("fuerte")