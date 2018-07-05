def main():
    # entrada
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    # calculos
    while True:
        auxiliar = numero2
        numero2 = numero1 % numero2
        numero1 = auxiliar
        if numero2 == 0:
            break
    #saida
    print(auxiliar)

if __name__ =='__main__':
    main()