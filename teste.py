import pandas as pd
from config.paths import DATA_RAW
import logging

logger = logging.getLogger(__name__)

#ler arquivo
def ler_csv(arquivo):
    df = pd.read_csv(arquivo ,encoding= 'latin1',  sep=',' )
    return df

#extrair arquivos
def extrair_arquivo():
    tabelas = []
    tabela_error=[]
    for arquivo in DATA_RAW.glob('*.csv'):
        try:
            tabela=ler_csv(arquivo)
            tabelas.append(tabela)

        except Exception as e:
            logger.exception('Erro ao ler o arquivo! ')
            tabela_error.append(arquivo.name)
    if not tabelas:
        raise ValueError('O arquivo .csv não foi carregado!')

    return tabelas , tabela_error

#transforma tabela
def criar_tabela(tabelas):
    if not tabelas:
        raise ValueError('Nenhuma tabela para montar')
    return pd.concat(tabelas, ignore_index=True)

arquivo , errors = extrair_arquivo()
tabela = criar_tabela(arquivo)
print(tabela.head(4))
print(tabela.columns)