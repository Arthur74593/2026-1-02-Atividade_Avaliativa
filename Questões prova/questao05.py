# Escreva um programa que leia um número inteiro positivo repeticoes,
#  depois leia repeticoes números inteiros e calcule:

# a soma total,
# a média,
# o maior valor,
# o menor valor,
# a quantidade de valores acima da média.

repeticoes = int(input("Digite a quantidade de numeros a serem analisados:"))
valores = []

if repeticoes>0:
    for i in range(repeticoes):
        n = int(input(f'Informe o valor {i+1}:'))
        valores.append(n)
        soma = sum(valores)
        media = soma/repeticoes
        maior = max(valores)
        menor = min(valores)
        cont = 0
    
    for v in valores: 
        if v > media:
                cont += 1
                
print(f'A soma é: {soma}')
print(f'a media é: {media}')
print(F'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
print(f'A quantidade de números acima de média é: {cont}')
    

