#perfeito
#entradas
def main():
    print("Saudações...")
    n = int(input("Digite um número: "))
#processamento
    n2 = n /2
    n3 = n/3
    if n == 1+n2+n3:
#saidas
        print(n, "é um número perfeito")
    else:
        print(n, "não é um numero perfeito")



if __name__ == '__main__':
    main()
