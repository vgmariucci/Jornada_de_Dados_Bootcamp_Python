import glob
import os

import pandas as pd


# # Uma funcao de extract que le e consolida os json
def extrair_dados_e_consolidar(file_path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(file_path, "*.json"))  # Use Path.glob
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# Uma funcao que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Função para calcular o kpi de vendas
    """
    df["Total"] = df["Quantidade"] * df["Venda"]

    return df


# Uma funcao que da load em csv ou parquet
def carregar_dados(
    opcoes_de_saida: list, df: pd.DataFrame, path_arquivos_de_saida: str
):
    """
    Funcao para exportar ou carregar os dados com as opções de saída
    sendo csv, parquet ou ambos
    """
    for opcao in opcoes_de_saida:
        if opcao == "csv":
            df.to_csv(f"{path_arquivos_de_saida}/kpis_de_vendas.csv", index=False)
        if opcao == "parquet":
            df.to_parquet(
                f"{path_arquivos_de_saida}/kpis_de_vendas.parquet", index=False
            )


def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):

    pasta_com_arquivos_de_saida = "arquivos_de_saida"
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_com_kpi_de_vendas = calcular_kpi_de_total_de_vendas(data_frame)

    carregar_dados(
        formato_de_saida, data_frame_com_kpi_de_vendas, pasta_com_arquivos_de_saida
    )


if __name__ == "__main__":

    json_files_path_argumento = "data"
    pasta_com_arquivos_de_saida = "arquivos_de_saida"
    opcoes_arquivos_de_saida = ["csv", "parquet"]
    data_frame = extrair_dados_e_consolidar(json_files_path_argumento)
    data_frame_com_kpi_de_vendas = calcular_kpi_de_total_de_vendas(data_frame)

    carregar_dados(
        opcoes_arquivos_de_saida,
        data_frame_com_kpi_de_vendas,
        pasta_com_arquivos_de_saida,
    )
