import unittest

def dividir(a,b):

    return a/b
    
class matematica(unittest.TestCase):
    
    
   def test_dividir_por_zero(self):

    with self.assertRaises(ZeroDivisionError):
        dividir(10,0)

    print("[sucesso] ZeroDivisionError capturado")

if __name__ == "__main__":
    unittest.main()