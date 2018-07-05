def main():
    #entrada
    binario = int(input("digite um numero em binário: "))
    #processamento
    decimal = bin_to_dec(binario)
    #saida
    print("o valor inserido é igual a {}.".format(decimal))

def bin_to_dec(binario):
    x = binario
    total = 0
    contador = 0
    while x != 0:
        aux = x%10
        x = x//10
        total += aux*(2**contador)
        contador += 1
    return total

if __name__ == '__main__':
    main()
