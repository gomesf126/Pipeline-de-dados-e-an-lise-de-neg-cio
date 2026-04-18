import logging
from pipeline.pipeline import pipeline
from extract.extract import extrair_arquivo,transformar_tabela

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s"
)


