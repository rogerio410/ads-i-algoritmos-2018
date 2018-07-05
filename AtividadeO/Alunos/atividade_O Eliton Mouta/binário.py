def main():
#entradas
    def converter(numero):
        decimal = 0
        numero = str(numero)
        numero = numero[::-1]
        tamanho = len(numero)
        for i in range(tamanho):
            if numero[i] =='1':
                decimal = decimal+2**1
        return decimal
    n = int(input())
    b = converter(n)
    print(b)
#processamento

#saida


if __name__ == '__main__':
    main()
