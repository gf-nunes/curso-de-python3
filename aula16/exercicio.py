"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
from curses.ascii import isdigit
from readline import get_history_item

# num_inteiro = input('Digite um número inteiro: ')

# if num_inteiro.isdigit():
#     num_inteiro = int(num_inteiro)

#     if num_inteiro % 2 == 0:
#         print(f"{num_inteiro} é par")
#     else:
#         print(f"{num_inteiro} é ímpar")
# else:
#     print('Isso não é um número inteiro.')


# if not num_inteiro.isdigit():
#     print('Isso não é um número inteiro')
# else:
#     num_inteiro = int(num_inteiro)

#     if not num_inteiro % 2 == 0:
#         print(f'{num_inteiro} é ímpar')
#     else:
#         print(f'{num_inteiro} é par')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Informe a hora (0-23): ')

# if hora.isdigit():
#     hora = int(hora)

#     if hora > 23 or hora < 0:
#         print("Horário deve estar entre 0 e 23.")
#     else:
#         if hora <= 11:
#             print('Bom dia!')
#         elif hora <= 17:
#             print('Boa tarde!')
#         else:
#             print('Boa noite!')
# else:
#     print("Por favor, informe um horário entre 0  23.")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')