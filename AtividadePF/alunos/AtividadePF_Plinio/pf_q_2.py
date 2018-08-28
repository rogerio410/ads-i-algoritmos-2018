def main():
    N_total_fichas = int(input('quantas  fichas serão digitadas? \n'))
    dados_boiada = []
    while N_total_fichas > 0:
        ficha = input("digite a ficha separando os campos por ';'")
        ficha = ficha.split(';')
        dados_boiada += [ficha]
        N_total_fichas -= 1
    maior = dados_boiada[0]
    peso_maior = int(maior[1])
    menor = dados_boiada[0]
    peso_menor = int(menor[1])
    peso_total = 0
    contador = 0
    for i in range(len(dados_boiada)):
        contador +=1
        peso_i = int(dados_boiada[i][1])
        peso_total += peso_i
        if peso_i > peso_maior:
            maior = dados_boiada[i]
        if peso_i < peso_menor:
            menor = dados_boiada[i]
    media = peso_total / contador
    print('O numero de id do boi mais gordo é {}, seu peso é de {} Kg'.format(maior[0], maior[1]))
    print('O número de id do boi mais magro é {}, e seu peso é de {} Kg'.format(menor[0], menor[1]))
    print('A média de peso é ', media, 'Kg')

if __name__=='__main__':
    main()