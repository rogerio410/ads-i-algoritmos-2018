def main():
    # entrada
    num = int(input("Digite um numero inteiro de 4 ALGARISMOS: "))

    # processamento
    dezena1 = (num // 1) % 100
    dezena2 =  (num //100) % 1000
    raiz = num**(1/2)
    print("Com o número {} podemos dividi-lo em duas dezenas:\nPrimeira Dezena= {} e Segunda Dezena = {}".format(num, dezena2, dezena1))

    if raiz == dezena1 + dezena2:
        print("Raiz de {} é {}, que é soma de {} com {}.".format(num, raiz, dezena2, dezena1))

if __name__ == "__main__":
    main()
