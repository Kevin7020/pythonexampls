#dic = {1:'lunes', 2:'martes', 3:'miercoles'}
#print(dic[2])
#dic[4] = 'jueves'

class contadorDePalabras():
    def contar(self, text):
        dic = {}
        dic = text.lower().split()
            # if item in dic:
            #     dic[item] += 1
            # elif item not in dic:
            #     dic[item] = 1
        return (len(dic))

"""
dic = {}
large_text = "If you've done any programming before, you have undoubtedly come across a for loop or an equivalent to it. Many languages have conditions in the syntax of their for loop, such as a relational expression to determine if the loop is done, and an increment expression to determine the next loop value. In Python this is controlled instead by generating the appropriate sequence. Basically, any object with an iterable method can be used in a for loop. Even strings, despite not having an iterable method - but we'll not get on to that here. Having an iterable method basically means that the data can be presented in list form, where there are multiple values in an orderly fashion. You can define your own iterables by creating an object with next() and iter() methods. This means that you'll rarely be dealing with raw numbers when it comes to for loops in Python - great for just about anyone!"
#large_text = large_text.lower()
#splitedd = 

for item in large_text.lower().split():
    #large_text[item] = large_text.get(item, 0) +1
    if item in dic:
        #buffer = dic.get(item)
        #buffer +=1
        #dic[item] = buffer
        #buffer = 0
        dic[item] += 1
    elif item not in dic:
        dic[item] = 1

print(dic)
"""