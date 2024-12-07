import logging


from quantidade import Quantidade
from transacoes import Transacoes
from valor_monetario import ValorMonetario
from classificacao_lucro import ClassificacaoLucro


def tax_to_dict(valor_imposto):
    logging.info(f"Convertendo valor de imposto para dicionário: {valor_imposto}")
    return {'tax': str(ValorMonetario(valor_imposto).valor_monetario)}


def nao_deve_arrecadar_imposto(valor, quantidade):
    resultado = ValorMonetario(valor).valor_monetario * Quantidade(quantidade).quantidade < ValorMonetario(20000).valor_monetario
    logging.info(f"Verificando se não deve arrecadar imposto para valor={valor} e quantidade={quantidade}: {resultado}")
    return resultado


def calcular(operacoes):
    logging.info("Iniciando cálculo dos impostos.")
    gerenciador = Transacoes()
    impostos_calculados = []

    for i, operacao in enumerate(operacoes, start=1):
        logging.info(f"Processando operação {i}: {operacao}")
        try:
            if operacao['operation'] == 'buy':
                gerenciador.atualizar_preco_medio(operacao['unit-cost'], operacao['quantity'])
                impostos_calculados.append(tax_to_dict(0))
                logging.info(f"Operação de compra processada: {operacao}")
                continue

            if operacao['operation'] == 'sell':
                if nao_deve_arrecadar_imposto(operacao['unit-cost'], operacao['quantity']):
                    impostos_calculados.append(tax_to_dict(0))
                    logging.info(f"Venda abaixo do limite de arrecadação: {operacao}")
                    continue

                lucro = gerenciador.calcular_lucro(operacao['unit-cost'], operacao['quantity'])
                classificacao_lucro = gerenciador.classificar_lucro(lucro)
                logging.info(f"Lucro calculado: {lucro}, classificação: {classificacao_lucro.name}")

                if classificacao_lucro == ClassificacaoLucro.LUCRO:
                    gerenciador.incrementar_lucro(lucro)
                    imposto = gerenciador.calcular_valor_imposto()
                    impostos_calculados.append(tax_to_dict(imposto))
                    logging.info(f"Imposto arrecadado por lucro: {imposto}")
                    continue
                
                if classificacao_lucro == ClassificacaoLucro.PREJUIZO:
                    gerenciador.decrementar_prejuizo(lucro)
                    impostos_calculados.append(tax_to_dict(0))
                    logging.info(f"Decrementando prejuizo: {lucro}")
                    continue

                impostos_calculados.append(tax_to_dict(0))
                logging.info(f"Operação de venda processada sem lucro: {operacao}")

        except Exception as e:
            logging.error(f"Erro ao processar operação {i}: {operacao}, erro: {e}")

    logging.info(f"Finalizando cálculo dos impostos. Resultados: {impostos_calculados}")
    return impostos_calculados
