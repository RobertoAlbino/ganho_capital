import logging


from quantidade import Quantidade
from transacoes import Transacoes
from valor_monetario import ValorMonetario


def tax_to_dict(valor_imposto):
    logging.info(f"Convertendo valor de imposto para dicionário: {valor_imposto}")
    return {'tax': str(ValorMonetario(valor_imposto).valor_monetario)}


def valor_abaixo_teto_arrecadacao(valor, quantidade):
    total = ValorMonetario(valor).valor_monetario * Quantidade(quantidade).quantidade
    resultado =  total < ValorMonetario(20000).valor_monetario
    logging.info(f"valor_abaixo_teto_arrecadacao {resultado} para o valor={valor} e quantidade={quantidade}")
    return resultado


def calcular(operacoes):
    logging.info("Iniciando cálculo dos impostos.")
    gerenciador = Transacoes()
    impostos_calculados = []

    for i, operacao in enumerate(operacoes, start=1):
        logging.info(f"Processando operação {i}: {operacao}")
        try:
            if operacao['operation'] == 'buy':
                gerenciador.resetar_transacao()
                gerenciador.atualizar_preco_medio(operacao['unit-cost'], operacao['quantity'])
                impostos_calculados.append(tax_to_dict(0))
                logging.info(f"Operação de compra processada: {operacao}")
                continue

            if operacao['operation'] == 'sell':
                gerenciador.decrementar_quantidade(operacao['quantity'])
                lucro = gerenciador.calcular_lucro(operacao['unit-cost'], operacao['quantity'])
                obteve_lucro = gerenciador.obteve_lucro(operacao['unit-cost'])
                logging.info(f"Lucro calculado: {lucro}, obteve_lucro: {obteve_lucro}")

                if obteve_lucro:
                    logging.info("Operação com lucro")
                    gerenciador.incrementar_lucro(lucro)
                    if gerenciador.operando_em_prejuizo() or valor_abaixo_teto_arrecadacao(operacao['unit-cost'], operacao['quantity']):
                        impostos_calculados.append(tax_to_dict(0))
                        logging.info(f"Não deve arrecadar imposto: {operacao}")
                        continue
                    
                    imposto = gerenciador.calcular_valor_imposto()
                    impostos_calculados.append(tax_to_dict(imposto))
                    logging.info(f"Imposto arrecadado por lucro: {imposto}")
                    continue
                
                if lucro == ValorMonetario(0).valor_monetario:
                    logging.info("Operação neutra")
                    impostos_calculados.append(tax_to_dict(0))
                    logging.info(f"Operação de venda processada sem lucro: {operacao}")
                    continue
                
                logging.info("Operação com prejuízo")
                gerenciador.decrementar_prejuizo(lucro)
                impostos_calculados.append(tax_to_dict(0))

        except Exception as e:
            logging.error(f"Erro ao processar operação {i}: {operacao}, erro: {e}")

    logging.info(f"Finalizando cálculo dos impostos. Resultados: {impostos_calculados}")
    return impostos_calculados
