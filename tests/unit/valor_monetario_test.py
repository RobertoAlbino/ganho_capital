import os
import sys
import unittest
from decimal import Decimal

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ganho_capital'))
sys.path.append(path)

from ganho_capital.valor_monetario import ValorMonetario

class ValorMonetarioTest(unittest.TestCase):
    
    def test_com_inteiro(self):
        valor = ValorMonetario(10)
        self.assertEqual(valor.valor_monetario, Decimal('10.00'))

    def test_com_float(self):
        valor = ValorMonetario(10.50)
        self.assertEqual(valor.valor_monetario, Decimal('10.50'))

    def test_com_string(self):
        valor = ValorMonetario('10.75')
        self.assertEqual(valor.valor_monetario, Decimal('10.75'))

    def test_arredondando_pra_cima(self):
        valor1 = ValorMonetario(10.5556)
        self.assertEqual(valor1.valor_monetario, Decimal('10.56'))

        valor2 = ValorMonetario(10.544)
        self.assertEqual(valor2.valor_monetario, Decimal('10.54'))

    def test_com_numero_preciso(self):
        valor = ValorMonetario(Decimal('10.123456'))
        self.assertEqual(valor.valor_monetario, Decimal('10.12'))

    def test_com_numero_negativo(self):
        valor = ValorMonetario(-10.50)
        self.assertEqual(valor.valor_monetario, Decimal('-10.50'))

    def test_com_zero(self):
        valor = ValorMonetario(0)
        self.assertEqual(valor.valor_monetario, Decimal('0.00'))