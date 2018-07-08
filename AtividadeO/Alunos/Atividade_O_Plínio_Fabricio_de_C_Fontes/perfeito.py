def main():
    #entrada
    numero = int(input())
    soma = 0

    #processamento e saída
    for algorismo in range(1, numero -1):
        if numero % algorismo == 0:
            soma += algorismo
    if soma == numero:
        print('o número é perfeito')
    else:
        print('o número não é perfeito')

if __name__=='__main__':
    main()
