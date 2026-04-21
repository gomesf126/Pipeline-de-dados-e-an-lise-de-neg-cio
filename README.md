# Pipeline-de-dados-e-an-lise-de-neg-cio
Desenvolvendo soluções em dados com foco em análise de negócio  e engenharia de dados. Práticas em construções em pipelines ETL, limpeza, transformação analíse de dados com python e pandas. Focado em gerar insights que apoiam decisões e agregam valores ao negócio.

Objetivo

Construir um pipeline de dados capaz de:

Extrair múltiplos arquivos de vendas
Tratar e padronizar dados
Gerar métricas de negócio
Identificar padrões de faturamento e crescimento

Tecnologias
Python
Pandas
Logging
Arquitetura modular

Estrutura do Projeto
main.py → Orquestra o pipeline

extract/ → Leitura de arquivos  
transform/ → Limpeza e tratamento  
pipeline/ → Encadeamento das transformações  
analytics/ → Cálculo de métricas  
load/ → Salvamento dos dados  
config/ → Configurações e caminhos  
data/ → Armazenamento de dados  

Métricas implementadas
Faturamento por produto
Faturamento por cliente
Ranking de produtos
Ranking de lojas
Ticket médio
Crescimento mensal de vendas
Crescimento de clientes VIP

Destaques técnicos
Uso de groupby + agg para agregações
Cálculo de crescimento com pct_change()
Uso de groupby para múltiplas séries temporais
Pipeline modular escalável
Separação de responsabilidades
