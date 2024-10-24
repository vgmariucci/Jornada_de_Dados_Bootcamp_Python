CONSTANTE_BONUS = 1000

# 1) Solicite ao usuário que digite o nome dele
nome_usuario = input('Digite o seu nome: ')

# 2) Solicite ao usuário que digite o valor do seu salário
# Converter a entrada para número de ponto flutuante
salario = input('Valor do salário: ')
salario_float = float(salario)

# 3) Solicite ao usuário que digite o valor do bônus recebido
# converter a entrada para um número de ponto flutuante
bonus = input('Valor do bônus: ')
bonus_float = float(bonus)
# 4) Calcule o valor do bônus final (KPI)
valor_bonus_final = CONSTANTE_BONUS + salario_float*bonus_float

# 5) Imprimir o cálculo do KPI para o usuário
print(f'O valor do bônus final é: {valor_bonus_final}')

# 6) Imprimir a mensagem personalizada incluindo o nome do usuário, salário, bônus e bônus final
print('\n\n')
print(f'Olá {nome_usuario}.')
print(f'O salário informado é: {salario}')
print(f'O bônus informado é: {bonus}')
print(f'Portanto o bônus final é: {valor_bonus_final}')