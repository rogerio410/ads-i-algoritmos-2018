def main():

#entradas
    n = input()
#processamento
    dezena1 = n[0] + n[1]
    dezena2 = n[2] + n[3]
    soma = int(dezena1) + int(dezena2)
    for i in range(1000, 9999+1):
        d1 = 1[0] + i[1]
        d2 = 1[2] + i[3]
        soma = int(d1) + int(d2)
        if soma * soma:
            print(soma)
#saida

if __name__ == '__main__':
    main()
