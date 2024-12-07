import ast
import sys
import logging


import calculadora_imposto


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def processar():
    logging.info("Iniciando o processamento dos dados.")
    
    input_data = sys.stdin.read()
    logging.info("Dados recebidos do stdin.")
    
    datasets = input_data.strip().split('\n')
    logging.info(f"{len(datasets)} datasets encontrados para processamento.")

    for i, dataset in enumerate(datasets, start=1):
        try:
            data = ast.literal_eval(dataset)
            logging.info(f"Processando dataset {i}: {data}")
            resultado = calculadora_imposto.calcular(data)
            print(resultado)
        except Exception as e:
            logging.error(f"Erro ao processar o dataset {i}: {e}")

    logging.info("Processamento finalizado.")


if __name__ == "__main__":
    processar()
