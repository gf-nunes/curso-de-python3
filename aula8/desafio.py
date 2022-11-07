"""
Vídeo 21 e 22 - Desafio Prático

* Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa.
* Criar uma variavel com  ano atual (int).
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Oter o IMC da pessoa com 2 casas decimais (peso)

"""

nome = 'Gislane'
ano_nascimento = 1988
ano_atual = 2022
idade = ano_atual - ano_nascimento
altura = 1.80
peso = 107
imc = peso/(altura * altura)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.') 
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
