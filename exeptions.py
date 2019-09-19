try:
    a = 3
    b=0
    print(a/b)
except: #Handle ALL exceptions
    print("You cant divide by zero")

try:
    a = 3
    b=0
    print(a/b)
except ZeroDivisionError: #Handle only the zeroDivision exeption
    print("You cant divide by zero")

try:
    a = 3
    b=0
    print(a/b)
except ZeroDivisionError as myEx:
    print("You cant divide by zero " + str(myEx))


try:
    a = 3
    b=0
    print(a/b)
except ZeroDivisionError as myEx:
    print("You cant divide by zero " + str(myEx))
except:
    print("Something weird happened")
finally:
    print("Ending process")

########################################################

"""
class FueraDeRango(Exception):
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return self.value


try:
    a = 3
    b = 0
    #print(a/b)
    raise FueraDeRango("Mi excepcion")
    print('despues de excepcion')
except AssertionError as myEx:
#ZeroDivisionError as myEx:
    print('hubo una excepcion: ' + str(myEx))
except ZeroDivisionError as myEx:
    print('hubo una division por cero: ' + str(myEx))
except FueraDeRango as myEx:
    print('fuera de rango: ' + str(myEx))
except Exception as myEx:
    print('algo raro paso: ' + str(myEx))
else:
    print('corrio todo bien')
finally:
    print("terminando el proceso")
"""

################################################

# import logging as lg
# import persona


# class FueraDeRango(Exception):
#     def __init__(self, value):
#         self.value = value

#     def __int__(self):
#         return self.value


# LOGS_MESSAGE_FORMAT = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
# LOGS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# lg.basicConfig(filename='myLog.log', level=lg.DEBUG, format=LOGS_MESSAGE_FORMAT, datefmt=LOGS_DATE_FORMAT)

# miLog = lg.getLogger()


# try:
#     a = 3
#     b = 0
#     #print(a/b)
#     raise FueraDeRango("Mi excepcion")
#     print('despues de excepcion')
# except AssertionError as myEx:
# #ZeroDivisionError as myEx:
#     print('hubo una excepcion: ' + str(myEx))
# except ZeroDivisionError as myEx:
#     print('hubo una division por cero: ' + str(myEx))
# except FueraDeRango as myEx:
#     print('fuera de rango: ' + str(myEx))
#     miLog.exception('fuera de rango', exc_info=True) #.exception along with exc_info is going to print the stactrace and the message "fuera de rango" on the log
# except Exception as myEx:
#     print('algo raro paso: ' + str(myEx))
# else:
#     print('corrio todo bien')
# finally:
#     print("terminando el proceso")