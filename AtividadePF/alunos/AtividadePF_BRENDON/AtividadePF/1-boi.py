def main():
    cont_bois = 0
    n = int(input('Quantidade de fichas:'))
    pesado = 0
    magro = 10000
    soma = 0
    for i in range(n):
        id = int(input("Digite a identificação do boi: "))
        peso = float(input('Digtie o peso em Kg: '))
        cont_bois += 1
        soma += peso
        if peso > pesado:
            pesado = peso

        if peso < magro:
            magro = peso
    media = soma / cont_bois
    print('Boi mais pesado %d kg' % pesado)
    print('Boi mais magro %d kg' % magro)
    print('Media de peso: %.1f kg' % media)
    print('Quantidade de bois:', cont_bois)


if __name__ == '__main__':
    main()