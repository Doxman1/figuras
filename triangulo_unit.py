import unittest
from figuras import Figuras
class TestFiguras(unittest.TestCase):
	def setUp(self):
		self.figura = Figuras()
	def test_area_triangulo_5_4(self):
		resultado = self.figura.triangulo(5,4)
		self.assertEqual(10,resultado)
	def test_area_triangulo_5punto0_4punto0(self):
		resultado = self.figura.triangulo(5.0,4.0)
		self.assertEqual(10.0,resultado)
	def test_area_triangulo_eljerry_5(self):
		resultado = self.figura.triangulo('El Jerry',5)
		self.assertEqual("dato incorrecto",resultado)
	def test_area_triangulo_pichija_True(self):
		resultado = self.figura.triangulo('Pichi-JA',True)
		self.assertEqual("dato incorrecto",resultado)

if __name__ == '__main__':
	unittest.main()