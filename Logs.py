import logging as lg 

LOGS_MESSAGE_FORMAT = "%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s"
LOGS_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

lg.basicConfig(filename='myLog.log', level=lg.DEBUG, format=LOGS_MESSAGE_FORMAT, datefmt=LOGS_DATE_FORMAT)

if __name__ == '__main__': #if this is the main file that is being run then __name__ is going to be __main__
    miLog = lg.getLogger()  #Else if this is just being imported __name__ is going to be the name of the "module" or the file
    miLog.debug("This is on a DEBUG level")
    miLog.critical("This is on a CRITICAL level")