def main():
    #entrada
    numero = int(input("digite o numero a ser verificado: "))
    #saida
    print("o numero {} é perfeito".format(numero)) if is_perfeito(numero) else print("o numero {} não é perfeito".format(numero))

def is_perfeito(numero):
    total = 0
    for i in range(1,numero):
        if numero%i == 0 : total += i
    return total == numero

if __name__ == '__main__':
    main()
