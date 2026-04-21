import logging
from pipeline.pipeline import pipeline
from extract.extract import extrair_arquivo,transformar_tabela
from analytics.analytics import calc_metric
from load.load import salvar_df,salvar_metricas


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s"
)

def main():

    logging.info("Iniciando extração...")
    tabelas, erros = extrair_arquivo()

    if erros:
        logging.warning(f'Arquivo com erro: {erros}')

    logging.info("Transformando dados...")
    df = transformar_tabela(tabelas)

    logging.info("Aplicando pipeline...")
    df_final = pipeline(df)

    logging.info("Calculando métricas...")
    metricas = calc_metric(df_final)

    logging.info("Salvando dados...")
    salvar_df(df_final)
    salvar_metricas(metricas)

    for nome , tabela in metricas.items():
        print(f'\n {nome.lower()}')
        print(tabela)
if __name__ == "__main__":
    main()

