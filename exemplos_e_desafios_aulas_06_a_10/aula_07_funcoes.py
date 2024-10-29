import csv

caminho_arquivo_csv = (
    "C:/Users/vgmar/Desktop/Jornada_de_Dados/python_bootcamp/arquivos_csv/vendas.csv"
)


def ler_csv(caminho_arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(caminho_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


dados_csv = ler_csv(caminho_arquivo_csv)
print(dados_csv)


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Funcao que filtra produtos entregues
    """
    lista_produtos_entregues = []

    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_entregues.append(produto)

    return lista_produtos_entregues


produtos_entregues = filtrar_produtos_entregues(dados_csv)
print(produtos_entregues)


def somar_valores_dos_produtos_entregues(
    lista_com_produtos_filtrados: list[dict],
) -> int:
    """
    Soma todos os valores dos produtos filtrados
    """
    valor_total = 0

    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("preco"))

    return valor_total


valor_total_produtos_entregues = somar_valores_dos_produtos_entregues(
    produtos_entregues
)
print(valor_total_produtos_entregues)
