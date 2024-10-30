from aula_08_ETL import pipeline_calcular_kpi_de_vendas_consolidado

json_files_path = "data"
opcoes_arquivos_de_saida = ["csv", "parquet"]


pipeline_calcular_kpi_de_vendas_consolidado(json_files_path, opcoes_arquivos_de_saida)
