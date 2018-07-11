def main():
    resposta_da_letra = input("Para resposta da letra 'a', digite 1 \n" 
                              "Para resposta da letra 'b', digite 2 \n"
                              "Para resposta da letra 'a', digite 3 \n"
                              "Para resposta da letra 'a', digite 4 \n"
                              "Para encerrar digite 0 \n")

    while resposta_da_letra == '0':
        break
    else:
        if resposta_da_letra  == '1':
            print(adicao_esquerda_direita())
        elif resposta_da_letra == '2':
            print(adicao_direita_esquerda())
        elif resposta_da_letra == '3':
            print(separacao_positivos_negativos_esquerda_direita())
        elif resposta_da_letra == '4':
            print(separacao_positivos_negativos_direita_esquerda())

def adicao_esquerda_direita():
    n =0
    soma = 0
    for numero in range(1,10001):
        if n % 2 == 0:
            soma -= 1/numero
        else:
            soma += 1/numero
        n += 1
    return soma


def adicao_direita_esquerda():
    n = 0
    soma = 0
    numero = 10000
    while numero > 0:
        if n % 2 == 0:
            soma -= 1/numero
        else:
            soma += 1/numero
        numero -= 1
        n += 1
    return soma


def separacao_positivos_negativos_esquerda_direita():
    n = 0
    soma_positivos = 0
    soma_negativos = 0
    for numero in range(1, 10001):
        if n % 2 == 0:
            soma_positivos += 1 / numero
        else:
            soma_negativos += 1/numero
    soma_negativos_positivos = soma_positivos - soma_negativos
    return soma_negativos_positivos

def separacao_positivos_negativos_direita_esquerda():
    n = 0
    soma_positivos = 0
    soma_negativos = 0
    numero = 10000
    while numero > 0:
        if n % 2 == 0:
            soma_negativos += 1/numero
        else:
            soma_positivos += 1/numero
        numero -= 1
    soma_geral = soma_positivos - soma_negativos
    return soma_geral

if __name__=='__main__':
    main()