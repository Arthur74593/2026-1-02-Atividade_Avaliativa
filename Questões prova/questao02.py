# Escreva um programa Python que leia um número inteiro positivo e armazene
#  na variável repeticoes; e exiba na tela uma sequência 
# de repeticoes números inteiros aleatórios entre 1 e 100.
import random

repetições = int(input("Digite a quantidade de números aleatórios:"))

for i in range(1,repetições+1):
    numero_aleatorio = random.randint(1, 100)
    print(f'{i}° número aleatório:{numero_aleatorio}')
