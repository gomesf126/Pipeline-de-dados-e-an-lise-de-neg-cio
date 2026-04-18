from pathlib import Path
#diferionar a base do projeto
BASE_DIR = Path(__file__).parent.parent
#diretorios
DATA_DIR       = BASE_DIR / 'data'
DATA_RAW       = DATA_DIR / 'raw'
DATA_PROCESSED = DATA_DIR / 'processed'

#garantir as pastas
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)