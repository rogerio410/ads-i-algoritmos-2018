from ordenacao import *

def main():
    fichas = int(input('Digite a quantidade de fichas: '))
    lista_de_bois = []
    soma_dos_pesos = 0

    for i in range(fichas):
        id_do_boi = int(input('Digite o numero de identificação do {}º boi: '.format(i+1)))
        peso_do_boi = int(input('Digite o peso do {}º boi: '.format(i+1)))
        lista_de_bois.append([id_do_boi, peso_do_boi])
        soma_dos_pesos += peso_do_boi

    lista_de_bois_ordenada = bubble_sort(lista_de_bois, key=lambda x: x[1])

    media_de_peso = soma_dos_pesos/fichas

    print('\nPeso do boi mais magro:', lista_de_bois_ordenada[0][1])
    print('Peso do boi mais gordo:', lista_de_bois_ordenada[-1][1])
    print('A média de peso: {:.1f}'.format(media_de_peso))
    print('Quantidade de Bois:', fichas)


if __name__ == '__main__':
    main()
