import unittest
from main import main  # Asumiendo que tienes una función principal en main.py

class TestMainFunction(unittest.TestCase):
    def test_main_function(self):
        self.assertEqual(main(), None)

if __name__ == '__main__':
    unittest.main()
