import os
import sys
import unittest

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ganho_capital'))
sys.path.append(path)

import ganho_capital.calculadora_imposto

class CalcularImpostoTest(unittest.TestCase):

    def test_cenario_compra_unica(self):
        operacoes = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 1000}
        ]
        resultado = ganho_capital.calculadora_imposto.calcular(operacoes)
        esperado = [{"tax": "0.00"}]
        self.assertEqual(resultado, esperado)
    
    def test_valor_abaixo_teto_arrecadacao_retorna_verdadeiro(self):
        assert ganho_capital.calculadora_imposto.valor_abaixo_teto_arrecadacao(10000, 1)
    
    def test_valor_abaixo_teto_arrecadacao_retorna_falso(self):
        assert not ganho_capital.calculadora_imposto.valor_abaixo_teto_arrecadacao(10000, 3)

    def test_valor_abaixo_teto_arrecadacao_retorna_falso(self):
        assert not ganho_capital.calculadora_imposto.valor_abaixo_teto_arrecadacao(10000, 2)
    
    def test_tax_to_dict_convertendo_valor_monetario(self):
        esperado = {"tax": "10000.00"}
        self.assertEqual(ganho_capital.calculadora_imposto.tax_to_dict(10000), esperado)
    
    def test_tax_to_dict_convertendo_valor_monetario(self):
        esperado = {"tax": "10000.35"}
        self.assertEqual(ganho_capital.calculadora_imposto.tax_to_dict(10000.3456), esperado)
    
    

