def main():
    horario = input('Digite um horário no formato hh:mm:ss: ').split(':')
    print('{} hora(s), {} minuto(s) e {} segundo(s)'.format(horario[0], horario[1], horario[2]))


if __name__ == '__main__':
    main()
