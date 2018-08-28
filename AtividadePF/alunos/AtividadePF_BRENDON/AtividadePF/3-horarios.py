def main():
    horario = input().split(':')
    hora = horario[0]
    minuto = horario[1]
    segundos = horario[2]
    print(hora, 'hora(s)', minuto, 'minuto(s)', segundos, 'segundo(s)')


if __name__ == '__main__':
    main()
