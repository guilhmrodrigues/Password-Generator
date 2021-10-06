#maiúsculas e minúsculas
#símbolos e espaços
'''Substituição simples de criptografia.
Ex.: Security = chave 
5ecur1ty = senha '''

'''Utilizar a regra dos hexadecimais
1 = 1
2 = 2
3 = 3
Até 9 = 9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F '''

chave = input('Digite a base da sua senha: ')

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "1O0"
    elif letra in "Bb": senha = senha + "#&#"
    elif letra in "Cc": senha = senha + "1e%"
    elif letra in "Dd": senha = senha + "3jk"
    elif letra in "Ee": senha = senha + "/=&"
    elif letra in "Ff": senha = senha + "5dx"
    elif letra in "Gg": senha = senha + "!><"
    elif letra in "Hh": senha = senha + "6yp"
    elif letra in "Ii": senha = senha + "%$#"
    elif letra in "Jj": senha = senha + "0!0"
    elif letra in "Kk": senha = senha + "/z_"
    elif letra in "Ll": senha = senha + "$##"
    elif letra in "Mm": senha = senha + "#:>"
    elif letra in "Nn": senha = senha + ":>O"
    elif letra in "Oo": senha = senha + "&!?"
    elif letra in "Pp": senha = senha + "=_="
    elif letra in "Qq": senha = senha + "ot/"
    elif letra in "Rr": senha = senha + "!>/"
    elif letra in "Ss": senha = senha + "@#*"
    elif letra in "Tt": senha = senha + "-8_"
    elif letra in "Uu": senha = senha + "*E$"
    elif letra in "Vv": senha = senha + "?5/"
    elif letra in "Xx": senha = senha + "|?|"
    elif letra in "Yy": senha = senha + "7Up"
    elif letra in "Ww": senha = senha + "+?h"
    elif letra in "0": senha = senha + "9"
    elif letra in "1": senha = senha + "8"
    elif letra in "2": senha = senha + "7"
    elif letra in "3": senha = senha + "6"
    elif letra in "4": senha = senha + "5"
    elif letra in "5": senha = senha + "4"
    elif letra in "6": senha = senha + "3"
    elif letra in "7": senha = senha + "2"
    elif letra in "8": senha = senha + "1"
    elif letra in "9": senha = senha + "0"
    else: senha = senha + letra
print(senha)
