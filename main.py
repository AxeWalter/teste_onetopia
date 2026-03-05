from conexaoAPI import request_api
from extracao import parsing_data
from db_configs.data_manipulation import insert_all
import logging


logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    try:
        number_of_cryptos = 200  # 200 cryptos = 1 token da API
        currency = "BRL"

        logging.info("Iniciando coleta de dados da API...")
        api_data = request_api(number_of_cryptos, currency)
        logging.info(f"{len(api_data)} coletados com sucesso!")

        logging.info("Iniciando limpeza dos dados...")
        clean_data = parsing_data(api_data)
        logging.info("Dados limpos com sucesso!")

        logging.info("Iniciando insercao de dados no Banco...")
        insert_all(clean_data)
        logging.info("Dados inseridos com sucesso!")

    except Exception as e:
        logging.error(e, exc_info=True)

    finally:
        logging.info("-" * 50)


if __name__ == '__main__':
    main()