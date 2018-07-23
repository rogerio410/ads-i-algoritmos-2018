def main():
#entrada
    numero=int(input("Digite um número inteiro: "))
    cont = 1
    soma = 0


#processamento
    while cont < numero:
        if numero % cont == 0:
            soma = soma +cont
            cont = cont +1
            
        else:
            cont = cont + 1

#saida
    if soma == numero:
        print('Numero eh perfeito')
    else:
        print('Numero n eh perfeito')
       


if __name__ == '__main__':
   main()
