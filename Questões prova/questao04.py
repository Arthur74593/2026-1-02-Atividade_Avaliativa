# Escreva um programa que leia um inteiro positivo numero e exibe
#  o número de dígitos de numero.

numero = int(input("Digite o número que você quer verificar:"))
n_digitos = len(str(numero))
if numero >0:
    print(f'A quantidade de digitos é: {n_digitos}')