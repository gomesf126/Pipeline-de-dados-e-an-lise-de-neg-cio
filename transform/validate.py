
import pandas as pd

'''VALIDAR DADOS INICIAIS'''

def validar_dados_iniciais(df: pd.DataFrame)->pd.DataFrame:
    nulos = df.isnull().sum(axis=0)
    duplicadas = df.duplicated().sum()
    valores_unico = df.nunique()
    tipo= df.dtypes
    df.info()
    descricoes = df.describe(include='all')

    print(f"\nValores nulos encontrados {nulos[nulos > 0]}")
    print(f"\nLinhas duplicados {duplicadas}")
    print(f"\nValores unicos {valores_unico}")
    print(f"\nTipo de dados {tipo}")
    print(f"\nValores estatistico numérico {descricoes.T}")
    return df

def validar_dados_finais(df: pd.DataFrame)->pd.DataFrame:
    nulos = df.isnull().sum(axis=0)
    duplicadas = df.duplicated().sum()
    valores_unico = df.nunique()
    tipo= df.dtypes
    df.info()
    descricoes = df.describe(include='all')

    print(f"\nValores nulos encontrados {nulos[nulos > 0]}")
    print(f"\nLinhas duplicados {duplicadas}")
    print(f"\nValores unicos {valores_unico}")
    print(f"\nTipo de dados {tipo}")
    print(f"\nValores estatistico numérico {descricoes.T}")
    return df