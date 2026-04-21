from transform.validate import validar_dados_iniciais #,validar_dados_finais

from transform.transform import (
transform_column,
transform_num,
transform_num_nulos,
transform_num_negativos,
transform_data,
)
from transform.features import (
    feature_faturamento,
    feature_tempo,
    feature_nome,
)


def pipeline(df):
    return (
        df
        .pipe(validar_dados_iniciais)
        .pipe(transform_column)
        .pipe(transform_num)
        .pipe(transform_num_nulos)
        .pipe(transform_num_negativos)
        .pipe(transform_data)
        .pipe(feature_faturamento)
        .pipe(feature_tempo)
        .pipe(feature_nome)
        #.pipe(validar_dados_finais)
    )
