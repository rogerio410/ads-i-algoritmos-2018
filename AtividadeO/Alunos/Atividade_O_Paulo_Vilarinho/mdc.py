
def main():
    #entrada
    numero1 = int(input("digite o numero 1 "))
    numero2 = int(input("digite o numero 2 "))
    #processamento
    resposta = Euclides(numero1,numero2)
    #saida
    print("o mdc é {}".format(resposta))


def Euclides(a,b):
    if a > b :
        divisor = b
        dividendo = a
    else :
        divisor = a
        dividendo = b
    resto = dividendo%divisor
    while resto!=0 : #criterio de continuidade Enquanto o resto for diferente de 0
        dividendo = divisor#trabalho é fazer divisões subsequentes
        divisor = resto
        resto = dividendo%divisor #convergência de dados é atribuir ao resto o valor dos restos das divisões

    return divisor

if __name__ == '__main__':
    main()
