"""
Vídeo 26 - Operadores lógicos
and, or, not
in e not in
"""

# AND - E
#(verdadeiro e verdadeiro) = verdadeiro
#(verdadeiro e falso) = falso


# OR - OU
#(verdadeiro ou verdadeiro) = verdadeiro
#(falso ou verdadeiro) = verdadeiro

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'gislane'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else: 
    print('Usuario ou senha iválidos.')
