print("Primeira aula")

# Comando de Input: É uma função incorporada para capturar dados de entrada do usuário.
# Os dados inseridos pelo usuário são retornados pela função como uma string.
input("Digite seu nome:")

# Aqui, ele primeiro pede o input para digitar o nome e depois retorna o print
print ("Olá, "+ input("Digite seu nome: ")+ "!")


# EXERCÍCIO 1: Crie um programa que o usuário digita o nome e retorna o número de caracteres.
tamanho_nome = len(input("Digite seu nome:"))
print("O seu nome possui", tamanho_nome, "caracteres.")

# EXERCICIO 2: Crie um programa em que o usuario digita dois valores e apareça a soma
valor_1 = int(input("Digite o primeiro valor:"))
valor_2 = int(input("Digite o segundo valor:"))

soma = valor_1 + valor_2
print(soma)

# DESAFIO: Cálculo de Bônus com Entrada do Usuário
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido

nome = input("Digite o seu nome:")
salario = int(input("Digite o seu salário:"))
bonus = float(input("Digite a porcentagem do bônus que vocÊ recebeu:"))

kpi = 1000+(salario*bonus)
print("O seu bÔnus será de", kpi, "reais.")