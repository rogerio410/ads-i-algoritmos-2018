def main():
    hora, minutos, seg = input('Digite o horário no formato hh:mm:ss: ').split(':')
    print('%s hora(s), %s minuto(s) e %s segundo(s)' % (hora, minutos, seg))


if __name__ == '__main__':
    main()
