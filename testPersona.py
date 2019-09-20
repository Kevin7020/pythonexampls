import unittest

class simpleTest(unittest.TestCase):

    #Returns true or false
    def test(self):
        li = [1, 2, 3]
        self.assertTrue(len(li) == 4)

if __name__ == "__main__":
    unittest.main()
