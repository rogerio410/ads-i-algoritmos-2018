def main():
    #entrada
    numero1 = int(input())
    numero2 = int(input())

    #processamento
    if numero1 >= numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1
    dividendo = maior
    divisor = menor
    while dividendo % divisor != 0: #critério de continuidade
        resto = dividendo % divisor #trabalho
        dividendo = divisor #convergência de dados
        divisor = resto #convergência de dados
    #saída
    print(divisor)

if __name__=='__main__':
    main()
