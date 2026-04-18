
import pandas as pd
"""

                        ---TRANSFORM: LIMPAR COLUNAS---

"""
def transform_column(df):
    df = df.rename(columns={'quantidade vendida': 'quantidade_vendida',
                            'primeiro nome': 'primeiro_nome',
                            'preco unitario': 'preco_unitario'
                            })
    return df


def transform_num(df):
    return df.assign(
                quantidade_vendida = lambda x: pd.to_numeric(x["quantidade_vendida"]
                   .astype(str)
                   .str.strip()
                   ,errors='coerce'
                   ),

                preco_unitario = lambda x: pd.to_numeric(x['preco_unitario']
                    .astype(str)
                    .str.strip()
                    .str.replace(r'[^\d,.-]', '', regex=True )
                    .str.replace('.','', regex=False)
                    .str.replace(',','.',regex=False)
                    ,errors='coerce')
            )

def transform_num_nulos(df):
    return df.assign(
        quantidade_vendida = lambda x: x['quantidade_vendida'].fillna(0).astype(int),
        preco_unitario = lambda x: x['preco_unitario'].fillna(x['preco_unitario'].median() ).astype(float)
    )

def transform_num_negativos(df):
    if (df['quantidade_vendida'] < 0).any():
        raise ValueError("Quantidade negativa encontrada")
    if (df['preco_unitario'] < 0).any():
        raise ValueError('Preço com valores negativos encontrado')
    return df




def transform_data(df):
    data = df["data"].astype(str).str.strip()
    data_auto = pd.to_datetime(data, errors="coerce")
    return df.assign(data=data_auto)
    '''2024-12-31 (ISO)  31/12/2024 (BR)  12/31/2024 (US)  2024/12/31, etc.'''
