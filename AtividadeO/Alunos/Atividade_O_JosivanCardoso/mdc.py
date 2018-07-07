
# Nao implementou o Algoritmo de Euclides
def main():
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    i = 1
    if num1 < num2:
        menor = num1
    else:
        menor = num2

    while i <= menor:
        if (num1 % i == 0) and (num2 % i == 0):
            mdc = i
        i += 1

    print('\nmdc(', num1,',', num2, ') =', mdc)
    
if __name__ == '__main__':
    main()
