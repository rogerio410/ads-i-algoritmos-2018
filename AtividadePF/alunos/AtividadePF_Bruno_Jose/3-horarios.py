def main():
    horario = input("Digite um horario no formato (hh:mm:ss) = ").split(":")
    hh = int(horario[0])
    mm = int(horario[1])
    ss = int(horario[2])

    print("%d hora(s), %d minuto(s) e %d segundo(s)" % (hh, mm, ss))


if __name__ == '__main__':
    main()