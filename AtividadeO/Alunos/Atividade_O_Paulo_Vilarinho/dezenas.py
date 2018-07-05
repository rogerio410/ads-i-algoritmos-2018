def main():
    #entrada
    #processamento
    for numero in range(1000,10000):
        if (numero%100 + numero//100) == (numero**(1/2)) :
            #saida
            print(numero)

if __name__ == '__main__':
    main()
