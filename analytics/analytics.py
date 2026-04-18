import pandas as pd
from extract.extract import (extrair_arquivo,transformar_tabela)

arquivo = extrair_arquivo()
tabela = transformar_tabela(arquivo)
df = pd.DataFrame(tabela)



'''1. Faturamento (ESSENCIAL)
Função:
faturamento
'''

'''2. Produto mais vendido
top produtos
ranking
Função:
top_produtos'''

'''3. Performance por loja
faturamento
Função:
faturamento_por_loja'''

'''4. Análise temporal
INSIGHTS:
vendas por mês
vendas por dia
sazonalidade

Função:
analise_temporal
'''

'''5. Clientes (simples)

Você tem:
Primeiro Nome
Sobrenome

'''

'''6. Ticket médio (muito importante)
Função: calcular_ticket_medio
'''

'''7. Quantidade média por compra
Clientes compram muito ou pouco?
Função: top_produtos'''

'''8. Clientes mais valiosos (top clientes)
quem compra mais
quem gera mais faturamento
Função: top_clientes'''

'''9. Produtos com baixa performance

produtos com baixo faturamento
produtos com baixa quantidade

Função:
produtos_baixa_performance'''

'''10. Crescimento ao longo do tempo

vendas por mês
tendência (subindo ou caindo)

Função:
analise_crescimento'''

'''11. Dia da semana mais forte
Função: dia_forte'''

'''11. Distribuição de preço

produtos são baratos ou caros?

média de preço
mediana
desvio padrão

Função:
analise_preco'''

'''12. Anomalias (nível mais avançado)

preços muito altos ou muito baixos
quantidades estranhas

Função:
detectar_outliers'''

'''13. Margem simulada (nível negócio)

lucro = faturamento * 0.3'''

