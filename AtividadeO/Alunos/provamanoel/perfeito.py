def main():
    num = int(input('Digite numero positivo: '))
    soma = 0  # soma dos divisores
    contador = (num //2 )+1
    for i in range(1,contador,1):
        if num % i == 0:
            soma += i
        #  print(soma)
    if soma == num:
        print('o numero {} é pefeito'.format(num))



if __name__ == '__main__':
    main()


