
def calc_metric(df):


    faturamento_produto = (df
               .groupby('produto', as_index=False)
               .agg(faturamento = ('faturamento','sum'))
               .sort_values(by='faturamento', ascending=False)
               .head(6) )

    faturamento_cliente =(df
               .groupby('nome_completo', as_index=False)
               .agg(faturamento = ('faturamento','sum'))
               .sort_values(by='faturamento', ascending=False)
               .head(6)
               .round(2)
    )
    faturamento_loja=(df
              .groupby('loja', as_index=False)
              .agg(faturamento = ('faturamento','sum'))
              .sort_values(by='faturamento', ascending=False)
              .head(6)
              .round(2))

    base =(df.groupby('produto', as_index=False)
                 .agg(faturamento = ('faturamento','sum'),
                      quantidade = ('quantidade_vendida','sum'))
                 )

    produtos_alta_qtd_baixo_fat = base.sort_values(by='quantidade', ascending=False).head(6)
    produtos_baixa_qtd_alto_fat  = base.sort_values(by='faturamento', ascending=False).head(6)

    ranking_produtos = (df
                       .groupby('produto', as_index=False)
                       .agg(faturamento = ('faturamento','sum'))
                       .assign(ranking = lambda x: x['faturamento'].rank(method='dense', ascending=False).astype(int) )
                       .sort_values(by='ranking' )
    )
    ranking_produto_loja = (df.groupby('loja', as_index=False)
                        .agg(faturamento = ('faturamento','sum'),
                             quantidade = ('nome_completo','nunique'))
                        .assign(ticket_medio = lambda x: x['faturamento'] / x['quantidade'],
                                ranking_loja = lambda x: x['faturamento'].rank(method='dense', ascending=False).astype(int) )
                        .sort_values(by='faturamento', ascending=False)
                        .head(6))


    produto_analise = 'Televisão'
    mes_analise = [1,2,3,4,5,6,7,8,9,10,11,12]
    filtro = (
        (df['mes_num'].isin(mes_analise)) &
        (df['produto'] == produto_analise)
    )

    vendas_mes_tv =(
                     df.loc[filtro]
                    .groupby(['produto','mes','mes_num'], as_index=False)
                    .agg(faturamento = ('faturamento','sum'))
                    .sort_values(by='mes_num'))

    crescimento_vendas_mes_tv = (
                     df[filtro]
                    .groupby(['mes', 'mes_num'], as_index=False)
                    .agg(faturamento=('faturamento', 'sum'))
                    .sort_values(by='mes_num', kind='stable')
                    .assign(crescimento = lambda x: x['faturamento'].pct_change().round(2))
    )





    cliente_analise= ['Guilherme Lima','Victor Lira']
    mes_cliente = [1,2,3,4,5,6,7,8,9,10,11,12]
    filtro_cliente = (
        (df['nome_completo'].isin(cliente_analise)) &
        (df['mes_num'].isin(mes_cliente))

    )

    crescimento_faturamento_cliente_vip = (df[filtro_cliente]
                   .groupby(['nome_completo','mes_num'], as_index=False)
                   .agg(faturamento = ('faturamento','sum'),
                        quantidade_comprada = ('quantidade_vendida','sum'))
                   .sort_values(by=['nome_completo','mes_num'])
                   .assign(crescimento = lambda x: x.groupby('nome_completo')['faturamento'].pct_change().round(2))
                   )



    return (
        {
         'faturamento_produto'               : faturamento_produto,
         'faturamento_cliente'               : faturamento_cliente,
         'faturamento_loja'                  : faturamento_loja,
         'produtos_alta_qtd_baixo_fat'       : produtos_alta_qtd_baixo_fat,
         'produtos_baixa_qtd_alto_fat'       : produtos_baixa_qtd_alto_fat,
         'ranking_produtos'                  : ranking_produtos,
         'ranking_produto_loja'              : ranking_produto_loja,
         'vendas_mes_tv'                     : vendas_mes_tv,
         'crescimento_vendas_mes_tv'         : crescimento_vendas_mes_tv,
        'crescimento_faturamento_cliente_vip': crescimento_faturamento_cliente_vip
         }
    )



