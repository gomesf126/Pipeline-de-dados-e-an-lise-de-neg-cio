

"""
                               --FEATURE ENGINEERING---

"""

def feature_faturamento(df):
    return df.assign(
        faturamento = lambda x: x['quantidade_vendida'] * x['preco_unitario']
    )

mapa_mes = {
    1: 'Jan', 2: 'Fev', 3: 'Mar',
    4: 'Abr', 5: 'Mai', 6: 'Jun',
    7: 'Jul', 8: 'Ago', 9: 'Set',
    10: 'Out', 11: 'Nov', 12: 'Dez'
}
mapa_semana = {
    'Monday': 'Seg',
    'Tuesday': 'Ter',
    'Wednesday': 'Qua',
    'Thursday': 'Qui',
    'Friday': 'Sex',
    'Saturday': 'Sáb',
    'Sunday': 'Dom'
}
def feature_tempo(df):
    return df.assign(
        dia    = lambda x: x['data'].dt.day,
        mes    = lambda x: x['data'].dt.month.map(mapa_mes),
        ano    = lambda x: x['data'].dt.year,
        semana = lambda x: x['data'].dt.day_name().map(mapa_semana)
    )


def feature_nome(df):
    return df.assign(
        nome_completo = lambda x: ( x['primeiro_nome'].fillna('').str.strip() + ' ' +
                                    x['sobrenome'].fillna('')).str.strip()
    )


