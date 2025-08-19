import unittest
from src import utils  # <- importa src/utils.py

class TestUtils(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(utils.suma(2, 3), 5)
        self.assertEqual(utils.suma(-1, 1), 0)

    def test_es_par(self):
        self.assertTrue(utils.es_par(4))
        self.assertFalse(utils.es_par(5))

    def test_saludo(self):
        self.assertEqual(utils.saludo("Jason"), "Hola Jason!")

if __name__ == "__main__":
    unittest.main()
