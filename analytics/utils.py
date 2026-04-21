

def ajustar_escala(df):
    valor_max = df['faturamento'].max()

    if valor_max < 1_000_000:
       divisor, unidade = 1_000 , 'reais'
    else:
      divisor, unidade = 1_000_000, 'milhoes'


    return df.assign(faturamento_escala = lambda x: x['faturamento'].div(divisor).round(2), unidade=unidade)



"""def ajustar_escala(df):
    max_valor = df['faturamento'].max()
    if max_valor >= 1_000_000:
        return df.assign(
            faturamento_escala = lambda x: x['faturamento'].div(1_000_000).round(2), unidade='milhões'
        )
    elif(max_valor >= 1_000):
        return df.assign(faturamento_escala = lambda x:  x['faturamento'].div(1_000).round(2), unidade='mil')
    else:
        return df.assign(faturamento_escala = lambda x: x['faturamento'].round(2), unidade='reais')

    """