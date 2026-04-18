import pandas as pd
#receber as configurações dos caminhos das pastas row processed
from config.paths import DATA_RAW
import logging
logger  = logging.getLogger(__name__)

'''EXTRACT: LER ARQUIVO'''
def ler_csv(arquivo):
    encodings = ['utf-8','latin1','cp1252']
    for count in encodings:
        try:
            return pd.read_csv(arquivo, encoding=count, sep=None, engine='python')
        except (UnicodeDecodeError, UnicodeError) :
            continue
    raise ValueError(f'Formato inválido para o arquivo: {arquivo}. Esperado .csv')


def tratar_colunas(df: pd.DataFrame)->pd.DataFrame:
    #padronizar colunas
    df.columns = df.columns.astype(str).str.strip().str.lower()
    df = df.loc[:,~df.columns.str.contains('^unnamed', case=False)]
    return df

COLUNAS_SCHEMAS = {
    'vendas': ['sku', 'produto', 'quantidade vendida',
                'primeiro nome', 'sobrenome', 'data',
                'loja', 'preco unitario'
               ]
}


def validar_colunas(df, COLUNAS_SCHEMAS, arquivo):
    columns_df = set(df.columns)
    obrigatorias = set(COLUNAS_SCHEMAS)
    faltando = obrigatorias - columns_df
    if faltando:
        raise ValueError(f'[SCHEMA ERROR] {arquivo} MISSING COLUMNS: {sorted(faltando)}')
    return df


def extrair_arquivo():
    tabelas=[]
    arquivos_falhos=[]

    for arquivo in DATA_RAW.glob('*.csv'):
        try:
            logger.info('Lendo arquivo %s !',arquivo.name)

            df = ler_csv(arquivo)#chamar o arquivo
            df = tratar_colunas(df)#padronizar/tratar as colunas
            df = validar_colunas(df, COLUNAS_SCHEMAS['vendas'], arquivo.name)#df:leitura do arquivo |colunas_obrigatorias: colunas | arquivo: nome do arquivo lido

            tabelas.append(df)#juntar as os DataFrames

        except Exception :
            logger.exception('Erro ao ler o arquivo %s',arquivo.name)
            arquivos_falhos.append(arquivo.name)

    if not tabelas:
        raise ValueError(f'Nenhum csv válido foi carregado!')
    return tabelas, arquivos_falhos

def transformar_tabela(tabelas):
    if not tabelas:
        raise ValueError('Nenhuma tabela concatenar!')
    return pd.concat(tabelas, ignore_index=True)





"""tabelas , arquivos_falhos = extrair_arquivo()

if arquivos_falhos:
    logger.info('Arquivos falhos %s',arquivos_falhos)
if not tabelas:
    raise ValueError('Nenhum arquivo encontrado')

df = transformar_tabela(tabelas)

"""




