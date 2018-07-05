def main():
    #entrada
    letra = input("digite qual letra da questão voce quer realizar.(a,b,c,d) ")
    #processamento
    if letra == "a":
        resposta = letra_a()
    elif letra == "b":
        resposta = letra_b()
    elif letra == "c":
        resposta = letra_c()
    elif letra == "d":
        resposta = letra_d()
    #saida
    print(resposta)


def letra_a():
    total = 0
    for i in range(1,10001):
        if i%2 == 0 :
            total -= 1/i
        else :
            total += 1/i
    return total

def letra_b():
    total = 0
    for i in range(1,10001):
        if (10001 - i)%2 == 0 :
            total -= 1/(10001 - i)
        else :
            total += 1/(10001 - i)
    return total

def letra_c():
    total_positivo = 0
    total_negativo = 0
    for i in range(1,10001,2):
        total_positivo += 1/i
    for i in range(2,10001,2):
        total_negativo += 1/i
    return total_positivo-total_negativo

def letra_d():
    total_positivo = 0
    total_negativo = 0
    for i in range(1,10001,2):
        total_negativo += 1/(10001-i)
    for i in range(2,10001,2):
        total_positivo += 1/(10001-i)
    return total_positivo-total_negativo


if __name__ == '__main__':
    main()
