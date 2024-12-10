import os
import sys
import unittest

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ganho_capital'))
sys.path.append(path)

from ganho_capital.quantidade import Quantidade
from ganho_capital.transacoes import Transacoes
from ganho_capital.valor_monetario import ValorMonetario
class TransacoesTest(unittest.TestCase):
    
    def test_assert_instancia_vem_zerada(self):
        transacoes = Transacoes()
        self.assertEqual(transacoes.custo_total, ValorMonetario(0.00).valor_monetario)
        self.assertEqual(transacoes.lucro_total, ValorMonetario(0.00).valor_monetario)
        self.assertEqual(transacoes.preco_medio_calculado, ValorMonetario(0.00).valor_monetario)
        self.assertEqual(transacoes.quantidade_total, Quantidade(0.00).quantidade)
    
    def test_reseta_transacoes(self):
        transacoes = Transacoes()
        transacoes.quantidade_total = Quantidade(0.00).quantidade
        transacoes.custo_total = ValorMonetario(1000.00).valor_monetario
        transacoes.lucro_total = ValorMonetario(1000.00).valor_monetario
        transacoes.preco_medio_calculado = ValorMonetario(1000.00).valor_monetario
        
        transacoes.resetar_transacao()
        
        self.assertEqual(transacoes.custo_total, ValorMonetario(0.00).valor_monetario)
        self.assertEqual(transacoes.lucro_total, ValorMonetario(0.00).valor_monetario)
        self.assertEqual(transacoes.preco_medio_calculado, ValorMonetario(0.00).valor_monetario)
    
    def test_atualizar_preco_medio(self):
        transacoes = Transacoes()
        transacoes.atualizar_preco_medio(100.00, 10)

        self.assertEqual(transacoes.custo_total, ValorMonetario(1000.00).valor_monetario)
        self.assertEqual(transacoes.quantidade_total, Quantidade(10).quantidade)
        self.assertEqual(transacoes.preco_medio_calculado, ValorMonetario(100.00).valor_monetario)
    
    def test_calcular_lucro(self):
        transacoes = Transacoes()
        transacoes.atualizar_preco_medio(100.00, 10)
        lucro = transacoes.calcular_lucro(150.00, 5)

        self.assertEqual(lucro, ValorMonetario(250.00).valor_monetario)
    
    def test_operando_em_prejuizo(self):
        transacoes = Transacoes()
        transacoes.incrementar_lucro(-100.00)

        self.assertTrue(transacoes.operando_em_prejuizo())
    
    def test_calcular_valor_imposto(self):
        transacoes = Transacoes()
        transacoes.incrementar_lucro(1000.00)

        imposto = transacoes.calcular_valor_imposto()
        self.assertEqual(imposto, ValorMonetario(200.00).valor_monetario)
    
    def test_incrementar_quantidade(self):
        transacoes = Transacoes()
        transacoes.atualizar_preco_medio(10, 55)

        self.assertEqual(transacoes.quantidade_total, Quantidade(55).quantidade)
    
    def test_decrementar_quantidade(self):
        transacoes = Transacoes()
        transacoes.atualizar_preco_medio(100.00, 10)
        transacoes.decrementar_quantidade(5)

        self.assertEqual(transacoes.quantidade_total, Quantidade(5).quantidade)
    
    def test_calcular_preco_medio(self):
        transacoes = Transacoes()
        transacoes.quantidade_total = Quantidade(5).quantidade
        transacoes.preco_medio_calculado = ValorMonetario(20).valor_monetario
        
        preco_medio = transacoes.calcular_preco_medio(10, 5)

        self.assertEqual(preco_medio, ValorMonetario(15).valor_monetario)
    
    def test_obteve_lucro_true(self):
        transacoes = Transacoes()
        transacoes.preco_medio_calculado = ValorMonetario(20).valor_monetario
        
        assert transacoes.obteve_lucro(30)
    
    def test_obteve_lucro_false(self):
        transacoes = Transacoes()
        transacoes.preco_medio_calculado = ValorMonetario(50).valor_monetario
        
        assert not transacoes.obteve_lucro(30)
    
    def test_incrementar_lucro(self):
        transacoes = Transacoes()
        transacoes.incrementar_lucro(10000)
        transacoes.incrementar_lucro(10000)
        
        self.assertEqual(transacoes.lucro_total, ValorMonetario(20000).valor_monetario)
    
    def test_decrementar_lucro(self):
        transacoes = Transacoes()
        transacoes.incrementar_lucro(10000)
        transacoes.incrementar_lucro(10000)
        
        transacoes.decrementar_prejuizo(-10000)
        
        self.assertEqual(transacoes.lucro_total, ValorMonetario(10000).valor_monetario)
    
    def test_operando_em_prejuizo(self):
        transacoes = Transacoes()
        transacoes.decrementar_prejuizo(-10000)
        
        assert transacoes.operando_em_prejuizo()
    
    def test_calcular_valor_imposto(self):
        transacoes = Transacoes()
        transacoes.lucro_total = 1000
        
        imposto = transacoes.calcular_valor_imposto()
        
        self.assertEqual(imposto, ValorMonetario(200).valor_monetario)
    
    def test_calcular_valor_imposto(self):
        transacoes = Transacoes()
        transacoes.lucro_total = 1000
        
        imposto = transacoes.calcular_valor_imposto()
        
        self.assertEqual(imposto, ValorMonetario(200).valor_monetario)
    
    def test_calcular_lucro(self):
        transacoes = Transacoes()
        transacoes.preco_medio_calculado = 10
        
        lucro = transacoes.calcular_lucro(20, 10)
        
        self.assertEqual(lucro, ValorMonetario(100).valor_monetario)
    

    
    
    

