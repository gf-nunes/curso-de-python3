"""
Vídeo 20 - Formatação de Strings

"""

nome = 'Gislane'
idade = 34
altura = 1.80
e_maior = idade > 18
peso = 107
data_atual = 2022
imc = peso/(altura * altura )

print(nome, 'tem', idade, 'anos e seu imc é', imc)

print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}') #Valor formatado
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))