"""def eh_maiuscula(S):
    for i in S:
        if i == i.upper:
            return True
        else:
            return False
"""

def split_frase():
    S = input('')
    palavra = 1
    for i in S:
        if i == ' ':
            palavra += 1

    print(palavra)


print(split_frase())
