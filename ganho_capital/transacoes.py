import logging


from quantidade import Quantidade
from valor_monetario import ValorMonetario
from classificacao_lucro import ClassificacaoLucro


class Transacoes:
    
    
    def __init__(self):
        self.custo_total = ValorMonetario(0.00).valor_monetario
        self.lucro_total = ValorMonetario(0.00).valor_monetario
        self.quantidade_total = Quantidade(0).quantidade


    def atualizar_preco_medio(self, custo_unitario, quantidade):
        custo_unitario = ValorMonetario(custo_unitario).valor_monetario
        quantidade = Quantidade(quantidade).quantidade
        logging.info(f"Atualizando preço médio: custo_unitario={custo_unitario}, quantidade={quantidade}")
        
        self.custo_total += custo_unitario * quantidade
        self.quantidade_total += quantidade
        
        logging.info(f"Novo estado: custo_total={self.custo_total}, quantidade_total={self.quantidade_total}")


    def calcular_preco_medio(self):
        if self.quantidade_total == Quantidade(0).quantidade:
            logging.info("Quantidade total é zero, retornando preço médio como 0.")
            return Quantidade(0).quantidade
        
        preco_medio = self.custo_total / self.quantidade_total
        logging.info(f"Preço médio calculado: custo_total={self.custo_total}, quantidade_total={self.quantidade_total}, preco_medio={preco_medio}")
        return preco_medio


    def classificar_lucro(self, lucro):
        lucro = ValorMonetario(lucro).valor_monetario
        if lucro > ValorMonetario(0.00).valor_monetario:
            return ClassificacaoLucro.LUCRO
        if lucro < ValorMonetario(0.00).valor_monetario:
            return ClassificacaoLucro.PREJUIZO
        if lucro == ValorMonetario(0.00).valor_monetario:
            return ClassificacaoLucro.NEUTRO
    
    
    def incrementar_lucro(self, lucro):
        self.lucro_total += ValorMonetario(lucro).valor_monetario
        logging.info(f"Lucro total: {self.lucro_total}")
    
    
    def decrementar_prejuizo(self, lucro):
        self.lucro_total -= abs(ValorMonetario(lucro).valor_monetario)
        logging.info(f"Lucro total: {self.lucro_total}")
    
    
    def calcular_valor_imposto(self):
        return ValorMonetario(self.lucro_total).valor_monetario * ValorMonetario(0.20).valor_monetario
        

    def calcular_lucro(self, preco_venda, quantidade):
        preco_venda = ValorMonetario(preco_venda).valor_monetario
        quantidade = Quantidade(quantidade).quantidade
        preco_medio = self.calcular_preco_medio()
        
        lucro = (preco_venda - preco_medio) * quantidade
        logging.info(f"Calculando lucro: preco_venda={preco_venda}, quantidade={quantidade}, preco_medio={preco_medio}, lucro={lucro}")
        return lucro
