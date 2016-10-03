import unittest
from figuras import Figuras
class TestFiguras(unittest.TestCase):
	def setUp(self):
		self.figura = Figuras()
	def test_area_circunferencia_5_4(self):
		resultado = self.figura.circunferencia(5)
		self.assertEqual(78.53,resultado)
	def test_area_circunferencia_5punto0_4punto0(self):
		resultado = self.figura.circunferencia(5.0)
		self.assertEqual(78.53,resultado)
	def test_area_circunferencia_eljerry_5(self):
		resultado = self.figura.circunferencia('El Jerry')
		self.assertEqual("dato incorrecto",resultado)
	def test_area_circunferencia_pichija_True(self):
		resultado = self.figura.circunferencia(True)
		self.assertEqual(3.14,resultado)

if __name__ == '__main__':
	unittest.main()