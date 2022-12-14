"""
Vídeo 28 - Documentação e funções built-in úteis
"""

from curses.ascii import isdigit

# num1 = input('Digie um número: ')
# num2 = input('Digite outro número: ')

# num1 = int(num1)
# num2 = int(num2)

# print(num1 + num2)

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)

#     print(num1+num2)
# else: 
#     print('Não pude converter os números para realizar a conta.')

import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('Digie um número: ')
num2 = input('Digite outro número: ')