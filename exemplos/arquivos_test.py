import unittest
from operaçãos import somar_numero, eh_par 


class Testegeral(unittest.TestCase):
    def test_somar_numero_ (self):
        self.assertEqual(somar_numero(1,2),3)

    def test_eh_par(self):
        self.assertTrue(eh_par(8), True)
        self.assertFalse(eh_par(7), False)

if __name__=='__main__':

    unittest.main()

