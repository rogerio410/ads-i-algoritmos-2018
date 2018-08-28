def main():
    entrada = input('digite no formato hh:mm:ss \n')
    entrada_separada = entrada.split(':')
    print('{} hora(s), {} minuto(s) e {} segundos(s)'.format(entrada_separada[0], entrada_separada[1],
                                                                 entrada_separada[2]))
if __name__ == '__main__':
    main()