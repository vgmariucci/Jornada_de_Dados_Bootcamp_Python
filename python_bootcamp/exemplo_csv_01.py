import csv
from pathlib import Path
import pprint

nome_do_arquivo_csv = 'exemplo_csv_01.csv' 
root_path = Path(__file__).parent
csv_path = Path(__file__).parent / 'arquivos_csv' / nome_do_arquivo_csv

print('\n\nCaminho do arquivo:\n')
print(csv_path)

# Inicializa uma lista vazia para armazenar os dados
dados = []

# Usa o gerenciador de contexto 'with' para abrir e ler o arquivo csv
with open(csv_path, 'r', encoding='utf-8') as arquivo:
    print('\nAbrindo o arquivo csv para leitura.\n')
    # Cria um objeto leitor de csv
    leitor_csv = csv.DictReader(arquivo)
    
    # Itera sobre as linhas do arquivo csv
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

# Exibe os dados lidos do arquivo csv
for registro in dados:
    pprint.pprint(registro)