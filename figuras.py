import math


class Figuras:

    def rectangulo(self, base, altura):
        try:
            base = float(base)
            altura = float(altura)
            resultado = base * altura
            return resultado
        except Exception:
            return 'dato incorrecto'

    def triangulo(self, base, altura):
        try:
            base = float(base)
            altura = float(altura)
            resultado = (base * altura) / 2
            return resultado
        except Exception:
            return 'dato incorrecto'

    def circunferencia(self, radio):
        try:
            radio = float(radio)
            resultado = math.pi * (radio**2)
            residuo = resultado % 0.01
            return resultado - residuo
        except Exception:
            return 'dato incorrecto'
