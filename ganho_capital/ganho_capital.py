import ast
import sys
import logging


import calculadora_imposto
from correlation_id_filter import CorrelationIdFilter


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(correlation_id)s - %(message)s"
)
logging.getLogger().addFilter(CorrelationIdFilter())


def processar():
    logging.info("Iniciando o processamento dos dados.")
    
    input_data = sys.stdin.read()
    logging.info("Dados recebidos do stdin.")
    
    datasets = input_data.strip().split('\n')
    logging.info(f"{len(datasets)} datasets encontrados para processamento.")

    for dataset in datasets:
        try:
            data = ast.literal_eval(dataset)
            logging.info(f"Processando dataset")
            resultado = calculadora_imposto.calcular(data)
            print(resultado)
        except Exception as e:
            logging.error(f"Erro ao processar o dataset: {e}")

    logging.info("Processamento finalizado.")


if __name__ == "__main__":
    processar()
