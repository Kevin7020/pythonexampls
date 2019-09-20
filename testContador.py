import unittest
import dictionariesv2

class simpleTest(unittest.TestCase):

    #Returns true or false
    def test(self):
        cont = dictionariesv2.contadorDePalabras()
        
        self.assertTrue(cont.contar("If you've done any programming before") == 6)
        self.assertTrue(cont.contar("") == 0)

if __name__ == "__main__":
    unittest.main()