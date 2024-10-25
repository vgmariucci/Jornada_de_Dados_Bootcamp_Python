CONSTANTE_BONUS = 1000


def verifica_nome_do_usuário(nome_usuario):
    if nome_usuario.isdigit():
        print(
            "\nO nome do usuários não pode conter números, apenas letras."
            " Tente novamente."
        )
        nome_usuario = input("Informe o nome de usuário: ")
        verifica_nome_do_usuário(nome_usuario)
    else:
        pass
    return nome_usuario


def verifica_valor_salario(salario):
    if salario.isdigit():
        salario = float(salario)
    else:
        print("O valor digitado precisa conter apenas números. Tente novamnte.")
        salario = input("Informe o salário: ")
        salario = verifica_valor_salario(salario)

    return salario


def verifica_valor_bonus(bonus):
    if bonus.isdigit():
        bonus = float(bonus)
    else:
        print("O valor digitado precisa conter apenas números. Tente novamnte.")
        bonus = input("Informe o bônus: ")
        bonus = verifica_valor_bonus(bonus)

    return bonus


while True:
    print("\n")
    usuario = input("Informe o nome de usuário: ")
    usuario = verifica_nome_do_usuário(usuario)

    salario = input("Informe o salário: ")
    salario = verifica_valor_salario(salario)
    print(type(salario))

    valor_bonus = input("Informe o bônus: ")
    bonus = verifica_valor_bonus(valor_bonus)
    print(type(bonus))

    # 4) Calcule o valor do bônus final (KPI)
    valor_bonus_final = CONSTANTE_BONUS + salario * bonus
    # 5) Imprimir a mensagem personalizada incluindo o nome do usuário, salário,
    # bônus e bônus final
    print("\n\n")
    print(f"Olá {usuario}.")
    print(f"O salário informado é: {salario}")
    print(f"O bônus informado é: {bonus}")
    print(f"Portanto o bônus final é: {valor_bonus_final}")
