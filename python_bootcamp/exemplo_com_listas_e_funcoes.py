###############################################################################
#
# Dada a lista abaixo, desenvolva uma função que ordene os valores em ordem
# crescente.
#
###############################################################################

# Lista com números desordenados
numeros = [2, 4, 6, 7, 1, 3, 12]



# Definindo a função responsável por ordenar os números de uma lista em ordem crescente
def ordena_numeros_em_ordem_crescente(lista_com_numeros: list) -> list:

    # Lista vazia para armazenar os números ordenados
    numeros_ordenados_em_ordem_crescente = lista_com_numeros.copy()

    for i in range(len(numeros_ordenados_em_ordem_crescente)):
        for j in range(i+1, len(numeros_ordenados_em_ordem_crescente)):
            if numeros_ordenados_em_ordem_crescente[i] > numeros_ordenados_em_ordem_crescente[j]:
                numeros_ordenados_em_ordem_crescente[i], numeros_ordenados_em_ordem_crescente[j] = numeros_ordenados_em_ordem_crescente[j], numeros_ordenados_em_ordem_crescente[i]
    
    return numeros_ordenados_em_ordem_crescente

# Executa a função para ordenar os números em ordem crescente passando como argumento da função as lista "numeros"
nova_lista = ordena_numeros_em_ordem_crescente(numeros)
print(nova_lista)

