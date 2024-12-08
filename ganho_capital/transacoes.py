import logging


from quantidade import Quantidade
from valor_monetario import ValorMonetario


class Transacoes:
    
    
    def __init__(self):
        self.custo_total = ValorMonetario(0.00).valor_monetario
        self.lucro_total = ValorMonetario(0.00).valor_monetario
        self.preco_medio_calculado = ValorMonetario(0.00).valor_monetario
        self.quantidade_total = Quantidade(0).quantidade
    
    
    def resetar_transacao(self):
        if self.quantidade_total == Quantidade(0).quantidade:
            logging.info("Transação resetada")
            self.custo_total = ValorMonetario(0.00).valor_monetario
            self.lucro_total = ValorMonetario(0.00).valor_monetario
            self.preco_medio_calculado = ValorMonetario(0.00).valor_monetario


    def atualizar_preco_medio(self, custo_unitario, quantidade):
        custo_unitario = ValorMonetario(custo_unitario).valor_monetario
        quantidade = Quantidade(quantidade).quantidade
        logging.info(f"Atualizando preço médio: custo_unitario={custo_unitario}, quantidade={quantidade}")
        
        logging.info(f"Antigo: custo_total={self.custo_total}, quantidade_total={self.quantidade_total}")
        
        self.preco_medio_calculado = self.calcular_preco_medio(custo_unitario, quantidade)
        self.custo_total += custo_unitario * quantidade
        self.quantidade_total += quantidade
        
        logging.info(f"Novo: custo_total={self.custo_total}, quantidade_total={self.quantidade_total}")


    def calcular_preco_medio(self, valor_acao_comprada, quantidade_acao_comprada):
        logging.info(f"1 {self.quantidade_total}")
        logging.info(f"2 {self.preco_medio_calculado}")
        logging.info(f"3 {quantidade_acao_comprada}")
        logging.info(f"4 {valor_acao_comprada}")
        logging.info(f"5 {self.quantidade_total}")
        logging.info(f"6 {quantidade_acao_comprada}")
        preco_medio = ValorMonetario(((self.quantidade_total * self.preco_medio_calculado) + (quantidade_acao_comprada * valor_acao_comprada)) / (self.quantidade_total + quantidade_acao_comprada)).valor_monetario
        logging.info(f"Preço médio atualizado {preco_medio}")
        return preco_medio


    def obteve_lucro(self, preco_venda):
        return ValorMonetario(preco_venda).valor_monetario > self.preco_medio_calculado
    
    
    def incrementar_lucro(self, lucro):
        logging.info(f"Lucro para ser incrementado: {lucro}")
        logging.info(f"Lucro antes incrementar: {self.lucro_total}")
        self.lucro_total += ValorMonetario(lucro).valor_monetario
        logging.info(f"Lucro após incrementar: {self.lucro_total}")
    
    
    def decrementar_prejuizo(self, lucro):
        logging.info(f"Lucro para ser decrementado: {lucro}")
        logging.info(f"Lucro antes decrementar: {self.lucro_total}")
        self.lucro_total -= abs(ValorMonetario(lucro).valor_monetario)
        logging.info(f"Lucro após decrementar: {self.lucro_total}")
    
    
    def decrementar_quantidade(self, quantidade):
        logging.info(f"Quantidade antes decrementar: {self.quantidade_total}")
        self.quantidade_total = self.quantidade_total - Quantidade(quantidade).quantidade
        logging.info(f"Quantidade após decrementar: {self.quantidade_total}")
    
    
    def operando_em_prejuizo(self):
        transacoes_em_prejuizo = self.lucro_total < 0
        logging.info(f"Operando em prejuizo: {transacoes_em_prejuizo}")
        return transacoes_em_prejuizo
    
    
    def calcular_valor_imposto(self):
        logging.info(f"Calculando imposto sobre lucro total de: {self.lucro_total}")
        return self.lucro_total * ValorMonetario(0.20).valor_monetario
        

    def calcular_lucro(self, preco_venda, quantidade):
        preco_venda = ValorMonetario(preco_venda).valor_monetario
        quantidade = Quantidade(quantidade).quantidade
        
        lucro = ValorMonetario((preco_venda - self.preco_medio_calculado) * quantidade).valor_monetario
        logging.info(f"Calculando lucro: preco_venda={preco_venda}, quantidade={quantidade}, preco_medio={self.preco_medio_calculado}, lucro={lucro}")
        return lucro
