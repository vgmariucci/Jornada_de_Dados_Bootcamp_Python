from aula_09_utils_logs_e_decoradores import log_decorator


@log_decorator
def soma(x, y):
    soma = x + y
    return soma


lista_a = [2, 4, 6, "f", 6, "t"]
lista_b = [3, 5, 11, 1, 6, 7]

for i in range(len(lista_a)):
    y = soma(lista_a[i], lista_b[i])
