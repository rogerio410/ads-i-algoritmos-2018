def main():

    numero = int(input('Digite um número para verificar se ele é perfeito: '))
    soma = 0
    numero_somado = 0
    
    while soma < numero:
        soma += numero_somado
        numero_somado += 1

    if soma == numero:
        print('É um número perfeito!')
    else:
        print('Não é um número perfeito!')


if __name__ == '__main__':
    main()
