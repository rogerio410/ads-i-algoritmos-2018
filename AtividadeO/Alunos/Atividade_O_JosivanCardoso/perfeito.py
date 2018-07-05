def main():
    n = int(input('Digite o numero: '))

    i = 1
    soma = 0
    while i < n:
        if n % i == 0:
            soma += i
            if soma == n:
                perfeito = 'Perfeito'
            else:
                perfeito = 'Nao eh perfeito'
        i += 1

    
    print(perfeito)
    
if __name__ == '__main__':
    main()
